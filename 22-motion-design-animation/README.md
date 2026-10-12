# 22 · Motion Design & Animation bằng code: launch video, hậu kỳ, hoạt hình ngắn, web UI motion

> Mục này mở ra từ danh sách 15 repo người dùng gửi ("15 repo GitHub biến Claude Opus 5.5 thành motion design studio", 2026-10-12) cộng link `tejashmakwana/motionmaxxing`. Mỗi repo được đọc trực tiếp (README, SKILL.md, commits, tác giả) và đối chiếu với directory/blog bên ngoài; **mọi claim trong bài đăng gốc đều được kiểm lại** (mục 7). Liên quan: mục 19 (OpenMontage, làn sóng video skill), 06 (UI/UX, Taste Skill, Anatomy), 20 (plugin/skill), 03 (evaluator loop).

---

## 0. Tóm tắt 60 giây

- Toàn bộ nhóm này là **"video as code"**: agent viết HTML/CSS/JS (GSAP, canvas, three.js, Remotion/React), một engine seek từng frame trong **headless Chromium** (Puppeteer/Playwright), **FFmpeg** ghép + master âm thanh (-14 LUFS). Không có model sinh video nào ở đây; "AI" là coding agent + skill có gu.
- Ba tầng: **nền tảng chính thức** (HyperFrames 61k★ của HeyGen, Remotion 63k★, GSAP skills 16k★, Motion 34k★, LottieFiles skill 2k★) → **skill pack cộng đồng** (10 repo, 114–1.300★, phần lớn 1–3 tuần tuổi, ra đời ngay sau Opus 5.5 ngày 22/9/2026) → **kit dạy học/bán khóa** (hyperframes-student-kit, Barty-Bart).
- Mẫu chung đáng học: **storyboard phải được duyệt trước khi render**, **timeline.json là nguồn sự thật** cho scene/audio/review, **contact sheet 1 frame/beat để agent tự soi**, **quality gate bằng script** (lint DOM, LUFS, collision), **"never claim done without re-render"**.
- Bài đăng gốc phóng đại ở vài chỗ: không repo nào "chỉ cần đưa link sản phẩm"; "120fps" của Motion là marketing; Remotion chính xác theo **frame** chứ không phải mili-giây; "Netflix engineers" là bịa; "5 prompt" thực ra "5 iterations".
- Coverage độc lập gần bằng 0 cho 10 repo cộng đồng; số sao tăng nhanh phần lớn nhờ bài đăng viral. Dùng được, nhưng coi là **thử nghiệm cá nhân**, không phải thư viện production.

---

## 1. Bản đồ 16 repo

| # | Repo | ★ / fork (12/10/2026) | Tuổi · commit | License | Loại | Renderer |
|---|---|---|---|---|---|---|
| A1 | AbubakrChan/product-launch-motion | 162 / 24 | 27/7/2026 · 12 | MIT + NOTICE | 1 SKILL.md | HTML/GSAP → HyperFrames hoặc Remotion → FFmpeg |
| A2 | charlie947/motion-graphics-skills | 214 / 36 | 26/9–11/10 · 28 | MIT | 15 skill | HyperFrames hoặc ffmpeg+Chrome (không bundle) |
| A3 | howseen-ai/claude-motion-design | 450 / 53 | 27/9–2/10 · 32 | MIT | 1 skill + Python | Playwright + ffmpeg tmix |
| B1 | nateherkai/hyperframes-student-kit | 1.300 / 388 | 18/4, republish 8/9 · ~13 | có LICENSE (loại chưa rõ) | workspace 15 skill | HyperFrames/GSAP |
| B2 | Barty-Bart/motion-graphics | 610 / 106 | 25/9–12/10 · 5 | MIT | 5 skill | Playwright + ffmpeg; SAM 2.1 local |
| C1 | cth9191/animate | 507 / 84 | 4–5/10 · 10 | MIT | skill + plugin | canvas → Playwright → ffmpeg |
| C2 | whaleyxbt/claude-motion | 325 / 35 | 29/9–9/10 · 11 | MIT (+Remotion) | 4 skill + AGENTS.md | Remotion; web-sims Chromium 60fps; SFX Python |
| C3 | haidrrrry/claude-remotion-skill | 390 / 43 | 13/6–12/8 · 9 | MIT (+Remotion) | 1 skill + .skill | Remotion 30fps |
| D1 | motiondivision/motion | 34.000 / 1.400 | 2018 (Framer Motion) · 8.267 | MIT; Motion+ trả phí | thư viện | WAAPI + ScrollTimeline, fallback JS |
| D2 | 199-biotechnologies/motion-dev-animations-skill | 160 / 28 | 7/11/2025 · 6 | MIT | 1 SKILL.md | sinh code Motion v11 (cũ) |
| E1 | heygen-com/hyperframes | 61.100 / 5.500 | 10/3/2026 · 5.483 | Apache-2.0 | engine + CLI + 21 skill | Puppeteer Chrome + FFmpeg; Lambda; cloud |
| E2 | remotion-dev/remotion | 63.400 / 5.000 | 6/2020 · 38.677 | Remotion License (free ≤3 nhân viên) | framework React | Chrome + FFmpeg; Lambda |
| E3 | remotion-dev/skills | 5.000 / 556 | 19/1/2026 · 88 | không có LICENSE (theo Remotion) | 12 skill | – |
| E4 | greensock/gsap-skills | 16.200 / 954 | 4/3/2026 · 24 | MIT (GSAP: Standard License) | 8 skill | – |
| E5 | LottieFiles/motion-design-skill | 2.100 / 133 | 12/3/2026 · 4 | MIT | 1 skill + 16 reference | – (nguyên lý, không thư viện) |
| + | Tejashmakwana/motionmaxxing | 114 / 13 | 6/10/2026 · 2 | Apache-2.0 | 1 SKILL.md | HTML+GSAP → headless Chrome + ffmpeg (HyperFrames hoặc plain) |

---

## 2. Nền tảng chính thức (nhóm E)

### 2.1 HyperFrames (HeyGen) — "Write HTML. Render video. Built for agents."

- **Cơ chế:** composition là `index.html` thuần; timing bằng `data-start`, `data-duration`, `data-track-index`, `class="clip"`; adapter GSAP (mặc định), CSS, Lottie, Three.js, Anime.js, WAAPI. `@hyperframes/engine` seek timeline tới từng frame trong **headless Chrome (Puppeteer)**, chụp, FFmpeg encode; `producer` trộn audio. Tất định. Chạy local/Docker/AWS Lambda (`@hyperframes/aws-lambda`) hoặc `cloud render` do HeyGen host. Xuất MP4/MOV/WebM/GIF/PNG.
- **CLI:** `npx hyperframes init|preview|render|lint|check|snapshot|publish|doctor|catalog|add|keyframes|skills update|cloud render|lambda …`. Yêu cầu Node 22+, FFmpeg; Git LFS tùy chọn (~240MB baseline).
- **Skill:** 21 skill (README; bảng liệt kê 20): router `/hyperframes`, 10 workflow (`/product-launch-video`, `/faceless-explainer`, `/pr-to-video`, `/embedded-captions`, `/talking-head-recut`, `/motion-graphics`, `/music-to-video`, `/slideshow`, `/general-video`, `/remotion-to-hyperframes` ~80% dịch máy), 9 domain skill (`-core`, `-animation`, `-keyframes`, `-creative`, `/media-use`, `-cli`, `-audio`, `-registry`, `/figma`). Cài `npx skills add heygen-com/hyperframes` hoặc `claude plugin install hyperframes@hyperframes`. Host: Claude Code, Codex, Cursor, Gemini CLI, IBM Bob…
- **Lịch sử:** tạo 10/3/2026, npm 0.1.0 ngày 23/3, mở nguồn Apache-2.0 (HeyGen April 2026 release), 6/2026 thêm 9 workflow skill + cloud render + Claude MCP connector, 7/2026 nằm trong HeyGen Video Agent, KeyFrames mở nguồn, Figma skill. Sao: ~21,6k tháng đầu → 32,5k (1/7) → 57,4k (6/10) → **61,1k (12/10)**. Vẫn **0.8.x pre-1.0**, 180 PR mở. Adopter nêu tên: tldraw, TanStack.
- **So với Remotion (chính README):** "Remotion đặt cược vào React component; HyperFrames đặt cược vào HTML thuần"; thừa nhận Remotion Lambda chín hơn.
- **Rủi ro:** stack nặng (Node 22, Chrome, FFmpeg); media library / cloud render / Video Agent là tính năng cần tài khoản HeyGen (lực hút lock-in); claim "rẻ hơn 91%" của bên thứ ba chưa kiểm chứng. `hyperframes-student-kit` **không phải** repo HeyGen.

### 2.2 Remotion — video bằng React, đơn vị thời gian là frame

- `useCurrentFrame()`, `durationInFrames`, `fps` trong `<Composition>`; headless Chrome chụp từng frame, FFmpeg encode (Node API, CLI, **Lambda** render hàng loạt, Vercel, WebCodecs client-side). Hiện **v4** (v4.0.534, 7/10/2026; release vài ngày/lần), v5 chưa ra; 63,4k★, 38.677 commit, 162 issue.
- **License:** không phải OSI. Free cho cá nhân, công ty **≤3 nhân viên**, phi lợi nhuận, đánh giá; còn lại cần Company License (Creators $25/seat/tháng; Automators $0,01/render, tối thiểu $100/tháng; Enterprise từ $500/tháng; remotion.pro/license 10/2026). Sẽ "đổi nhẹ" ở v5.
- **Cho agent:** tagline "Video tools for the agent era"; ba luồng: agentic (coding agent + skill/plugin), interactive (Studio kéo-thả ghi ngược vào code), programmatic. **MCP server đã deprecated** (hosted MCP tắt không sớm hơn 31/8/2026) vì stale, Remotion trả token, agent gọi không ổn, trùng `/remotion-docs` skill. Media Parser deprecated 1/2/2026 → Mediabunny. Remotion Recorder: app quay facecam+screen (4 nguồn, caption Whisper.cpp local, cắt im lặng).
- **Sửa claim:** chính xác theo **frame** (33,3 ms ở 30fps), không phải "mili-giây".

### 2.3 remotion-dev/skills — 12 skill chính thức

`/remotion-best-practices` (router "Skills 2.0": chỉ nạp context liên quan), `/remotion-create`, `/remotion-markup` (composition, animation, layout, typography, media, effects, audio, fonts, timing), `/remotion-studio`, `/remotion-render`, `/remotion-maps` (Mapbox, MapLibre, MapTiler, GeoJSON, CesiumJS), `/remotion-captions`, `/remotion-saas`, `/remotion-interactivity`, `/remotion-docs`, `/remotion-upgrade`, `/remotion-multimedia` (Mediabunny). Host chính thức: **Claude Code, Codex, Kimi Code, Cursor**; `npx skills add remotion-dev/skills` hoặc opt-in khi `bun create video`. Repo mirror tự động từ `packages/skills` của monorepo (commit "Update template" vài ngày/lần) → **không có LICENSE riêng**, nội dung trôi theo thời gian.

### 2.4 greensock/gsap-skills — 8 skill chính thức của GSAP

- `gsap-core`, `gsap-timeline`, `gsap-scrolltrigger`, `gsap-plugins` (ScrollTo, ScrollSmoother, Flip, Draggable, Inertia, Observer, SplitText, ScrambleText, MorphSVG, physics, CustomEase, GSDevTools…), `gsap-utils`, `gsap-react` (`useGSAP`, `gsap.context()`, SSR), `gsap-performance`, `gsap-frameworks`; kèm `.claude-plugin/`, `.cursor-plugin/`, `copilot-instructions.md`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `skills/llms.txt`. Host: Cursor, Claude Code, Codex, Windsurf, Copilot, Google Antigravity, OpenCode, Pi ("40+ agent"). 16,2k★ nhưng chỉ 24 commit, không commit code từ 4/2026; gittrend: 128 ngày trending.
- **Licensing (đã xác minh):** Webflow mua GSAP mùa thu 2024; **29–30/4/2025** (GSAP 3.13) GSAP "100% free kể cả thương mại", mọi plugin Club (SplitText, MorphSVG, ScrollSmoother…) vào gói npm `gsap` công khai, `gsap-trial` bỏ. Vẫn là **license độc quyền miễn phí**, không phải open source: cấm dùng trong công cụ animation no-code cạnh tranh với Webflow, cấm reverse engineering. Skill repo thì MIT.

### 2.5 LottieFiles/motion-design-skill — nguyên lý, không thư viện

- 1 SKILL.md v1.0.0 + 16 reference: `director/` (core-philosophy, decision-framework, **12 nguyên lý Disney cho UI**, motion-personality, emotion-mapping, choreography, narrative-structure, context-adaptation), `patterns/` (entrance-exit, state-feedback, ambient-continuous, multi-element), `reference/` (timing-easing-tables, property-selection, quality-checklist, troubleshooting).
- Nội dung cụ thể: checklist 8 bước (mục tiêu cảm xúc → personality → property chính → duration → họ easing → hero/staging → lớp phụ + ambient → "1/3 rules"); 4 archetype (Playful 150–300ms ease-out-back; Premium 350–600ms; Corporate 200–400ms mặc định UI; Energetic 100–250ms ease-out-expo); bảng duration (tooltip 80–120ms … reveal 600–1200ms); entrance ease-out, exit ease-in; không linear cho chuyển động không gian; không opacity-only cho state quan trọng; stagger tổng <500ms.
- Thư viện-agnostic (CSS, Framer Motion, GSAP, Lottie, Spring); **không sinh file Lottie**; LottieFiles định vị là "judgment" đi kèm Lottie Creator MCP (blog 15/4/2026: "MCP cung cấp tool, skill cung cấp phán đoán"). 2,1k★, **4 commit, 1 contributor**, không cập nhật từ 5/2026; trendshift +1.108★ (13/8–12/10).

### 2.6 Motion (motiondivision/motion) — Framer Motion độc lập

- Matt Perry tách khỏi Framer **12/11/2024** ("Framer Motion is now independent, introducing Motion") sau 6 năm; Framer sponsor đầu, Tailwind thứ hai; lý do: dùng ngoài React (vanilla, Vue). Motion for Vue 19/3/2025 (`motion-v`). Import `motion/react` thay `framer-motion` (npm `framer-motion` 14.1.0 vẫn phát hành song song). Tag **v14.1.0 (9/10/2026)**, v14.0.0 (2/10) — churn 13→14 trong một tuần. Sponsor: Framer, Cursor, Linear, Figma, Sanity, Clerk.
- **Engine hybrid:** WAAPI + ScrollTimeline cho transform/opacity/filter/clipPath chạy trên compositor; fallback JS cho spring, gesture, layout. "120fps" = chạy mượt tới tần số quét màn hình 120Hz, **không phải benchmark**, không áp dụng cho phần JS-driven.
- **Motion+** (motion.dev/plus): Solo $399 một lần, Team theo seat; 490+ example, 110+ tutorial, component premium (Carousel, AnimateNumber, Ticker, Cursor, Typewriter, ScrambleText, splitText, Curtains), Motion UI 30 section shadcn, AI Kit (transition editor, CSS spring), Discord riêng. **AI chính thức:** `npx motion-ai` cài skill `/motion` (+ `/motion-audit`, `/css-spring`, `/see-transition`), MCP `mcp.motion.dev`, `motion.dev/llms.txt`. Rủi ro: docs/example ngày càng sau paywall.

---

## 3. Launch video (nhóm A)

### 3.1 product-launch-motion (AbubakrChan) — "director's discipline, not a template"

- 1 SKILL.md; 12 reference (direction, story, sync, motion, camera, look, sound, QA, 14-shot catalog, **34 traps**, shipping, renderer contract); 8 script (`assemble`, `transitions`, `wire-audio`, `wire-grade`, `level-sfx`, `word-timings.mjs`, `master.sh`, `verify-cue.sh`); template `film.example.json`, `cues.example.json`, `BRIEF.md`, `frame-skeleton.html`; `evals/` (BASELINE.md, evals.json).
- **14 bước:** intake → BRIEF.md → 3 creative direction → **truth pass** (screenshot/số liệu thật) → SCRIPT.md 40–60s → VO → word timings → STORYBOARD.md → build → assemble → gates → render/master → verify → ship (bản dọc, caption, poster). Mỗi shot một HTML/GSAP; HyperFrames (mặc định) hoặc Remotion render; FFmpeg master 2-pass loudnorm -14 LUFS / -1 dBTP.
- **VO khớp từng từ ("Law 2"):** TTS tự chọn (Kokoro local, tự thu, ElevenLabs) → Whisper cho word timestamp → `audio/cues.json`; mỗi reveal khóa vào một từ. **Camera:** rig 2 node GSAP (dolly, parallax, orbit, rack focus, whip pan, zoom-to-detail); Three.js chỉ cho 1 hero shot. **Grade:** grain giữ qua frame, bloom/halation, chromatic aberration, light sweep, vignette.
- Phim tham chiếu 45s/11 shot render ~51s trên Mac M (phim thuộc khách hàng, không tái dùng). Commit "Correct every claim two audits could not verify" cho thấy tác giả tự audit README. 0 issue, **không có coverage độc lập**.

### 3.2 motion-graphics-skills (charlie947) — 15 skill, không renderer

- brand-intake (viết `brand.md` + `MOTION.md` mọi skill đọc trước), motion-brief-writer, reference-to-motion, motion-prompt-writer, launch-video, **apple-launch-film** (trigger "Apple keynote", có thể audit bằng skill `apple-design` bên thứ ba), vox-explainer, **animated-chart**, milestone-reveal, motion-effects (16 effect loop 8s), title-sequence-3d, model-showdown (1 brief qua 3 model), newsletter-promo, loop-cover, **reel-export** (9:16, safe zone). Số đếm lệch trong chính repo (About 13, README 15/"Fourteen").
- Mỗi skill sinh HTML/CSS/JS theo hợp đồng `window.seek()`; cần HyperFrames hoặc ffmpeg+Chrome để ra MP4. Host Claude Code, Codex (`.agents/skills`), Claude Desktop (zip); không Cursor. Không TTS, không beat-sync, không tách nền. README khuyên **Opus 5.5 qua `/model`**; "không cần API key".
- Tác giả Charlie Hills (MarTech AI Substack, 71k reader tự nhận; `social-media-skills` 4k★); Substack "Opus 5.5 Motion Graphics" bán board 16 effect. Coverage: chỉ directory.

### 3.3 claude-motion-design (howseen-ai) — Playwright + ffmpeg, beat sync thật

- Phim = một hàm `seek(t)` trong HTML (GSAP/WAAPI chỉ là kỹ thuật); **Playwright** chụp từng frame sau khi font load, WAAPI pause; subframe trộn bằng ffmpeg **`tmix`** (shutter 180°, không trộn qua cut); x264 BT.709; draft 540p trước master. `render.py` (probe/draft/full), `audio.py` (loudnorm -14), `fetch_assets.py` (Mixkit, Pexels, Unsplash, svgl, simple-icons, Geist), `scripts/remake/` (remake "frame-locked" phase 0–3 có split-screen sync check, kèm cảnh báo IP).
- **Beat sync:** tìm **drop thật bằng band energy** (numpy, không beat grid), offset nhạc để drop rơi đúng frame chính; SFX đặt trên peak đo được. Không TTS, không tách nền.
- Org Howseen (Pháp, SaaS GEO/AI-visibility), Raphaël Aubry; 17 commit ngày 27/9. trendshift +450★ (26/9–12/10); skillsdirectory A 100/100; ProSkills 22 medium static findings. Demo 24s 60fps "Opus 5.5, in **5 iterations**" (tự báo).
- **Sửa số liệu mục 19:** bảng trendshift ở mục 19 ghi ~45k★ là **sai** (aggregator); số thật 450★.

---

## 4. Hậu kỳ footage (nhóm B)

### 4.1 hyperframes-student-kit (Nate Herk) — workspace 15 skill, 1,3k★

- Không phải repo HeyGen. Workspace đầy đủ: `.claude/skills` + `.agents/skills` mirror, `.codex/`, AGENTS.md, CLAUDE.md, MOTION_PHILOSOPHY.md, style-library/, style-templates/, `video-projects/` (12 project dạy), tests/, skills-lock.json. 15 skill: cut-mistakes, cut-silences, edit-video, gsap, hyperframes, hyperframes-cli, hyperframes-registry, hyperframes-video-beats, make-a-video, motion-showreel, short-form-edit, short-form-video, style-library, video-storytelling, website-to-hyperframes (5 vendored từ HyperFrames → "14 vs 15").
- **Pipeline:** transcribe (ElevenLabs Scribe mặc định; Whisper API/local) → **cut-silences theo khoảng trống transcript** (giữ pause <0,55s, cắt dài còn 0,14–0,24s, head pad 0,22s, tail 0,34s; mất 15–20%) → **cut-mistakes** (lặp từ "the the", false start, retake theo text similarity; có confidence; **bắt buộc review**; HTML review tool; **không xóa "um/uh"**) → retimed transcript, EDL, beat-sync validation, preflight → **406 draft card** motion graphics 2 style (manifest/CSS token/slot), 2 scene template → `npx hyperframes render`. Kie.ai tùy chọn cho asset sinh.
- Rủi ro: issue #16 `kie.mjs` upload **bất kỳ file local** (exfiltration khi chạy agent); skillsllm scan WARNING (1 high npm audit sharp/libheif + 3 medium); GSAP/Google Fonts từ CDN; kit là funnel cho cộng đồng trả phí (Skool); ~200–285k token/build (YouTube guide, chưa xác minh). Yêu cầu Node 22+, FFmpeg+ffprobe, Chrome.

### 4.2 Barty-Bart/motion-graphics — B-roll biến hình + tách nền local

- 5 skill: **motion-broll**, **object-separation**, explainer-high-energy (~15s), explainer-default (~60s), explainer-engaging (~12s loop).
- **motion-broll:** video + SRT/VTT → `words.py` ước lượng word time **±0,2s** (faster-whisper tùy chọn; skill không transcribe) → Claude lập bảng clip để duyệt → mỗi clip là HTML trên `motion.js` spring engine: **một hình liên tục biến hình** (size, radius, màu, swap nội dung với blur, cursor click/drag), mỗi thay đổi ghim vào từ nói → `render.js` Playwright 4 subframe/frame (180°) + ffmpeg → MP4 cutaway, **ProRes 4444 .mov trong suốt**, compare.html, viewer.html, TIMING.md. Cắt cuối cùng vẫn làm trong NLE của bạn.
- **object-separation:** Meta **SAM 2.1** local (hiera-large 898MB NVIDIA ≥12GB; base-plus 323MB; tiny 156MB CPU ~5s/frame) torch/transformers/opencv trong venv; click điểm ở frame đầu; chunk 60 frame; ra `separated.mp4` tô xanh + mask PNG **nhị phân** (không soft alpha; yếu ở tóc). Không upload gì.
- Tác giả Bart Słodyczka (Melbourne, YouTube; `elevenlabs-twilio-ai-caller` 141★); coverage = 2 video của chính tác giả (25/9, 5/10) có affiliate/Skool. Issue #4: setup.sh relative path, crop 4K. Trùng tên với skill `/motion-graphics` của HyperFrames.

---

## 5. Hoạt hình ngắn & explainer (nhóm C)

### 5.1 cth9191/animate — 7 style thủ công, storyboard gate cứng

- Skill + plugin (`/plugin marketplace add cth9191/animate` → `/plugin install animate@animate`; hoặc `npx skills add`). Host Claude Code (fork port OpenCode). 10 commit trong 2 ngày 4–5/10/2026 (0.2.0 → 0.4.0 "voice-overs timed to the words"); commit đầu "Remove references to the studied creator" → grammar học từ một YouTube creator đã xóa tên.
- **Quy trình:** 0 Intake (gallery style) → 1 Story check (FORMATS.md, bảng beat, fact web-check) → 2 Look check (2–4 style frame) → 3 **Storyboard check** (mọi beat vẽ, duyệt từng panel; **"No animation before the storyboard is approved"**) → 4 Build (`build.mjs`, `tile.mjs`, score tổng hợp, `export.mjs`, `review.mjs`: contact sheet, cut grid, text-collision, LUFS) → 5 Deliver `renders/share.mp4` → 6 Learn (đề xuất rule vào `craft.md`).
- **Render:** một `index.html` `<canvas>`, seed tất định, Playwright/Chromium chụp frame → WAV + stems → ffmpeg MP4; audio tổng hợp trong code (-14 LUFS) hoặc beat-map nhạc người dùng (`beats.mjs`); VO tùy chọn ElevenLabs + faster-whisper. Animate "on 1s/2s", motion blur 4 sub-frame; 9:16/1:1/4:5/16:9; agent song song cho phim dài.
- **7 style:** cut paper, crosshatch ink, riso, sketchbook, manim-math, pixel art, isometric line art + slot custom đo từ reference (`compare.mjs`, `measure/refs.mjs`). SKILL.md thẳng thắn: chỉ **cut paper và crosshatch đã "carried full pieces"**. Tác giả "Chase" (285 follower; scroll-world 558★, taste-vault 106★, blender-to-web 91★). skillsdirectory grade B 84/100 (2 finding "installs packages at runtime").

### 5.2 whaleyxbt/claude-motion — taste + review loop + sound engine

- 4 skill trong `.claude/skills/`: **motion-design**, **review-loop**, **sound-design**, **web-sims** + AGENTS.md (Codex/OpenCode/Cursor) + ví dụ Remotion + `sfx/` Python + `sims/`.
- **timeline.json là nguồn sự thật**: mọi beat là timestamp có tên; scene, audio, review cùng đọc. Pipeline: idea → storyboard → timeline.json → Remotion scene → draft nửa độ phân giải (`npm run draft`) → **contact sheet** (`npm run sheet`: 1 frame/beat, +0,3s, lưới 4×2) → review theo checklist → sửa → lặp; song song cue sheet → `python3 -m sfx` → LUFS → render + mux. **Web-sims:** một HTML offline three.js inline, `render(t)` thuần theo thời gian, Chromium bước frame vào ffmpeg **60fps frame-exact** ("regardless of how slow a frame is"), `beats.py`.
- **"Taste" bằng số:** bezier vào (0.16, 1, 0.3, 1); exit = nửa entrance; word stagger 0,09s; spring preset; 3 font (Instrument Serif/Inter/JetBrains Mono); một màu coral; grain 0,09; danh sách anti-pattern; đọc được ở 360px. **Review loop:** "never reports a video as done without reviewing contact sheets"; collision, clipping, safe area 60px, -14 LUFS ±1, true peak < -1 dBFS; **không được claim đã sửa khi chưa re-render** (soi 1 frame/beat, không phải mọi frame). **Sound engine:** Python stdlib, không sample (typing, click, whoosh, chime, pad), auto-master; cue sheet ví dụ 128 sound.
- Tác giả "whaley" 18 tuổi, Serbia (`patchright-enhanced` 495★). Nguồn bài VN có lẽ là post X @N01ennn "Netflix engineers posted 20 GitHub repos… built for Opus 5.5" — **"Netflix engineers" không có căn cứ**. Không nhầm với **Anthropic "Claude Motion" beta (9/10/2026)**. CoWork-OS PR #403 đã port review loop/timeline/sound engine.

### 5.3 haidrrrry/claude-remotion-skill — 10 rule chống "flat fades & linear motion"

- 1 skill `remotion-motion-graphics/` (SKILL.md + `references/motion-patterns.md` 17 component + `design-rules.md` + `assets/theme.ts`) + file `.skill` cho Claude Desktop/claude.ai; skills.sh 732 install (pass Gen Agent Trust Hub, Socket, Snyk).
- Scope → setup (remotion, @remotion/cli, transitions, motion-blur, google-fonts) → build → `npx remotion render` h264 CRF 17 → **verify bắt buộc** (`remotion still`/ffmpeg frame) → fix → re-render. 30fps mặc định. SFX WAV sinh bằng Node. 10 rule: không linear (spring/bezier + clamp); entrance 2–3 property; stagger 3–6 frame; exit nhanh hơn entrance; 5 lớp (mesh/assets/graphics/grade/grain+vignette); Ken Burns + OffthreadVideo; idle breathing; timing theo `fps`; một `theme.ts`; render→inspect→fix. Transition: `TransitionSeries` hoặc whip pan/scale-through/mask wipe 8–14 frame; motion blur `Trail` khi >30px/frame.
- Rủi ro: commit đầu (13/6/2026) từ tài khoản khác owner, có `seo-boost.sh` đã xóa; README SEO 18 topic; ít hoạt động; trùng vai với remotion-dev/skills chính thức. **Sửa claim:** mục tiêu là "flat" (phẳng) chứ không phải "mờ"; skill còn **thêm** blur chủ ý.

---

## 6. Web UI motion (nhóm D)

- **motiondivision/motion**: xem 2.6. Khuyến nghị dùng skill chính thức `npx motion-ai` + MCP thay vì skill bên thứ ba.
- **199-biotechnologies/motion-dev-animations-skill**: 1 SKILL.md + examples (hero-fade-up, scroll-reveal, card-hover, parallax-layers, magnetic-button), templates Next.js, `validate_motion_config.py`; auto-trigger theo từ khóa (không có slash command); Clarify → Plan → Implement → Verify (60fps, reduced-motion, keyboard, bundle <50KB, CLS 0); chỉ transform/opacity/filter; spring stiffness 300–400, damping 20. **Nhắm Motion v11** (hiện v14) và dừng từ 11/2025 (chỉ một SEO pass 30/3/2026); `DEPLOYMENT_STATUS.md` ghi "DEPLOYED & READY" nhưng checkbox test chưa tick; "87% less context" tự báo. Org 199 Biotechnologies (London/Singapore; `claude-deep-research-skill` 1,2k★). → **lỗi thời, dùng tham khảo cấu trúc skill thôi.**

---

## 7. Kiểm chứng bài đăng gốc (claim → thực tế)

| Claim trong bài | Thực tế |
|---|---|
| product-launch-motion: "chỉ cần đưa link hoặc ảnh sản phẩm" | **Sai**: input là BRIEF.md + screenshot/số thật ("truth pass"); không nhận URL. Word-sync, grading đúng; "camera 3D" chủ yếu 2.5D GSAP; VO do TTS ngoài |
| motion-graphics-skills: "15 skill, Apple Keynote, biểu đồ, reels" | Đúng (từ 11/10); About repo vẫn ghi 13 |
| claude-motion-design: "beat sync bằng Playwright + FFmpeg, 5 prompt trên Opus 5.5" | Render Playwright+ffmpeg đúng; beat sync là numpy; "5 **iterations**" tự báo, không phải 5 prompt |
| student-kit: "tự cắt dead air, lọc nói vấp, 406 mẫu thẻ" | Đúng; cut-mistakes **review-gated**, không xóa "um/uh"; 406 card là draft |
| Barty-Bart: "B-roll biến hình theo lời, bóc tách người local" | Đúng; output tách nền là mask nhị phân, không phải alpha sạch |
| animate: "7 phong cách, duyệt storyboard trước render" | Đúng; chỉ 2/7 style đã chạy phim đầy đủ |
| claude-motion: "soi lại từng khung hình, 60fps" | 1 frame/beat (contact sheet); 60fps chỉ ở web-sims |
| claude-remotion-skill: "trị chuyển cảnh mờ" | Dịch sai "flat"; skill thêm blur |
| motion: "120fps cho React, Vue, JS thuần" | Tự mô tả; 120fps = marketing |
| motion-dev-animations-skill: "một câu lệnh… chuẩn production" | Phóng đại; nhắm Motion v11 cũ, chưa test |
| hyperframes: "không cần mở trình duyệt" | Không hiện cửa sổ nhưng **vẫn dùng headless Chrome** |
| remotion: "chính xác đến mili-giây" | Chính xác đến **frame** |
| remotion/skills: "Claude Code, Codex, Cursor" | Đúng (+ Kimi Code) |
| gsap-skills: "toàn bộ plugin miễn phí thương mại" | Đúng từ 30/4/2025; license độc quyền, cấm công cụ no-code cạnh tranh Webflow |
| "Netflix engineers" / "biến Opus 5.5 thành studio" | Không có căn cứ; tác giả là cá nhân/startup nhỏ |

---

## 8. motionmaxxing (link người dùng) — "looksmaxxing for motion graphics"

- **Hồ sơ:** `Tejashmakwana/motionmaxxing`, Apache-2.0 (vendored GSAP/Three.js/opentype/Inter giữ license riêng), 114★/13 fork, **2 commit ngày 6/10/2026** (co-author Claude), không release; topics agent-skills, claude-code, gsap, hyperframes. Tác giả Tejas Makwana (@makwanatejas170, 8 follower); skill "lives inside **FinalMotion**" (finalmotion.video, trang waitlist "coming soon").
- **Cơ chế:** một SKILL.md "motion director and critic". Brand capture từ website (`brand.mjs`, `fetch_logo.mjs` qua SVGL/Simple Icons) → ≥3 ý tưởng với test "che logo" và "đổi đối thủ" → STORYBOARD.md → script VO → animate HTML + GSAP 3.12.5 (`runtime/motion.js`, không build) → render tất định headless Chrome + ffmpeg (HyperFrames hoặc plain HTML); Three.js r186 cho hero3d; ElevenLabs tùy chọn (`voice.py`, `mix.py` -14 LUFS); Codex CLI image_generation tùy chọn.
- **Protocol 10 bước** (0 toolbox/taste → 9 delivery) và **quality gate G0–G5**: render hợp lệ; proof đọc được [mắt]; không >3 frame phẳng; end hold ≤1,4s; một hero/frame [mắt]; không page chrome (`lint.mjs`). Thang **Slop / Mid / Maxxed**. Output: `final.mp4`, `index.html`, STORYBOARD.md, NOTE.md bắt buộc.
- **Dữ liệu "gu":** `library/moments.jsonl` 716 dòng; claim 53 moment chuyên nghiệp → ~150 designer rule, ~4.288 move, 12 ease, "slop autopsy" 25 pattern; 2 taste file; 2 calibration study + PROVENANCE.md. Showcase 3 before/after (Cluely, Spotify, Wispr Flow; không chính thức).
- **Giới hạn tự khai (docs/KNOWN-LIMITS.md):** "9/10 blind A/B" là thế hệ trước, 1 rater, 5 brief ("signal, not benchmark"); moments.jsonl do 6 AI analyst agent giải mã, **unverified**, phim nguồn private; G1/G4 chấm bằng mắt; `lint.mjs` chỉ thấy DOM; `look.py` đếm cut dư; ElevenLabs music timing không ổn; brand capture fail trên trang login/anti-headless; WebGL 7–11 fps 1080p. Coverage: skillsllm (scan PASSED 7/10), everydev, 2 awesome-list (một list mô tả sai là dùng Remotion).
- **Vị trí:** cùng lớp với claude-motion (C2) và product-launch-motion (A1) nhưng là **một protocol end-to-end có brand capture + dataset timing + gate script**; mới nhất, nhỏ nhất, ít kiểm chứng nhất.

---

## 9. Phân tích & khuyến nghị

1. **Chọn engine trước, skill sau:** HyperFrames (HTML thuần, Apache-2.0, cloud/Lambda, HeyGen hậu thuẫn) vs Remotion (React, chín hơn, Lambda tốt hơn, **license công ty ≥4 người**). Skill cộng đồng chỉ là lớp "gu" trên hai engine này hoặc Playwright+ffmpeg tự chế.
2. **Mẫu chất lượng đáng chép** (đồng điệu với mục 03/06/09/19): storyboard gate trước render (animate, motionmaxxing, product-launch-motion); timeline/cues JSON là nguồn sự thật (claude-motion, product-launch-motion); contact sheet 1 frame/beat (claude-motion, animate); gate bằng script (lint DOM, LUFS, collision, flat-frame) + "không claim done khi chưa re-render"; truth pass chỉ dùng số liệu/screenshot thật.
3. **Âm thanh là nửa còn lại:** -14 LUFS / -1 dBTP xuất hiện ở hầu hết repo; beat/drop detection (howseen), SFX sinh trong code (claude-motion, animate), VO word-sync (product-launch-motion, animate 0.4).
4. **Chi phí thật:** Node 22 + Chrome + FFmpeg (+ Python/torch với SAM); token lớn cho vòng render–review (student-kit ~200k+/build); ElevenLabs/Kie nếu dùng. Model: Opus 5.5 được khuyên nhưng không bắt buộc.
5. **Bảo mật:** skill tải asset/gói lúc chạy (animate, howseen, student-kit); issue #16 student-kit upload file local tùy ý → chạy trong sandbox (mục 11), bật allow-list.
6. **Độ tin cậy nguồn:** 10/16 repo <3 tuần tuổi, 1 tác giả, coverage = directory/newsletter/YouTube của chính tác giả. Ghi ngày + số sao khi trích; xem lại sau 1 quý.
7. **Cho kho này:** có thể gom "quality gate cho video" thành checklist (mục 09) và đóng gói thành plugin (mục 20) dùng với Routine (mục 21).

---

## 9b. Kiểm chứng ảnh "Cài 28 repo này để dùng Claude Code cho motion graphics" (Charlie Hills, người dùng gửi 2026-10-12)

> Ảnh khung explorer `motion-designer/` chia 28 repo thành 5 nhóm, ghi tổng **1.149.527★**. Tác giả là Charlie Hills, cũng là tác giả `charlie947/motion-graphics-skills` (§3.2). Số sao dưới đây đọc trang GitHub ngày 12/10/2026; 6 repo đã có ở §1 lấy lại số ở đó.

| Nhóm (ảnh) | Repo thật | ★ ảnh → ★ 12/10 | License | Ghi chú |
|---|---|---|---|---|
| Engines | mrdoob/three.js | 116,2k → 116,3k | MIT | |
| | juliangarnier/anime | 73,4k → 73,5k | MIT | |
| | motiondivision/motion | 33,9k → 34,0k | MIT (Motion+ trả phí) | §2.6 |
| | pmndrs/react-three-fiber | 32,8k → 32,9k | MIT | |
| | airbnb/lottie-web | 32,2k → 32,2k | MIT | |
| | greensock/GSAP | 28,9k → 29,1k | **GreenSock Standard "no-charge" License** (không phải OSI) | §2.4 |
| Render | FFmpeg/FFmpeg | 64,9k → 65,0k | LGPL-2.1+ (một phần GPL) | Repo GitHub chỉ là mirror |
| | remotion-dev/remotion | 62,7k → 63,4k | **Remotion License** (công ty ≥4 người phải trả phí) | §2.2 |
| | heygen-com/hyperframes | 59,4k → 61,1k | Apache-2.0 | §2.1 |
| | manim | 41,4k → 41,5k | MIT | Số trong ảnh là **ManimCommunity/manim**; bản gốc 3b1b/manim có 94,9k★ |
| | motion-canvas/motion-canvas | 19,3k → 19,3k | MIT | |
| | redotvideo/revideo | 4,1k → 4,1k | MIT | Fork của Motion Canvas, render headless |
| UI parts | shadcn-ui/ui | 125,2k → 125,4k | MIT | Mục 06 |
| | DavidHDev/react-bits | 48,7k → 49,0k | **MIT + Commons Clause** (cấm bán lại) | |
| | magicuidesign/magicui | 22,5k → 22,6k | MIT | |
| | ibelick/motion-primitives | 6,5k → 6,5k | MIT | |
| | 21st-dev/magic-mcp | 6,0k → 6,0k | ISC | README: đã chuyển thành "the 21st MCP", repo chỉ giữ cấu hình cũ |
| Sound | openai/whisper | 110,2k → 110,4k | MIT | Mục 14 |
| | Tonejs/Tone.js | 14,8k → 14,8k | MIT | |
| | katspaugh/wavesurfer.js | 10,4k → 10,4k | BSD-3-Clause | |
| | elevenlabs/skills | 482 → 484 | MIT | Skill cho API ElevenLabs (trả phí/giới hạn gói free) |
| Skills & MCP | anthropics/skills | 180,1k → 180,7k | Apache-2.0 phần lớn; docx/pdf/pptx/xlsx **source-available** | |
| | "mcp-for-Blender" | (bị che) → 30,5k | MIT | `ahujasid/blender-mcp` nay redirect về **ahujasid/mcp-for-blender**; ~30,1k là số suy ra từ tổng của ảnh |
| | greensock/gsap-skills | 16,1k → 16,2k | MIT | §2.4 |
| | remotion-dev/skills | 4,9k → 5,0k | không có LICENSE | §2.3 |
| | CloudAI-X/threejs-skills | 3,5k → 3,5k | README ghi MIT, repo không có trường license | |
| | Dakkshin/after-effects-mcp | 719 → 730 | MIT | ExtendScript; cần Adobe After Effects có bản quyền |
| | charlie947/motion-graphics-skills | 112 → 214 | MIT | **Repo của chính tác giả ảnh**, nhỏ hơn mọi repo khác trong danh sách hai bậc độ lớn |

**Kết luận kiểm chứng**

- **Số sao đúng:** cộng các số trong ảnh với ~30,1k của repo Blender ra đúng 1.149.527, khớp với snapshot vài ngày trước 12/10 (tổng hiện tại ~1,155M). Không phát hiện số bịa.
- **Phóng đại ở cách đóng khung:** "Cài 28 repo này để dùng Claude Code" là sai về bản chất. Chỉ 9 mục là skill hoặc MCP cài vào Claude Code (anthropics/skills, gsap-skills, remotion/skills, threejs-skills, elevenlabs/skills, motion-graphics-skills, mcp-for-blender, after-effects-mcp, magic-mcp). Còn lại là **thư viện/engine** để agent viết code dùng (`npm i`, `pip install`, cài FFmpeg), không phải thứ "cài vào Claude Code". Tổng ★ là chỉ số độ nổi tiếng, không đo mức phù hợp cho motion graphics (shadcn/ui và whisper chiếm ~236k).
- **License cần đọc trước khi dùng thương mại:** Remotion (công ty ≥4 người phải trả phí), GSAP (license riêng, không phải OSI), react-bits (Commons Clause), anthropics/skills (một phần source-available), FFmpeg (LGPL/GPL khi phân phối), After Effects (phần mềm trả phí).
- **Thiếu so với mục này:** không có bước **quality gate** (storyboard duyệt trước, contact sheet, -14 LUFS) mà §9 coi là cốt lõi; cũng không có Lottie skill chính thức (`LottieFiles/motion-design-skill`, §2.5). Danh sách hợp làm **bản đồ thư viện**; quy trình thì theo §9.
- **Chọn tối thiểu cho Claude Code:** một engine (HyperFrames *hoặc* Remotion) + skill chính thức của engine đó + GSAP skills + FFmpeg + Whisper (phụ đề) là đủ cho phần lớn video launch. Thêm three.js/R3F khi cần 3D, mcp-for-blender khi cần Blender.

---

## 10. Nguồn

- Nhóm A/B: github.com/AbubakrChan/product-launch-motion (README, SKILL.md, scripts/, evals/, commits, issues), github.com/AbubakrChan, github.com/charlie947/motion-graphics-skills (README, commits), github.com/charlie947, charliehills.substack.com/p/opus-55-motion-graphics, skillsllm.com/skill/motion-graphics-skills, github.com/howseen-ai/claude-motion-design (README, commits, issues), github.com/howseen-ai, trendshift.io/repositories/265851, skillsdirectory.com/skills/howseen-ai-motion-design, github.com/ProSkillsMD/proskills/issues/7473, github.com/nateherkai/hyperframes-student-kit (README, .claude/skills, cut-mistakes/SKILL.md, cut-silences/SKILL.md, issues), github.com/nateherkai, opsmavix.com/blog/hyperframes-student-kit, skillsllm.com/skill/hyperframes-student-kit, aident.ai/blog/edit-videos-claude-code-hyperframes, github.com/Barty-Bart/motion-graphics (README, skills/motion-broll/SKILL.md, skills/object-separation/SKILL.md, issues), github.com/Barty-Bart, aitoolsreview.co.uk (2 video), autoae.online/blog/claude-motion-graphics-skills, mindstudio.ai/blog/ai-video-editing-claude-code-hyperframes
- Nhóm C/D: github.com/cth9191/animate (README, plugins/animate/skills/animate/SKILL.md, commits), github.com/cth9191, skillsdirectory.com/skills/cth9191-animate, skills.sh/cth9191/animate, github.com/whaleyxbt/claude-motion (README, .claude/skills/review-loop, motion-design, commits), github.com/whaleyxbt, skills.sh/whaleyxbt/claude-motion, x.com/N01ennn/status/2108182955671580771 (snippet), github.com/CoWork-OS/CoWork-OS/pull/403, github.com/haidrrrry/claude-remotion-skill (README, SKILL.md, references/motion-patterns.md, commits), skills.sh/haidrrrry/claude-remotion-skill, github.com/motiondivision/motion (tags, releases), registry.npmjs.org (motion, framer-motion, motion-v), motion.dev/blog/framer-motion-is-now-independent-introducing-motion, motion.dev/blog/introducing-motion-for-vue, motion.dev/docs/react, motion.dev/docs/gsap-vs-motion, motion.dev/plus, motion.dev/docs/ai-kit-install, github.com/199-biotechnologies/motion-dev-animations-skill (SKILL.md, DEPLOYMENT_STATUS.md, commits), github.com/199-biotechnologies, skills.sh/199-biotechnologies/motion-dev-animations-skill, agentskillshub.top/best/claude-video-skills, support.claude.com/ja/articles/17454997 (Claude Motion beta)
- Nhóm E: github.com/heygen-com/hyperframes (README, commits), github.com/heygen-com, hyperframes.dev, hyperframes.heygen.com, developers.heygen.com/hyperframes-overview, heygen.com/blog (April/June/July 2026 release), registry.npmjs.org/hyperframes, repos.ecosyste.ms (5 repo), trendshift.io/repositories/28102, themenonlab.blog, silenceper.com, yuv.ai/blog/hyperframes-heygen, webreactiva.com/blog/hyperframes, github.com/remotion-dev/remotion (releases, LICENSE.md), remotion.dev (the-fundamentals, recorder, ai/skills, ai/mcp, blog), remotion.pro/license, github.com/remotion-dev/skills (README, commits), motionbox.io/blog/remotion-for-coding-agents, mer.vin (remotion agent skills), github.com/greensock/gsap-skills (commits), github.com/greensock, gittrend.io/repo/greensock/gsap-skills, gsap.com/blog/3-13, gsap.com/community/standard-license, blog.codepen.io (2025-05-05), github.com/LottieFiles/motion-design-skill (skills/motion-design/SKILL.md, commits), github.com/LottieFiles, trendshift.io/repositories/167710, lottiefiles.com/blog (Lottie Creator MCP, 15/4/2026), uichemy.com/design-skills/lottiefiles-motion-design
- motionmaxxing: github.com/Tejashmakwana/motionmaxxing (README, SKILL.md, docs/KNOWN-LIMITS.md, commits), github.com/Tejashmakwana, finalmotion.video, skillsllm.com/skill/motionmaxxing, everydev.ai/tools/motionmaxxing, github.com/zhuyansen/awesome-claude-video-skills, github.com/charetterat/awesome-agent-motion-skills, github.com/topics/motionmaxxing
- §9b (ảnh 28 repo của Charlie Hills, 2026-10-12): số sao đọc trang GitHub của 22 repo (three.js, anime, react-three-fiber, lottie-web, GSAP, FFmpeg, 3b1b/manim, ManimCommunity/manim, motion-canvas, revideo, shadcn-ui/ui, react-bits, magicui, motion-primitives, magic-mcp, whisper, Tone.js, wavesurfer.js, elevenlabs/skills, anthropics/skills, ahujasid/mcp-for-blender, CloudAI-X/threejs-skills, Dakkshin/after-effects-mcp); 6 repo còn lại lấy từ §1
