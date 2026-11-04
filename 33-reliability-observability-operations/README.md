# 33 · Reliability, Observability & Operations: phần mềm chạy được, phát hiện hỏng và phục hồi được

> Phạm vi nghiên cứu **2026-11-04**: đọc mã, LICENSE, CI và đường gọi được dẫn tại SHA cố định; không cài/chạy upstream, không phát sinh sự cố hay đo RTO/RPO. Đây là hồ sơ chọn và tích hợp công cụ cho xưởng phần mềm, không phải bộ runbook đã được thử trên production.

## 1. Vì sao xưởng cần một mục vận hành riêng

[Mục 07](../07-eval-observability/README.md) đánh giá ứng dụng LLM; [mục 13](../13-dev-stack-devops/README.md) giữ dev stack; [mục 32](../32-platform-delivery-engineering/README.md) lo hạ tầng/phát hành. Mục này giữ hợp đồng **sau khi phát hành**: điều gì là thành công đối với người dùng, ai nhận cảnh báo, dữ liệu đi đâu, khi nào dừng rollout, và khôi phục thế nào. App vừa trả HTTP 200 chưa chứng minh nghiệp vụ đúng, queue không kẹt hay backup dùng được.

| Năng lực xưởng | Artifact tối thiểu ở dự án nhận | Cổng có thể làm thất bại |
|---|---|---|
| Biết ai chịu trách nhiệm | Service owner, dependency map, on-call/runbook, độ quan trọng | Service không có người xử lý/đường escalation; runbook không có quyền và điều kiện thực thi |
| Đo tác vụ người dùng | SLI query, numerator/denominator, latency boundary, window, exclusions | Query sai sample; drop telemetry tạo tỷ lệ đẹp; tenant/route quan trọng biến mất |
| Quyết định SLO | Objective và error-budget policy được chủ sản phẩm/ops chấp nhận | Metric không đại diện hành trình người dùng; mục tiêu đặt sau khi xem kết quả |
| Thu telemetry có giới hạn | Schema, allowlist/redaction, retention, access, cardinality/cost budget | Canary secret/PII tới exporter; queue/drop hoặc metric cardinality vượt ngân sách |
| Phát hiện và xử lý sự cố | Alert rule fixtures, routing/ack, timeline incident, escalation | Alert tạo đúng nhưng không đến nơi/không được nhận; silence không hết hạn |
| Phục hồi | Backup ID, restore receipt, RPO/RTO mục tiêu/đo được, kết quả nghiệp vụ | Snapshot tồn tại nhưng key/quyền/dependency không khôi phục được |

Không có một bộ công cụ bắt buộc cho mọi xưởng: service nhỏ có thể bắt đầu từ metrics có chủ sở hữu, log có cấu trúc và restore drill. Chỉ thêm tracing/SLO operator/chaos khi chúng giải một failure mode đã xác định.

## 2. Chọn công cụ theo quyết định cần đưa ra

| Nhiệm vụ | Lựa chọn đã đọc | So với lựa chọn khác | Điều kiện vận hành |
|---|---|---|---|
| Chuẩn hoá/giới hạn telemetry trước exporter | OpenTelemetry Collector Contrib, phạm vi redaction processor | OTel SDK tại source giảm dữ liệu từ đầu; filter/transform processor phục vụ policy khác, không tự có cùng semantics | Distribution phải chứa component, pipeline phải thực sự tham chiếu processor đúng thứ tự |
| Generate SLO rules theo GitOps/CI | Sloth | Pyrra nếu cần UI/budget view; rule Prometheus viết tay nếu số SLO rất nhỏ | Pin generator/plugins; validate, rule tests rồi rollout; YAML hợp lệ không chứng minh SLI đúng |
| SLO UI + operator/FS backend | Pyrra | Sloth ưu tiên compilation/CLI; Prometheus/Grafana dùng trực tiếp nếu chưa cần operator | RBAC, rule discovery và query backend phải khớp; kiểm cardinality khi grouping |
| Backup file/object | [restic ở mục 09](../09-engineering-checklists/README.md#operations-recovery-cost-evidence) | Snapshot của storage/DB hoặc Velero theo môi trường | Metadata check khác đọc payload và khác restore ứng dụng; bảo vệ key và retention |
| Backup Kubernetes resource/PV | [Velero ở mục 09](../09-engineering-checklists/README.md#operations-recovery-cost-evidence) | Backup native DB cho tính nhất quán nghiệp vụ | Restore cả service dependency và kiểm record/transaction; không chỉ đếm pod Running |

## 3. Hồ sơ đọc mã

<a id="otel-collector-egress"></a>

### 3.1 OpenTelemetry Collector Contrib: telemetry egress có policy cụ thể

| Thuộc tính | Giá trị |
|---|---|
| Repo / tổ chức | [open-telemetry/opentelemetry-collector-contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib), dự án OpenTelemetry |
| Phiên bản / license | `970f597792f2e60786e480dad4598b1078ba5627` · Apache-2.0 · đọc 2026-11-04 |
| Phạm vi `code-read` | `processor/redactionprocessor`: config → factory cho traces/logs/metrics → `processAttrs` và xử lý log body; đọc metadata/CI |
| Cơ chế | Allowlist loại key không được phép trước value masking; `ignored_keys`/`ignored_key_patterns` được giữ và bỏ qua xử lý; `allowed_values` có ưu tiên cho phép so với mask. Factory gắn các hàm xử lý vào pipeline khi processor được cấu hình. |
| Độ ổn định component | `metadata.yaml`: traces beta, logs/metrics alpha ở SHA đã đọc; mức ổn định của Collector nói chung không áp tự động cho mọi processor. |
| Giá trị cho xưởng | Tập trung egress policy, giữ cùng schema/allowlist ở nhiều dịch vụ, có thể thử canary PII và contract fixtures trước khi đổi config. |
| Rủi ro / dữ liệu rời máy | Exporter quyết định đích; telemetry vẫn có thể chứa nội dung nghiệp vụ. Bật `allow_all_keys`, thêm ignore quá rộng hoặc policy không bao phủ kiểu dữ liệu làm thay đổi bảo vệ. Regex không phải bằng chứng đã ẩn danh mọi PII. |
| Tích hợp | Pin distribution/version và config; kiểm component có trong binary; đặt redaction trước exporter và thử cả resource/scope/span/log body/metric attributes. `summary: debug` có thể lộ tên key; quyết định rõ summary/retention, không bật vì nghĩ chỉ là diagnostic vô hại. |
| Giới hạn | Chưa audit tất cả receiver/exporter, bảo vệ mạng/auth hay mọi loại payload. Không suy default allowlist của một processor bảo vệ pipeline chưa cài nó. |

**Bằng chứng:** [LICENSE](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/970f597792f2e60786e480dad4598b1078ba5627/LICENSE) · [processor/redactionprocessor/README.md](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/970f597792f2e60786e480dad4598b1078ba5627/processor/redactionprocessor/README.md) · [processor/redactionprocessor/config.go](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/970f597792f2e60786e480dad4598b1078ba5627/processor/redactionprocessor/config.go) · [processor/redactionprocessor/processor.go](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/970f597792f2e60786e480dad4598b1078ba5627/processor/redactionprocessor/processor.go) · [processor/redactionprocessor/factory.go](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/970f597792f2e60786e480dad4598b1078ba5627/processor/redactionprocessor/factory.go) · [processor/redactionprocessor/metadata.yaml](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/970f597792f2e60786e480dad4598b1078ba5627/processor/redactionprocessor/metadata.yaml) · [.github/workflows/build-and-test.yml](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/970f597792f2e60786e480dad4598b1078ba5627/.github/workflows/build-and-test.yml).

<a id="sloth-slo-generator"></a>

### 3.2 Sloth: SLO là source, Prometheus rule là artifact sinh ra

| Thuộc tính | Giá trị |
|---|---|
| Repo / tác giả | [slok/sloth](https://github.com/slok/sloth), cộng đồng Sloth; không suy bảo đảm hỗ trợ thương mại |
| Phiên bản / license | `dfab41f326c042e75f9cf7262ef66d19a755cb54` · Apache-2.0 · đọc 2026-11-04 |
| Cơ chế | CLI `generate` đi vào generator, sinh recording rules/metadata và multiwindow multi-burn alerts. `validate` gọi generator, kiểm spec và SLO trùng ID; trả lỗi khi validation fail. Không chỉ parse YAML. |
| Default cần biết | CLI dùng SLO period mặc định `30d`; có flag tắt recording/alert/default plugins và thêm plugin. Config được chọn mới là hợp đồng thật, không suy mọi mode có cùng cổng. |
| Giá trị cho xưởng | Review mục tiêu/SLI như code, tạo artifact nhất quán giữa service, giảm copy-paste PromQL và drift giữa dashboard/alert. |
| CI đã đọc | Unit/check, CLI integration và Kubernetes integration; workflow không được tự chạy ở kho này. |
| Rủi ro | Generator hợp lệ vẫn có thể dùng sai denominator hoặc loại bỏ nhóm lỗi; plugin mở rộng có quyền thực thi/biến đổi trong môi trường CI và phải được review/pin. Các objective 99.x chỉ là ví dụ, không phải SLA mẫu. |
| Tích hợp | Lưu source SLO và phiên bản generator/plugins; validate → generate → kiểm rules bằng Prometheus tooling/fixtures → diff artifact → rollout → kiểm alert routing/ack. Negative fixture phải làm cổng đỏ. |
| Thay thế | Pyrra nếu cần operator/UI; rule viết tay khi ít service; dịch vụ SLO managed khi chấp nhận data flow/cost và khóa nền tảng. |

**Bằng chứng:** [LICENSE](https://github.com/slok/sloth/blob/dfab41f326c042e75f9cf7262ef66d19a755cb54/LICENSE) · [README.md](https://github.com/slok/sloth/blob/dfab41f326c042e75f9cf7262ef66d19a755cb54/README.md) · [cmd/sloth/commands/generate.go](https://github.com/slok/sloth/blob/dfab41f326c042e75f9cf7262ef66d19a755cb54/cmd/sloth/commands/generate.go) · [cmd/sloth/commands/validate.go](https://github.com/slok/sloth/blob/dfab41f326c042e75f9cf7262ef66d19a755cb54/cmd/sloth/commands/validate.go) · [internal/app/generate/generate.go](https://github.com/slok/sloth/blob/dfab41f326c042e75f9cf7262ef66d19a755cb54/internal/app/generate/generate.go) · [internal/plugin/slo/core/alert_rules_v1/plugin.go](https://github.com/slok/sloth/blob/dfab41f326c042e75f9cf7262ef66d19a755cb54/internal/plugin/slo/core/alert_rules_v1/plugin.go) · [.github/workflows/ci.yaml](https://github.com/slok/sloth/blob/dfab41f326c042e75f9cf7262ef66d19a755cb54/.github/workflows/ci.yaml).

<a id="pyrra-slo-operations"></a>

### 3.3 Pyrra: SLO có UI và vòng reconcile, vẫn phải kiểm đích thật

| Thuộc tính | Giá trị |
|---|---|
| Repo / tổ chức | [pyrra-dev/pyrra](https://github.com/pyrra-dev/pyrra), cộng đồng Pyrra |
| Phiên bản / license | `a71aef6f7dd9e2774662211a805af5ab54445216` · Apache-2.0 · đọc 2026-11-04 |
| Cơ chế | `slo/rules.go` tạo burn-rate recording/alert rules từ Objective. Kubernetes reconciler tạo/cập nhật `PrometheusRule`, hoặc ConfigMap/Mimir theo mode; README còn có filesystem backend cho ngoài Kubernetes. |
| Giá trị | UI xem objective, error budget và burn rate; đưa SLO cho người vận hành/sản phẩm thay vì chỉ giữ PromQL trong repo. |
| Giới hạn đường gọi | Có lựa chọn tắt alerting/burnrates; controller cập nhật resource không chứng minh Prometheus đã discover/evaluate rule hay notification đến on-call. |
| CI | Workflow Go dùng version từ `go.mod`, gọi `make test`/`make pyrra`; không lấy biến môi trường cũ trong workflow làm version runtime thật. Chưa chạy test hoặc UI. |
| Dữ liệu / quyền | Query Prometheus/backend, cấp quyền reconcile tài nguyên; grouping tạo thêm series. Không thu user ID/raw URL làm label chỉ để drill-down dễ hơn. |
| Tích hợp | Service owner định nghĩa indicator/target/window; kiểm grouping/label routing, RBAC tối thiểu và namespace; sau reconcile kiểm rule được evaluate và alert tới kênh thử, có ack và auto-resolve. |
| Thay thế | Sloth cho compile rules; Prometheus + Grafana/alert rules trực tiếp nếu quy mô nhỏ; managed SLO khi chấp nhận provider. Không cần chạy hai generator cho cùng SLO. |

**Bằng chứng:** [LICENSE](https://github.com/pyrra-dev/pyrra/blob/a71aef6f7dd9e2774662211a805af5ab54445216/LICENSE) · [README.md](https://github.com/pyrra-dev/pyrra/blob/a71aef6f7dd9e2774662211a805af5ab54445216/README.md) · [slo/rules.go](https://github.com/pyrra-dev/pyrra/blob/a71aef6f7dd9e2774662211a805af5ab54445216/slo/rules.go) · [kubernetes/controllers/servicelevelobjective.go](https://github.com/pyrra-dev/pyrra/blob/a71aef6f7dd9e2774662211a805af5ab54445216/kubernetes/controllers/servicelevelobjective.go) · [.github/workflows/go.yaml](https://github.com/pyrra-dev/pyrra/blob/a71aef6f7dd9e2774662211a805af5ab54445216/.github/workflows/go.yaml).

## 4. Đường vận hành có thể kiểm lại

1. **Trước release:** chốt SLI/SLO theo hành trình người dùng, owner, dependency map, RPO/RTO và action khi error budget cạn. Đo đúng/thời gian/chi phí tách nhau; model response quality ở mục 07 bổ sung cho service SLO.
2. **Trước export:** fixture chứa canary secret, PII dạng string/số/nested, label cardinality và payload quá lớn. Kiểm ở **đích nhận thử** sau toàn bộ pipeline; chỉ unit test regex không phủ mapping/exporter. Lưu input/output/config hash và mẫu đã che.
3. **Trước đổi alert:** compiler + PromQL/rule fixtures có healthy, fast burn, slow burn, thiếu traffic và thiếu series. Quy định khi data thiếu là unknown hay incident; không tự coi mẫu rỗng là 100% thành công. Lưu số fixture, kỳ vọng và số alert phát sinh.
4. **Trong rollout:** đối chiếu canary/control bằng các metric đã chọn; log lý do tiếp tục/dừng. Rollback binary không tự đảo schema/data migration hoặc side effect đã commit; nối [mục 32](../32-platform-delivery-engineering/README.md) và [21](../21-autonomous-workflows/README.md).
5. **Khi incident:** alert phải có owner, runbook, customer impact, deploy/dataset/model revision; diễn tập nhận thông báo/ack/escalation và khôi phục dịch vụ. Viết timeline, điều gì chưa biết, action có người chịu trách nhiệm; không dùng số MTTR nhỏ để che sự cố bỏ sót.
6. **Sau restore:** khôi phục ở môi trường tách biệt với production, có khoá/quyền/dependency cần thiết; kiểm record nghiệp vụ, referential integrity, queue/outbox và tenant isolation. Ghi RPO/RTO **đo được**, backup ID và thời điểm cắt dữ liệu; không suy từ lịch backup hoặc pod Running.

Chaos/fault injection bắt đầu từ một giả thuyết và phạm vi nhỏ: worker chết, provider timeout, telemetry exporter nghẽn hay storage mất quyền. Có abort condition, owner và đường khôi phục; thử ở môi trường phù hợp rủi ro. Đợt nghiên cứu này chưa chạy chaos, kiểm alert routing, tải telemetry hay restore drill nên không gọi bất cứ stack nào “production-ready”.

## 5. Nguồn và giới hạn khảo sát

Nguồn ghim SHA trong §3 là source/LICENSE/CI chính thức đã đọc; so sánh Restic/Velero dẫn hồ sơ có bằng chứng ở mục 09, không tạo thực thể trùng. Không dùng sao làm điểm chất lượng. API GitHub trực tiếp bị proxy từ chối ở lượt đọc này, nên không bổ sung số sao hay kết luận archived/bảo trì từ việc clone thành công. Benchmark, hiệu quả alert và khả năng chịu tải ngoài phạm vi chưa được xác minh.
