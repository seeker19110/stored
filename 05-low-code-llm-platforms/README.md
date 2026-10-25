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

## Bổ sung: kiểm ảnh "AI Agents A-Z" (`gyoridavid/ai_agents_az`), kho template n8n của một kênh YouTube (ảnh người dùng gửi, 2026-10-25)

> Ảnh là README trên điện thoại, liệt kê "Season 1" từ Episode 1 (prescription agent) đến Episode 10 (n8n best practices). Đã clone đủ lịch sử (110 commit, HEAD `764fac2`), đọc README từng tập và quét **toàn bộ 55 file JSON** (1.551 node) bằng script: loại node, loại credential, host được gọi, chuỗi giống API key. Không import workflow nào vào n8n.

### Hồ sơ nhanh

| Mục | Thông tin (đọc 25/10/2026) |
|---|---|
| Repo | https://github.com/gyoridavid/ai_agents_az · **~3,9k★**, 946 fork (shields) |
| Tác giả | David Gyori: 109/110 commit, 1 commit của người khác. Kênh YouTube "AI Agents A-Z" và cộng đồng trả phí trên Skool |
| License | **Không có file LICENSE** (shields: "not specified"). Về pháp lý mọi quyền thuộc tác giả: import để dùng thì được ngầm hiểu là cho phép, nhưng đóng gói lại hay bán lại thì không có giấy phép |
| Hoạt động | 30/3/2025 → **19/12/2025** (Episode 42). **Đã hơn 10 tháng không commit** |
| Nội dung thật | 33 thư mục tập (1–25, 31, 35, 36, 38–42; thiếu 26–30, 32–34, 37), mỗi tập có README + JSON workflow; thêm 10 file Python (app Modal chạy FLUX/Qwen), 5 mp4 và 5 mp3 mẫu. Repo nặng 112 MB, riêng `episode_9/example_bgvideo.mp4` là 49 MB |

### Kiểm ảnh

- **10 tập trong ảnh đều có thật** và đúng tên. Ảnh chỉ chụp Season 1; README thật kéo tới Episode 42.
- **Phần lớn kho là làm video "faceless" hàng loạt**, không phải "AI agent" theo nghĩa chung. Từ Episode 7 trở đi chủ yếu là YouTube Shorts, truyện kinh dị/trả thù, video ngủ, UGC, influencer ảo trên Instagram, cùng các bài so model sinh ảnh/video (Seedance, Hailuo, Wan 2.2, Veo 3.1, Sora 2, FLUX, Qwen Image, Z-Image).
- Năm tập đầu (đơn thuốc, digest, LinkedIn có duyệt HITL, deep research, viết blog) mới là "agent" đúng nghĩa và là phần đáng học nhất cho mục 03/21.
- **Tên tập không khớp:** README gốc ghi Episode 38 là "Create AI reaction videos with Veo 3.1", nhưng README trong thư mục là "Gemini 3 recreates YouTube shorts", tức là dựng lại video người khác.

### Điều ảnh không nói (quét JSON)

- **Không lộ secret:** không chuỗi nào giống API key (OpenAI, Google, Replicate, Slack, fal) trong file hiện tại, kể cả commit "Remove pinned data".
- **Node:** 1.225 node `n8n-nodes-base` + 282 node `@n8n/n8n-nodes-langchain`; không có community node (các node lạ là workflow ComfyUI đi kèm).
- **Credential cần chuẩn bị:** HTTP header/bearer (111 chỗ, gọi API trả phí trực tiếp), OpenAI (32), Supabase (23), Ollama (16), Gmail (11), YouTube (10), OpenRouter (9), Facebook Graph (8)…
- **Dịch vụ ngoài:** fal.ai (24 lần gọi `queue.fal.run`), Modal, Together, MiniMax, ElevenLabs, Cloudflare Workers AI. Sora 2/Veo đi qua **kie.ai**, một bên bán lại API không chính thức.
- **"Free" trong tên tập thường là:** dùng tín dụng dùng thử, chạy GPU của mình (ComfyUI, Colab), hoặc gói free có giới hạn.

**Phụ thuộc vào máy chủ của tác giả:**

- Nhiều tập cần container `gyoridavid/ai-agents-no-code-tools` (6,4k lượt pull) và `gyoridavid/narrated-story-creator` (5,7k lượt pull) trên Docker Hub. **Hai image này không có repo mã nguồn công khai** (GitHub trả "repo not found"), nên khó kiểm bên trong làm gì. Image cập nhật lần cuối 9/2025 và 5/2025.
- Chỉ `gyoridavid/short-video-maker` (~1,4k★, MIT) là có mã: Kokoro TTS (chỉ tiếng Anh) + whisper.cpp + video nền từ Pexels + **Remotion**. Công ty trên 3 người phải mua license Remotion (mục 22 §2.2). Repo này dừng từ 6/2025.
- Hai workflow còn hard-code IP mạng LAN của tác giả (`192.168.68.60:8000`); Episode 19 trỏ thẳng tới endpoint Modal riêng của tác giả. Import xong phải đổi các địa chỉ này.

**License model:** các tập FLUX.1 Kontext [dev] và FLUX.1 [dev] dùng trọng số theo **FLUX Non-Commercial License**, không dùng cho kênh kiếm tiền được; muốn dùng thương mại thì chọn FLUX.1 Schnell, tương tự cảnh báo FLUX.2 ở mục 19 §1e. File Modal ghim commit diffusers và revision model, là điểm tốt.

**Phễu thương mại:** README mỗi tập dẫn tới Skool trả phí ("premium versions of the workflows… with the hosted GPU media server"; 77 link) và có link affiliate n8n (24 tập). Bản trong repo là bản miễn phí; bản "premium" nằm sau cộng đồng trả phí.

**Rủi ro nội dung:**

- Episode 36 tạo "bodycam footage" giả bằng Sora 2; Episode 38 dựng lại Shorts của người khác; Episode 21 là "10 niche faceless kiếm tiền trong một tháng".
- Không workflow nào gắn nhãn nội dung AI. YouTube và TikTok đều yêu cầu khai báo nội dung tổng hợp trông như thật.
- Kiểu nội dung sản xuất hàng loạt dễ bị coi là "inauthentic/repetitious content" khi xét kiếm tiền **(chi tiết chính sách chưa xác minh trong đợt này)**.

### So sánh & dùng thế nào

| | ai_agents_az | `enescingoz/awesome-n8n-templates` | Thư viện chính thức n8n.io/workflows | OpenMontage / skill video (mục 19, 22) |
|---|---|---|---|---|
| Bản chất | ~55 workflow của một kênh, kèm video hướng dẫn | Danh sách workflow cộng đồng gom từ nhiều nguồn **(chưa clone)** | Template do n8n và cộng đồng đăng, có trang mô tả | Agent viết code dựng video |
| License | Không có | Xem từng mục | Theo điều khoản n8n | Tùy repo |
| Cập nhật | Dừng 12/2025 | **(chưa kiểm)** | Liên tục | Liên tục |

- **Đáng lấy:** Episode 3 (đăng LinkedIn có bước duyệt người, HITL qua Gmail) và Episode 4–5 (deep research → viết blog) là mẫu tốt để học cấu trúc agent trong n8n. Episode 10 (best practices) chỉ là video, thư mục không có workflow.
- **Trước khi import:**
  - Xem từng node HTTP: gửi gì, tới đâu, dùng credential nào.
  - Thay IP LAN và endpoint Modal của tác giả.
  - Đặt hạn mức chi tiêu trên fal/kie/OpenAI, vì vòng lặp tạo video gọi API trả phí nhiều lần.
- **Không nên:** chạy image Docker không có mã nguồn trên máy có dữ liệu thật (nếu cần thì chạy trong VM riêng); đóng gói lại workflow để bán, vì repo không có license; dùng FLUX [dev] cho kênh thương mại.
- n8n tự nó là fair-code (Sustainable Use License): dùng nội bộ thì được, bán dịch vụ host n8n cho khách thì phải xem lại điều khoản (bảng đầu mục này).

**Nguồn:** clone đủ lịch sử github.com/gyoridavid/ai_agents_az 25/10/2026 (110 commit, HEAD 764fac2 19/12/2025; README.md, `episode_*/README.md`, quét 55 file JSON bằng script, `episode_19/flux_kontext_dev_modal.py`, `episode_16/guide-start-server.md`, commit "Remove pinned data from workflow") · github.com/gyoridavid/short-video-maker (clone nông; README, LICENSE MIT, package.json `@remotion/*` ^4.0.286) · hub.docker.com/v2/repositories/gyoridavid/{ai-agents-no-code-tools,narrated-story-creator,short-video-maker} (lượt pull, ngày cập nhật) · img.shields.io/github/{stars,forks,license,last-commit}/gyoridavid/… 25/10/2026 · bên thứ ba: osrepos.com/repo/gyoridavid-ai_agents_az · sourcepulse.org/projects/11055697 · growwstacks.com/blog/free-n8n-automation-templates-goldmine

## Nguồn

- https://www.knowlee.ai/blog/dify-alternatives-2026 · https://toolhalla.ai/blog/dify-vs-flowise-vs-langflow-2026 · https://www.jahanzaib.ai/blog/flowise-vs-dify-vs-n8n-ai-agents · https://rapidclaw.dev/blog/low-code-ai-agent-platforms-compared-2026 · https://makerstack.co/reviews/langflow-review/ · https://enterprisedna.co/directories/compare/dify-vs-flowise-vs-langflow/
- Bổ sung (12/10/2026): https://github.com/open-webui/open-webui · https://github.com/danny-avila/LibreChat · https://github.com/lobehub/lobehub · https://github.com/Mintplex-Labs/anything-llm · https://github.com/CherryHQ/cherry-studio · https://github.com/simstudioai/sim · https://github.com/labring/FastGPT · https://github.com/coze-dev/coze-studio · https://github.com/node-red/node-red · https://github.com/janhq/jan
