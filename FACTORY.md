# Bản đồ tri thức cho xưởng phát triển phần mềm

> Đợt nghiên cứu: **2026-11-04**. Đây là cách ghép hồ sơ trong kho thành quy trình lựa chọn, kiểm chứng và vận hành công cụ. Các cổng và ngưỡng dưới đây là **đề xuất áp dụng tại repo sản phẩm**, không phải kết quả triển khai một xưởng đã được `stored` chạy thử.

Một xưởng cần tạo ra phần mềm đáp ứng nghiệp vụ, giao lại được cho người khác và duy trì được sau phát hành. Vì vậy đầu ra cần nối được **nhu cầu → quyết định → hợp đồng → thay đổi → kiểm chứng → bản phát hành → số đo thực địa**. Số agent, số prompt, số dòng mã hay số công cụ không thay chuỗi bằng chứng này.

## 1. Chọn phạm vi theo loại sản phẩm

| Tuyến sản phẩm | Mục lõi | Mục bổ sung khi có nhu cầu | Thứ cần chứng minh trước khi giao |
|---|---|---|---|
| Web/SaaS nghiệp vụ | 06, 13, 28, 29, 30, 31, 32, 33, 34 | 01–05, 16–18, 20–21 | Luồng người dùng thật, phân quyền theo tenant, giao dịch/migration, khôi phục và vận hành |
| Thư viện/SDK/API dùng chung | 04, 08–09, 16, 29–32 | 01–03, 07, 34 | Tương thích consumer, versioning, license, gói phát hành và nguồn gốc artifact |
| Sản phẩm AI/RAG/agent | 01–05, 07, 10–12, 17, 21, 24–26 | 14–15, 18, 28–34 | Baseline không agent, eval miền đích, quyền tool/dữ liệu, chi phí và thất bại có kiểm soát |
| Mobile/desktop | 06, 13, 29–33 | 11, 14, 18, 34 | Thiết bị/OS thật, offline, nâng cấp dữ liệu, ký gói và rollback khả thi |
| Media/voice/CAD | 14, 19, 22, 26–27 | 06–07, 11–12, 30–34 | License từng tài sản/model, đơn vị/timebase, đầu ra đo được và kiểm trong host đích |

Các mục 08, 09, 16, 18, 20 và 23 giúp chuẩn hóa cách học, công cụ hỗ trợ và bài học triển khai; chúng phục vụ mọi tuyến nhưng không buộc mọi dự án phải cài thêm công cụ.

## 2. Bản đồ đầy đủ 34 chuyên mục

| Mục | Năng lực xưởng cần lấy | Đầu ra hoặc cổng kiểm nên mang về repo sản phẩm |
|---|---|---|
| [01 Coding agents](01-ai-coding-agents/README.md) | Giao lát công việc cho agent có giới hạn | Diff, test và quyết định quyền của từng thao tác |
| [02 Agent frameworks](02-agent-frameworks/README.md) | Điều phối tool, state, handoff | Trace, test handoff, giới hạn lượt và lỗi tool |
| [03 Patterns & loops](03-agentic-patterns-loops/README.md) | Vòng lặp có điểm dừng | Task state, ngân sách, replay và bộ eval trajectory |
| [04 Protocols](04-protocols-standards/README.md) | Hợp đồng tích hợp agent | Phiên bản giao thức, conformance và kiểm quyền độc lập |
| [05 Low-code](05-low-code-llm-platforms/README.md) | Tự động hóa nghiệp vụ dễ thay đổi | Workflow export, credential references, test lỗi/retry |
| [06 UI/UX](06-ui-ux-design/README.md) | Giao diện nhất quán, dùng được | Component states, keyboard/a11y, visual và usability |
| [07 Eval](07-eval-observability/README.md) | Đo chất lượng AI | Corpus có quyền, baseline, rubric và kết quả theo nhóm |
| [08 Học tập](08-awesome-lists-learning/README.md) | Nâng năng lực qua tác vụ thật | Bài thực hành, review và khả năng tái lập |
| [09 Checklists](09-engineering-checklists/README.md) | Chọn control theo rủi ro | Control → người chịu trách nhiệm → bằng chứng còn hiệu lực |
| [10 LLM/RAG/memory](10-local-llm-rag-memory/README.md) | Tri thức truy xuất có quyền | Recall, citation, tenant isolation, xóa và cache invalidation |
| [11 Browser/sandbox](11-browser-computer-use-sandbox/README.md) | Tự động hóa giao diện trong ranh giới | Cách ly phiên, domain policy, receipt và read-back |
| [12 AI security](12-ai-security-guardrails/README.md) | Chống lạm quyền qua model/tool | Negative tests cho injection, egress và dữ liệu nhạy cảm |
| [13 Dev stack](13-dev-stack-devops/README.md) | Chọn stack và cách dựng nền | Version pins, môi trường tái lập, kiểm local/CI |
| [14 Voice/multimodal](14-voice-multimodal/README.md) | Chuỗi xử lý tín hiệu đầu-cuối | Latency từng chặng, barge-in, quality và quyền dữ liệu |
| [15 AI for data](15-ai-for-data/README.md) | Phân tích dữ liệu có kiểm chứng | Contract, query scope, reconciliation và nguồn dữ liệu |
| [16 Docs/tools](16-docs-tools/README.md) | Tri thức kỹ thuật có thể duy trì | Docs build, link/source freshness và ownership |
| [17 Prompt](17-prompt-engineering/README.md) | Prompt/model config được quản lý như thay đổi | Dataset tách holdout, version và chống regression |
| [18 Việt Nam](18-vietnam-community/README.md) | Ngôn ngữ và bối cảnh triển khai Việt Nam | Corpus tiếng Việt, ngày hiệu lực luật và giới hạn xác minh |
| [19 Video/media](19-agentic-video-media/README.md) | Dây chuyền nội dung có truy xuất quyền | Asset provenance, timebase và QC bản xuất |
| [20 Plugins](20-claude-plugins-ecosystem/README.md) | Chọn, khóa và nâng cấp phần mở rộng | SHA/license/permissions, routing eval và rollback |
| [21 Autonomous workflows](21-autonomous-workflows/README.md) | Tác vụ dài hạn có thể phục hồi | Idempotency, replay, timeout và đối soát kết quả chưa biết |
| [22 Motion](22-motion-design-animation/README.md) | Animation/video tái lập theo điều kiện | Font/assets/runtime cố định, frame sampling, audio sync |
| [23 Bài học repo](23-own-repos-lessons/README.md) | Chuyển kinh nghiệm thành control | Bài học có nguồn → test bắt lỗi → owner |
| [24 AI data engineering](24-ai-data-engineering/README.md) | Dữ liệu huấn luyện/eval có lineage | Split, dedup, quyền, version và phục hồi artifact |
| [25 Post-training](25-model-adaptation-post-training/README.md) | Thích nghi model có cơ sở | So prompt/RAG/SFT, loss mask, export và inference eval |
| [26 OCR](26-document-intelligence-ocr/README.md) | Tài liệu thành dữ liệu giữ nguồn gốc | Page/bbox, bảng/đơn vị, lỗi từng trang, quality theo miền |
| [27 CAD/BIM](27-3d-cad-bim-engineering/README.md) | Tác vụ hình học có thể kiểm tra | Unit/tolerance, hình học hợp lệ, host read-back |
| [28 Product discovery](28-product-discovery-experimentation/README.md) | Chọn đúng bài toán và đo hiệu quả | Giả thuyết, task success, event/exposure và quyết định |
| [29 Architecture/API](29-software-architecture-api-contracts/README.md) | Yêu cầu, ranh giới và tương thích | Traceability, ADR, dependency rules, contract diff |
| [30 Software testing](30-software-testing-quality/README.md) | Kiểm chất lượng phần mềm thông thường | Unit/integration/E2E, property/mutation, tải và a11y |
| [31 Supply chain](31-software-supply-chain-security/README.md) | Tin cậy mã/phụ thuộc/artifact | SAST/SCA/secrets, SBOM, provenance và verify policy |
| [32 Platform/delivery](32-platform-delivery-engineering/README.md) | Môi trường và đường phát hành chuẩn | IaC plan, build một lần, promote digest, rollout/rollback |
| [33 Reliability/ops](33-reliability-observability-operations/README.md) | Phát hiện và phục hồi lỗi production | SLI/SLO, burn-rate, alert drill và restore drill |
| [34 Backend/data/identity](34-backend-data-identity-integration/README.md) | Giao dịch, danh tính và tích hợp nghiệp vụ | Migration, tenant isolation, authorization, outbox/reconcile |

Sáu mục 29–34 tách lớp kỹ thuật sản phẩm thông thường khỏi các lớp AI đã có: software testing khác eval model; supply-chain security khác prompt injection; observability production khác trace LLM; dữ liệu giao dịch khác corpus huấn luyện. Chọn một hồ sơ gốc và dẫn chéo để không nhân bản công cụ.

## 3. Chín cổng giao hàng và trách nhiệm

Khung tham chiếu G0–G8 lấy từ vòng đời X-Templates đã đọc ở commit nguồn cuối tài liệu. Bảng dưới là bản ghép cho xưởng, không khẳng định mọi công cụ trong catalog tự thực thi những cổng này. Tên đường dẫn là gợi ý ở **repo sản phẩm**.

| Cổng | Người chịu trách nhiệm | Artifact tối thiểu | Điều kiện đi tiếp |
|---|---|---|---|
| G0 Khung bài toán | Product owner | Vấn đề, người dùng, baseline, ngân sách, phạm vi không làm | Có chỉ số thành công đo được; giả thuyết chưa biết được ghi rõ |
| G1 Phân loại | Tech lead + owner dữ liệu | Loại sản phẩm, dữ liệu/tenant, độ nhạy cảm, critical journeys | Xác định control áp dụng và ai xử lý ngoại lệ |
| G2 Nghiên cứu | Tech lead | ADR, 2–4 lựa chọn, license/TCO, version pins và nguồn | Lựa chọn phù hợp ràng buộc; giả định có phép thử nhỏ |
| G3 Đặc tả | Product + QA | Acceptance cases, hành vi lỗi, API/event/schema | Mỗi yêu cầu trọng yếu truy được tới test hoặc phép nghiệm thu |
| G4 Thiết kế | Architecture + security + UX | Ranh giới, threat model, data lifecycle, UI states | Mỗi rủi ro cao có cách giảm và phép kiểm; thay đổi hợp đồng được review |
| G5 Dựng nền | Developer/platform | Môi trường, CI, secret references, telemetry tối thiểu | Lỗi cố tình đưa vào fixture làm cổng tương ứng thất bại |
| G6 Xây lát dọc | Developer/agent + reviewer | PR, test nghiệp vụ, bằng chứng trên SHA hiện tại | Check bắt buộc pass; test có chạy; vấn đề còn mở có owner |
| G7 Kiểm/phát hành | Release owner | Candidate digest, manifest bằng chứng, migration/rollback plan | Không có blocker chưa xử lý; artifact đúng candidate; người có quyền quyết định |
| G8 Vận hành/học lại | Service owner/on-call | SLO, dashboard, runbook, restore drill, product outcomes | Alert đến đúng nơi; phục hồi đo được; kết quả quay lại backlog |

Một người có thể giữ nhiều vai trong đội nhỏ nhưng cần rõ **ai có quyền thay đổi, ai xác minh, ai chấp nhận rủi ro**. Hai phiên agent có cùng quyền ghi không tạo ra sự độc lập về quyền. Với production, bảo vệ cổng bằng CI/policy và phân quyền hệ thống.

## 4. Ba mức áp dụng, tránh dựng nền quá lớn

| Mức | Dùng khi | Giữ ngay từ đầu | Bổ sung theo rủi ro |
|---|---|---|---|
| Thử nghiệm | Chưa có người dùng/dữ liệu thật | Acceptance cases, pin phụ thuộc, secrets ngoài git, unit/contract smoke, giới hạn chi phí | Có thể gom đặc tả/ADR vào một file; dùng database và deployment đơn giản |
| Production đội nhỏ | Có người dùng thật, giao dịch hoặc SLA | Integration với dịch vụ thật có kiểm soát, quyền/tenant negative tests, migration/backup, release digest, alert + runbook | E2E critical journeys, load theo tải dự kiến, license/CVE policy và restore drill |
| Rủi ro cao/nhiều đội | Dữ liệu nhạy cảm, tài chính, nhiều tenant/nhóm | Toàn bộ control production có evidence ownership | Review bảo mật độc lập, DR/RTO/RPO được diễn tập, isolation mạnh hơn, consumer compatibility matrix |

Mức là lựa chọn quản trị của dự án, không phải chứng nhận. Không dùng nhãn “MVP” để bỏ qua bảo vệ dữ liệu thật. Ngưỡng latency, coverage, mutation hay availability cần xuất phát từ critical journeys và ngân sách; không chép một tỷ lệ chung cho mọi sản phẩm.

## 5. Ba đường khởi đầu cho nền tảng dùng chung

Chọn đường phù hợp stack đã có. Xưởng nên chứng minh một lát dọc trước khi biến nó thành template cho hàng loạt repo.

| Đường | Các mảnh ghép để khảo sát | Phép nghiệm thu đầu tiên | Khi cần đổi lựa chọn |
|---|---|---|---|
| Web/API TypeScript | Framework §13 + Vitest/Playwright §30 + hợp đồng §29 + PostgreSQL/identity §34 | Người dùng A tạo dữ liệu → người B khác tenant không đọc được → deploy candidate → rollback mà dữ liệu vẫn đọc được | Worker/CPU đặc thù, mobile-native, yêu cầu vận hành hoặc năng lực đội khác |
| Python cho data/AI | pytest/Hypothesis/Testcontainers §30 + RAG/eval §07/10 + data versioning §24 + service identity §34 | Corpus có phiên bản → eval baseline/candidate → API kiểm quyền → job bị gián đoạn và phục hồi không nhân side effect | Khi tác vụ tất định/SQL đủ tốt thì bỏ tầng model; khi serving vượt tài nguyên thì đo runtime khác |
| API/worker nghiệp vụ | SQL/migration §34 + contract diff §29 + durable execution §21 + SLO §33 | Migration trên dữ liệu đại diện → gửi trùng/timeout/crash → một nghiệp vụ có thể đối soát, không thất thoát bản ghi | Chỉ đưa broker/workflow engine vào khi hàng đợi đơn giản không đáp ứng yêu cầu đã đo |

Template chỉ nên chứa các lựa chọn đã kiểm ở repo tích hợp: toolchain pin, cấu hình cổng có fixture bắt lỗi, migration mẫu, service skeleton, runbook và tài liệu nâng cấp. Mọi template có owner, phiên bản, migration notes và thời hạn hỗ trợ. `stored` giữ nghiên cứu và hồ sơ, không giữ implementation template.

## 6. Hợp đồng bằng chứng phát hành

Đề xuất một manifest tại repo sản phẩm, do runner tin cậy ghi; nội dung dưới đây chỉ minh họa trường dữ liệu, không là schema chuẩn đã ban hành:

| Nhóm trường | Cần giữ | Kiểm để tránh báo xanh sai |
|---|---|---|
| Identity | Source SHA, candidate digest, workflow/run ID, runner/tool versions | Báo cáo gắn đúng candidate được promote, không lấy log của commit trước |
| Scope | Target, configuration, environment, dataset/schema revision | Có đúng suite, tenant model, platform và vùng critical đã chọn |
| Result | Exit status, collected/executed/passed/failed/skipped/xfail, timestamps | Không coi 0 test là đạt; skip/xfail không được chuyển thành pass |
| Evidence | Artifact URI, checksum, producer identity, retention/access | Artifact đọc được với quyền phù hợp; thiếu artifact hoặc quá hạn cần kiểm lại |
| Decision | Blockers, ngoại lệ, owner, lý do, hạn hết hiệu lực | Ngoại lệ hết hạn hoặc thiếu người chịu trách nhiệm không tự đi tiếp |

Phân biệt **pass, fail, chưa chạy, bị chặn, không áp dụng**. Chỉ pass khi kiểm đã thực thi và đúng phạm vi; “không áp dụng” cần lý do. Job bị cancel, infrastructure error hoặc scanner không tải được database là chưa có kết luận.

Fixture âm nên gồm: API thay đổi không tương thích, truy cập khác tenant, migration không tương thích phiên bản cũ, test không được collect, artifact sai digest, exception hết hạn, canary vượt error budget. Mỗi fixture cần làm cổng của nó thất bại. Những phép thử này thực hiện tại repo tích hợp; đợt này chỉ chạy các kiểm của chính catalog.

## 7. Phát hành, phục hồi và dữ liệu

1. Build candidate trong môi trường có dependency/toolchain pin; quét và tạo SBOM/provenance cho **artifact đó**. Chữ ký hợp lệ còn cần policy đúng issuer, identity và subject digest.
2. Đưa candidate qua integration/contract/E2E và migration rehearsal. Khi promote, dùng artifact digest đã kiểm; nếu rebuild phải kiểm candidate mới hoặc có bằng chứng tương đương phù hợp chính sách.
3. Expand schema trước, cho old/new application đọc được trong cửa sổ rollout; backfill có checkpoint và đối soát; contract schema sau khi các consumer cũ đã rời hệ thống.
4. Rollout theo phạm vi đã chọn với health/SLO gates và thời gian quan sát đủ cho tác vụ quan trọng. Đặt owner cho quyết định rollback; không dùng metric đẹp ở một instance để suy toàn hệ thống đạt.
5. Rollback ứng dụng, khôi phục dữ liệu và bù nghiệp vụ là ba cơ chế khác nhau. Backup có file chưa chứng minh restore được; đo RPO/RTO bằng phục hồi ở môi trường cách ly và kiểm tính toàn vẹn.
6. Khi timeout sau side effect, ghi nhận kết quả chưa biết và đối soát bằng receipt/business key. Retry của framework không tự tạo exactly-once cho hệ thống bên ngoài.

## 8. Vòng học của xưởng và chi phí sở hữu

| Nhóm chỉ số | Cách đọc hữu ích | Điều dễ hiểu sai |
|---|---|---|
| Giá trị sản phẩm | Task success/funnel theo cohort, giả thuyết và khoảng quan sát | Tăng click không chứng minh người dùng hoàn tất việc |
| Dòng giao hàng | Lead time theo cùng định nghĩa start/end; deployment count theo service | Nhiều commit hay deploy không tự chứng minh chất lượng |
| Độ ổn định thay đổi | Số release gây rollback/incident trên tổng release theo cửa sổ cố định | Retry một deploy không nên được đếm thành nhiều lần thành công |
| Phục hồi | Thời gian detect/ack/restore từng sự cố, kể cả chưa phục hồi | Bỏ các sự cố dài hoặc đo từ lúc bắt đầu sửa làm số đẹp giả |
| AI economics | Chi phí trên một task được chấp nhận, gồm retry/eval/reviewer | Giá token thấp không chứng minh tổng chi phí thấp |
| Bảo trì | Thời gian nâng dependency, CVE/exception quá hạn, template drift | Tạo repo mới nhanh nhưng để lại nhiều bản fork không nâng được |

Chi phí sở hữu cần tính người vận hành, lưu trữ log/artifact/backup, egress, license/seat, GPU idle, secret rotation, nâng version và xử lý sự cố. Có thể bắt đầu bằng bảng đơn giản; không cần xây data platform riêng chỉ để đo xưởng.

Một bài học đáng đưa về template khi có triệu chứng, nguyên nhân, phạm vi áp dụng, control có thể kiểm và phép thử bắt regression. Đối chiếu control hiện có trước khi sinh yêu cầu mới; bàn giao X-Templates ở [X-TEMPLATES.md](X-TEMPLATES.md).

## 9. Giới hạn kiểm chứng và nguồn

Đợt này nâng phạm vi nghiên cứu của 28 mục và thêm sáu mục, không kiểm lại toàn bộ lịch sử hơn một nghìn hồ sơ. Ngày snapshot catalog không là ngày xác minh mọi hồ sơ. Mỗi profile mới/đọc lại ghi SHA, nguồn và mức bằng chứng riêng. Đọc LICENSE/implementation/CI là `code-read`, chưa chứng minh package hoạt động ở dự án của xưởng.

Các pipeline và cổng trong tài liệu là tổng hợp/đề xuất từ hồ sơ đã dẫn. Môi trường hiện tại chỉ chạy validator catalog, integrity tests và Markdown lint; không chạy sản phẩm, benchmark, scanner, model training hoặc deployment của upstream.

Nguồn khung vòng đời và bằng chứng đã đọc ngày 2026-11-04:

- [X-Templates lifecycle tại 23447d8](https://github.com/seeker19110/X-Templates/blob/23447d817d2bc8cf68093591177f85fd72a8a2f6/framework/00-method/lifecycle.md): G0–G8, quy mô và bằng chứng.
- [X-Templates evidence tại cùng SHA](https://github.com/seeker19110/X-Templates/blob/23447d817d2bc8cf68093591177f85fd72a8a2f6/framework/00-method/evidence-and-sources.md): phân biệt đo được/suy luận/chưa biết; evidence do runner ghi.
- [X-Templates coverage/mutation](https://github.com/seeker19110/X-Templates/blob/23447d817d2bc8cf68093591177f85fd72a8a2f6/framework/14-testing-quality/coverage-and-mutation.md): test quality, critical scope và không hạ cổng để đạt.
- Các nguồn triển khai/LICENSE/CI theo từng chuyên mục và [SOURCES.md](SOURCES.md); cách đánh giá theo [METHOD.md](METHOD.md).
