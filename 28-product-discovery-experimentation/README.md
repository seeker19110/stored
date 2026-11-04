# 28 · Product Discovery, UX Research & Experimentation

Từ vấn đề người dùng đến quyết định sản phẩm có bằng chứng. Ngày đọc **2026-11-02**: đã đọc README/LICENSE, workflow kiểm và các file triển khai dẫn trong hồ sơ; **chưa triển khai dịch vụ, bắt gói SDK hoặc chạy thí nghiệm người dùng**.

## 1. Chuỗi quyết định trước khi chọn công cụ

| Câu hỏi | Phương pháp / công cụ | Bằng chứng cần giữ |
|---|---|---|
| Người dùng đang gặp khó ở đâu? | Phỏng vấn, quan sát công việc, khảo sát có mục tiêu | Tuyển mẫu, consent, ghi nhận ẩn danh, phân biệt quan sát với diễn giải |
| Giải pháp có dễ dùng? | Prototype + usability test theo tác vụ | Completion, lỗi, thời gian, hỗ trợ cần dùng; người dùng đích và người khuyết tật |
| Hành vi thực tế thế nào? | PostHog/funnel/cohort; replay khi cần | Event dictionary, mẫu số, identity, phiên bản tracking, tỷ lệ thiếu event |
| Thay đổi có tạo tác động? | GrowthBook/experiment engine + assignment/exposure log | Hypothesis, randomization unit, sample size/MDE, guardrails, SRM |
| Phát hành có kiểm soát? | Unleash/feature flags | Rollout, kill switch, owner/expiry, rollback đã diễn tập |
| Vì sao người dùng bỏ cuộc? | Formbricks + replay đã che dữ liệu | Ngữ cảnh khảo sát, selection bias, giới hạn capture và retention |

[Mục 06](../06-ui-ux-design/README.md) kiểm chất lượng UI; [07](../07-eval-observability/README.md) kiểm AI; mục này kiểm **người dùng có hoàn thành công việc tốt hơn không**. Chỉ số model tốt hơn chưa đủ để kết luận sản phẩm tốt hơn.

## 2. Hồ sơ công cụ

### PostHog

| Thuộc tính | Giá trị |
|---|---|
| Repo | [PostHog/posthog](https://github.com/PostHog/posthog) |
| Snapshot | 40,593★, chưa archive (GitHub API, 2026-11-02); HEAD `1df14a1b82c7` ngày 2026-11-02 |
| License | MIT (core); proprietary (ee); [file thật](https://github.com/PostHog/posthog/blob/1df14a1b82c7a24e0a4a0d19b7c708c9e76ee9a5/LICENSE) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/PostHog/posthog/blob/1df14a1b82c7a24e0a4a0d19b7c708c9e76ee9a5/products/feature_flags/backend/models/feature_flag.py); [CI tại cùng commit](https://github.com/PostHog/posthog/tree/1df14a1b82c7a24e0a4a0d19b7c708c9e76ee9a5/.github/workflows); đọc mã/đặc tả, chưa chạy |

Nền tảng analytics/replay/flags/experiments. Model feature flag có validation cho variants và eligibility; kết hợp hành vi và thử nghiệm, nhưng không thay thiết kế nghiên cứu hay metric contract.

**Tích hợp và giới hạn:** README chỉ hướng tự host hobby và không bảo đảm hỗ trợ deployment mở. LICENSE loại ee; kiểm feature/tài nguyên theo edition. SDK/capture endpoint/retention cần audit riêng; không suy self-host thành mọi dữ liệu không rời mạng.

### GrowthBook

| Thuộc tính | Giá trị |
|---|---|
| Repo | [growthbook/growthbook](https://github.com/growthbook/growthbook) |
| Snapshot | 8,556★, chưa archive (GitHub API, 2026-11-02); HEAD `0553a68def70` ngày 2026-10-30 |
| License | MIT (core); GrowthBook Enterprise License (enterprise dirs); [file thật](https://github.com/growthbook/growthbook/blob/0553a68def700abbcaaca8f5096da913f197804c/LICENSE) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/growthbook/growthbook/blob/0553a68def700abbcaaca8f5096da913f197804c/packages/sdk-js/src/GrowthBook.ts); [CI tại cùng commit](https://github.com/growthbook/growthbook/tree/0553a68def700abbcaaca8f5096da913f197804c/.github/workflows); đọc mã/đặc tả, chưa chạy |

SDK có trackingCallback/onFeatureUsage và state assignment; code trả sớm khi thiếu callback. Do đó chọn biến thể và ghi exposure thành công là hai việc phải kiểm riêng. CI có test thống kê và backend/frontend.

**Tích hợp và giới hạn:** SDK + event/warehouse/analysis; kiểm stable subject ID, sticky assignment và callback dedupe. Một flag được bật không chứng minh tác động có ý nghĩa; enterprise backend/frontend/shared là license riêng.

### Formbricks

| Thuộc tính | Giá trị |
|---|---|
| Repo | [formbricks/formbricks](https://github.com/formbricks/formbricks) |
| Snapshot | 13,211★, chưa archive (GitHub API, 2026-11-02); HEAD `76b05fb98dd8` ngày 2026-11-02 |
| License | AGPL-3.0 (core); MIT (SDKs); proprietary (ee); [file thật](https://github.com/formbricks/formbricks/blob/76b05fb98dd870000d820ad8a27527e483dcfbb0/LICENSE) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/formbricks/formbricks/blob/76b05fb98dd870000d820ad8a27527e483dcfbb0/apps/web/lib/response/service.ts); [CI tại cùng commit](https://github.com/formbricks/formbricks/tree/76b05fb98dd870000d820ad8a27527e483dcfbb0/.github/workflows); đọc mã/đặc tả, chưa chạy |

Khảo sát link/web/in-app phục vụ phản hồi có ngữ cảnh. Service response giữ status finished, language, contact/meta và file upload; phân tích cần tách đáp án hoàn thành, bỏ dở và selection bias.

**Tích hợp và giới hạn:** SDK/API/export nối kho dữ liệu; hạn chế PII/file upload, consent và retention. LICENSE tách core, SDK và ee; không suy nhãn AGPL toàn repo hay mọi feature tự host đều miễn phí.

### OpenReplay

| Thuộc tính | Giá trị |
|---|---|
| Repo | [openreplay/openreplay](https://github.com/openreplay/openreplay) |
| Snapshot | 13,087★, chưa archive (GitHub API, 2026-11-02); HEAD `9f1dcebfa5bd` ngày 2026-10-30 |
| License | AGPL-3.0 (default); MIT (một số thư mục); proprietary (ee); [file thật](https://github.com/openreplay/openreplay/blob/9f1dcebfa5bd98967c902b77b8fe7ed120ab5b2b/LICENSE) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/openreplay/openreplay/blob/9f1dcebfa5bd98967c902b77b8fe7ed120ab5b2b/tracker/tracker/src/main/app/sanitizer.ts); [CI tại cùng commit](https://github.com/openreplay/openreplay/tree/9f1dcebfa5bd98967c902b77b8fe7ed120ab5b2b/.github/workflows); đọc mã/đặc tả, chưa chạy |

Session replay có sanitizer cho DOM. Mã default privateMode=false, obscureTextEmails=true và obscureTextNumbers=false; cơ chế masking tồn tại không đồng nghĩa mọi nội dung mặc định đã che.

**Tích hợp và giới hạn:** Bật private mode/masking có kiểm bằng dữ liệu giả; xét input, DOM/shadow DOM, URL/network/plugin và quyền xem replay. LICENSE nhiều lớp; chưa bắt gói hay đánh giá capture end-to-end.

### Unleash

| Thuộc tính | Giá trị |
|---|---|
| Repo | [Unleash/unleash](https://github.com/Unleash/unleash) |
| Snapshot | 13,924★, chưa archive (GitHub API, 2026-11-02); HEAD `92cf79aad5d1` ngày 2026-11-02 |
| License | AGPL-3.0; [file thật](https://github.com/Unleash/unleash/blob/92cf79aad5d18e04cf72909e31f9b35a7840c355/LICENSE) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/Unleash/unleash/blob/92cf79aad5d18e04cf72909e31f9b35a7840c355/src/lib/features/playground/feature-evaluator/strategy/unknown-strategy.ts); [CI tại cùng commit](https://github.com/Unleash/unleash/tree/92cf79aad5d18e04cf72909e31f9b35a7840c355/.github/workflows); đọc mã/đặc tả, chưa chạy |

Feature management/rollout có SDK và strategy evaluation. Playground báo incomplete/unknown với custom strategy không thể đánh giá offline; trạng thái này không được đổi thành passed.

**Tích hợp và giới hạn:** SDK/server flag evaluation cần identity/context consistent, fallback khi mất server và kill switch. Server AGPL; edition Enterprise và license SDK kiểm riêng. Flag là cơ chế rollout, không thay authorization hoặc bằng chứng nhân quả.

## 3. Chuẩn phương pháp và cổng quyết định

Hướng dẫn gốc [GOV.UK: lập kế hoạch nghiên cứu](https://www.gov.uk/service-manual/user-research/plan-user-research-for-your-service) yêu cầu nghiên cứu theo người dùng/tác vụ thực tế. [Đo thành công dịch vụ](https://www.gov.uk/service-manual/measuring-success/measuring-the-success-of-your-service) kết hợp metric với nghiên cứu định tính. Đây là hướng dẫn phương pháp, không phải một chứng nhận tự động cho sản phẩm.

[Microsoft Research: trước thí nghiệm](https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-pre-experiment-stage/) và [sau thí nghiệm](https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-post-experiment-stage/) là nguồn cho data quality/guardrails và kiểm SRM. Phần vận dụng dưới đây là tiêu chí đề xuất của kho:

1. **Trước thu dữ liệu:** nêu quyết định cần đưa ra, phân khúc người dùng, metric chính và guardrails; chọn đúng đơn vị randomization (user/account/team). Phân tích power/MDE trước; lưu chính sách dừng và phương pháp thống kê, không nhìn p-value mỗi ngày bằng kiểm fixed-horizon rồi tự dừng khi xanh.
2. **Tracking contract:** định nghĩa event/schema/version, timestamp, event ID chống gửi trùng, subject ID và trạng thái consent. Assignment khác exposure; log việc người dùng thật sự được thấy treatment. Không gửi prompt/tài liệu/PII mặc định để làm analytics.
3. **Kiểm instrumentation:** event test, join rate, missing/duplicate event, A/A và SRM theo phương pháp đã chọn. Khác mẫu số hoặc attribution window thì không so trực tiếp hai dashboard.
4. **Khi chạy:** theo dõi crash/latency/chi phí/hỗ trợ và metric gây hại theo phân khúc; feature flag có đường tắt và kill switch. Kiểm tenant isolation và quyền xem replay, thời hạn retention/xóa dữ liệu.
5. **Khi kết luận:** báo effect size, khoảng bất định, cỡ mẫu, dữ liệu loại bỏ, ảnh hưởng guardrail và kết quả chưa đủ lực thống kê. Không có ý nghĩa thống kê không chứng minh hai phương án tương đương.
6. **Với AI:** giữ offline task eval + safety ở [07](../07-eval-observability/README.md)/[12](../12-ai-security-guardrails/README.md), bổ sung task completion/acceptance, tỷ lệ sửa tay, time-to-value, retention theo cohort, chi phí mỗi tác vụ được chấp nhận. Tách thay model khỏi thay UI khi cần biết nguyên nhân.

## 4. Stack ghép và giới hạn lựa chọn

- **Nhóm nhỏ, chưa có traffic đủ:** nghiên cứu định tính + usability + event tối thiểu; có thể dùng Formbricks. Không cần triển khai tất cả nền tảng để bắt đầu.
- **Đã có warehouse/event tốt:** GrowthBook + SDK/exposure callback + dữ liệu hiện có; test consistency giữa server/client và assignment sau login.
- **Cần điều tra hành trình:** PostHog hoặc OpenReplay tùy nhu cầu; kiểm masking bằng dữ liệu giả trước capture thật. Self-host chỉ là vị trí triển khai, chưa chứng minh mọi SDK/integration giữ dữ liệu trong mạng.
- **Cần rollout tin cậy:** Unleash + owner/expiry + kill switch; flag không thay transaction hoặc authorization. Nối với [13](../13-dev-stack-devops/README.md), [15](../15-ai-for-data/README.md), [21](../21-autonomous-workflows/README.md).

<a id="factory-2026-11-04"></a>

## 5. Nâng trần 4/11/2026: hợp đồng thử nghiệm độc lập nhà cung cấp và đo giá trị của xưởng

**Trần hiện tại:** §3 đã có A/A, SRM, exposure và metric. Khoảng thiếu là cách đưa chúng vào hợp đồng phát hành: tách flag evaluation, exposure và phân tích; đo đầu ra được khách hàng chấp nhận, không chỉ số code/PR do agent tạo. Phần metric/gate là thiết kế đề xuất, chưa chạy A/B hoặc đo ROI tại kho này.

| Lựa chọn | Khi hợp | Cần nối thêm | Giới hạn |
|---|---|---|---|
| PostHog ở §2 | Analytics/replay/flags trong cùng nền tảng | Event dictionary, consent, masking, phân quyền/retention | Tự host không tự chứng minh SDK/integration không gửi dữ liệu ngoài |
| GrowthBook ở §2 | Experiment gắn warehouse và assignment/exposure | Callback, metric model, audit query, unit randomization | Callback có trong mã chưa chứng minh event tới kho dữ liệu |
| Unleash ở §2 | Quản trị flag/rollout có owner và kill switch | Analytics/experiment engine độc lập | Flag không thay authorization hoặc bằng chứng nhân quả |
| OpenFeature + flagd dưới đây | Cần giao diện evaluation và daemon có thể thay provider | Cấu hình flag, SDK provider, exposure pipeline, phân tích thống kê | Không phải toàn bộ nền tảng A/B và không tự giải SRM/power |

<a id="flagd"></a>

### flagd: bucketing có hợp đồng, chưa phải kết luận thử nghiệm

| Thuộc tính | Giá trị |
|---|---|
| Repo / SHA / license | [open-feature/flagd](https://github.com/open-feature/flagd), `902555686f8bb1a89fe40c4b532e78c4e098110d`, Apache-2.0 |
| Kiểm chứng 2026-11-04 | `code-read`: evaluator JSON/fractional, LICENSE/README và `build.yaml`; chưa chạy daemon/provider hoặc kiểm tương đương SDK |
| Cơ chế đã đọc | `fractional.go` phân biệt explicit hashing input với nhánh implicit; nhánh implicit dùng `[flagKey, targetingKey]`, từ chối missing/null/non-string/empty `targetingKey`. Do đó không ghi "mọi rollout đều bắt buộc targetingKey": input explicit là đường khác. |
| CI | `build.yaml` chạy `make test` và có lane FIPS; không suy nhãn FIPS trong workflow thành chứng nhận hệ triển khai hoặc mọi bản phân phối. |
| Tích hợp | Ghim daemon/provider/schema/flag version và context; lập fixture assignment cho cùng subject qua client/server, login, restart, đổi rule. Định nghĩa fallback khi mất nguồn hoặc lỗi evaluation; ghi reason/error cùng exposure, không chỉ giá trị boolean. |
| Giới hạn | Percentage rollout không tự là randomization đúng ở cấp account/team; thay key hoặc rule có thể đổi tập nhận. Cần phân tích thống kê và pipeline exposure riêng. Không dùng feature flag làm cổng quyền truy cập dữ liệu. |

**Hợp đồng từ khám phá đến phát hành:**

1. Chọn một tác vụ khách hàng và quyết định cụ thể: tỷ lệ hoàn thành được chấp nhận, thời gian/chi phí tới đầu ra, defect escape/rework; giữ cả phân khúc và guardrail. Với xưởng nội bộ, số dòng code/PR/agent chạy là activity, không tự là giá trị.
2. Trước xây lớn, phỏng vấn/quan sát hoặc prototype theo §1–§3; đối chiếu lựa chọn nhỏ, quy trình thủ công và baseline hiện có. Nếu traffic thấp hoặc đơn vị là cả khách hàng, ưu tiên usability/cohort có giới hạn thay vì A/B thiếu lực.
3. Đóng băng metric contract: numerator/denominator, window, assignment unit, consent, exposure, query/version, exclusion và phương pháp dừng. Chi phí/tác vụ đạt cần tính cả sửa tay/review/retry, không chỉ tiền token của lần gọi thành công.
4. Trước rollout, chạy fixture event, A/A và SRM theo phương pháp đã chọn; kiểm dữ liệu trùng/thiếu, context thay sau login, cross-tenant leakage và fallback. Một evaluation thành công nhưng chưa có exposure hợp lệ không được tính vào mẫu đã thấy treatment.
5. Phát hành theo flag với owner/expiry, guardrail latency/crash/chi phí và kill switch diễn tập; kết nối [32](../32-platform-delivery-engineering/README.md) và [33](../33-reliability-observability-operations/README.md). Hết thời hạn phải có quyết định giữ/bỏ/đo thêm và dọn flag theo quy trình.
6. Báo effect size/khoảng bất định theo phân khúc, tác động guardrail, mẫu bị loại và chi phí trên đầu ra được chấp nhận. Không kết luận "không khác" khi phép thử thiếu lực; không dùng traffic bên trong xưởng thay người dùng đích.

**Đã đổi so với đợt trước:** bổ sung lớp provider/daemon và kiểm assignment, tách nó khỏi exposure/experiment engine; đưa outcome economics vào nghiệm thu phần mềm. **Nguồn §5:** [README.md](https://github.com/open-feature/flagd/blob/902555686f8bb1a89fe40c4b532e78c4e098110d/README.md) · [LICENSE](https://github.com/open-feature/flagd/blob/902555686f8bb1a89fe40c4b532e78c4e098110d/LICENSE) · [core/pkg/evaluator/fractional.go](https://github.com/open-feature/flagd/blob/902555686f8bb1a89fe40c4b532e78c4e098110d/core/pkg/evaluator/fractional.go) · [core/pkg/evaluator/json.go](https://github.com/open-feature/flagd/blob/902555686f8bb1a89fe40c4b532e78c4e098110d/core/pkg/evaluator/json.go) · [.github/workflows/build.yaml](https://github.com/open-feature/flagd/blob/902555686f8bb1a89fe40c4b532e78c4e098110d/.github/workflows/build.yaml); phương pháp nghiên cứu/SRM tiếp tục dùng nguồn gốc đã dẫn ở §3.

## Nguồn

Các permalink trong từng hồ sơ cố định đúng phiên bản đã đọc; số sao/trạng thái archive là snapshot GitHub API ngày 2026-11-02. Không chạy mã, huấn luyện model hoặc tái lập kết quả của upstream.
