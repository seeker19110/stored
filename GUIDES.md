# Chọn công cụ theo bài toán

Các tuyến đọc dưới đây ghép những hồ sơ đã có trong kho. Bắt đầu bằng ràng buộc, chọn 2–4 ứng viên để thử trên tác vụ thật, giữ baseline và kiểm lại ngày/license trong hồ sơ. Đây là bản đồ tham khảo, không phải cấu hình triển khai đã được kho chạy thử.

Để xây **xưởng phát triển phần mềm**, đọc [FACTORY.md](FACTORY.md): bản đồ 34 mục, chín cổng giao hàng, trách nhiệm, bằng chứng phát hành và đường khởi đầu theo loại sản phẩm. Đợt 2026-11-04 bổ sung các tuyến sản phẩm thông thường bên dưới để ghép với các chuyên mục AI.

| Bài toán | Tuyến đọc | Quyết định và bằng chứng cần có |
|---|---|---|
| Agent sửa code trong repo | [01](01-ai-coding-agents/README.md) → [03](03-agentic-patterns-loops/README.md) → [07](07-eval-observability/README.md) → [13](13-dev-stack-devops/README.md) | Chọn harness theo quyền, context, sandbox và test contract. Patch/commit/submission chưa có nghĩa test pass; kiểm diff và kết quả độc lập. |
| Agent doanh nghiệp có nhiều người dùng | [02](02-agent-frameworks/README.md) → [04](04-protocols-standards/README.md) → [12](12-ai-security-guardrails/README.md) → [21](21-autonomous-workflows/README.md) | Danh tính user/agent/workload, scope theo tài nguyên/tenant, checkpoint, idempotency và thu hồi quyền. Framework có hook không chứng minh policy đã được cấu hình. |
| RAG tài liệu tiếng Việt | [26](26-document-intelligence-ocr/README.md) → [10](10-local-llm-rag-memory/README.md) → [18](18-vietnam-community/README.md) → [07](07-eval-observability/README.md) | Chọn parser trước embedding/reranker; giữ page/bbox/citation và ACL. Chấm retrieval lẫn đáp án trên tài liệu miền đích. |
| OCR hóa đơn/hợp đồng | [26](26-document-intelligence-ocr/README.md) → [17](17-prompt-engineering/README.md) → [15](15-ai-for-data/README.md) | Native PDF hay scan; schema, trường null, đơn vị/tiền, đối chiếu cross-field. JSON hợp lệ chưa chứng minh trích đúng. |
| Fine-tune model cho domain | [24](24-ai-data-engineering/README.md) → [25](25-model-adaptation-post-training/README.md) → [07](07-eval-observability/README.md) → [10](10-local-llm-rag-memory/README.md) | So prompt/RAG với SFT/LoRA trước. Split/holdout, quyền dữ liệu/weights, chất lượng trước-sau, export và ngân sách phục vụ. |
| AI chạy offline/thiết bị | [10](10-local-llm-rag-memory/README.md) → [13](13-dev-stack-devops/README.md) → [14](14-voice-multimodal/README.md) | Runtime/ops được hỗ trợ, RAM/cold start/pin/nhiệt, chất lượng sau quantization; phân biệt offline inference với bước tải model ban đầu. |
| Browser automation dùng tài khoản thật | [11](11-browser-computer-use-sandbox/README.md) → [12](12-ai-security-guardrails/README.md) → [21](21-autonomous-workflows/README.md) | Tách browser context/credential, giới hạn domain/hành động, kiểm trạng thái sau thao tác, đối soát trước retry khi timeout. |
| UI đẹp, dùng được và tạo giá trị | [06](06-ui-ux-design/README.md) → [22](22-motion-design-animation/README.md) → [28](28-product-discovery-experimentation/README.md) | Accessibility/tokens/visual + kiểm chuỗi frame và i18n; sau đó usability/task completion/funnel. Ảnh đẹp và metric model không thay bằng chứng người dùng. |
| Voice agent tiếng Việt | [14](14-voice-multimodal/README.md) → [18](18-vietnam-community/README.md) → [07](07-eval-observability/README.md) | VAD/state, barge-in, A/V transport, STT/TTS theo giọng/domain; đo task success, độ trễ lượt nói và lỗi thực tế. |
| Dữ liệu từ nhiều hệ thống | [15](15-ai-for-data/README.md) → [21](21-autonomous-workflows/README.md) → [09](09-engineering-checklists/README.md) | Snapshot/CDC, schema evolution, watermark/backfill, contract/lineage. Có scheduler chưa chứng minh dữ liệu đầy đủ hoặc restore được. |
| Video/motion dùng thương mại | [19](19-agentic-video-media/README.md) → [22](22-motion-design-animation/README.md) → [14](14-voice-multimodal/README.md) | License model/font/nhạc/ảnh, timeline/frame/timebase, A/V sync, loudness, chất lượng bản xuất và provenance. |
| Agent Revit/AutoCAD/Blender | [27](27-3d-cad-bim-engineering/README.md) → [23](23-own-repos-lessons/README.md) → [11](11-browser-computer-use-sandbox/README.md) | Mesh/B-rep/BIM, unit/tolerance, host version, dry-run→confirm→readback; schema pass không chứng minh hình học/thi công đúng. |
| Chọn plugin/skill và đưa vào quy trình | [20](20-claude-plugins-ecosystem/README.md) → [04](04-protocols-standards/README.md) → [12](12-ai-security-guardrails/README.md) | Phạm vi cài, pin/lock/update, quyền/telemetry, eval kích hoạt, rollback và license nội dung. |

## Tuyến đọc cho xưởng phát triển phần mềm

| Nhu cầu của xưởng | Tuyến đọc | Đầu ra cần mang về repo sản phẩm |
|---|---|---|
| Từ yêu cầu đến kiến trúc/API | [28](28-product-discovery-experimentation/README.md) → [29](29-software-architecture-api-contracts/README.md) → [06](06-ui-ux-design/README.md) → [30](30-software-testing-quality/README.md) | Acceptance cases, ADR, ranh giới module, hợp đồng và compatibility checks |
| Chặn lỗi trước khi giao | [09](09-engineering-checklists/README.md) → [30](30-software-testing-quality/README.md) → [07](07-eval-observability/README.md) | Unit/integration/E2E theo rủi ro; eval AI khi có model; bằng chứng test thực sự chạy |
| Bảo vệ dependency và artifact | [31](31-software-supply-chain-security/README.md) → [12](12-ai-security-guardrails/README.md) → [20](20-claude-plugins-ecosystem/README.md) | License/secret/CVE policy, SBOM, provenance, identity/digest verification |
| Tạo nền và đường phát hành dùng chung | [13](13-dev-stack-devops/README.md) → [32](32-platform-delivery-engineering/README.md) → [33](33-reliability-observability-operations/README.md) | Toolchain pin, IaC, promote cùng artifact, rollout/rollback và health gates |
| SaaS nhiều tenant, giao dịch và tích hợp | [34](34-backend-data-identity-integration/README.md) → [29](29-software-architecture-api-contracts/README.md) → [21](21-autonomous-workflows/README.md) | Authn/authz, migration rehearsal, isolation, idempotency và đối soát kết quả chưa biết |
| Có thể trực và phục hồi production | [33](33-reliability-observability-operations/README.md) → [34](34-backend-data-identity-integration/README.md) → [32](32-platform-delivery-engineering/README.md) | SLO, alert drill, incident runbook, backup/restore với RPO/RTO đo được |
| Đưa bài học vào template của xưởng | [23](23-own-repos-lessons/README.md) → [FACTORY.md §8](FACTORY.md#8-vòng-học-của-xưởng-và-chi-phí-sở-hữu) → [X-TEMPLATES.md](X-TEMPLATES.md) | Triệu chứng có nguồn, control hiện có, delta thực sự và fixture bắt regression |

## Mẫu quyết định áp dụng

Ghi bài toán và người dùng; ràng buộc dữ liệu/hardware/license/ngân sách; 2–4 lựa chọn cùng loại; bằng chứng hồ sơ; phép thử nhỏ trên tác vụ thật; phần chưa kiểm; điều kiện đổi lựa chọn. Dùng [METHOD.md](METHOD.md) để giữ phép so sánh cùng cơ sở.

Không cần dùng toàn bộ stack: bắt đầu từ phương án nhỏ đáp ứng tác vụ, rồi thêm thành phần khi phép đo cho thấy thiếu. Với dự án cần triển khai, code và cấu hình chạy thuộc repo tích hợp theo [WORKFLOW.md](WORKFLOW.md).
