# 31 · Bảo mật chuỗi cung ứng phần mềm và bằng chứng phát hành

> Khép đường từ source và dependency đến artifact được phép chạy: biết thành phần, phát hiện rủi ro, kiểm nguồn gốc và đưa quyết định policy vào CI/deploy. Đây là chuỗi cung ứng phần mềm nói chung; hành vi LLM/tool xem [mục 12](../12-ai-security-guardrails/README.md).

## 1. Trần cần đạt cho xưởng phần mềm

Một repo xanh CI chưa trả lời artifact nào đang chạy, do builder nào tạo, dùng dependency nào, ai phê duyệt ngoại lệ hay bản nào phải thu hồi khi có CVE mới. Xưởng cần gắn source SHA → dependency lock → build identity → artifact digest → SBOM/provenance → policy decision → deployment inventory. Agent có thể đề xuất bản vá; quyền bỏ qua cổng và trust root phải độc lập với tác vụ viết code.

**Ngày đọc:** 2026-11-04. Ba hồ sơ dưới được đọc LICENSE, implementation/callsite và CI tại full SHA. Không cài/chạy upstream, không quét sản phẩm và không tái lập benchmark; số sao để trống. License trong bảng áp dụng code của repo đã đọc, không tự bao phủ dependency, dữ liệu advisory hoặc dịch vụ kết nối.

| Lớp | Công cụ đã có trong kho | Nâng sâu ở mục này |
|---|---|---|
| Secret/SAST | Gitleaks, TruffleHog, Semgrep, CodeQL | Phủ cả history/artifact, baseline có expiry và phát hiện secret phải đi kèm rotation |
| SCA/SBOM | OSV-Scanner, Trivy, Grype, Syft | Gắn SBOM đúng digest; phân biệt scan một lần với theo dõi sau phát hành |
| Provenance/signature | SLSA, cosign | Xác minh builder/issuer/subject/digest và chính sách thực thi, không chỉ có chữ ký |
| Supply-chain workflow | in-toto | Ràng buộc các bước, người ký và artifact materials/products |
| Portfolio/triage | OWASP Dependency-Track | Theo dõi component qua nhiều phiên bản sản phẩm và policy |
| Graph quan hệ | GUAC | Truy vấn phạm vi ảnh hưởng; giữ trust decision riêng với việc ingest |

## 2. Ba hồ sơ đọc mã mới

<a id="factory-2026-11-04-in-toto"></a>

### 2.1 in-toto: layout, người ký và chuỗi materials/products

| Thuộc tính | Kết quả đọc |
|---|---|
| Repo · license · SHA | `in-toto/in-toto` · Apache-2.0 · `e352b43ad7cb8915d84c36d791aa61346152a0a3` |
| Tác giả/quản trị | Dự án in-toto; LICENSE ghi New York University và repository có GOVERNANCE/MAINTAINERS. Đây là Python implementation, không đồng nhất với mọi in-toto attestation consumer |
| Cơ chế | Chủ chuỗi ký layout gồm steps, functionary keys, thresholds, artifact rules và inspections; mỗi bước có link metadata chứa materials/products và chữ ký |
| Enforcement | `in_toto_verify` kiểm layout signatures/expiry, link signatures, thresholds và rules trước khi chạy inspections; CLI trả 1 khi verification thất bại, 2 khi tham số sai |
| Hai bẫy quan trọng | Artifact không bị rule tiêu thụ mặc định được phép; cần terminal `DISALLOW *` khi policy muốn đóng tập. Command alignment là **soft verify**, mismatch chỉ ghi warning trong Python implementation đã đọc, không tự làm verification fail |
| Ranh giới | Chỉ artifact được truyền làm materials/products mới được ghi; không tự quan sát mọi file đã đọc/ghi. Chữ ký không bảo đảm người ký/builder trung thực. Inspections là lệnh thực thi từ layout đã được tin cậy, nên verifier cũng cần scope/quyền nhỏ |
| Tích hợp | Với chuỗi build nhỏ, chốt layout/key custody và rule MATCH giữa từng bước; review negative fixtures thiếu link, sai signer, đổi digest, file phát sinh ngoài policy, layout hết hạn. Command bắt buộc phải được kiểm bằng policy/inspection riêng thay vì tin expected_command |
| CI | `ci.yml` gọi `_test.yml`: tox trên nhiều OS/Python, một nhánh dependency-main là experimental. Chưa chạy các test này tại kho |

**Nguồn:** [LICENSE](https://github.com/in-toto/in-toto/blob/e352b43ad7cb8915d84c36d791aa61346152a0a3/LICENSE) · [layout/rules README](https://github.com/in-toto/in-toto/blob/e352b43ad7cb8915d84c36d791aa61346152a0a3/README.md) · [verify callsite](https://github.com/in-toto/in-toto/blob/e352b43ad7cb8915d84c36d791aa61346152a0a3/in_toto/verifylib.py) · [CLI outcomes](https://github.com/in-toto/in-toto/blob/e352b43ad7cb8915d84c36d791aa61346152a0a3/in_toto/in_toto_verify.py) · [CI](https://github.com/in-toto/in-toto/blob/e352b43ad7cb8915d84c36d791aa61346152a0a3/.github/workflows/_test.yml).

<a id="factory-2026-11-04-owasp-dependency-track"></a>

### 2.2 OWASP Dependency-Track: SBOM là đầu vào cho quản trị rủi ro liên tục

| Thuộc tính | Kết quả đọc |
|---|---|
| Repo · license · SHA | `DependencyTrack/dependency-track` · Apache-2.0 · `2e3fd965a76bbfdd9e7ec1fb990600cc1f4f11ba` |
| Quản trị/phạm vi | Dự án OWASP, quản lý component theo project/version; frontend và tài liệu là repository riêng. Nguồn đọc là nhánh main hiện có, không tự suy mọi image/tag v4/v5 cùng API |
| Đường gọi | `BomResource` nhận SBOM và trả token theo dõi xử lý; `EventResource` đọc workflow status; `CelPolicyEngine` biên dịch/đánh giá điều kiện policy và tạo policy violations |
| Bẫy CI | Upload HTTP thành công không phải phân tích thành công. Endpoint BOM token cũ nêu rõ `processing=false` còn có thể là token không tồn tại; endpoint cũ deprecated, phải dùng API đúng phiên bản và kiểm terminal status, project/version cùng policy result |
| Vận hành | Có state/database và nguồn advisory ngoài; cần backup/restore, quyền API theo project, khả năng reach feed và tuổi feed. Migration v4/v5 phải đọc tài liệu cutover rồi pin image/digest; không đổi tag latest mà không chủ ý |
| Tích hợp | Upload CycloneDX cho đúng release digest; chờ kết quả có timeout/error rõ; query policy violations đã hoàn tất rồi adapter CI quyết định chặn. Theo dõi lại các bản còn chạy khi advisory thay đổi, không chỉ scan lúc merge |
| CI | `ci-test.yaml` chạy Maven/JDK và có workflow E2E riêng; chưa triển khai server hoặc chạy kiểm tích hợp |

**Nguồn:** [LICENSE](https://github.com/DependencyTrack/dependency-track/blob/2e3fd965a76bbfdd9e7ec1fb990600cc1f4f11ba/LICENSE.txt) · [BOM upload/token](https://github.com/DependencyTrack/dependency-track/blob/2e3fd965a76bbfdd9e7ec1fb990600cc1f4f11ba/apiserver/src/main/java/org/dependencytrack/resources/v1/BomResource.java) · [event status](https://github.com/DependencyTrack/dependency-track/blob/2e3fd965a76bbfdd9e7ec1fb990600cc1f4f11ba/apiserver/src/main/java/org/dependencytrack/resources/v1/EventResource.java) · [policy enforcement](https://github.com/DependencyTrack/dependency-track/blob/2e3fd965a76bbfdd9e7ec1fb990600cc1f4f11ba/apiserver/src/main/java/org/dependencytrack/policy/cel/CelPolicyEngine.java) · [migration contract](https://github.com/DependencyTrack/dependency-track/blob/2e3fd965a76bbfdd9e7ec1fb990600cc1f4f11ba/V5_MIGRATION.md) · [CI](https://github.com/DependencyTrack/dependency-track/blob/2e3fd965a76bbfdd9e7ec1fb990600cc1f4f11ba/.github/workflows/ci-test.yaml).

<a id="factory-2026-11-04-guac"></a>

### 2.3 GUAC: đồ thị phạm vi ảnh hưởng cần nguồn và trạng thái tin cậy

| Thuộc tính | Kết quả đọc |
|---|---|
| Repo · license · SHA | `guacsec/guac` · Apache-2.0 · `a3f0a4df51abcf271221cf9c400de3158d9c20fa` |
| Quản trị/phạm vi | README xác định là dự án OpenSSF incubating; tổng hợp SBOM, vulnerability và provenance thành quan hệ package/source/artifact |
| Cơ chế | Parser CycloneDX/SPDX/SLSA/DSSE đưa dữ liệu vào graph; graph phục vụ câu hỏi package/version/digest nào nằm trong sản phẩm nào và quan hệ nguồn gốc |
| Kiểm đường gọi | `pkg/ingestor/verifier/verifier.go` phân biệt identity đã verify với identity đáng tin. Trong DSSE parser tại SHA này, `GetIdentities` trả mảng rỗng và phần đưa trust information vào graph còn TODO; không diễn giải ingest thành trust decision đầy đủ |
| Rủi ro | README tự nêu có trường hợp phải dùng heuristic nối identifier; thiếu/sai purl/digest có thể làm thiếu hoặc nối nhầm quan hệ. Graph không tự thay việc verify artifact tại deploy |
| Vận hành | README phân biệt in-memory keyvalue với persistent ent/PostgreSQL; backend thử nghiệm/không hỗ trợ không nên được coi tương đương production. Ingestor/collector có thể gọi dịch vụ metadata ngoài; kiểm dữ liệu được gửi theo deployment |
| Tích hợp | Giữ origin, ingest time và evidence digest; truy vấn tác động cho CVE/namespace/version cụ thể; đối chiếu với deployment inventory. Gate release vẫn phải xác minh signer/builder/digest bằng verifier đã chốt trust root |
| CI | `ci.yaml` có Go unit tests/static analysis/lint; chưa chạy graph hay kiểm độ đầy đủ của truy vấn trong đợt này |

**Nguồn:** [LICENSE](https://github.com/guacsec/guac/blob/a3f0a4df51abcf271221cf9c400de3158d9c20fa/LICENSE) · [scope/backends](https://github.com/guacsec/guac/blob/a3f0a4df51abcf271221cf9c400de3158d9c20fa/README.md) · [verifier semantics](https://github.com/guacsec/guac/blob/a3f0a4df51abcf271221cf9c400de3158d9c20fa/pkg/ingestor/verifier/verifier.go) · [DSSE callsite](https://github.com/guacsec/guac/blob/a3f0a4df51abcf271221cf9c400de3158d9c20fa/pkg/ingestor/parser/dsse/parser_dsse.go) · [CycloneDX parser](https://github.com/guacsec/guac/blob/a3f0a4df51abcf271221cf9c400de3158d9c20fa/pkg/ingestor/parser/cyclonedx/parser_cyclonedx.go) · [CI](https://github.com/guacsec/guac/blob/a3f0a4df51abcf271221cf9c400de3158d9c20fa/.github/workflows/ci.yaml).

## 3. So sánh theo quyết định cần đưa ra

| Nhiệm vụ | Baseline nhỏ | Lựa chọn sâu hơn | Điểm không được đánh tráo |
|---|---|---|---|
| Biết thành phần của một image | Syft + SBOM theo digest | Dependency-Track khi nhiều release cần theo dõi | SBOM đầy đủ phụ thuộc cách build/detect; có file SBOM không chứng minh đầy đủ |
| Biết advisory ảnh hưởng gì | Grype / OSV-Scanner / Trivy | Dependency-Track portfolio hoặc GUAC graph | CVE match, exploitability và chấp nhận rủi ro là ba quyết định khác nhau |
| Xác minh artifact được phép dùng | cosign với issuer/subject/digest policy | in-toto khi cần ràng buộc nhiều bước/signer | Chữ ký hợp lệ không chứng minh code sạch hay builder không bị chiếm |
| Đánh giá upstream trước nhận dependency | OpenSSF Scorecard + đọc LICENSE/CI | Review release provenance, maintainer và sandbox build | Điểm Scorecard là tín hiệu, không phải giấy chứng nhận an toàn |
| Chặn policy của xưởng | Script tất định nhỏ/OPA-Conftest | Policy engine theo fleet khi có ownership rõ | Không để chính agent sửa threshold/allowlist để làm check xanh |

**Stack tối thiểu:** khóa dependency và tool → secret scan/SAST/SCA theo scope → build ở runner tách quyền → sinh SBOM/provenance gắn artifact digest → ký từ identity riêng → verify và đánh giá policy trước deploy → lưu inventory + theo dõi advisory sau phát hành. Chỉ thêm Dependency-Track khi có nhu cầu portfolio; chỉ thêm GUAC khi câu hỏi đồ thị liên repo có giá trị đủ bù chi phí vận hành. Không buộc mọi dự án nhỏ dựng đủ mọi dịch vụ.

## 4. Cổng nghiệm thu và bằng chứng phải giao cùng phần mềm

| Cổng | Fixture cố tình sai | Kỳ vọng kiểm được |
|---|---|---|
| Artifact identity | Thay byte artifact sau khi tạo SBOM/ký | Digest mismatch làm fail trước deploy |
| Signer/builder | Chữ ký đúng khóa nhưng issuer/subject/builder ngoài policy | Từ chối; không chỉ kiểm cryptographic validity |
| Supply-chain steps | Thiếu link hoặc sai functionary/threshold, tạo file ngoài rules | in-toto fail; test command mismatch có policy riêng vì native chỉ warning |
| Vulnerability/license | Component vi phạm policy, feed quá cũ hoặc scan timeout | Fail/inconclusive rõ; exception có owner, lý do, scope, expiry |
| Async analysis | Token rác, job thất bại, `processing=false` nhưng thiếu status | Không công nhận pass; so đúng project/version/release |
| Inventory/recall | CVE fixture ảnh hưởng bản cũ đang chạy | Truy ra deployment/owner và có cách rollback/rebuild |
| Secret exposure | Secret giả trong diff/history/artifact | Cổng phát hiện; quy trình incident có revoke/rotate, không chỉ xóa chuỗi khỏi HEAD |

Artifact bàn giao gồm source SHA, lock digest, builder identity, image/package digest, SBOM định dạng/version, provenance/signature bundle, policy version, kết quả checks và ngoại lệ còn hiệu lực. Giới hạn retention, quyền xem và log dữ liệu nhạy cảm phải được ghi theo sản phẩm. Backup/restore catalog và trust roots được diễn tập ở môi trường tích hợp; kho này chưa chứng minh khả năng đó.

## 5. Liên kết toàn xưởng và giới hạn nghiên cứu

- [09 · Checklist](../09-engineering-checklists/README.md): release checklist có owner và bằng chứng, không chỉ dấu tick.
- [11 · Sandbox](../11-browser-computer-use-sandbox/README.md): agent/PR không tin cậy không được cầm secret phát hành.
- [12 · AI Security](../12-ai-security-guardrails/README.md): prompt/tool injection và quyền agent là lớp bổ sung.
- [13 · Dev Stack](../13-dev-stack-devops/README.md): toolchain, build và release tái lập.
- [30 · Kiểm thử](../30-software-testing-quality/README.md): gate phải có test phủ định chứng minh nó bắt được lỗi.
- [32 · Delivery](../32-platform-delivery-engineering/README.md): deployment chỉ nhận digest đã verify; rollout/rollback có kiểm.

Ngày snapshot không phải ngày xác minh mọi hồ sơ cũ được dẫn. Phát hiện về parser/CLI chỉ áp dụng SHA đã đọc; chưa xác minh mọi cấu hình runtime, advisory feed, latency, độ phủ scanner hoặc tình trạng toàn bộ release. Không cộng các lớp thành một điểm an toàn duy nhất.
