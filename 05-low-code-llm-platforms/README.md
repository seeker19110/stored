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

## Nâng cấp 31/10/2026: rà repo lớn, Flowise đã archive

> Ba việc. (1) Đọc lại số sao, license, ngày push của mọi repo mục 05 trong catalog bằng GitHub search API (31/10/2026). (2) **Điều tra Flowise**: clone đủ lịch sử, đọc commit cuối, `SECURITY.md`, LICENSE, thông báo chính thức và tìm fork cộng đồng. (3) Tìm repo lớn còn thiếu bằng 9 truy vấn (topic `low-code`, `no-code`, `workflow-automation`; từ khoá "visual agent builder", "llm app builder", "agent builder" tạo sau 1/10/2025). Chọn **5 repo**, clone `--filter=blob:none`, đọc LICENSE, manifest, cấu trúc, CI, grep telemetry. **Không cài, không chạy script nào.**

### Flowise: vì sao archive và thay bằng gì

| Mục | Thông tin (đọc 31/10/2026) |
|---|---|
| Trạng thái | `FlowiseAI/Flowise` **archived**, 55,5k★, 25,1k fork; push cuối 13/8/2026. Dòng "Trạng thái chưa rõ" ở bảng đầu mục đã có câu trả lời |
| Mốc | **29/7/2026** đóng băng code, tag cuối `flowise@3.1.4` cùng ngày; **3/8** `SECURITY.md` đổi thành "PRODUCT SUNSET… no longer accepting new security vulnerability reports" (commit của nhân viên Workday); **13/8** commit cuối thêm "Flowise has been archived" vào README rồi archive; **31/8** hết vòng đời, nhóm lõi rời Discord/GitHub. Trang flowiseai.com/sunset ghi ngày archive là 10/8, lệch 3 ngày với GitHub |
| Lý do chính thức | Discussion #6727 và trang sunset: lập trình viên chuyển sang coding agent (Claude Code, OpenClaw) cho việc phức tạp; "The typical rigid workflow low code approach quickly hits the limit when it comes to complexity" |
| Ai quyết | Flowise thuộc Workday (mua khoảng 8/2025 theo tin báo chí, **chưa xác minh** từ thông cáo của Workday). Từ 11/2025 có 200 commit từ email `workday.com`, nhiều hơn email `flowiseai.com` (160) |
| Thay thế chính thức | **Không có.** Nhóm chỉ khuyên fork; code "Apache 2.0 licensed… is yours to keep building on". Không nêu ngày tắt Flowise Cloud hay cách xuất dữ liệu (một blog nói 30/11/2026, **chưa xác minh**) |
| License | `LICENSE.md` là Apache-2.0 **trừ** `packages/server/src/enterprise/` và các file ghi bản quyền riêng (FlowiseAI Commercial License), nên GitHub báo `NOASSERTION`. Fork phải bỏ hoặc thay phần enterprise |
| Fork cộng đồng | `Perruer/keelflow` (43★, tạo 24/9/2026, Apache-2.0 only, tự gọi là "security-maintained continuation"); `davobene/migrateflows` (4★, MIT) chuyển flow Flowise sang n8n. Chưa có fork nào đủ lớn |
| Rủi ro nếu còn chạy | Không còn nhận báo lỗi bảo mật. Đã có repo khai thác công khai cho **CVE-2026-58057** (RCE trên Windows qua MCP stdio, `CerberusMrXi/Flowise-CVE-2026-58057-exploit`, tạo 23/7/2026); chưa kiểm bản 3.1.4 đã vá hay chưa |

**Nên chuyển sang đâu:** canvas LangChain gần nhất là **Langflow** (MIT, 156,2k★); app LLM/RAG có giao diện quản trị → **Dify**; tự động hoá nhiều SaaS → **n8n** (fair-code); muốn để coding agent dựng workflow thay vì kéo thả → **n8n-mcp** (bảng dưới). Nếu buộc giữ Flowise: chạy sau VPN, không bật node MCP stdio, và tự theo dõi CVE.

### Repo cũ: điều đã đổi

| Repo | Thay đổi (12/10 → 31/10/2026) | Hệ quả |
|---|---|---|
| `FlowiseAI/Flowise` | **Archived 13/8/2026** | Xem trên; catalog ghi archived |
| `danny-avila/LibreChat` | **Đã chuyển sang `LibreChat-AI/LibreChat`**, 45,6k → 46,6k, push 31/10 | Link cũ còn chuyển hướng; catalog cần đổi trường `repo` |
| `coze-dev/coze-studio` | 21,7k → 21,8k; **push cuối vẫn 29/7/2026** | Hơn 3 tháng không commit trên nhánh chính; coi như tạm dừng. Canvas FlowGram của nó vẫn sống (bảng dưới) |
| `gyoridavid/ai_agents_az` | Vẫn dừng từ 19/12/2025 | Đúng như hồ sơ 25/10 |
| `activepieces/activepieces` | Bảng đầu ghi "–" → **25,3k**, push 31/10; GitHub báo `NOASSERTION` (MIT core + phần EE) | Bổ sung số |
| n8n · Dify · Langflow · Open WebUI | 207k → 209,2k · 158k → 160,1k · ~140–154k → 156,2k · 154k → 157,4k | Không đổi nhận định. n8n, Dify, Open WebUI, LobeHub, FastGPT đều hiện `NOASSERTION` vì license riêng (đúng như bảng đầu) |
| LobeHub, AnythingLLM, Cherry Studio, Sim, FastGPT | Tăng 0,5–1,5% | Không đổi |

### Bảng nhanh 5 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `czlonkowski/n8n-mcp` | Coding agent → n8n | 23,2k · MIT | 27/10/2026 | MCP server cho agent tra node n8n, kiểm và sửa workflow | **Telemetry mặc định thu workflow để làm dataset ML** |
| `ToolJet/ToolJet` | Nền tảng internal tool + AI | 41,2k · AGPL-3.0 (EE riêng) | 30/10/2026 | Dựng admin/dashboard bằng prompt hoặc qua MCP | Quickstart dùng image **EE**; submodule EE riêng tư |
| `Budibase/budibase` | Nền tảng app + agent | 28,4k · GPL-3.0 / MPL-2.0 / BSL | 29/10/2026 | App nội bộ, automation, agent AI có phân quyền theo người dùng | 3 license trong một repo; analytics bật trong compose |
| `iflytek/astron-agent` | Nền tảng agentic workflow | 9,0k · Apache-2.0 | 28/10/2026 | Workflow agent + RPA + MCP của iFlytek, Java/Python/Go | Mật khẩu mặc định yếu; gắn hệ sinh thái iFlytek |
| `bytedance/flowgram.ai` | Framework canvas workflow | 8,5k · MIT | 22/10/2026 | Thư viện canvas, form node, biến, runtime để tự dựng "Dify của riêng mình" | Bản Desktop chưa ký số |

### Hồ sơ từng repo

- **n8n-mcp.** 1.336 commit từ 7/6/2025, 39 tác giả nhưng gần như một người (Romuald Członkowski, ~1.230 commit dưới hai tên); **60% commit có trailer Claude**. Bản v2.99.2 (27/10/2026), ghim `n8n-workflow` 2.44.2. Có 7 tool tra cứu (không cần n8n) và 21 tool quản lý (cần `N8N_API_URL`, `N8N_API_KEY`); README hướng dẫn `DISABLED_TOOLS=…` để tắt hẳn tool ghi/xoá và tool credential ✅. **Telemetry bật mặc định** gửi `https://telemetry.n8n-mcp.com`: ID cài đặt băm từ hostname/home dir, tên tool, **workflow đã làm sạch** (giữ node, kết nối, tham số không nhạy cảm) và **câu `intent` người dùng gõ**; `PRIVACY.md` v2 (28/9/2026) nói thẳng mục đích "build datasets and machine learning models". Làm sạch chạy trên máy (`workflow-sanitizer.ts`, `intent-sanitizer.ts`) ✅, nhưng **không đọc `DO_NOT_TRACK`**; tắt bằng `npx n8n-mcp telemetry disable` hoặc `N8N_MCP_TELEMETRY_DISABLED=true`. Đi kèm `czlonkowski/n8n-skills` (6,6k★, MIT). Cài: `npx n8n-mcp` (stdio) sau khi tắt telemetry.
- **ToolJet.** 19.373 commit từ 3/2021, 760 tác giả. LICENSE là **AGPL-3.0**, nhưng `frontend/ee` và `server/ee` là submodule trỏ tới `ToolJet/ee-frontend`, `ToolJet/ee-server` **không truy cập công khai được**; lệnh Docker trong README chạy `tooljet/try:ee-lts-latest`, tức bản EE chứ không phải bản CE ⚠️. MCP server và plugin cho Claude Code/Codex đang beta. `.env.example`: `CHECK_FOR_UPDATES=true` và telemetry gửi về "ToolJet hub" mỗi 24 giờ, **bật mặc định**, tắt bằng `DISABLE_TOOLJET_TELEMETRY=true`. CI dày (Cypress, CodeQL, grype, license-compliance). Có kênh LTS (`v3.20.252-lts`) tách khỏi kênh beta.
- **Budibase.** 61.333 commit từ 3/2019, 211 tác giả. `LICENSE` là hướng dẫn: server/builder/worker **GPL-3.0**, client/bbui/sdk/string-templates **MPL-2.0** (để app dựng ra không bị GPL), `packages/pro` **BSL** (đổi sang GPLv3 sau 4 năm) dù `package.json` ghi `UNLICENSED`; kèm `SQS_LICENSE` của bên thứ ba. Agent AI: `packages/server/src/ai/tools/authorization.ts` lọc kết quả tool theo quyền của **người đang dùng** ("Tool is not available in this security context") ✅ — mẫu tốt cho agent nội bộ. Analytics: `hosting/docker-compose.yaml` đặt `ENABLE_ANALYTICS: "true"`, image đơn có sẵn token PostHog mặc định trong `runner.sh`. Bản v3.50.0 (15/10/2026).
- **Astron Agent (iFlytek).** 3.264 commit từ 22/9/2025, 125 tác giả. Apache-2.0 + NOTICE; README nhấn "no commercial restrictions" ✅ (khác FastGPT, Dify). Gồm `core/` (agent, workflow, knowledge, memory, plugin, tenant), `console/`, Casdoor cho đăng nhập, tuỳ chọn RPA (`iflytek/astron-rpa`). `.env.example` có **mật khẩu mặc định yếu** (`spark123`, `root123`, Redis `123`, MinIO `minioadmin123`); endpoint bot mặc định trỏ Spark của iFlytek (`spark-api-open.xf-yun.com`). Có workflow `claim-issue-reward.yml` trả thưởng cho người đóng issue. Bản v1.1.2 (1/9/2026). Cài: `cd docker/astronAgent && cp .env.example .env` (đổi hết mật khẩu) rồi `docker compose -f docker-compose-with-auth.yaml up -d`.
- **FlowGram (ByteDance).** 779 commit từ 2/2025, 45 tác giả, MIT. Không phải sản phẩm mà là **bộ khung để tự dựng nền tảng workflow**: `canvas-engine`, `node-engine`, `variable-engine`, `runtime`, `materials` (node LLM, Condition, Code); là canvas của Coze Studio. Mới thêm FlowGram Desktop (10/2026) xuất workflow ra HTTP và MCP, README tự ghi "Preview installers are unsigned". Không thấy telemetry. Hợp khi muốn nhúng canvas vào sản phẩm riêng thay cho Flowise.

### Mẫu chung rút ra

1. **"Low-code bị coding agent nuốt" đã thành lý do đóng cửa chính thức** (Flowise). Hướng sống sót của nhóm này là mở MCP để agent dựng thay người kéo thả: n8n-mcp, ToolJet MCP, FlowGram Desktop xuất MCP.
2. **Sản phẩm bị mua lại có thể đóng nhanh:** từ đóng băng tới hết vòng đời chỉ 33 ngày, không có đường chuyển đổi dữ liệu. Khi chọn nền tảng, ưu tiên định dạng flow xuất được và license cho phép fork (Apache/MIT không kèm thư mục thương mại).
3. **Telemetry ngày càng thu nội dung, không chỉ số đếm:** n8n-mcp thu workflow và câu lệnh để huấn luyện mô hình; ToolJet, Budibase bật analytics mặc định ở bản tự host.
4. **"Open source" nhiều tầng:** ToolJet (AGPL + EE riêng tư), Budibase (GPL + MPL + BSL), Flowise (Apache + thư mục thương mại). Đọc LICENSE từng thư mục và kiểm image Docker mặc định là CE hay EE.

**Nguồn (31/10/2026):** GitHub search API (`repo:` cho repo cũ, 9 truy vấn; `flowise` tạo sau 1/7/2026; `keelflow`) · clone `--filter=blob:none` FlowiseAI/Flowise (README.md, SECURITY.md, LICENSE.md, `packages/server/src/enterprise/LICENSE.md`, `git log` email theo domain, commit ba4c6509 và 9291856d, tag `flowise@3.1.4`) · https://github.com/FlowiseAI/Flowise/discussions/6727 · https://flowiseai.com/sunset · bên thứ ba: https://landing.elest.io/flowise-alternatives · https://byteiota.com/flowise-shutdown-august-31-migrate-your-ai-pipelines-now/ · https://dev.to/nodles/best-flowise-alternatives-in-2026-after-the-workday-acquisition-4834 · https://github.com/Perruer/keelflow · clone repo mới: n8n-mcp (README.md, PRIVACY.md, LICENSE, package.json, `src/telemetry/{config-manager,ingest-client,telemetry-types}.ts`), ToolJet (LICENSE, README.md, .gitmodules, .env.example, workflows), Budibase (LICENSE, `packages/*/package.json`, `packages/pro/license.md`, `packages/server/src/ai/tools/authorization.ts`, `packages/backend-core/src/configs/configs.ts`, `hosting/docker-compose.yaml`, `hosting/single/runner.sh`), astron-agent (README.md, LICENSE, NOTICE, `docker/astronAgent/{.env.example,docker-compose.yaml}`, workflows), flowgram.ai (README.md, LICENSE, `packages/`, `apps/`)

## Nguồn

- https://www.knowlee.ai/blog/dify-alternatives-2026 · https://toolhalla.ai/blog/dify-vs-flowise-vs-langflow-2026 · https://www.jahanzaib.ai/blog/flowise-vs-dify-vs-n8n-ai-agents · https://rapidclaw.dev/blog/low-code-ai-agent-platforms-compared-2026 · https://makerstack.co/reviews/langflow-review/ · https://enterprisedna.co/directories/compare/dify-vs-flowise-vs-langflow/
- Bổ sung (12/10/2026): https://github.com/open-webui/open-webui · https://github.com/danny-avila/LibreChat · https://github.com/lobehub/lobehub · https://github.com/Mintplex-Labs/anything-llm · https://github.com/CherryHQ/cherry-studio · https://github.com/simstudioai/sim · https://github.com/labring/FastGPT · https://github.com/coze-dev/coze-studio · https://github.com/node-red/node-red · https://github.com/janhq/jan
