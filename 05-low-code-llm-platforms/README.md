# 05 · Low-code / Visual LLM & Automation Platforms

| Dự án | Repo | License | ★ (10/2026) | Định vị | Ghi chú |
|---|---|---|---|---|---|
| **n8n** | n8n-io/n8n | Sustainable Use (fair-code, không OSI) | ~207k | Automation-first, có AI node/agent | Tăng từ 50k lên 200k+ trong ~2 năm |
| **Dify** | langgenius/dify | Apache-2.0 (kèm điều khoản) | ~158k | Nền tảng app LLM production: RAG, agent, workflow, prompt IDE | |
| **Langflow** | langflow-ai/langflow | MIT | ~140–154k | Visual builder trên LangChain/LangGraph, custom Python node | Vượt 100k★ 5/2026 |
| **Flowise** | FlowiseAI/Flowise | Apache-2.0 | ~55k | Drag-drop LangChain | **Trạng thái chưa rõ**: một nguồn nói archive 13/8/2026, nguồn khác nói được Workday mua – cần kiểm tra repo |
| **Activepieces** | activepieces/activepieces | MIT (core) | – | Alternative n8n, MCP-first | |
| **Open WebUI** | open-webui/open-webui | Open WebUI License (BSD-3 + điều khoản giữ thương hiệu, không OSI) | ~154k (12/10/2026) | Giao diện chat tự host cho LLM local; RBAC, RAG, tool MCP/OpenAPI | v0.12.0 (10/10/2026); không được gỡ thương hiệu "Open WebUI" khi quá 50 người dùng/30 ngày |

**Chọn thế nào:** tự động hóa quy trình nhiều SaaS → n8n; app chat/RAG cho doanh nghiệp → Dify; dev Python cần tùy biến → Langflow.

## Bổ sung: chat UI tự host & agent builder (đã xác minh 2026-10-12)

| Repo | ★ (12/10) | License | Hoạt động gần nhất | Vì sao chất lượng | Lưu ý |
|---|---|---|---|---|---|
| **danny-avila/LibreChat** | 45,6k | MIT | v0.8.8 pre-release (1/10/2026) | Chat đa nhà cung cấp tự host: agent, MCP, artifacts, code interpreter sandbox; đa người dùng OAuth2/LDAP | Các bản gần đây đều gắn nhãn pre-release; stack nặng hơn (MongoDB, Meilisearch) **(chưa xác minh)** |
| **lobehub/lobehub** (trước là lobe-chat) | 83,2k | LobeHub Community License (Apache-2.0 + điều kiện, không OSI) | 12/10/2026 | Workspace agent + chat web/desktop; 14,6k commit, phát hành gần như hằng ngày | Phân phối bản phái sinh cần license thương mại; repo đã đổi tên |
| **Mintplex-Labs/anything-llm** | 67,0k | MIT | v1.17.0 (1/10/2026) | App RAG + agent local-first (desktop/Docker), LanceDB tích hợp, 38 nhà cung cấp LLM, agent builder không code, MCP | Telemetry bật mặc định (tắt bằng `DISABLE_TELEMETRY`); đa người dùng chỉ có ở bản Docker |
| **CherryHQ/cherry-studio** | 52,6k | AGPL-3.0 (có license thương mại) | v2.1.6 (11/10/2026) | Client desktop đa LLM, agent, hơn 300 trợ lý dựng sẵn; khoảng 9,5k commit | AGPL; bản Enterprise đóng, trả phí |
| **simstudioai/sim** | 29,8k | Apache-2.0 | v0.9.18 (11/10/2026) | Canvas dựng, triển khai và giám sát workflow agent; hơn 1.000 tích hợp; model local qua Ollama/vLLM | Chat tự host cần API key do Sim cấp; cần từ 12 GB RAM |
| **labring/FastGPT** | 29,8k | FastGPT Open Source License (riêng, không OSI) | v4.17.2 (9/10/2026) | RAG knowledge base + workflow trực quan, khâu xử lý dữ liệu trưởng thành | Không được làm SaaS khi chưa có license thương mại; phải giữ thông báo bản quyền |
| **coze-dev/coze-studio** | 21,7k | Apache-2.0 | commit cuối 29/7/2026 | Bản mở của nền tảng agent/workflow Coze (ByteDance), Go + React, runtime Eino, canvas FlowGram | Hoạt động chậm lại (392 commit); một số tính năng chỉ có ở bản thương mại |

**Nhận xét:** trong nhóm chat UI, chỉ **LibreChat** và **AnythingLLM** dùng MIT thuần; Open WebUI, LobeHub, FastGPT dùng license riêng không OSI, Cherry Studio là AGPL — đọc LICENSE trước khi dựng dịch vụ cho người khác. Chọn nhanh: chat nội bộ nhiều model + đăng nhập doanh nghiệp → LibreChat; RAG tài liệu trên máy cá nhân → AnythingLLM; workflow agent trực quan, license thoáng → Sim. Đã cân nhắc nhưng không thêm: node-red (23,7k★, Apache-2.0, không chuyên LLM), jan (44,9k★, Apache-2.0, thiên về chạy model local — gần mục 10).

## Bổ sung: kiểm ảnh "54 trang làm web, thiết kế, app miễn phí" (AIHubSeek, ảnh người dùng gửi, 2026-10-13)

Ảnh liệt kê 3 cột × 18 công cụ (Build Websites, Generate Designs, Create Apps), tiêu đề "for Free". Tôi kiểm gói miễn phí từng ô ngày 13/10/2026 qua trang giá và bài review; những ô chưa tìm được nguồn chính thức ghi "(chưa xác minh)". Ở đây "miễn phí" nghĩa là có gói dùng mãi không trả tiền, không tính bản dùng thử.

**Các ô đúng (gói free thật, kèm giới hạn thường gặp):**

- **Web:** Wix, WordPress.com, Carrd, Strikingly, Webflow, Jimdo, SITE123, Tilda, Google Sites, Mobirise (app offline miễn phí), Brizy (plugin WordPress free), Dorik (theo trang hãng). Giới hạn chung: tên miền phụ của hãng, có quảng cáo hoặc huy hiệu, ít trang.
- **Thiết kế:** Canva, Adobe Express, Figma (gói Starter), Leonardo.Ai (token hằng ngày), Pixlr, Photopea (có quảng cáo), BeFunky, Visme, Piktochart, Fotor, Vecteezy, Pixabay (ảnh miễn phí theo giấy phép Pixabay).
- **App:** Glide, Adalo, Bubble, Kodular, MIT App Inventor, FlutterFlow, Firebase (gói Spark), Backendless, Softr, Retool, WeWeb, Appsmith (mã nguồn mở Apache-2.0), Draftbit (theo FAQ hãng: 5.000 credit một lần, không nạp lại).

**Các ô sai hoặc cần lưu ý:**

| Cột | Ô | Mức | Thực tế |
|---|---|---|---|
| Web | Squarespace | ❌ | Không có gói free, chỉ dùng thử 14 ngày; muốn xuất bản phải trả tiền |
| Web | Zyro | ❌ | Hostinger đã gộp Zyro vào Hostinger Website Builder (đổi tên 2022, gộp hẳn 12/2023); không có gói free |
| Web | Weebly | ⚠️ | Gói free vẫn còn ở Mỹ, nhưng Square đang dừng Weebly ở 67 quốc gia khác và khuyên người mới dùng Square Online. Ở Việt Nam có còn đăng ký được không: (chưa xác minh) |
| Web | GoDaddy | ⚠️ | Builder nay là Airo; các bài review nói gói free có 50 credit AI/tháng, nhưng mâu thuẫn ở chỗ có được xuất bản hay không (chưa xác minh) |
| Web | Ucraft, Pagecloud, Zyro-cũ | ⚠️ | Không tìm thấy trang giá chính thức hay tin đóng cửa; gói free của Ucraft được mô tả là "rất hạn chế" (chưa xác minh) |
| Thiết kế | Midjourney | ❌ | Không có gói free; gói thấp nhất 10 USD/tháng. Các nguồn mâu thuẫn về lượt dùng thử ~25 ảnh cho tài khoản mới |
| Thiết kế | DALL·E | ❌ | Đã ngừng: OpenAI gỡ dall-e-2/3 khỏi API ngày 12/5/2026 và gỡ DALL·E GPT khỏi ChatGPT ngày 30/8/2026. Thay bằng tạo ảnh trong ChatGPT (bản free có giới hạn lượt) |
| Thiết kế | Crello | ⚠️ | Đổi tên thành VistaCreate từ 10/2021 sau khi Vistaprint mua lại; tên trong ảnh đã cũ 5 năm |
| Thiết kế | Remove.bg | ⚠️ | Bản free chỉ cho tải ảnh xem trước khoảng 0,25 MP và chỉ dùng phi thương mại; ảnh đủ độ phân giải tốn credit |
| Thiết kế | DesignCap, Snappa | ⚠️ | Có gói free nhưng giới hạn lượt tải hoặc gắn watermark (chưa xác minh chi tiết) |
| App | Appy Pie | ❌ | Chỉ thấy dùng thử 7 ngày; người dùng phản ánh gần như không xuất bản được nếu không trả tiền |
| App | Thunkable | ⚠️ | Gói free tối đa 3 project công khai, **không xuất bản lên store**; xuất bản từ gói Builder ~59 USD/tháng |
| App | Zoho Creator | ⚠️ | Các nguồn mâu thuẫn: có trang ghi gói free 1 app, có trang ghi chỉ có dùng thử (chưa xác minh) |
| App | The Things Stack | ⚠️ | Đây là LoRaWAN network server cho thiết bị IoT, không phải công cụ dựng app; xếp sai cột |
| App | Pinecone | ⚠️ | Đây là vector database (có gói Starter free), không phải công cụ dựng app; xếp sai cột |
| App | Firebase, Backendless | ⚠️ | Có free tier thật, nhưng là backend; vẫn phải tự viết app hoặc ghép với một builder khác |

**Tổng:** khoảng 37/54 ô đúng như tiêu đề; 5 ô sai rõ (Squarespace, Zyro, Midjourney, DALL·E, Appy Pie); số còn lại có giới hạn quan trọng, tên đã cũ, hoặc xếp sai cột.

**Dùng ảnh thế nào:** coi là danh sách gợi ý để tự kiểm, không phải bảng "miễn phí". Ba điều cần kiểm trước khi chọn: (1) gói free có cho **xuất bản** không (Thunkable, Adalo, Bubble đều giới hạn ở bước này); (2) có cho **dùng thương mại** không (remove.bg, nhiều kho ảnh); (3) dữ liệu có **xuất ra được** không khi muốn rời nền tảng (FlutterFlow chỉ cho xuất mã ở gói trả phí). Nếu cần tự chủ hoàn toàn: Appsmith (mục này), WordPress tự host, hoặc các nền tảng ở bảng trên.

## Nguồn

- https://www.knowlee.ai/blog/dify-alternatives-2026 · https://toolhalla.ai/blog/dify-vs-flowise-vs-langflow-2026 · https://www.jahanzaib.ai/blog/flowise-vs-dify-vs-n8n-ai-agents · https://rapidclaw.dev/blog/low-code-ai-agent-platforms-compared-2026 · https://makerstack.co/reviews/langflow-review/ · https://enterprisedna.co/directories/compare/dify-vs-flowise-vs-langflow/
- Bổ sung (12/10/2026): https://github.com/open-webui/open-webui · https://github.com/danny-avila/LibreChat · https://github.com/lobehub/lobehub · https://github.com/Mintplex-Labs/anything-llm · https://github.com/CherryHQ/cherry-studio · https://github.com/simstudioai/sim · https://github.com/labring/FastGPT · https://github.com/coze-dev/coze-studio · https://github.com/node-red/node-red · https://github.com/janhq/jan
