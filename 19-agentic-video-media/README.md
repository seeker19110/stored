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
