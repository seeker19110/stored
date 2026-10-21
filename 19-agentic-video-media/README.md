# 19 · Agentic Video & Media Production

> Hệ thống để coding agent sản xuất video/media đầu-cuối, model sinh video mở, và làn sóng "video/motion skills" cho Claude Code. Mục này mở ra từ link người dùng gửi (`calesthio/OpenMontage`, 2026-10-12). Liên quan: mục 14 (TTS, VLM, ComfyUI), mục 04 (skills), mục 11 (sandbox).

---

## 1. calesthio/OpenMontage ⭐ (link từ người dùng)

### 1.1 Hồ sơ nhanh

| Thuộc tính | Giá trị (đọc 2026-10-12) |
|---|---|
| Repo | https://github.com/calesthio/OpenMontage · site openmontage.video · X @calesthioailabs |
| Mô tả | "World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio." |
| ★ / forks / watchers | **67.1k ★** · 8.5k forks · 370 watchers · 455 commit · 113 issue mở · 284 PR (một aggregator ghi 355 issue/70 PR mở – số liệu lệch) |
| License | **AGPL-3.0** |
| Ngôn ngữ | Python 3.10+ (tools, state), JS/React (Remotion composer), HTML/GSAP (HyperFrames), YAML (pipeline manifest), Markdown (skills); cần FFmpeg, Node 18+ (22+ cho HyperFrames) |
| Tác giả | `calesthio` – bio "Building open source AI Assisted and Agentic Tools", **Microsoft, Seattle**; 1.3k followers; repo khác: Crucix (12.1k★, agent giám sát nguồn dữ liệu), generative-media-skills (199★), Resonant, PhantomReach; sponsor: Bloome, Atlas Cloud |
| Lịch sử | #1 GitHub Trending "Repository of the Day"; bài viết đầu tiên ~6/2026; cadence: dồn dập 14–22/8/2026 (17 merge trong ngày 22/8), sau đó thưa (26/8, 6/9, 3/10 – refresh provider, thêm HeyGen Avatar); fix CVE-2026-67213 ngày 20/8 |

### 1.2 Kiến trúc "agent là orchestrator" (điểm đáng học nhất)

- **Không có code orchestrator.** `AGENTS.md` chỉ là stub bắt agent đọc `AGENT_GUIDE.md` → `PROJECT_CONTEXT.md`. Python chỉ cung cấp tool + persistence; mọi quyết định sáng tạo/review nằm trong file hướng dẫn. *"The intelligence is in the skills, not in improvised code."*
- **Pipeline cố định:** `research → proposal → script → scene_plan → assets → edit → compose`; mỗi stage có một **director skill** (Markdown) và sinh đúng một artifact (brief, script, scene plan, asset manifest, edit decisions, render report) phải validate qua **20+ JSON Schema**. *"Every video production request MUST go through the pipeline system. No exceptions."*
- **Approval gate theo stage:** manifest khai `human_approval_default`; stage gated dừng ở trạng thái `awaiting_human` và agent **phải kết thúc lượt**; "Approval is per-gate"; pre-authorize cả run phải được log như quyết định `approval_policy`. Stage `assets` luôn gated để người xem cảnh trước khi compose.
- **Ba lớp tri thức:** L1 `tools/` (cái gì tồn tại, giá bao nhiêu) → L2 `skills/` (OpenMontage muốn dùng tool thế nào) → L3 `.agents/skills/` (kỹ thuật theo vendor; **bắt buộc đọc trước khi gọi tool sinh**). Đọc source chỉ để debug/audit.
- **Tool registry runtime:** agent gọi `capability_catalog()`, `provider_catalog()` thay vì danh sách cứng; selector (`tts_selector`, `image_selector`, `video_selector`) chọn theo ưu tiên người dùng → sẵn có → thứ tự khám phá; README nói chấm 7 chiều (task fit, quality, control, reliability, cost, latency, continuity) và log cả phương án bị loại. *"Silent runtime swap is forbidden."*
- **State:** `projects/<id>/` với `checkpoint_<stage>.json`, bản cũ vào `history/`; `decision_log` chỉ **append**, không sửa.
- **Ngân sách:** `tools/cost_tracker.py`; ước tính chi phí ở proposal; mặc định trần $10/tổng, hỏi lại trên $0.50/hành động; call trả phí phải nêu tool/provider/model/lý do trước; chạy mẫu trước batch.
- **Quality:** reviewer meta-skill sau mỗi stage (tối đa 2 vòng; critical/suggestion/nitpick); pre-compose validation, post-render check bằng ffprobe/frame extraction/audio analysis; "slideshow-risk check" chặn output "animated PowerPoint"; *"Still-image fallback is forbidden"* khi yêu cầu có chuyển động.
- **Anti-pattern nêu rõ:** bỏ qua pipeline bằng script ad-hoc, gọi tool sinh mà chưa đọc L3, đổi provider/render path không xin phép, giấu đường degrade, hardcode provider/key, sinh asset trước khi plan được duyệt.
- **Backlot:** bảng điều khiển local (`python -m backlot open`) hiện tiến độ, gate, chi tiêu.

### 1.3 Pipeline & provider

11 pipeline trong README (About nói 12): Animated Explainer, Animation, Avatar Spokesperson, Cinematic, Clip Factory, Documentary Montage (ghép footage mở từ Archive.org/NASA/Wikimedia), Hybrid, Localization & Dub, Podcast Repurpose, Screen Demo, Talking Head (+ character animation). Provider: FLUX, Kling, Veo, Runway, WAN 2.2 (qua ComfyUI), HeyGen Avatar; TTS ElevenLabs/OpenAI/Google/**Piper (free)**; nhạc Suno/ElevenLabs; stock Pexels/Pixabay/Unsplash. **Zero-key path** hoàn toàn miễn phí.

### 1.4 Đánh giá từ bên ngoài

| Nguồn | Nội dung |
|---|---|
| pinggy.io (26/6/2026) | Free tier chạy end-to-end, explainer 60s mất ~10–15 phút; chi phí ví dụ: Ghibli-style 12 ảnh FLUX ~$0.15, history 70s OpenAI TTS ~$0.02, ad 4 ảnh ~$0.69. Điểm yếu: setup nặng (Python+Node+FFmpeg+SDK), chưa có Docker, pipeline cao cấp phụ thuộc API trả phí |
| knightli.com (22/6/2026) | Hướng dẫn cài; lỗi thường gặp: venv, `npm ERR_INVALID_ARG_TYPE` (fix `npx --yes npm install`), PowerShell policy, 401/429, GPU/CUDA; khuyên `make demo` 15–30s trước; "không phải one-prompt video generator" |
| dev.to/andrew-ooo | Piper kém ElevenLabs; footage archive giới hạn thẩm mỹ public-domain; **model agent quyết định chất lượng** (model mạnh chọn pipeline/script tốt hơn rõ rệt); phí agent ~$3–7 cho video 60s trên model top; AGPL: dùng nội bộ/consulting ok, SaaS phải mở mã sửa đổi |
| hysenlabs, opensourcealternatives.to, explainx | AGPL là caveat chính; "fast-moving, cần hardening trước production"; số liệu tool/skill lệch giữa nguồn (52 vs 100+ tool; 400+ vs 700+ skill) |
| Thảo luận cộng đồng | OpenMAIC (THU) bàn dùng OpenMontage làm MCP service cho nội dung học tập; OpenViking (Volcengine) RFC dùng làm benchmark context |

### 1.5 Nhận xét & cách tận dụng

- **Giá trị cốt lõi:** không phải model video mà là **mẫu kiến trúc "skills-as-orchestrator"** ở quy mô lớn: pipeline manifest + director skill + schema + gate + decision log + cost tracker. Đây là bản mở rộng tự nhiên của SKILL.md (mục 04) và evaluator pattern (mục 03) sang domain sáng tạo nhiều bước, nhiều provider.
- **Bài học tái dùng cho bất kỳ agent workflow nào:** (1) artifact chuẩn hóa + schema mỗi stage; (2) gate theo stage với trạng thái `awaiting_human` và agent phải dừng lượt; (3) registry runtime thay danh sách cứng; (4) ba lớp tri thức tách "cái gì/như thế nào/kỹ thuật vendor"; (5) append-only decision log; (6) reviewer meta-skill có giới hạn vòng.
- **Rủi ro:** AGPL với SaaS; dự án trẻ, nhiều issue mở, cadence commit chậm từ 9/2026; setup phức tạp (chưa Docker); chất lượng phụ thuộc model agent và provider trả phí; marketing numbers chưa nhất quán.
- **Gợi ý:** chạy zero-key path trong sandbox (mục 11) để học kiến trúc; nếu dùng thương mại, kiểm tra AGPL; so sánh với `generative-media-skills` (cùng tác giả, nhẹ hơn) nếu chỉ cần sinh ảnh/âm thanh.

---

## 1b. krillinai/OpenCreator, tên cũ KrillinAI (ảnh README người dùng gửi, 2026-10-13)

### 1b.1 Hồ sơ nhanh

| Thuộc tính | Giá trị (đọc 2026-10-13) |
|---|---|
| Repo | https://github.com/krillinai/OpenCreator (link cũ `krillinai/KrillinAI` chuyển hướng về đây) · site open-creator.ai |
| Mô tả (About) | "Formerly KrillinAI. Open-source AI workspace for creators, powered by Codex. Create videos, images, voice, avatars, translations, and edits with Agents in one place." |
| ★ / fork | **~13k ★ · ~1,4k fork** (shields 13/10/2026; ảnh chụp ghi 11.5k/1.1k là số cũ) · 28 issue mở · 5 PR mở · bản phát hành v3.2.6 |
| License | **Apache-2.0** từ 21/9/2026. Trước đó GPL-3.0: `LICENSE` gốc tạo 27/12/2024 là GPLv3; `runtime/krillinai/LICENSE` đổi GPLv3 → Apache ở commit bfbf59a ngày 29/9/2026 |
| Tên gọi | KrillinAI → KlicStudio (khoảng 2025) → KrillinAI (đổi lại 12/9/2025) → OpenCreator (9/2026) |
| Lịch sử | Commit đầu 17/12/2024; 936 commit; 358 commit từ 1/8/2026 (đọc git 13/10/2026). Huy hiệu Trendshift "#1 Repository of the Day" có thật, trang Trendshift không ghi ngày (chưa xác minh ngày) |
| Ngôn ngữ | TypeScript ~82%, Go ~9% (ảnh chụp; Go là `runtime/krillinai`, lõi dịch video cũ) |

### 1b.2 Kiến trúc (đọc README + mã)

- **Không tự viết vòng lặp agent.** Dùng **Codex CLI** (app-server) làm động cơ; OpenCreator thêm daemon cục bộ, giao diện web và vỏ desktop. Chạy tác vụ thật cần đăng nhập ChatGPT hoặc API key (Codex hoặc nhà cung cấp tương thích OpenAI).
- **Ba lớp:** `apps/web` (React 18 + Vite) → `apps/daemon` (Fastify, Runtime API + SSE, SQLite, lịch chạy, duyệt quyền, bộ nhớ) → Codex + bộ công cụ media (FFmpeg, yt-dlp, Whisper, dịch vụ AI). `apps/desktop` là Electron nạp lại đúng bản web.
- **Một máy trạng thái cho hai giao diện:** thao tác trên workspace và lệnh trong hội thoại cùng đẩy sự kiện vào một máy trạng thái; mỗi lần sửa tạo phiên bản mới, không ghi đè.
- **Daemon chỉ nghe loopback:** `server.listen({ host: '127.0.0.1', port: 0 })` (`apps/daemon/src/main.ts`), token tạm in ra stdout một lần.
- **Skills:** 7 skill trong `skills/` điều khiển CLI KrillinAI (phụ đề, TTS, render ngang/dọc, ảnh bìa, kiểm kế hoạch pipeline). Mặc định dùng `$CODEX_HOME` chung, nên đổi skill/MCP ở đây là đổi cấu hình Codex toàn máy.
- **CI:** `pnpm audit --audit-level high`, test daemon/desktop/web, actionlint cho workflow phát hành.

### 1b.3 Kiểm ảnh README

| Ô trong ảnh | Kết luận |
|---|---|
| "Formerly KrillinAI" | ✅ Đúng; còn một tên trung gian là KlicStudio |
| "Open-source" | ⚠️ Mã Apache-2.0, nhưng tài khoản, gói đăng ký, tín dụng và "official model services" đi qua gateway `open-creator.ai` (mặc định trong `OPENCREATOR_GATEWAY_ORIGIN`, thanh toán Stripe). Tự cấu hình key riêng vẫn dùng được |
| "powered by Codex" | ✅ Đúng như mã: Codex là nguồn sự thật cho vòng lặp agent, Skills, MCP |
| "videos, images, voice, avatars, translations, and edits" | ⚠️ Digital Avatar và Auto Clips đang ghi "In development"; 10 công cụ còn lại ✅ Available |
| 11.5k★ · 1.1k fork | ⚠️ Số cũ; nay ~13k / ~1,4k |
| "#1 Repository of the Day" | ✅ Huy hiệu Trendshift #1 có thật; ngày đạt chưa xác minh |
| 14 ngôn ngữ README | ✅ 13 bản dịch trong `docs/<lang>/` + tiếng Anh |
| Ngôn ngữ mã TS/Go | ✅ Khớp cấu trúc repo |

**Tổng: 5✅ / 3⚠️ / 0❌.** Ảnh không sai ô nào; điều đáng biết nằm ngoài ảnh (mục dưới).

### 1b.4 Điều ảnh không nói

- **Telemetry bật mặc định ở bản desktop chính thức.** `apps/desktop/src/main/telemetry.ts` gửi mỗi 6 giờ `install_id`, số lần mở, phút hoạt động, phiên bản, hệ điều hành, kiến trúc tới `https://admin.clawee.work/api/v1/public/desktop-usage`; `telemetryEnabled: true` trong `settings-store.ts`. Có công tắc tắt trong Cài đặt, mô tả nói rõ máy chủ ghi IP và không gửi nội dung dự án/file/hội thoại. README không nhắc. Quan hệ giữa domain `clawee.work` và dự án: chưa xác minh. Bản build từ nguồn không gửi (endpoint rỗng khi không phải bản chính thức).
- **Đổi giấy phép GPL-3.0 → Apache-2.0 trên mã có 22 email tác giả khác nhau** (commit trước 8/2026). Repo không có CLA/DCO trong `CONTRIBUTING.md`. Đổi từ GPL sang giấy phép dễ dãi hơn thường cần đồng ý của người giữ bản quyền; repo không ghi đã xin (chưa xác minh). Ai phân phối lại phần mã cũ nên để ý.
- **Trình tải video** nhận YouTube, TikTok, Douyin, Instagram… qua yt-dlp, có thể cần cookie nền tảng. Đây là công cụ, rủi ro điều khoản dịch vụ và bản quyền nằm ở người dùng.
- **Đánh giá bên ngoài:** chưa thấy bài dùng thử độc lập. Bài aiindigo.com ("deep dive") đọc như quảng bá; bản mirror SourceForge vẫn ghi GPLv3 (ảnh chụp cũ).

### 1b.5 Nhận xét & cách tận dụng

- **So với OpenMontage (§1):** OpenMontage để agent làm orchestrator qua skill + schema + gate; OpenCreator đặt **máy trạng thái trong daemon** và cho agent (Codex) cùng giao diện trực quan đẩy sự kiện vào đó. Mẫu đáng học: một nguồn sự thật cho cả UI lẫn hội thoại, mỗi lần sửa là một phiên bản.
- **Thế mạnh thật:** dịch phụ đề + lồng tiếng (14 ngôn ngữ nguồn, 101 ngôn ngữ đích theo README) có từ thời KrillinAI; giấy phép Apache-2.0 nay thoáng hơn AGPL của OpenMontage.
- **Rủi ro:** phụ thuộc Codex CLI và tài khoản OpenAI/nhà cung cấp; telemetry mặc định bật; nguồn gốc giấy phép phần mã cũ; dự án đổi tên ba lần, tốc độ thay đổi cao (358 commit trong ~2,5 tháng).
- **Gợi ý:** chạy bản web từ nguồn (`pnpm web:dev`, không gửi telemetry) với `CODEX_HOME` riêng để khỏi đụng cấu hình Codex chung; nếu dùng desktop, tắt "Send anonymous usage data".

---

## 1c. saturndec/waoowaoo (nay là waooAI/waoowaoo): từ "studio phim ngắn AI" thành workspace ảnh/video (link người dùng, 2026-10-13)

> Người dùng gửi `saturndec/waoowaoo`. Repo đã chuyển sang tổ chức `waooAI/waoowaoo` (link cũ vẫn chuyển hướng; shields trả cùng số cho cả hai). Đã clone toàn bộ repo (27 commit, HEAD `dfec20e` 21/9/2026), đọc README các bản, `LICENSE` qua `git log`, `docs/INSTALL.md`, `docker-compose.yml`, `Dockerfile.codex-runtime`, `package.json`. Chưa chạy test vì cần MySQL, Redis và Temporal.

### 1c.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 13/10/2026) |
|---|---|
| Repo | `waooAI/waoowaoo` (tên cũ `saturndec/waoowaoo`) · ~15k★, ~3,2k fork · ~140 issue mở, **0 PR mở** · release ổn định mới nhất v0.4.1 (3/4/2026); tag `v0.5.0-beta.1` (5/9/2026); commit cuối 21/9/2026 |
| Tác giả | "saturn" (`saturndec`, ~23 commit) và bot `waoowaoo-publisher` (4 commit). Mã được đẩy theo từng đợt phát hành, không có lịch sử phát triển chi tiết. Đội ngũ có bản web thương mại (waitlist tại waoowaoo.com) |
| Đóng góp | README: nhóm lõi tự làm, PR từ ngoài chỉ để tham khảo, **không merge trực tiếp** |
| Stack (v0.5) | Next.js 16 + React 19, MySQL + Prisma, **Temporal** (durable execution), Redis, MinIO riêng, NextAuth, Caddy (HTTPS cục bộ cổng 1443) |
| Model | Bản preview chỉ mở cấu hình **OpenRouter**: GPT Image 2, các bản Nano Banana, Seedance, MiniMax H3/H3 Max. Người dùng tự trả phí qua key OpenRouter của mình |

### 1c.2 Hai sản phẩm khác nhau dưới cùng một tên

| | v0.3.0 → v0.4.1 (3–4/2026) | v0.5.0-beta.1 (9/2026) |
|---|---|---|
| Mô tả | "waoowaoo AI 影视 Studio": công cụ làm **phim ngắn/truyện tranh động** từ tiểu thuyết: phân tích kịch bản, sinh nhân vật và cảnh nhất quán, dựng phân cảnh thành video, lồng tiếng nhiều vai | "AI creative workspace for images and videos": Assistant bên phải + canvas để quản lý tài liệu tham chiếu, sinh ảnh/video, tinh chỉnh thành phiên bản mới |
| Lồng tiếng / nhạc | Có | **Chưa có** trong bản preview |
| Người làm | README ghi "hiện chỉ mình tôi phát triển" | "waoowaoo team", nhóm lõi |
| Giấy phép | Không có file `LICENSE` tới 27/4/2026, sau đó **CC BY-NC-SA 4.0** (giấy phép nội dung, cấm thương mại) | **Elastic License 2.0**: dùng cá nhân/nội bộ, sửa và phân phối được; cấm cung cấp thành dịch vụ cho bên thứ ba. README tự ghi "source-available, not OSI-approved open source" |

Bản v0.5 thay đổi gần như toàn bộ mã (2.372 file, +147k / −191k dòng so với bản trước). Phần lớn bài giới thiệu bên ngoài (sourcepulse, addrom, skillsllm) và nhiều bản sao vẫn mô tả sản phẩm cũ. Bản sao trên Gitee còn ghi MIT, **sai** với cả hai giấy phép thật.

### 1c.3 Điều cần biết trước khi cài (đọc mã)

- **Container của app được gắn Docker socket** (`/var/run/docker.sock`) để tự khởi container Assistant cho từng dự án. Quyền này tương đương quyền root trên máy host; `docs/INSTALL.md` cũng chỉ ghi "use a trusted local installation". Chỉ nên cài trên máy hoặc VM riêng.
- **Assistant chạy OpenAI Codex CLI 0.146** trong container riêng (sandbox bubblewrap, giới hạn mặc định 2 CPU, 2 GB RAM, 256 tiến trình, tự tắt sau 15 phút rảnh).
- **HTTPS cục bộ bằng CA riêng của Caddy**: quy trình cài yêu cầu tin `root.crt` trên máy. Phần này làm cẩn thận: prompt cài đặt bắt agent hỏi rồi mới tin chứng chỉ, không xuất `root.key`, không bỏ kiểm TLS.
- **Cài kiểu "nhắn coding agent tự cài"**, ghim image theo digest bất biến của release. Prompt cài cũng cấm agent chạy tác vụ AI trả phí khi chưa được đồng ý và cấm hỏi key trong chat. Đây là mẫu prompt cài đặt đáng tham khảo.
- **Có hai bản**: self-hosted (repo này, `BILLING_MODE=OFF`) và bản cloud có tính tiền (script test nhắc thư mục `ee/` không có trong repo).
- **Bản preview**: README cảnh báo còn lỗi; dữ liệu giữa các bản beta trước đây không tương thích, phải xóa dữ liệu cũ khi nâng cấp.

### 1c.4 So sánh & dùng thế nào

| Dự án (shields 13/10/2026) | ★ · license | Khác waoowaoo |
|---|---|---|
| OpenMontage (§1) | ~68k · AGPL-3.0 | Agent điều phối pipeline video, mã mở OSI |
| OpenCreator (§1b) | ~13k · Apache-2.0 | Workspace sáng tạo trên Codex CLI, mạnh về dịch/lồng tiếng |
| `HBAI-Ltd/Toonflow-app` | ~17k · MIT theo GitHub (một trang tổng hợp ghi AGPL, chưa xác minh) | Gần với waoowaoo bản cũ nhất: tiểu thuyết → kịch bản → ảnh/video phim ngắn |
| `xuanyustudio/LocalMiniDrama` | ~2k · MIT | Phim ngắn/truyện tranh động chạy offline, SQLite, hỗ trợ Ollama |

- **Muốn đúng sản phẩm "tiểu thuyết → phim ngắn"** như phần lớn bài viết mô tả: đó là v0.4.1 (CC BY-NC-SA, cấm thương mại) hoặc Toonflow/LocalMiniDrama. Bản waoowaoo hiện tại đã đổi hướng thành workspace ảnh/video chung.
- **Không nên** dùng waoowaoo làm nền cho dịch vụ bán cho khách (ELv2 cấm), cũng không nên gửi PR với hy vọng được merge.
- **Đáng mượn:** prompt cài đặt cho agent (ghim digest, hỏi trước khi tin chứng chỉ và trước khi tốn tiền), và việc tách Assistant thành container có hạn mức tài nguyên.

**Nguồn §1c:** https://github.com/waooAI/waoowaoo (clone đầy đủ, HEAD dfec20e; README.md, README_en.md, README_zh.md, bản README ở v0.4.1 `531de26`, LICENSE ở `8bc8eb3` và `41ec33d`, docs/INSTALL.md, docker-compose.yml, Dockerfile.codex-runtime, package.json) · https://github.com/saturndec/waoowaoo · https://www.waoowaoo.com/ · https://trendshift.io/repositories/22585 · https://www.sourcepulse.org/projects/25569794 · https://addrom.com/waoowaoo-ai-studio-self-hosted-ai-agent-platform-for-short-drama-and-film-video-production/ · https://skillsllm.com/skill/waoowaoo · https://gitee.com/chees_cn/waoowaoo · https://gittrend.io/repo/waooAI/waoowaoo · https://awesome.ecosyste.ms/projects/github.com%2FwaooAI%2Fwaoowaoo · https://www.elastic.co/licensing/elastic-license · https://github.com/HBAI-Ltd/Toonflow-app · https://github.com/xuanyustudio/LocalMiniDrama · https://www.sourcepulse.org/projects/23907340 · https://www.sourcepulse.org/projects/28710401

## 1d. Kiểm ảnh: topviewai/topview-3d-builder, dựng cảnh 3D cho agent trước khi sinh video (ảnh người dùng gửi, 2026-10-16)

> Ảnh là đầu README trên GitHub: logo tím, tiêu đề "Let AI build your 3D scenes", câu "From an idea, to a 3D scene built by your agent, to a real animated video. Free, runs locally, no sign-up.", bốn huy hiệu (license Apache 2.0 · python >=3.11 · node >=20.6 · runs 100% local), dải link Quick Start | Examples | Tutorial | 3D Builder | Topview.ai | Issues, và video `3D-BUILDER-hero-9MB.mp4` (1:42) cảnh hành lang với các ma-nơ-canh màu. Đã clone toàn bộ repo (69 commit, HEAD `a0671f9` 16/10/2026), đọc README, `NOTICE`, `.mcp.json`, ba manifest plugin, skill `topview-3d-cli` và các file tham chiếu, `agent/pyproject.toml`; chạy test Python; cài bản phát hành từ PyPI rồi tự dựng và render một cảnh.

### 1d.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 16/10/2026) |
|---|---|
| Repo | `topviewai/topview-3d-builder` · **68★, 24 fork**, 2 PR mở, chưa có GitHub Release (tag `v0.1.3`…`v0.1.7`) · commit đầu 24/9/2026 với tên "Scene3D by TopView", công bố mã mở 15/10/2026 (X, dev.to) |
| Chủ | **Topview** (topview.ai), dịch vụ sinh video/ảnh AI trả phí theo credit. Người commit: Albert 30, 郭益雄 27, 3 người khác 4 commit mỗi người |
| Giấy phép | Mã, schema, tài liệu: **Apache-2.0**. Tài sản dựng sẵn trong `builtin-assets/` (nhân vật, tư thế, ảnh bìa): **CC BY 4.0**, phải ghi "Scene3D built-in assets © Topview, CC BY 4.0". Font editor: OFL 1.1 |
| Thành phần | CLI Python `topview-3d-cli` (PyPI, chỉ phụ thuộc `jsonschema`) điều khiển renderer Node/three.js chạy trong Chromium headless; Studio (editor web cục bộ, ~555 file); skill cho Claude Code, Codex, Cursor |
| Phạm vi bản này | 4 ma-nơ-canh (Child, Youth, Female, Man), 121 tư thế **tĩnh**, 5 khối hình cơ bản, camera tĩnh và keyframe vị trí. Skill tự ghi: **không có thư viện chuyển động**, không hứa hẹn dáng đi hay hoạt ảnh cơ thể |

### 1d.2 Kiểm từng ô trong ảnh

| Ô trong ảnh | Kiểm | Ghi chú |
|---|---|---|
| "Free, runs locally, no sign-up" | ⚠️ | Đúng với phần **dựng và render**: tự chạy bản 0.1.7, dựng cảnh hai nhân vật + camera và render một khung 640×360 trong khoảng 2 giây, không cần tài khoản; lời gọi mạng duy nhất trong CLI là tới Studio ở `localhost`. Nhưng câu này gộp cả bước "to a real animated video", mà bước đó cần một dịch vụ sinh video. Video ví dụ trong README ghi "rendered by Topview.ai" |
| license Apache 2.0 | ✅ | Đúng với mã. Tài sản dựng sẵn là CC BY 4.0, phải ghi công khi dùng |
| python >=3.11 | ✅ | `requires-python = ">=3.11"` |
| node >=20.6 | ⚠️ | README và bài dev.to ghi 20.6+, nhưng `editor/package.json` khai `engines.node >=18.0.0`. Đã chạy được với Node 24.22 |
| runs 100% local | ⚠️ | Lõi đúng, **plugin thì không**: `.mcp.json` ở gốc repo khai máy chủ MCP từ xa `https://mcp-3d.topview.ai` (OAuth). Manifest Codex trỏ thẳng tới file này, marketplace Codex đặt `"authentication": "ON_INSTALL"`. Manifest Claude không khai, nhưng Claude Code **tự nạp `.mcp.json` ở gốc plugin** (docs plugins-reference: "loads `.mcp.json` at the plugin root first"). Cài plugin vào Claude Code vì thế cũng đăng ký máy chủ `topview-3d`. Nó chỉ chạy được khi người dùng đồng ý OAuth, không âm thầm gửi dữ liệu. Bài dev.to không nhắc tới máy chủ MCP này |
| Link Quick Start · Examples · Tutorial · 3D Builder · Topview.ai · Issues | ⚠️ | Quick Start và Issues trỏ đúng chỗ. **Examples gãy**: neo `#see-what-you-can-make` không có heading tương ứng (mục gần nhất là `### Example`). 3/6 link dẫn về topview.ai (tutorial, trang sản phẩm, trang chủ) |
| Video hero 1:42 | ⚠️ | Phần dựng cảnh khớp sản phẩm; phần video thật cuối cùng do Topview sinh, không phải do công cụ mã mở này tạo |

**Tổng:** 2✅ / 5⚠️ / 0❌. Không có ô sai hẳn. Ngoài link Examples gãy, các ⚠️ có chung một gốc: ảnh gộp phần mã mở chạy cục bộ (dựng, kiểm, render khung tham chiếu) với bước sinh video trả phí của Topview.

### 1d.3 Điều ảnh không nói (đọc mã và tự chạy)

- **Bước sinh video là phễu về Topview, nhưng có thứ tự và cổng đồng ý.** `references/generate.md` buộc agent dùng trước dịch vụ người dùng đã nêu hoặc công cụ đã cài trên máy. Chỉ khi không có gì, agent mới **tự đăng ký** máy chủ MCP `https://mcp-browser.topview.ai` vào cấu hình host (với Cursor là gộp vào `~/.cursor/mcp.json` cấp người dùng, sao lưu trước, không in file), rồi để người dùng tự hoàn tất OAuth. Agent bị cấm hỏi mật khẩu, cookie hay token. Commit `58b06ab` (14/10) mới thêm việc tự kết nối này.
- **Một lần đồng ý sinh là chạy hết vòng đó.** Skill viết: sau khi người dùng cho phép một "generation round", agent upload khung tham chiếu, gửi, chờ, nhận kết quả **mà không hỏi lại**, chỉ báo dịch vụ, nội dung upload và chi phí. Sửa cảnh 3D thì phải hỏi lại cho vòng mới. Đây là một ngân sách đồng ý theo vòng; nếu dùng với credit thật, nên tự đặt trần chi phí.
- **Skill ở HEAD ghim một phiên bản chưa có trên PyPI.** Commit `24c2374` (15/10) ghim `topview-3d-cli==0.1.8` ở skill và cả ba plugin, nhưng PyPI (đọc 16/10/2026) mới tới **0.1.7** (0.1.3 cũng không có). Làm đúng bước 1 của skill (`uvx --python 3.12 topview-3d-cli@0.1.8 doctor --json`) sẽ lỗi cài đặt. Phần hướng dẫn xử lý lỗi của skill giả định lỗi do mirror cũ, không xét trường hợp bản chưa phát hành.
- **Test:** `pytest` thư mục test của CLI (cài từ mã nguồn): **214 pass, 28 skip** (cần editor đã build), **1 fail** (`test_node_batch_state_reports_primitive_sizes`, `ERR_MODULE_NOT_FOUND`). Test này cần editor đã build nhưng thiếu điều kiện skip như 28 test kia, nên là lỗi môi trường chứ không phải lỗi logic.
- **Chạy thật bản 0.1.7:** `doctor` báo đủ (Python, Node, runtime đóng gói, 4 nhân vật, 121 tư thế, 5 khối); `browser ensure` tận dụng Chromium sẵn có; `project init` → `node batch` (2 nhân vật + 1 camera) → `render` ra `frame-0.png` cùng sha256 kiểm được. Khung hình là ma-nơ-canh trên lưới, đúng mục tiêu "tham chiếu dàn cảnh", không phải ảnh thành phẩm.
- **Thiết kế đáng học:** cảnh là tệp JSON (`.topview-3d/`) sửa bằng lệnh có `expectedSceneSequence` (khoá lạc quan, lệnh dựa trên trạng thái cũ thì bị từ chối); `node batch --dry-run` và `evaluate` kiểm số (chạm đất, va chạm, khoảng cách, khung hình) **trước** khi render; mỗi lần render ghi `documentSha256` và đánh dấu bản render cũ là `stale`. Đây là cùng ý "kiểm bằng máy trước khi tiêu credit" mà OpenMontage (§1) làm ở mức pipeline.

### 1d.4 So sánh & dùng thế nào

| Dự án (shields 16/10/2026) | ★ · license | Khác topview-3d-builder |
|---|---|---|
| `ahujasid/blender-mcp` | ~31k · MIT | Agent điều khiển Blender đầy đủ qua MCP: mạnh hơn nhiều về mô hình, vật liệu, hoạt ảnh, nhưng phải cài Blender. Repo của chủ kho `design-os-3d-blender` dùng hướng này (mục 23 §6.1; mục 14) |
| `earthtojake/text-to-cad` | ~21k · MIT | Cùng mẫu "plugin cho coding agent + CLI + viewer cục bộ", nhưng cho CAD cơ khí (mục 20 §3e) |
| Higgsfield 3D Jutsu, Spline AI Agent, Topview 3D Builder bản web | dịch vụ trả phí | Prompt → cảnh 3D chỉnh được → video, chạy trên cloud; bản web của Topview tính phí mỗi lần dựng cảnh (trang Topview, chưa xác minh giá) |
| `topviewai/skill` | ~40 · Apache-2.0 | Skill khác của cùng hãng, gọi dịch vụ Topview qua MCP để sinh media; không phải công cụ cục bộ |

- **Dùng được ngay cho:** dựng phân cảnh tham chiếu (vị trí nhân vật, hướng nhìn, góc máy, chuyển động camera) rồi đưa khung hình vào **bất kỳ** model video nào có nhận ảnh tham chiếu. Phần này mã mở thật và chạy cục bộ.
- **Trước khi cài plugin:** hiểu rằng plugin đăng ký sẵn một máy chủ MCP từ xa của Topview. Nếu chỉ cần phần cục bộ, cài CLI từ PyPI (`pip install topview-3d-cli==0.1.7`, bản đã kiểm ở đây) và chép riêng skill, bỏ `.mcp.json`. Ghim phiên bản có thật trên PyPI.
- **Không trông đợi** hoạt ảnh nhân vật: bản này chỉ có tư thế tĩnh và keyframe vị trí. "Real animated video" là việc của model video phía sau.
- **Rủi ro dự án:** repo 3 tuần tuổi, 68★, do một công ty có sản phẩm trả phí phát triển; phần cục bộ có lợi ích thật nhưng vai trò chính là kênh dẫn tới dịch vụ sinh video của Topview.

**Nguồn §1d:** https://github.com/topviewai/topview-3d-builder (clone đầy đủ, HEAD a0671f9; README.md, NOTICE, LICENSE, builtin-assets/LICENSE, .mcp.json, .claude-plugin/{plugin,marketplace}.json, .codex-plugin/plugin.json, .agents/plugins/marketplace.json, skills/topview-3d-cli/SKILL.md, references/{generate,doctor-browser,camera,checks,add-character}.md, agent/pyproject.toml, agent/topview_3d_cli/local_studio.py, editor/package.json) · https://pypi.org/pypi/topview-3d-cli/json (đọc 16/10/2026: bản mới nhất 0.1.7) · https://code.claude.com/docs/en/plugins-reference (`.mcp.json` ở gốc plugin được nạp trước) · https://dev.to/topviewai/from-one-prompt-to-an-editable-3d-scene-we-open-sourced-a-local-first-agent-workflow-npa (15/10/2026) · https://x.com/TopviewAIhq/status/2110615678805774657 · https://www.topview.ai/3d-builder · https://github.com/topviewai/skill · https://github.com/ahujasid/blender-mcp · https://github.com/earthtojake/text-to-cad · https://docs.spline.design/spline-ai/ai-agent · https://higgsfield.ai/blog/higgsfield-3d-jutsu

## 1e. Kiểm bài "10 kho mã nguồn cực kỳ mạnh mẽ mà bạn không nên bỏ qua" (bài người dùng gửi, 2026-10-19)

> Bài liệt kê 10 repo cho quy trình sáng tạo nội dung: kịch bản → ảnh → giọng → nhạc → dựng video → Shorts → podcast → đăng bài. Đã clone cả 10 (blob:none, đủ lịch sử), đọc README/LICENSE/package.json, lấy số sao + license qua shields ngày 19/10/2026. Link mục 2 trong bài bị cắt ("ScrapeCre…"); repo đúng là `ScrapeCreators/social-media-research-skills`.

### 1e.1 Bảng kiểm

| # | Repo | ★ · license (19/10/2026) | Commit cuối · số commit | Kiểm | Điều bài không nói |
|---|---|---|---|---|---|
| 1 | `krillinai/OpenCreator` | ~14k · Apache-2.0 | 19/10/2026 · 983 | ✅ | Đã có hồ sơ §1b: dùng Codex CLI làm động cơ; tài khoản, tín dụng và "official model service" là dịch vụ trả phí |
| 2 | `ScrapeCreators/social-media-research-skills` | ~4,2k · MIT | **26/8/2026 · 7** | ⚠️ | **Bắt buộc `SCRAPECREATORS_API_KEY`** (dịch vụ thu thập dữ liệu trả phí của chính tác giả); 13 skill là lớp prompt trên API đó. Chỉ 7 commit |
| 3 | `LearningCircuit/local-deep-research` | ~9,3k · MIT | 19/10/2026 · **8.382** · v1.10.7 | ✅ | Web + tài liệu cá nhân, model local và cloud đúng như bài. Có CodeQL, Semgrep, OpenSSF Scorecard. Huy hiệu "SimpleQA ~95%" là **tự đo** trên dataset của dự án |
| 4 | `black-forest-labs/flux2` | ~2,8k · Apache-2.0 (mã) | **12/3/2026 · 12** | ✅ có lưu ý | Đúng: **Klein 4B và 4B Base** trọng số Apache-2.0, ~8 GB VRAM. Nhưng **Klein 9B, 9B KV, 9B Base và FLUX.2 [dev] dùng FLUX Non-Commercial License** → làm thumbnail/quảng cáo thương mại chỉ được với bản 4B. Repo là mã inference, ít commit |
| 5 | `hexgrad/kokoro` | ~9,5k · Apache-2.0 | **6/8/2025 · 71** | ✅ | 82M tham số, trọng số Apache. Thư viện đã **14 tháng không commit**; không clone giọng (mục 14) |
| 6 | `ace-step/ACE-Step-1.5` | ~14k · MIT (mã) | 29/8/2026 · 1.410 · v0.1.8 | ✅ | Chạy local < 4 GB VRAM theo README (bản XL 4B cần ≥ 12 GB). "Chất lượng giữa Suno v4.5 và v5" là **tự nhận**. License trọng số trên Hugging Face **(chưa xác minh)** |
| 7 | `YILS-LIN/short-video-factory` | ~5,8k · **AGPL-3.0** | 16/10/2026 · 145 · v1.3.0 | ⚠️ | **AGPL-3.0**: nhúng vào dịch vụ phải mở mã. App **Electron 22** (hết hỗ trợ từ 2/2024). TTS chỉ có **EdgeTTS** (gọi dịch vụ đọc online của Microsoft Edge qua thư viện không chính thức); LLM qua API tương thích OpenAI. README tiếng Trung |
| 8 | `Anil-matcha/AI-Youtube-Shorts-Generator` | ~5,5k · MIT | 11/10/2026 · 29 | ⚠️ | Chế độ mặc định `--mode api` dùng **MuAPI** (dịch vụ trả phí theo clip, README quảng bá nhiều lần). `--mode local` chạy được bằng yt-dlp + faster-whisper + OpenCV, nhưng **vẫn cần API key OpenAI hoặc Gemini** cho bước chọn đoạn |
| 9 | `souzatharsis/podcastfy` | ~6,7k · Apache-2.0 | **4/5/2026** · 399 · v0.4.0 | ✅ | 100+ LLM (có local), TTS OpenAI/Google/ElevenLabs/Edge. Đã 5 tháng không commit |
| 10 | `langchain-ai/social-media-agent` | ~2,9k · MIT | 19/10/2026 · 1.058 | ✅ có lưu ý | URL → nháp X/LinkedIn, có duyệt (HITL) và lên lịch đúng như bài. Cần **Anthropic API + LangSmith + FireCrawl + Arcade** (Arcade lo đăng nhập và đăng bài), tùy chọn Supabase/Slack. Là ví dụ tham chiếu của LangGraph, không phải sản phẩm |

**Tổng:** 7✅ / 3⚠️ / 0❌. Mọi repo đều tồn tại và làm đúng việc bài mô tả. Điểm bài bỏ qua là **chi phí và ràng buộc**: 4/10 repo cần dịch vụ trả phí hoặc API key bên thứ ba để chạy được (mục 2, 8, 10, và OpenCreator ở mức tài khoản), 1 repo AGPL, và 4/6 biến thể FLUX.2 là non-commercial.

### 1e.2 Ghép thành quy trình, và chọn bản nào

| Bước | Lựa chọn trong bài | Mở hoàn toàn / chạy local? | So với kho |
|---|---|---|---|
| Nghiên cứu chủ đề | Local Deep Research | ✅ (local model + SearXNG) | Repo trưởng thành nhất trong danh sách |
| Nghiên cứu mạng xã hội | Social Media Research Skills | ❌ cần API ScrapeCreators | Chỉ là skill trên API trả phí |
| Ảnh | FLUX.2 [klein] 4B | ✅ (Apache, ~8 GB VRAM) | Chạy qua ComfyUI (mục 14) tiện hơn dùng repo inference trực tiếp |
| Giọng | Kokoro | ✅ (Apache, CPU được) | Không clone giọng; cần giọng riêng thì xem mục 14 (Chatterbox, Fish Audio) và mục 18 (TTS tiếng Việt) |
| Nhạc | ACE-Step 1.5 | ✅ (MIT mã; trọng số chưa xác minh) | |
| Dựng video ngắn | Short Video Factory | ⚠️ AGPL, Electron cũ, EdgeTTS | OpenMontage (§1) và các skill motion (mục 22) hợp hơn nếu dựng bằng agent |
| Cắt Shorts từ video dài | AI YouTube Shorts Generator | ⚠️ local mode vẫn cần LLM API | |
| Podcast | Podcastfy | ✅ nếu chọn LLM local + Edge/OpenAI TTS | |
| Đăng bài | Social Media Agent | ❌ cần 4 dịch vụ ngoài | Mẫu học cách làm HITL với LangGraph (mục 02, 21) |

**Dùng thế nào:** một quy trình **chạy local toàn bộ và dùng thương mại được** gồm Local Deep Research + FLUX.2 Klein 4B + Kokoro + ACE-Step 1.5 (kiểm license trọng số trước) + Podcastfy với LLM local. Các mục còn lại hoặc gắn với dịch vụ trả phí của tác giả (2, 8), hoặc cần nhiều API bên ngoài (10), hoặc có ràng buộc license/bảo trì (7). Trước khi nhúng vào sản phẩm: đọc license trọng số trên Hugging Face (FLUX.2, ACE-Step), và tránh AGPL nếu không muốn mở mã.

### 1e.3 Bản infographic "Nhà máy nội dung AI" (người dùng gửi, 2026-10-20)

Ảnh dạng cây thư mục VS Code (`ai-content-factory.md`) liệt kê **đúng 10 repo của §1e**, chia 6 nhóm: 01 Nghiên cứu & ý tưởng (Social Media Research Skills, Local Deep Research) · 02 Không gian sáng tạo (OpenCreator) · 03 Hình ảnh (FLUX.2) · 04 Giọng đọc & âm nhạc (Kokoro, ACE-Step 1.5) · 05 Video & podcast (Short Video Factory, AI YouTube Shorts Generator, Podcastfy) · 06 Phân phối nội dung (Social Media Agent). Mô tả từng dòng khớp bảng 1e.1; ảnh ghi đủ tên `ScrapeCreators/social-media-research-skills` (bài gốc bị cắt link).

- **Kiểm lại 20/10/2026:** số sao, license và release không đổi so với 1e.1 (shields: Social Media Research Skills ~4,3k, Local Deep Research ~9,4k, còn lại như cũ). Short Video Factory có thêm commit `a9516c1` (19/10, bỏ đường lùi phụ đề FFmpeg, dùng engine phụ đề riêng) nhưng vẫn v1.3.0, AGPL-3.0, `electron ^22.3.27`.
- **Điều ảnh vẫn không nói:** dòng cuối có nhắc "chọn theo nhu cầu, phần cứng & ngân sách", nhưng không ghi repo nào cần dịch vụ trả phí hay license nào hạn chế. Các lưu ý ⚠️ ở 1e.1 và bộ chạy local ở 1e.2 vẫn giữ nguyên.

**Nguồn §1e:** clone 19/10/2026 (blob:none, đủ lịch sử; README.md, LICENSE, package.json): github.com/{krillinai/OpenCreator, ScrapeCreators/social-media-research-skills, LearningCircuit/local-deep-research, black-forest-labs/flux2 (bảng model + model_licenses/LICENSE-FLUX-NON-COMMERICAL), hexgrad/kokoro, ace-step/ACE-Step-1.5, YILS-LIN/short-video-factory (package.json electron ^22.3.27), Anil-matcha/AI-Youtube-Shorts-Generator, souzatharsis/podcastfy, langchain-ai/social-media-agent} · img.shields.io/github/{stars,license}/… 19/10/2026 · skillselion.com/marketplace/ScrapeCreators/social-media-research-skills · skills-hub.ai/sources/social-media-research-skills · bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence · huggingface.co/hexgrad/Kokoro-82M · huggingface.co/ACE-Step/Ace-Step1.5

## 1f. Kiểm bài "Tự làm video AI xây kênh, chỉ cần 1 tài khoản AI": bộ 4 repo của CuongIT (ảnh người dùng gửi, 2026-10-21)

> Bài Facebook của CuongIT (GitHub `Cuongyd196`, 105 follower) giới thiệu "3 repo GitHub đã có sẵn các skill + ứng dụng CIT Voice Studio". Theo bài, người dùng chỉ cần thêm một gói AI (ChatGPT Plus, Claude Pro hoặc Google AI Pro) và một agent desktop (Codex, Claude Code hoặc Antigravity), rồi mở thư mục repo và làm theo README. Đã clone đủ lịch sử cả 4 repo, đọc README, SKILL.md, package.json, mã TTS và LICENSE, đọc số sao/fork qua shields ngày 21/10/2026. **Không cài và không chạy script nào của các repo.**

### 1f.1 Hồ sơ nhanh

| Repo | ★ · fork (21/10/2026) | Commit · thời gian | Engine | License thật | Kiểm |
|---|---|---|---|---|---|
| `Cuongyd196/auto-compare-video` | 220 · 125 | 21 · 24/7 → 24/9/2026 | HyperFrames 0.7.58 (ghim) + GSAP | MIT (có file) | ⚠️ |
| `Cuongyd196/remotion-cuongit-template` | 208 · 123 | 14 · 22/1 → 16/10/2026 | Remotion 4.0.407 (ghim) | **Không có file LICENSE**. Badge ghi MIT, `package.json` ghi `UNLICENSED` | ❌ license |
| `Cuongyd196/auto-video-gen` | 184 · 112 | 11 · 13/7 → 28/9/2026 | HyperFrames ^0.4.34 | MIT, nhưng là bản sao `hoquanghai/Auto-Create-Video` và file LICENSE đã thay tên tác giả gốc | ⚠️ |
| `Cuongyd196/cit-voice-studio` | 119 · 48 | 35 · 23/9 → 3/10/2026, tag 1.0.0–1.0.3 | App đóng mã (PyInstaller, FastAPI, ONNX Runtime) chạy VieNeu-TTS v3 Turbo | README ghi Apache-2.0, nhưng repo **không có mã nguồn và không có file LICENSE** | ⚠️ |

Số sao trong ảnh (215/206/181/112) lệch nhẹ so với bảng vì ảnh chụp sớm hơn.

**Điểm chung của 3 repo video:**

- Mỗi repo là **template kèm một skill**: `create-video`, `remotion-topic-explainer`, `create-news-video`.
- Skill được chép thành hai bản: `.claude/skills/` cho Claude Code và `.agents/skills/` cho Antigravity (Codex cũng đọc được `.agents/skills`). Không có bản riêng cho Gemini.
- Kịch bản do **chính agent viết**, trong mã không có lệnh gọi LLM API nào. Vế "chỉ cần 1 tài khoản AI" vì vậy là đúng.
- Không repo nào có CI. Chỉ auto-video-gen có test (60 case vitest, thừa hưởng từ bản gốc).
- Tất cả do một tác giả làm, dưới vài danh tính git; mỗi repo có 0–3 commit mang trailer Claude.

### 1f.2 Điều bài không nói (đọc mã)

#### auto-compare-video: video "A vs B" khoảng 20 giây, hai nhân vật robot

**Luồng chạy:**

1. Agent viết 8 câu thoại.
2. `generate-vo.mjs` gọi TTS cho từng câu, đo độ dài bằng `ffprobe` rồi ghi `durations.json`.
3. Agent **chép tay** các số đo vào đối tượng `VO` và các thẻ `<audio>` trong `index.html`.
4. `hyperframes render` xuất video. Lúc render không bước nào đọc `durations.json`.

**Lỗi lệch tiếng đã xảy ra trong repo:**

- Video mẫu `thien-thach-vs-sao-bang` được tạo lại giọng bằng Edge TTS ở commit `1dbc29d`.
- Clip mới dài 1,8–3,0 giây mỗi câu, tổng khoảng 20 giây.
- `index.html` vẫn giữ số đo Vbee cũ (1,0–2,0 giây, comment còn ghi "Real Vbee"), nên phụ đề và nhân vật chạy lệch với tiếng.
- Miệng robot chỉ lắc theo nhịp cố định 0,22 giây chứ không bám âm thanh.

**Không có bước kiểm chứng nội dung.** Agent tự viết phần so sánh, và README/skill không yêu cầu ghi nguồn. Khi bật `AUTO_CREATE_VIDEO=1`, quy trình đi thẳng từ chọn chủ đề đến chốt kịch bản mà không dừng cho người duyệt. Với kênh "chia sẻ kiến thức", đây là rủi ro lớn nhất của repo.

**Lặt vặt:**

- `package.json` của mỗi video có script `prepublish`, mà npm vẫn chạy khi `npm install` cục bộ. Script này gọi `sync-channel.mjs` để sửa `index.html` theo `.env`.
- `npx --yes` tự tải HyperFrames mà không hỏi.
- README dùng link affiliate Vbee.
- README nói font Be Vietnam Pro được nhúng sẵn, thực tế font này và GSAP được tải từ Google Fonts/jsDelivr lúc render.
- Provider mặc định không khớp giữa các nơi: `.env.example` ghi `edge`, README tiếng Anh ghi `vieneu`, skill ghi code lùi về `vbee` nhưng code thật lùi về `vieneu`.

#### remotion-cuongit-template: video giải thích 9:16 dài 40–60 giây

**Phần agent viết và phần dùng lại được:**

- Agent viết gần như mọi thứ: kịch bản, script sinh audio, toàn bộ thư mục `src/<Topic>/` và chỗ sửa trong `Root.tsx`.
- Phần dùng lại thật chỉ có:
  - `scripts/generate-tts.ts`: gọi Edge TTS hoặc CIT Voice Studio, đo độ dài từ header MP3/WAV, ghi `manifest.json`;
  - hai component `BrandHeader` và `SubtitleBox`.
- Phụ đề được chia đều 6 từ một khúc theo thời lượng cảnh, không có timestamp từng từ.

**License:**

- Repo không có file LICENSE, nên về pháp lý mọi quyền vẫn thuộc tác giả. Badge MIT không có giá trị, và `package.json` còn ghi `UNLICENSED`.
- README có nhắc Remotion "cần company license trong một số trường hợp" nhưng không nói ngưỡng: Remotion miễn phí cho cá nhân và công ty tối đa 3 người, công ty lớn hơn phải mua license (mục 22 §2.2).

**Font Segoe UI bị commit vào repo:** hai file `public/fonts/SegoeUI-{Regular,Bold}.ttf` (bản 5.65).

- Bảng name của font ghi "© 2022 Microsoft Corporation… Microsoft supplied font": chỉ được dùng theo điều khoản của sản phẩm Microsoft đi kèm, nên **không được phân phối lại**.
- Trước khi dùng, thay bằng một font OFL như Be Vietnam Pro hoặc Inter.

**Lặt vặt:**

- Ba file manifest lộ đường dẫn trên máy tác giả (`D:\cuongit\...`).
- `DockerExplainer` hard-code tên kênh "CƯỜNG IT" và `durationInFrames=1280`, trái với chính skill của repo.

#### auto-video-gen: URL tin tức hoặc GitHub → video 9:16

**Là bản sao của `hoquanghai/Auto-Create-Video`** (322★, MIT, 34 commit từ 29/4 đến 2/5/2026, có CI test và typecheck):

- 54/64 file trùng đường dẫn và 31 file giống hệt từng byte, kể cả `docs/superpowers/` ghi ngày 2026-04-29.
- Lịch sử mở đầu bằng commit `#Init` ngày 13/7/2026, không giữ commit gốc.
- README có ghi rõ đây là "bản fork… toàn bộ công sức thiết kế pipeline gốc thuộc về tác giả gốc".
- Nhưng file `LICENSE` đã đổi dòng copyright từ "Ho Quang Hai" thành "CuongIT". MIT yêu cầu giữ nguyên thông báo bản quyền gốc, nên đúng ra phải **thêm** dòng mới chứ không thay.
- Phần bổ sung thật của bản này: provider Vbee, hai theme `dark-neon`/`light-pro`, kiến trúc TTS dạng module kèm Edge TTS.

**Nội dung và bản quyền:**

- Agent tự lấy bài bằng WebFetch, viết `script.json` (schema Zod, tối đa 8 cảnh) rồi chạy pipeline.
- Code tải **og:image của bài báo** làm nền video, tức dùng lại ảnh có bản quyền của báo. Repo không có lời nhắc bản quyền nào.

**README lệch so với code:**

- "5 phút" chỉ là một câu trong README; bản gốc ghi "60 giây" ở tiêu đề và "~5 phút" ở bảng so sánh.
- Thư viện SFX không có sẵn trong repo: phải chạy `sfx:download` (cào myinstants.com) rồi `sfx:filter`.
- README ghi "SFX/BGM" nhưng pipeline không có BGM.
- Danh sách template, đường dẫn output và con số 60 FPS trong README không khớp code. Thực tế có 6 loại cảnh (`hook`, `comparison`, `stat-hero`, `feature-list`, `callout`, `outro`), render 30 fps, file ra là `video.mp4`.

**Đã kiểm `.claude/settings.json` đi kèm repo:** file chỉ cho phép sẵn vài lệnh đọc (curl GitHub API, `gh repo view`), là dấu vết phiên làm việc của tác giả. Không nguy hiểm.

#### cit-voice-studio: app TTS tiếng Việt

**Repo không có mã nguồn.** Toàn bộ repo là 5 file tài liệu (README, PRIVACY, DIEU-KHOAN, THIRD-PARTY-NOTICES và một ảnh), và README tự nói mã nguồn không công khai, chỉ phát hành bộ cài. Mọi điều dưới đây vì vậy là lời tác giả, **không kiểm được bằng mã**.

**Bộ cài:** bản v1.0.3 gồm .exe cho Windows (~363 MB), .deb (~463 MB) và .dmg (~427–447 MB), kèm mirror Google Drive.

**Công nghệ và model (theo file notices):**

- Python đóng gói bằng PyInstaller, chạy FastAPI/Uvicorn và ONNX Runtime; giao diện React hiển thị trong pywebview.
- Model mặc định là **VieNeu-TTS v3 Turbo** (ONNX int8) cùng MOSS Audio Tokenizer Nano, cả hai đều Apache-2.0 theo notices.
- Tùy chọn Supertonic 3 cho 31 ngôn ngữ khác, giấy phép OpenRAIL-M có điều khoản hạn chế sử dụng.
- ASR Zipformer tiếng Việt dùng để kiểm câu đồng ý khi clone giọng.
- Không có trọng số non-commercial (như F5-TTS-Vietnamese, viXTTS), nên theo lời README thì dùng thương mại được.

**Clone giọng có cổng đồng ý:**

- Người dùng phải ghi âm trực tiếp câu cam kết khoảng 8 giây; app không clone từ file có sẵn.
- Có điều khoản cấm mạo danh, và file xuất ra mang metadata "AI-generated".
- Đây là thiết kế đáng học (mục 14).

**API HTTP ở `127.0.0.1:8001`** (`/api/tts/generate`, `/stream`, `/voices`…): đây là cổng 3 repo video gọi tới qua provider `vieneu`/`cit`.

- Ở chế độ localhost, API **không xác thực**, nên mọi tiến trình trên máy đều gọi được.
- Chế độ LAN dùng header `X-API-Key` trên HTTP thường, không mã hóa.

**Bộ cài không ký số và không công bố checksum.** Đây là điểm đáng ngại nhất trong cả bộ, vì README hướng dẫn:

- bỏ qua cảnh báo SmartScreen;
- chạy `xattr -dr com.apple.quarantine` trên macOS;
- tắt Smart App Control của Windows 11, dù tự thừa nhận có thể không bật lại được.

**README mâu thuẫn với chính tài liệu của nó:**

- README nói "không cần Internet sau khi cài", nhưng lần clone giọng đầu tiên tải ASR ~77 MB, các bản FP32/Nano/Supertonic/GPU phải tải thêm, và bật GPU kéo gói PyPI/PyTorch không ghim phiên bản.
- README ghi Apache-2.0 cho một binary đóng mã mà repo không có file LICENSE hay NOTICE.

### 1f.3 Bài nói đúng gì, thiếu gì

| Claim của bài | Thực tế |
|---|---|
| "3 repo đã có sẵn các skill" | ✅ Mỗi repo có một skill, chép thành hai bản (Claude Code và Antigravity/Codex). Không có bản riêng cho Gemini |
| "chỉ cần 1 tài khoản AI" | ✅ cho phần viết kịch bản. ⚠️ cho phần giọng: Edge TTS miễn phí nhưng là dịch vụ đọc online không chính thức của Microsoft, văn bản bị gửi lên Microsoft, và thư viện `edge-tts-universal` dùng giấy phép **AGPL-3.0** (cả 3 repo đều kéo). Vbee, ElevenLabs và LucyLab trả phí. CIT Voice Studio cần máy 8–16 GB RAM |
| "chia sẻ miễn phí" | ⚠️ Miễn phí để dùng, nhưng: 1 repo không có license (về pháp lý không được phép tái sử dụng), 1 repo commit font Microsoft, 1 repo là bản sao đã đổi copyright, còn app giọng đóng mã |
| "mở thư mục bằng công cụ AI rồi làm theo readme.md" | ✅ Cách dùng này đúng. Nhưng README lệch code ở nhiều chỗ (template, fps, đường dẫn, provider mặc định), nên agent đọc skill và code sẽ chính xác hơn đọc README |
| (không nói) license Remotion | Công ty trên 3 người phải mua license Remotion |
| (không nói) kiểm chứng nội dung | Không repo nào có bước kiểm nguồn hay fact-check, và auto-video-gen dùng lại ảnh của báo |

**Tổng:** cả 4 repo tồn tại và làm đúng việc mô tả, ở mức "template + skill cho agent". Bộ này hợp để **học cách đóng gói quy trình làm video thành skill**, chưa hợp để nhúng nguyên vào sản phẩm hay kênh thương mại.

### 1f.4 Dùng thế nào

**Bài học cấu trúc:** tách phần "agent viết nội dung" khỏi phần "script tất định đo, ghép và render". Đây cũng là mẫu của OpenMontage (§1) và của skill HyperFrames (mục 22). Lỗi lệch tiếng của auto-compare-video cho thấy: **để code đọc `durations.json` lúc dựng**, đừng để agent chép số bằng tay (cùng tinh thần "cổng máy" ở mục 23).

**Nếu dùng từng repo:**

- **auto-video-gen:**
  - Dùng thẳng bản gốc `hoquanghai/Auto-Create-Video` (có CI); chỉ chọn bản của CuongIT khi cần Vbee hoặc hai theme mới.
  - Sửa `LICENSE` để giữ cả hai dòng copyright.
  - Bỏ nền og:image, hoặc chỉ dùng ảnh mình có quyền.
- **remotion-cuongit-template:**
  - Chờ tác giả thêm LICENSE hoặc xin phép trước khi tái sử dụng.
  - Xóa font Segoe UI.
  - Mua license Remotion nếu công ty trên 3 người.
  - Hoặc dựng lại từ `remotion-dev/skills` (mục 22 §2.3).
- **auto-compare-video:**
  - Thêm bước ghi nguồn tham khảo và người duyệt trước khi render.
  - Sửa lại thời gian trong video mẫu.
- **Giọng đọc:**
  - Cần mã mở thì dùng thẳng `pnnbao97/VieNeu-TTS` (Apache-2.0, mục 18) thay cho CIT Voice Studio.
  - Nếu dùng app, tải từ GitHub Releases (không dùng mirror Drive), đừng tắt Smart App Control cho toàn máy, và giữ API ở localhost.

**Thay thế cùng loại:** OpenMontage (§1), Short Video Factory (§1e, AGPL), workflow `/faceless-explainer` của HyperFrames (mục 22), MoneyPrinterTurbo (§3).

**Nguồn §1f:** clone đủ lịch sử 21/10/2026: github.com/Cuongyd196/auto-compare-video (HEAD 50b1f34; CLAUDE.md, AGENTS.md, `.claude/skills/create-video/`, `videos/*/{package.json,index.html,generate-vo.mjs,assets/vo/durations.json}`, commit 1dbc29d, LICENSE) · github.com/Cuongyd196/remotion-cuongit-template (HEAD 3af5eac; package.json, src/Root.tsx, scripts/generate-tts.ts, public/fonts/SegoeUI-*.ttf (đọc bảng name), `.claude/skills/remotion-topic-explainer/`, docs/cit-voice-studio.md) · github.com/Cuongyd196/auto-video-gen (HEAD 86cda98; README.md, README.full.md, README.en.md, LICENSE, package.json, package-lock.json (`edge-tts-universal` 1.4.0 AGPL-3.0), src/pipeline.ts, src/render/script-schema.ts, `.claude/settings.json`, `.claude/skills/create-news-video/`) · github.com/Cuongyd196/cit-voice-studio (HEAD 0b0b995; README.md, PRIVACY.md, DIEU-KHOAN.md, THIRD-PARTY-NOTICES.md) · github.com/hoquanghai/Auto-Create-Video (clone 21/10/2026, 34 commit, so sánh từng file với auto-video-gen) · img.shields.io/github/{stars,forks,license,followers}/… 21/10/2026 · github.com/Cuongyd196 (profile "CuongIT") · github.com/vu05051995/auto-compare-video (fork, 0★) · github.com/dongphuongman/hyframe-video, github.com/ptit9x/auto-generate-short-videos (biến thể cùng họ, 0★) · remotion.pro/license

## 2. Làn sóng "video / motion skills" cho Claude Code (trendshift topic ai-video, 10/2026)

| Repo | Số hiển thị (★?) | Ghi chú |
|---|---|---|
| zhuyansen/awesome-claude-video-skills | ~55k | Danh sách skill video cho Claude |
| allenv0/SCM | ~47k | |
| howseen-ai/claude-motion-design | ~45k **(sai — thực tế 450★ ngày 12/10, xem mục 22)** | Motion design bằng skill; Playwright + ffmpeg |
| guanmo-ai/awesome-ai-motion · gongnyang/awesome-ai-motion | ~30k · ~10.5k | |
| joeseesun/opus-video-prompts · zhuyansen/awesome-opus-5.5-video | ~27.5k · ~15.6k | Prompt video cho Claude Opus |
| adunext/adu-motion-video · unclejobs-ai/motion-video-skill | ~24k · ~11.6k | |
| FavioVazquez/showtime · Remocn/remocn-studio | ~23k · ~16k | |
| ferndesk/no-slop-motion | ~0.9k | Chống "motion slop" (so với Taste Skill, mục 06) |

**Nhận định:** số liệu chỉ từ một trang aggregator và tăng rất nhanh → cần xác minh từng repo (đã kiểm: claude-motion-design thực tế 450★, tức bảng này có thể lệch ~100 lần — **không dùng các số ★ ở bảng này**; 16 repo motion/video đã xác minh ở mục 22); nhưng xu hướng rõ: *video/motion được đóng gói thành skill cho coding agent* thay vì app riêng. OpenMontage là bản "full pipeline" của xu hướng này.

## 3. Model & công cụ video mở liên quan

| Dự án | ★ (ước lượng) | Ghi chú |
|---|---|---|
| Remotion | 63,4k (12/10/2026) | Video bằng React; engine compose của OpenMontage (license riêng cho công ty ≥4 người; chi tiết mục 22) |
| Open-Sora 2.0 | ~24k | Nhiều sao nhất nhóm model; 11B |
| CogVideoX-1.5 | ~12.5k | Apache-2.0, 16GB VRAM |
| HunyuanVideo (Tencent) | ~11.9k | 60–80GB VRAM, license cộng đồng |
| Wan 2.1/2.2 | – | Model text/image-to-video mở; OpenMontage bundle workflow ComfyUI |
| OpenShorts, MoneyPrinterTurbo, ShortGPT | – | Tự động hóa video ngắn |
| codebase-video (plugin Claude Code) | – | Biến codebase thành video thuyết minh, agent khác verify claim |
| vimax-agnes | – | Pipeline idea → story → scene → video, free tier |
| FRAMEWORKERS (arXiv 2608.29814), *Agentic Artifact Creation* (2608.28122) | – | Nghiên cứu multi-agent cho sản xuất video |
| LTX-2 (Lightricks), Wan 2.2 | – | X-Studio chọn cho "xưởng video" (mục 23 §3.2): render cache SHA-256, MotionSpec, `qc.py` kiểm LUFS/độ dài/khung; nghiên cứu `RESEARCH-VIDEO-FACTORIES.md` so sánh video factory mở |
| codebase-video, vimax-agnes, MoneyPrinterTurbo | – | Xem thêm "video factory" trong X-Studio docs |

## 4. Nguồn

- https://github.com/calesthio/OpenMontage (README, AGENTS.md, AGENT_GUIDE.md, commits) · https://github.com/calesthio · https://openmontage.video
- https://pinggy.io/blog/openmontage_agentic_video_production/ · https://knightli.com/en/2026/06/22/openmontage-ai-video-production-guide/ · https://dev.to/andrew-ooo/openmontage-review-open-source-agentic-video-production-296l · https://hysenlabs.com/projects/calesthio-openmontage · https://www.opensourcealternatives.to/item/openmontage · https://explainx.ai/blog/openmontage-agentic-video-production-claude-code-2026 · https://www.visionstory.ai/open-source/openmontage · https://tosea.ai/blog/openmontage-agentic-video-production-guide · https://www.blog.brightcoding.dev/2026/10/10/calesthioopenmontage-agentic-video-production-from-natural-language
- §1b OpenCreator (13/10/2026): https://github.com/krillinai/OpenCreator (clone đầy đủ, 936 commit, HEAD 2b80bca 13/10/2026; README, LICENSE, CONTRIBUTING.md, `apps/desktop/src/main/telemetry.ts`, `settings-store.ts`, `apps/daemon/src/main.ts`, `startup.ts`, `.github/workflows/ci.yml`, commit afe6aa4/4d29f87/bfbf59a/406dec8) · https://trendshift.io/repositories/13360 · https://sourceforge.net/projects/krillinai.mirror/ · https://aiindigo.com/blog/krillinai-deep-dive-technical-review · https://tessl.io/registry/skills/github/krillinai/KrillinAI/krillinai-tts/review
- https://github.com/THU-MAIC/OpenMAIC/discussions/346 · https://github.com/volcengine/OpenViking/discussions/1083
- https://trendshift.io/topics/ai-video · https://www.atlascloud.ai/blog/tips/github-ai-video-generator-skill-directory-free-tools-vs-paid-apis-2026 · https://agenticvideos.org/ · https://arxiv.org/pdf/2608.29814 · https://arxiv.org/pdf/2608.28122
