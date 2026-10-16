# 06 · UI/UX, Design Tools & Design-for-AI

> Thư viện component, công cụ thiết kế mở, công cụ AI sinh giao diện, tài nguyên học UI/UX, và lớp "giao diện cho agent".

## 1. Thư viện component & design system (web)

| Thư viện | Repo | ★ (2026) | Kiểu | Nhận xét |
|---|---|---|---|---|
| **shadcn/ui** | shadcn-ui/ui | ~126k (16/10) | Copy-paste source (CLI) trên Tailwind | Mặc định cho React+Tailwind; từ 7/2026 cài mới dùng **Base UI**, vẫn hỗ trợ Radix |
| **MUI** | mui/material-ui | ~99k (16/10) | Material Design, đầy đủ | An toàn cho enterprise |
| **Radix UI** | radix-ui/primitives | ~19–35k (nguồn lệch) | Headless primitives | Chậm lại sau khi WorkOS mua |
| **Base UI** | mui/base-ui | ~11k (16/10) | Headless, từ team Radix + MUI + Floating UI | Lựa chọn khi bắt đầu mới |
| **Mantine** | mantinedev/mantine | ~32k (16/10) | "Batteries included", 100+ component | |
| **Vuetify** | vuetifyjs/vuetify | ~41k | Material 3 cho Vue | |
| **Headless UI / DaisyUI** | tailwindlabs/headlessui · saadeghi/daisyui | – | Tailwind-native | |
| **Storybook** | storybookjs/storybook | – | Phát triển/test/doc component cô lập | Chuẩn de-facto |

**Design system tham khảo (doanh nghiệp):** Atlassian, GitHub Primer, GitLab Pajamas, Google Material, IBM Carbon, Shopify Polaris (bảng so sánh có cột "AI-ready", MCP, `llms.txt`: §7f.3) — xem `klaufel/awesome-design-systems`, designsystemsrepo.com, designsystems.surf.

## 2. Công cụ thiết kế / canvas mã nguồn mở

| Dự án | Repo | License | ★ | Định vị |
|---|---|---|---|---|
| **Excalidraw** | excalidraw/excalidraw | MIT | ~134k | Whiteboard phong cách vẽ tay, self-host |
| **Penpot** | penpot/penpot | MPL-2.0 | ~61k | **Thay thế Figma** mã mở, xuất CSS/HTML thật, Docker self-host |
| **tldraw** | tldraw/tldraw | tldraw license | ~51k | Infinite canvas SDK, gần Figma nhất về cảm giác |
| **Onlook** | onlook-dev/onlook | Apache-2.0 | – | Visual editor cho React/Tailwind, "Cursor cho designer" |
| **OpenDesign** | open-design.ai | – | – | Agent-native design tool |
| **FigCraft** | storytold/figcraft | MIT OR Apache-2.0 | ~0,6k (14/10/2026) | Dựng lại Figma bằng Rust nhờ agent, alpha 5 ngày tuổi, điều khiển được qua CLI/MCP (§7e) |

## 3. AI sinh giao diện (design-to-code / prompt-to-UI)

| Công cụ | Mở? | Ghi chú |
|---|---|---|
| **v0.app** (Vercel) | Đóng | Rebrand 1/2026, full-stack sandbox, Git, DB connectors; mạnh nhất ở scaffolding frontend |
| **Lovable** | Đóng | Prompt → app full-stack (Supabase) |
| **Bolt.new** (StackBlitz) | Core `bolt.diy` mở | WebContainer trong trình duyệt |
| **Google Stitch** | Đóng | Sinh UI + màu/typography/spacing tái dùng |
| **MagicPath** | Đóng | Layout + hướng thiết kế trên infinite canvas |
| **Subframe** | Đóng | Canvas compose React/Tailwind, export code sạch |
| **Figma Make / AI** | Đóng | Tích hợp trong Figma |

Danh sách: `narrowin/awesome-generative-ui` (LLM sinh/compose UI động), `maxbogo/awesome-ai-tools-for-ui`.

## 4. "Taste" cho coding agent – chống giao diện AI generic

- **Taste Skill** (`Leonxlnx/taste-skill`, ~46k★ theo listing): bộ Agent Skills cho Claude Code/Cursor/Codex; cấm các trope "AI slop": purple mesh gradient, hero căn giữa, 3 card giống nhau, font Inter + ảnh stock; 3 "dial" variance/motion/density; v2 đọc brief (loại trang, đối tượng, vibe) trước khi code.
- **Refactoring UI Skill**: áp quy tắc spacing/typography/color/hierarchy từ sách Refactoring UI.
- **Frontend-design skill** của Anthropic (trong marketplace Claude Code) + Taste làm lớp "quality enforcement".
- Chưa có benchmark độc lập chứng minh hiệu quả; bằng chứng chủ yếu là demo & cộng đồng.
- **Thêm từ repo của chủ kho (mục 23, 2026-10-12):** `impeccable` (plugin/skill "taste" được case-study-ft41 ghi trong `ui-ux-intelligence-provider.md`), `nextlevelbuilder/ui-ux-pro-max-skill` (45 file, vendor trong Hermes-Agents), `google-labs-code/design.md` (file DESIGN.md mô tả hệ thiết kế cho agent; spec + linter, xem §7c), `popular-web-designs` (54 design system tóm tắt). xboss có cổng tĩnh `check:contrast` + `check:ui-ux-guard` và Lighthouse CI chặn merge 4 category — "taste" chỉ bền khi có cổng máy đi kèm.

## 5. Tài nguyên học UI/UX cho developer

| Tài nguyên | Loại | Ghi chú |
|---|---|---|
| **Refactoring UI** (Wathan & Schoger) | Sách + video (trả phí) | Kinh điển cho dev không phải designer |
| **Laws of UX** (Jon Yablonski) | Web miễn phí + sách | Nguyên lý tâm lý học (Fitts, Hick, Jakob…) |
| `bradtraversy/design-resources-for-developers` | Awesome list | Ảnh, font, màu, template, CSS framework |
| `klaufel/awesome-design-systems` | Awesome list | Design system hướng dev |
| Design Systems Gallery / designsystems.surf | Thư viện ví dụ | Cảm hứng & chuẩn |
| Material Design 3, Apple HIG, Fluent 2 | Guideline chính thức | |

## 6. Lớp giao diện cho agent (Agentic UI / Generative UI)

| Dự án | Repo | Vai trò | Ghi chú |
|---|---|---|---|
| **CopilotKit** | CopilotKit/CopilotKit | Frontend stack cho agent, tác giả **AG-UI** | Gọi vốn $27M 5/2026; nặng & opinionated, như application framework |
| **assistant-ui** | assistant-ui/assistant-ui | Headless React primitives cho chat/agent | Ghép tốt với Vercel AI SDK |
| **Vercel AI SDK** + **AI Elements** | vercel/ai | Toolkit streaming, framework-agnostic; AI Elements = component lắp ráp | Gần tầng transport |
| **AG-UI** | ag-ui-protocol/ag-ui | Giao thức sự kiện agent ↔ UI | AWS AgentCore, MS Agent Framework, Oracle A2UI tích hợp |

**Nhận định:** năm 2026 lựa chọn quyết định bởi giao thức (AG-UI) hơn là bộ component.

## 7. Case study: Anatomy – skill vẽ minh họa isometric tương tác (link từ người dùng, 2026-10-12)

| Thuộc tính | Giá trị (đọc 2026-10-12) |
|---|---|
| Repo | https://github.com/wheresryan22/anatomy · release v1.0.0 ngày **10/10/2026** · kèm `wheresryan22/anatomy-figures` (npm `anatomy-figures`, 51–52 máy đã vẽ, 5 theme, React + custom elements, 10★) |
| Mô tả | "An agent skill for creating detailed, interactive isometric illustrations of real-world machines and complex systems… A Claude skill that explains an idea by building it as a real, working object." |
| ★ / forks / commit | **3.8k ★ sau ~2 ngày** · 299 forks · 87 commit · 1 issue · 3 PR mở; 35 commit trong 11–12/10 (gộp PR #20–#39), contributor thứ hai `rudycelekli` (10 fix audit/React/browser) |
| License | MIT ("© 2026 Ryan") |
| Tác giả | Ryan (@wheresryan22, "self-proclaimed misfit"), thành viên org FrameHeadquarters, 106 followers; repo khác: sfinterface-numbers (107★), xq (C, archived) |
| Tương thích | Claude Code, OpenCode, Codex (`$anatomy`); Node 20.10+ (skills CLI cần Node 22), Chrome/Chromium cho bước kiểm tra; **không API key, không `npm install`** |
| Cài | `npx skills add wheresryan22/anatomy -g -a claude-code` → `/anatomy explain how a token bucket rate limiter works, interactive` |

### Cách hoạt động (từ `SKILL.md`)

- **Ý tưởng cốt lõi:** biến khái niệm kỹ thuật thành **một vật thể vật lý thật** mà cơ chế vận hành chính là khái niệm (cache key → ổ khóa pin-tumbler chỉ xoay khi mọi pin khớp; rate limiter → bồn token). Từ chối "hộp xếp chồng trừu tượng". Mọi số trên readout đến từ **cùng một model nhỏ** điều khiển chuyển động.
- **Quy trình 10 bước:** (1) **Size it** – Figure 40–80 part (~30–90 phút), Hero 80–150 part (~2–4 giờ), Epic 6+ giờ; không tự chạy Epic nếu người dùng chưa chọn → (2) **Truth first**: thu thập số liệu/hành vi thật, đặt vào module thuần → (3) Invent the object, một câu "cái gì chuyển động và nghĩa là gì" → (4) Parts list ≥40 part (base, structure, mechanism, controls, lit subject) → (5) camera azimuth 45°/elevation 30°, `fitProjection` → (6) build geometry một lần → (7) **paint back to front** → (8) frame trong card (số hình, tiêu đề, hint, live readout) → (9) motion theo thời gian, tôn trọng reduced-motion, dừng khi offscreen → (10) **verify like a critic**: đọc từng PNG ở zoom 4×.
- **Luật cứng đáng chép lại:** *"Solids, not wireframes."* · *"Every line ends on something: a face, another line or a terminal dot."* · không ống/cáp nào xuyên qua vật khác kể cả giữa chuyển động · *"Shaders never pop or cut off."* · hình chiếm 55–65% card và vẫn đọc được ở 390px.
- **Kit (không phụ thuộc ngoài Node):** `kit/iso-kit.ts` (camera, solids, parts library, SVG renderer), `lathe.mjs` (vật tròn), `tube.mjs` (ống/cáp), `audit.mjs` (chứng minh hình học), `gl.mjs` (WebGL: lửa, nước, plasma), `turn*.mjs` (3D beta), `kit/react/draw.tsx` (server-safe) + `live.tsx`; `references/` 8 guide (craft, kit, motion, react, verify, webgl, walkthrough, 3d) nạp khi cần.
- **Kiểm chứng bằng máy:** `scripts/capture.mjs` (screenshot headless Chrome), `drive.mjs` (chuỗi tương tác), `node build.mjs --audit` phải in "audit passed" khi có ống/vật tròn, `scripts/lines.mjs` phải báo **0 line end**; check 4× ở cả theme sáng/tối; `evals/evals.json` chứa prompt test.
- **Output:** HTML standalone (`pageHtml`), SVG đơn (`figureSvg`), hoặc component React/Next.js; 8 ví dụ (dial-indicator, desk-computer, arcade-cabinet, raptor-engine, ripple-tank, test-rig, spot-plate, turning-dial 3D).
- **Giới hạn tác giả nêu:** không phải chart library; vẽ máy/dụng cụ/đồ nội thất, không vẽ người hay bản đồ chính xác; build chậm có chủ đích; shader cần WebGL; 3D là beta; Codex sandbox có thể chặn browser check (README có hướng dẫn).

### Bối cảnh & so sánh

| Nhóm | Ví dụ | Khác biệt với Anatomy |
|---|---|---|
| Skill sơ đồ "diagram-as-code" | Mermaid skills (design-doc-mermaid ~44k install), Excalidraw skills (~28.7k install, Kroki/CLI export), Garry Tan `diagram` (Mermaid → Excalidraw editable), `diagram-design` (44 loại, branded; xem §7b) | Sơ đồ 2D trừu tượng; Anatomy là **minh họa vật thể 3D-isometric có mô phỏng** |
| Skill thẩm mỹ frontend | Taste Skill (mục 4 ở trên), Refactoring UI skill, `ibelick/ui-skills` (~9.4k★, directory chứa Anatomy cùng animated-sprites, animation-vocabulary, antfu-design, beautiful-shadows) | Anatomy nằm ở nhánh "visual/craft" của cùng hệ sinh thái |
| Motion/video skills | claude-motion-design, awesome-claude-video-skills (mục 19) | Video/animation thay vì SVG tương tác |

### Nhận xét & bài học

1. **Skill kèm kit + audit + eval** là mẫu đáng học: thay vì chỉ prompt, skill mang theo thư viện hình học không phụ thuộc, script kiểm chứng bằng máy (audit hình học, đếm line end, screenshot 4×) và bộ prompt eval. Đây là "evidence or it's a FAIL" (mục 09) áp vào đồ họa.
2. **Sizing trước khi làm** (Figure/Hero/Epic + ước tính thời gian, hỏi người dùng) là cách kiểm soát chi phí token/thời gian rõ ràng, giống gate `[BLOCKER]`/approval ở mục 09 và 19.
3. **"Truth first"**: readout và chuyển động lấy từ một model số nhỏ → tránh minh họa "đẹp nhưng sai"; tái dùng cho dataviz và explainer.
4. **Rủi ro:** dự án 2 ngày tuổi, 1 contributor chính; build 30 phút–6 giờ mỗi hình rất tốn token; phụ thuộc Chrome headless; chưa có đánh giá độc lập (bài ai.sulat.com không truy cập được, 403). Số sao tăng nhanh nhờ bài đăng X ngày 10/10 và lan sang Weibo.
5. Liên hệ: mục 04 (chuẩn Agent Skills, cài qua `skills` CLI), mục 06 §4 (Taste Skill), mục 19 (motion skills), mục 09 (kiểm chứng bằng máy).

**Nguồn:** https://github.com/wheresryan22/anatomy (README, SKILL.md, releases/v1.0.0, commits) · https://github.com/wheresryan22 · https://github.com/wheresryan22/anatomy-figures · https://x.com/wheresryan22/status/2108948624004526516 · https://www.ui-skills.com/skills/wheresryan22/anatomy · https://www.skills.sh/wheresryan22/anatomy/anatomy · https://skillselion.com/guides/best-diagram-skills-for-claude-code · https://aipptskill.com/blog/ai-diagram-skills-guide/ · https://open-design.ai/skills/diagram/ · https://skillselion.com/guides/diagram-design-skill-claude-code-guide

## 7b. Case study: diagram-design — skill vẽ sơ đồ "editorial" theo thương hiệu (ảnh + link người dùng gửi, 2026-10-12)

> Đọc clone đầy đủ (287 commit, HEAD `80c8f28`, plugin 2.6.75) và đối chiếu các con số trong ảnh chụp README.

### 7b.1 Hồ sơ nhanh

| Mục | Thông tin (12/10/2026) |
|---|---|
| Repo | `cathrynlavery/diagram-design` · **~51,8k★**, 3,3k fork, 87 issue + PR mở; tạo 16/4/2026; license **MIT**; trang diagramdesign.dev |
| Mô tả | "An agent skill that draws diagrams as one self-contained HTML + SVG file, in your brand. 44 diagram types. No shadows. No Mermaid slop." |
| Tác giả | Cathryn Lavery (LittleMight; email commit `@bestself.co`, tức BestSelf Co.); tác giả chính 122/287 commit (hai email), bot release 63, tổng 51 tên tác giả. 78/250 commit không merge (~31%) có trailer Claude |
| Host | Claude Code (marketplace `/plugin`), Codex, GitHub Copilot, Factory Droid, Claude Cowork (mirror nội bộ tổ chức), OpenCode, Pi; hoặc `npx skills add cathrynlavery/diagram-design` (chỉ skill, không có lệnh `/export-diagram`, `/import-mermaid`, `/profile`, `/doctor`) |

**Đối chiếu ảnh:** "44 diagram types" **đúng** (44 file `references/type-*.md`); "stars 49k" là số cũ, nay ~51,8k; "version 2.6.74" đã lên 2.6.75 cùng ngày (bot bump mỗi lần merge vào `main`); "Skills 9.3K" là số lượt cài theo skills.sh **(chưa xác minh)**; "CI passing" đúng nghĩa: `ci.yml` chạy trên mọi PR. "#1 Repository Of The Day" là huy hiệu GitHub Trending, không kiểm được ngày.

### 7b.2 Cách hoạt động (đọc `SKILL.md`, 393 dòng, và `references/`)

- **Cổng thương hiệu trước sơ đồ đầu tiên:** nếu token style vẫn mặc định (paper `#f5f5f5`, ink `#2d3142`, accent `#bf4520`), skill **dừng và hỏi** lấy brand từ đâu (URL website, skill có sẵn, thư mục design system, dán token, giữ mặc định, profile đã lưu). Profile lưu ở `~/.diagram-design/profiles/`.
- **Triết lý "xoá trước":** mật độ mục tiêu 4/10, trên 9 node thì tách thành hai sơ đồ, màu nhấn chỉ cho 1–2 node; mục "khi nào **không** dùng" (danh sách → bảng, sơ đồ một hình → viết câu).
- **Output:** một file HTML tự chứa với SVG inline; xuất PNG (cần Playwright trong Python, skill kiểm trước khi chạy) và SVG đứng riêng. Nhập từ `.drawio`, Mermaid, `.excalidraw`.
- **Kiểm bằng máy:** `scripts/` có 30 `verify-*.py` và 39 `test-*.py` (hình học, tương phản màu, a11y, sankey, treemap, waterfall…), fixture "đối nghịch" (`sample-adversarial.mmd`, `waterfall-plausible-wrong.html`); `.maintainer-policy.json` liệt kê cổng local, gồm `claude plugin validate . --strict` ghim phiên bản CLI.
- **Riêng tư:** `PRIVACY.md` nói không server, không analytics, không telemetry; luồng ra ngoài duy nhất là Google Fonts khi mở file (bỏ link thì dùng font hệ thống) và trang web người dùng chỉ định khi lấy brand.

### 7b.3 Đánh giá

- **Điểm mạnh:** đúng mẫu "skill kèm kit + verifier + fixture đối nghịch" như Anatomy (§7), nhưng phạm vi rộng hơn (44 loại, chart lẫn schematic) và đóng gói cho 6+ host với version đồng bộ; luật thẩm mỹ cụ thể đến mức kiểm được.
- **Rủi ro:** (1) phụ thuộc Google Fonts khi xem file (tài liệu nội bộ nhạy cảm nên bỏ link font); (2) PNG cần Playwright + Chromium; (3) bản `npx skills` không tự cập nhật; (4) skill dài (393 dòng + hàng chục reference) nên tốn context mỗi lần nạp, dù reference chỉ nạp khi cần; (5) chưa thấy đánh giá độc lập về chất lượng sơ đồ so với Mermaid.
- **Khi nào dùng:** sơ đồ cho tài liệu đọc lâu, slide, bài viết, cần đúng brand. Với sơ đồ sống trong repo (review được bằng diff, render trên GitHub), Mermaid vẫn tiện hơn.
- **Tích hợp:** MIT, chép/vendor được; giữ `THIRD_PARTY_LICENSES.md` (icon Tabler, MIT). Cấu hình tối thiểu: chạy onboarding một lần cho mỗi dự án, lưu profile; tắt Google Fonts cho tài liệu nội bộ.

**Nguồn §7b:** https://github.com/cathrynlavery/diagram-design (clone đầy đủ, HEAD 80c8f28; README, SKILL.md, references/type-*.md, references/export.md, scripts/, .maintainer-policy.json, .github/workflows/ci.yml, PRIVACY.md, THIRD_PARTY_LICENSES.md) · https://diagramdesign.dev · https://skillselion.com/guides/diagram-design-skill-claude-code-guide

## 7c. Kiểm ảnh: VoltAgent/official-design-md, danh mục DESIGN.md "chính chủ" (ảnh người dùng gửi, 2026-10-13)

> Ảnh là phần đầu README (banner "Official DESIGN.md Collection", huy hiệu "DESIGN.md 7", Discord "138 online"). Đã clone toàn bộ repo (6 commit), tải đủ 11 file được liệt kê, và chạy linter chính thức của Google (`npx @google/design.md@0.4.0 lint`) trên từng file.

### 7c.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 13/10/2026) |
|---|---|
| Repo | `VoltAgent/official-design-md` · ~519★, 47 fork (shields), license **MIT** · chỉ có `README.md` + `LICENSE` |
| Lịch sử | 6 commit, cùng một người (necatiozmen / Necati Özmen): tạo 26/7/2026 với 7 mục → 8 mục ngày 29/8 (thêm Ant Design) → 11 mục ngày 14/9 (Oxide, Juspay, Microsoft FAST); commit cuối 21/9/2026 |
| Mô tả | "The tracker for first-party DESIGN.md adoption… not extracted, not reverse-engineered, not community-made." |
| Chủ list | VoltAgent (framework agent TypeScript). Cùng chủ: `awesome-design-md` (~121k★, 84 DESIGN.md **trích xuất** từ website), `official-mcp-servers` (mục 04 §2c), `awesome-agent-skills`, `awesome-claude-code-subagents` |
| Chuẩn gốc | DESIGN.md do Google Stitch công bố; Google mở bản nháp đặc tả ngày 21/4/2026 tại `google-labs-code/design.md` (~28k★, Apache-2.0, bản 0.4.0 ngày 27/7/2026, trạng thái alpha): YAML front matter chứa token + phần văn xuôi giải thích, kèm CLI `lint`/`diff`/`export` |
| Mô hình kinh doanh | README chèn quảng cáo EveryFeed và hai bộ starter kit trên getdesign.md. Trang getdesign.md/request bán **DESIGN.md riêng** $39 và "Website Starter Kit + DESIGN.md" $249, đều trả một lần (đọc 13/10/2026) |

### 7c.2 Kiểm từng ô trong ảnh

| Ô trong ảnh | Kiểm | Ghi chú |
|---|---|---|
| Tab "MIT license" | ✅ | `LICENSE`: MIT, © 2026 VoltAgent. Chỉ áp cho README; mỗi file được liệt kê thuộc chủ của nó (README tự ghi) |
| Huy hiệu "DESIGN.md 7" | ⚠️ cũ | Ảnh chụp trong khoảng 26/7–29/8/2026; nay huy hiệu ghi **11**, khớp đúng 11 dòng trong mục Collection |
| "138 online" (Discord) | ⚠️ | Huy hiệu sống, đổi theo giờ; không nói gì về chất lượng list |
| "published by companies and projects themselves" | ⚠️ 10/11 | 10/11 file nằm trên domain hoặc repo của chính chủ. Mục **VoltAgent** thì không đúng tinh thần: file trong `VoltAgent/voltagent` (thêm 11/5/2026) tự mô tả là *"Voltagent Inspired… An inspired interpretation of Voltagent's design language"*, giống **88%** theo dòng (difflib) với bản trích xuất `design-md/voltagent/DESIGN.md` mà `awesome-design-md` đăng từ 31/3/2026. Tức là bản trích xuất được đăng lại vào repo chính chủ, cùng một tác giả |
| "not extracted, not reverse-engineered" | ⚠️ | Đúng cho 10 file còn lại theo nội dung đọc được; đúng một ngoại lệ là chính mục của chủ list (ô trên) |
| "If a team ships an official DESIGN.md… it belongs here" | ⚠️ | Không có kiểm tra tự động (không CI, không script). Thêm mục qua issue rồi PR, người duyệt là chủ repo. 11/11 link còn sống (HTTP 200, 13/10/2026) |

**Tổng:** 1✅ / 5⚠️ / 0❌. Không ô nào sai hẳn, nhưng "chính chủ" mới đúng ở mức *đăng trên domain của mình*, chưa phải *chính chủ viết*, và list không kiểm file có đúng spec hay không.

### 7c.3 Linter chính thức chấm 11 file (0.4.0, chạy 13/10/2026)

| File | YAML token? | Lỗi | Cảnh báo | Nhận xét |
|---|---|---|---|---|
| Vercel | có | 0 | 0 | File duy nhất sạch hoàn toàn |
| Ant Design | có | 0 | 19 | 17 token mồ côi; nút chính chữ trắng trên `#1677ff` chỉ đạt 4,10:1 (dưới AA 4,5:1) |
| Mintlify | có | 0 | 43 | Typography viết dạng mảng, linter không nhận; thiếu màu `primary` |
| VoltAgent | có | 0 | 30 | 26 tham chiếu token không trỏ tới đâu |
| Atlassian | có | **29** | 446 | 1.738 dòng; đơn vị `%` không hợp lệ, 203 tham chiếu gãy. Một phần cảnh báo tương phản là dương tính giả (linter tính trên nền trong suốt `#00000000`) |
| Oxide | trong khối code | 0 | 162 | 37 tham chiếu gãy, typography dạng mảng |
| Clerk, Juspay, Microsoft FAST, Nuxt, Resend | **không** | 0 | 1 | "No YAML content found": văn xuôi thuần, linter không có gì để kiểm |

**Đọc bảng:** 6/11 file có token máy đọc được; chỉ 1/11 qua linter sạch. Câu README *"No Figma exports, no JSON schemas, no special tooling… nothing to parse"* lệch với chính spec của Google, vốn đặt token trong YAML và có CLI kiểm. Với agent, file văn xuôi vẫn dùng được làm ngữ cảnh, nhưng không kiểm được tương phản hay tham chiếu bằng máy.

### 7c.4 Dùng thế nào

- **Làm mẫu tham khảo, không chép nguyên:** README bảo "Copy it into your project root", nhưng đó là **hệ thiết kế của thương hiệu khác** (logo, màu, font có thể có quyền riêng). Hợp lý là đọc cách họ cấu trúc file (Vercel cho bản đúng spec, Microsoft FAST và Oxide cho bản dành cho dev của chính design system), rồi viết DESIGN.md cho brand của mình.
- **Muốn file có giá trị kiểm chứng:** viết theo spec của `google-labs-code/design.md` (YAML token + văn xuôi) và chạy `lint` trong CI, cùng kiểu "taste chỉ bền khi có cổng máy" ở §4 và các case study §7, §7b.
- **Phân biệt hai list cùng chủ:** `official-design-md` (11 file, ý định chính chủ) và `awesome-design-md` (84 file trích xuất từ CSS công khai, README tự ghi "We do not claim ownership"). Bản trích xuất hợp cho thử nghiệm; đưa vào sản phẩm thật thì nên tự viết.

**Nguồn §7c:** https://github.com/VoltAgent/official-design-md (clone đầy đủ, HEAD 7236b05) · https://github.com/VoltAgent/awesome-design-md (clone nông, HEAD c7c1bad 12/10/2026; `design-md/voltagent/DESIGN.md`) · https://github.com/VoltAgent/voltagent (lịch sử `DESIGN.md`: bd74d743, 11/5/2026) · https://github.com/google-labs-code/design.md (README, bản 0.4.0) · https://www.npmjs.com/package/@google/design.md · https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-design-md/ · https://the-decoder.com/googles-open-source-design-md-gives-ai-agents-a-prompt-ready-blueprint-for-brand-consistent-design/ · https://getdesign.md/request · 11 file: ant.design/design.md · atlassian.design/DESIGN.md · clerk.com/design.md · github.com/juspay/blend-design-system (DESIGN.md) · github.com/microsoft/fast (examples/design-system/DESIGN.md) · mintlify.com/design.md · nuxt.com/design.md · github.com/oxidecomputer/design-system (design.md) · resend.com/design.md · vercel.com/design.md · github.com/VoltAgent/voltagent (DESIGN.md)

## 7d. Kiểm ảnh: plugin87/ux-ui-agent-skills ("XIAS"), bộ skill biến Claude thành "Senior Design Architect" (ảnh + tên repo người dùng gửi, 2026-10-13)

> Ảnh là phần đầu README: tagline "Turn Claude into a Senior Design Architect — 15+ years of expertise…", câu "138 brand-grade design systems… any framework and any design system", logo XIAS với ba số 52 · 25 · 14, huy hiệu Trendshift "#10 Repository Of The Day" và chữ phủ tiếng Việt "1.628 lập trình viên đã star". Đã clone toàn bộ repo (144 commit), đếm từng con số, đối chiếu 138 design system với hai kho MIT khác, và tự chạy bộ cổng của repo.

### 7d.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 13/10/2026) |
|---|---|
| Repo | `plugin87/ux-ui-agent-skills` · **1.686★**, 177 fork, 8 issue mở (GitHub search API) · license **MIT** (© 2026 Thientan Soparat) · bản **v2.9.8** (10/10/2026) |
| Tác giả | Thientan Soparat (`plugin87`), 143/144 commit. Tài khoản có từ 2016; các repo khác của cùng người đều nhỏ: `figma-remote-server` (MCP Figma, 5★), `full-stack-design-skills` (10★), `homebrew-tap` |
| Lịch sử | Tạo 16/3/2026 · v1.0.1 (6/6) đóng gói sẵn skill của **Taste Skill** · v1.1.0 (7/6) thêm 138 design system và gỡ skill Taste · v2.9.x tháng 10 thêm hook, máy chủ MCP, brew. Listing agentskill.work ghi 438★ ở bản 2.3.1 (khoảng 22/6/2026), tức sao tăng gấp 4 trong khoảng 3,5 tháng |
| Phân phối | Plugin Claude Code (`.claude-plugin/`), `npx ux-ui-agent-skills init`, brew, máy chủ MCP (`ux-ui-mcp`). `AGENTS.md` cho Codex/Cursor/Copilot/Aider. npm: 7.178 lượt tải từ 1/6 đến 12/10/2026, 3.540 trong 30 ngày gần nhất |
| Bên trong | `CLAUDE.md` 319 dòng (luật + bộ định tuyến yêu cầu) · 25 skill trong `.claude/skills/` · 14 file token DTCG · 11 file spec component · 16 adapter framework · 39 script cổng (Python + Node + Playwright/axe) · 3 hook (preflight, cổng nhanh khi ghi file, chặn dừng lượt khi chưa đo) |

### 7d.2 Kiểm từng ô trong ảnh

| Ô trong ảnh | Kiểm | Ghi chú |
|---|---|---|
| "15+ years of expertise", "Senior Design Architect" | ⚠️ | Không phải kinh nghiệm của ai: đó là câu persona ở dòng 3 `CLAUDE.md` ("You are a Senior Design Architect with 15+ years… at the caliber of Apple, Google, Airbnb, and Stripe"). Persona không đo được; thứ đo được nằm ở cổng (ô "52") |
| "138 brand-grade design systems" | ⚠️ | Đếm đúng **138** thư mục trong `design-systems/library/`. Nhưng **64** tên trùng `VoltAgent/awesome-design-md` (MIT), trong đó **60** file có ≥ 80% dòng trùng nguyên văn với một bản trong lịch sử kho đó (cùng khung 9 mục "Visual Theme & Atmosphere… Agent Prompt Guide"). **51** tên trùng `bergside/awesome-design-skills` (TypeUI, MIT, ~3,1k★): 49/51 giữ nguyên câu mô tả, màu lấy từ token gốc (vd brutalism `#DD614C`), văn được viết lại theo khung trên và mỏng hơn (trung vị 71 dòng so với 154 của cả thư viện). 24 mục còn lại chưa rõ nguồn (chưa xác minh). Repo **không ghi công hay chép bản quyền** của hai kho MIT này ở đâu cả; MIT yêu cầu giữ thông báo bản quyền khi phân phối lại phần đáng kể |
| "any framework and any design system" | ⚠️ | Có 16 adapter (Angular, Vue, Svelte, Flutter, Jetpack Compose, React Native…) cộng React/Next/SwiftUI, nhưng cổng render chỉ chạy trên HTML và component React. Các framework khác là hướng dẫn dạng văn bản, không cổng nào kiểm |
| Logo "52" (cổng khách quan) | ⚠️ 49/52 | Tự chạy `node scripts/accuracy_report.mjs` trên HEAD 62092bd (13/10/2026, Chromium 1194 thay cho Chrome): **49/52**, README ghi "52/52 or it fails". 3 cổng trượt: (1) hook: 3/19 test fail vì hook không nhận ra trình duyệt trong sandbox, do môi trường; (2) harness component: số "65" màu `rgb(157,150,142)` trên nền trắng chỉ đạt **2,92:1** (cần 3:1), không phụ thuộc font nên khả năng cao là lỗi thật; (3) mẫu checkout: tràn +9px ở 280px và hai nút "Place order"/"Back to delivery" bấm không có phản hồi (chưa xác minh có do font hay không). Mô tả repo trên GitHub còn ghi "**50** objective gates", lệch với README |
| Logo "25" (skill chạy được) | ✅ | Đúng 25 `SKILL.md` trong `.claude/skills/` (ví dụ `/design-screen`, `/critique`, `/a11y-audit`, `/data-dashboard`, `/gate`) |
| Logo "14" (file token DTCG) | ✅ | Đúng 14 file trong `tokens/`; `npm test` (validate token, tương phản, spec component, hardcode, tham chiếu theme, emoji, link) qua hết, `npm run test:unit` 49/49 pass |
| Trendshift "#10 Repository Of The Day" | ✅ | Trang trendshift.io/repositories/24406 ghi "#10 on GitHub Trending". Đây là thứ hạng một ngày, không nói gì về chất lượng |
| "1.628 lập trình viên đã star" (chữ phủ tiếng Việt) | ⚠️ cũ | Hôm nay 1.686★. Chữ do người đăng lại thêm vào, không có trên README; số sao không phải số "lập trình viên" |
| "MIT license" | ✅ | `LICENSE` MIT. Xem lưu ý ghi công ở ô "138" |

**Tổng:** 4✅ / 5⚠️ / 0❌. Phần mã của chính tác giả (cổng đo trên trình duyệt thật, hook chặn "báo xong khi chưa đo") là thật và chạy được. Phần "138 design systems" lại chủ yếu là dữ liệu của hai kho MIT khác, đóng gói lại mà không ghi nguồn.

### 7d.3 So với các mục đã có

| | XIAS | Taste Skill (§4) | `awesome-design-md` (§7c) | `ui-ux-pro-max-skill` |
|---|---|---|---|---|
| Bản chất | Luật + token + cổng đo + thư viện DESIGN.md | Luật "taste" chống AI slop | Kho DESIGN.md trích xuất từ website | Kho tra cứu style/palette cho agent |
| Có cổng máy? | Có: 52 cổng (README ghi 34 cổng mở trình duyệt) (axe, tương phản theo trạng thái, phím, vùng chạm, 280px) | Không | Không (linter của Google là công cụ ngoài) | Không (chưa xác minh) |
| Quan hệ | Từng đóng gói Taste Skill (v1.0.1), lấy 60+ file của awesome-design-md | Nguồn gốc ý "slop tells" | Nguồn của ~60 design system trong XIAS | Cùng ngách |

Điểm XIAS hơn hẳn ba bên kia là **cổng đo trên bản render thật** và hook `Stop` buộc agent nói "UNMEASURED" khi chưa đo, đúng tinh thần "taste chỉ bền khi có cổng máy" ở §4.

### 7d.4 Dùng thế nào

- **Lấy phần cổng, không cần cả bộ:** các script `verify_states.mjs` (tương phản theo hover/focus/disabled), `verify_target_size.mjs`, `verify_overflow.mjs` (280px), `axe_audit.mjs`, `lint_intent.mjs` (nút xóa không được mang màu primary) có thể chạy độc lập trên HTML. Lưu ý chúng gọi `chromium.launch({ channel: 'chrome' })`: máy không có Chrome thì phải cài, hoặc nhiều cổng sẽ fail vì môi trường chứ không phải vì giao diện.
- **Không dồn 319 dòng `CLAUDE.md` vào dự án đã có luật riêng:** bộ luật của XIAS (theme đơn, token theo ý định, không emoji) có thể xung đột với design system sẵn có. `npx ux-ui-agent-skills add <phần>` cho phép lấy từng phần.
- **Thư viện 138 design system:** dùng để tham khảo như §7c. Muốn dùng thương mại thì lấy từ nguồn gốc (`awesome-design-md`, `bergside/awesome-design-skills`) để giữ đúng thông báo MIT, và nhớ đó là hệ thiết kế của thương hiệu khác.
- **Tự chạy lại cổng sau khi cài:** README nói 52/52, nhưng bản HEAD chạy trong sandbox còn trượt ít nhất một cổng tương phản thật.

**Nguồn §7d:** https://github.com/plugin87/ux-ui-agent-skills (clone đầy đủ, 144 commit, HEAD 62092bd 10/10/2026; README, CLAUDE.md, CHANGELOG.md, LICENSE, package.json, .claude-plugin/plugin.json, design-systems/library/, `git show b89881e:skills-lock.json`; tự chạy `npm test`, `npm run test:unit` 49/49, `node scripts/accuracy_report.mjs` 49/52, 13/10/2026) · GitHub search API 13/10/2026 (1.686★, 177 fork; repo khác của `plugin87`) · https://www.npmjs.com/package/ux-ui-agent-skills (api.npmjs.org: 3.540 lượt/30 ngày, 7.178 từ 1/6/2026) · https://trendshift.io/repositories/24406 · https://agentskill.work/en/skills/plugin87/ux-ui-agent-skills (438★, bản 2.3.1) · https://github.com/VoltAgent/awesome-design-md (clone, lịch sử `design-md/*/DESIGN.md`) · https://github.com/bergside/awesome-design-skills (clone; MIT © Bergside, `skills/*/SKILL.md`, `skills/*/DESIGN.md`) · https://tessl.io/registry/skills/github/bergside/awesome-design-skills/brutalism/evals · https://open-design.ai/systems/brutalism/ · https://github.com/Leonxlnx/taste-skill

## 7e. Case study: FigCraft (`storytold/figcraft`), dựng lại Figma bằng Rust nhờ agent (link người dùng gửi, 2026-10-14)

> Đã clone toàn bộ repo (267 commit), đọc README, `CLAUDE.md`, `ROADMAP.md`, `docs/gaps.md`, mã nhập `.fig`, workflow CI, rồi tự build và chạy test. FigCraft là app mới trong bộ "Crafting Apps" của ArtCraft (danh mục `catalog.rs` của launcher ngày 14/10/2026 có 14 app, gồm cả FigCraft và PrintCraft); kho đã có hai app anh em là FilmCraft ([mục 01](../01-ai-coding-agents/README.md) §3d) và ArtCraft Launcher (mục 01 §3e).

### 7e.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 14/10/2026) |
|---|---|
| Repo | `storytold/figcraft` · **616★**, 264 fork, 40 issue + 21 PR mở (shields) · license **MIT OR Apache-2.0**; tên, logo ArtCraft là thương hiệu riêng, bản fork phải gỡ · bản v0.5.1 (12/10/2026) |
| Định vị | "Interface design; an open-source, clean-room reimplementation of Figma, rebuilt in pure Rust": frame, auto layout, component/variant, vector network, style, variable, prototype, Dev Mode, phiên cộng tác. Chạy native trên macOS/Windows/Linux/FreeBSD và trong trình duyệt (WebAssembly) |
| Tác giả | Brandon Thomas (`echelon`, cựu CEO Storyteller.ai, nhà sáng lập ArtCraft/FakeYou) mở repo ngày **9/10/2026**. Người commit nhiều nhất là `BFlat`/`bflatastic` (210/267). Có 14 tên tác giả, trong đó 9 người ngoài góp qua PR |
| Cách làm | **191/267 commit (72%) ghi "Co-authored-by: Claude"** (Opus 5.5, có commit Sonnet 5.5). `CLAUDE.md` là hướng dẫn cho agent: mỗi phiên đọc `ROADMAP.md` và `docs/gaps.md`, rồi lấy việc ở đầu danh sách. Kế hoạch và ảnh chụp Figma để tham chiếu nằm trong `plan/`, thư mục này bị gitignore, không công khai. ROADMAP ước thời gian theo đơn vị "giờ của một agent Opus 5.5" |
| Quy mô | **204.110 dòng Rust** sau 5 ngày; 16 crate + 4 app (desktop, CLI, server, web); 2.088 hàm `#[test]` |
| Bộ anh em (GitHub search 14/10) | PhotoCraft 59,4k★ · ArtCraft 26,9k★ · PdfCraft 13,2k★ · FilmCraft 12,9k★ · LightCraft 12,2k★ · WordCraft 11,8k★ · VectorCraft 8,7k★ · EffectCraft 6,4k★ · GridCraft, CADCraft, DesignCraft, DeckCraft, SoundCraft · craft-launcher 2,5k★. Phần lớn tạo trong khoảng 30/9–9/10/2026; FigCraft là một trong những repo mới nhất và ít sao nhất |

### 7e.2 Kiểm lời tuyên bố

| Tuyên bố | Kiểm | Ghi chú |
|---|---|---|
| Có test và test thật sự chạy | ✅ | Khác FilmCraft (CI không chạy test), `ci.yml` của FigCraft chạy `cargo clippy -D warnings` + `cargo test --workspace` + kiểm phân tầng (`xtask layers`) + kiểm tài sản + build wasm32 trên mọi PR. Tự chạy `cargo test` cho 4 crate lõi (doc, layout, format, engine) ngày 14/10/2026: **1.092 pass, 0 fail, 2 ignored** |
| "Agent-ready": CLI, kênh JSON, MCP cùng một bộ lệnh | ✅ | Build `figcraft-cli` (release) rồi `render examples/ridgeline-app.figcraft` ra PNG 2639×1117, khớp ảnh trong README; `figcraft-cli commands` liệt kê bộ lệnh (README ghi "400+") |
| "Clean-room… no proprietary code, file formats" | ⚠️ | Không có cách kiểm độc lập: nguồn tham chiếu là `plan/` không công khai. `CLAUDE.md` cấm đọc bundle hay lưu lượng mạng của Figma và cấm dùng icon hay ảnh của họ. Phần đọc `.fig` thì dựa trên định dạng **kiwi**, vốn do đồng sáng lập Figma công bố mã mở. Vì vậy "no proprietary file formats" nên hiểu là không chép mã, chứ không phải không đọc định dạng của Figma |
| Mở được file `.fig` | ⚠️ | README ghi "best effort". `docs/gaps.md` xếp hạng 3: **"Nothing checked against real Figma files"**. Phần xuất `.fig` còn là thử nghiệm |
| "Accessible: screen readers get names, roles…" | ⚠️ | Có AccessKit trong mã, nhưng gaps.md hạng 22 ghi **"Screen readers never run; browser has no accessibility tree"**. README nói mạnh hơn mức đã kiểm |
| "No account, no telemetry, offline" | ✅/⚠️ | Đúng khi không chia sẻ. Bấm Share ▸ Online thì file được đẩy lên server công cộng mặc định `collab.craftapps.dev`, **không mã hóa đầu cuối**, ai có link là sửa được, file tồn tại tới 30 ngày sau lần mở cuối. README tự ghi rõ điều này |
| Mức sẵn sàng | ⚠️ alpha | Tự đánh giá: độ phủ menu/lệnh 100% (211/211, đo bằng `cargo xtask parity`), độ phủ tính năng khoảng 85%, "ready for real work" khoảng 53%. Hai con số sau là ước lượng. Còn cần 155–280 giờ agent nữa mới tới beta; multiplayer chưa có tài khoản; canvas vẽ bằng CPU |

**Tổng:** 3✅ / 5⚠️ / 0❌. Kỷ luật kỹ thuật tốt hơn FilmCraft: CI chặn PR, clippy cấm `unwrap`/`panic`, kiểm phân tầng. Nhưng các con số "parity" vẫn là tự chấm, và tính năng chưa từng được kiểm trên file Figma thật.

### 7e.3 So với các công cụ đã có trong kho

| | FigCraft | Penpot (§2) | Figma |
|---|---|---|---|
| Tuổi / độ chín | 5 ngày, alpha | Nhiều năm, đã dùng production (~61k★) | Sản phẩm thương mại |
| Mô hình | App native + wasm, file `.figcraft` trên máy; server cộng tác tự host được | Web app, self-host bằng Docker, định dạng mở (SVG/CSS) | Cloud, tài khoản |
| Đọc file Figma | Best effort, chưa kiểm trên file thật | Có plugin xuất từ Figma | Gốc |
| Cho agent | CLI + MCP + kênh JSON, mọi thao tác UI là một lệnh | Có API/plugin | MCP chính thức (Dev Mode) |
| License | MIT OR Apache-2.0 | MPL-2.0 | Đóng |

**Trùng tên:** `divikwu/figcraft` (4★) là một **MCP server cho Figma**, không liên quan tới dự án này.

### 7e.4 Dùng thế nào

- **Cho đội cần thay Figma ngay:** vẫn chọn Penpot. FigCraft mới 5 ngày tuổi, chưa kiểm trên file thật, chưa có tài khoản.
- **Cho agent sinh UI:** đây là điểm đáng thử nhất. `figcraft-cli mcp` cho agent dựng frame, component, auto layout rồi render PNG/SVG headless; cả 5 file mẫu trong `examples/` đều được dựng qua bộ lệnh này. Có thể dùng làm "canvas" cho agent thay vì để agent sinh HTML.
- **Không chia sẻ file nhạy cảm qua server mặc định.** Tự chạy `figcraft-server` sau Caddy/nginx, hoặc chia sẻ trong mạng LAN tin cậy.
- **Bài học quy trình** (giống FilmCraft): nhiều phiên agent cùng đọc một danh sách việc xếp hạng (`docs/gaps.md`), mỗi việc kết thúc bằng cập nhật ROADMAP và ước lượng giờ. Khác biệt đáng giá là FigCraft bật CI chặn PR ngay từ ngày đầu.
- **Tải bản build:** chỉ lấy từ release của `storytold/figcraft` hoặc getartcraft.com. Kho đã ghi nhận repo nhái mồi malware cho FilmCraft (mục 01 §3d).

**Nguồn §7e:** https://github.com/storytold/figcraft (clone đầy đủ, 267 commit, HEAD bcedfeb 14/10/2026; README, NOTICE, ATTRIBUTION.md, CLAUDE.md, ROADMAP.md, docs/gaps.md, crates/format/src/fig/mod.rs, .github/workflows/ci.yml; tự chạy 14/10/2026: `cargo test -p figcraft-doc -p figcraft-layout -p figcraft-format -p figcraft-engine` 1.092 pass, `figcraft-cli render` ra PNG) · shields 14/10/2026 (616★, 264 fork, release v0.5.1) · GitHub search API 14/10/2026 (51 repo của `storytold`) · https://github.com/storytold/craft-launcher (`crates/core/src/catalog.rs`, 14/10/2026) · https://getartcraft.com/apps/figcraft · https://petapixel.com/2026/10/07/someone-rebuilt-free-open-source-versions-of-photoshop-premiere-and-lightroom-using-ai/ · https://propakistani.pk/2026/10/09/free-open-source-copies-of-photoshop-premiere-and-lightroom-are-here/ · https://www.tweaktown.com/news/113989/developer-says-software-is-over-after-using-ai-to-recreate-adobes-entire-creative-cloud-suite-for-free/index.html · https://www.it-connect.fr/suite-adobe-rust-claude-opus-artcraft-crafting-apps/ · https://ecosistemastartup.com/artcraft-clona-7-apps-de-adobe-con-claude-opus-5-5/ · https://www.besthub.dev/articles/rewriting-adobe-suite-in-rust-12-open-source-apps-56k-stars-built-for-ai-agents-051d286733fe · https://notes.nicolasdeville.com/apps/artcraft/ · https://glama.ai/mcp/servers/divikwu/figcraft (dự án trùng tên)

## 7f. Zen Design System (Dizai Studio) và design system "AI-ready" (yêu cầu người dùng, 2026-10-16)

> Người dùng hỏi "Zen Design System và các system thiết kế UI/UX khác". Tên này ứng với nhiều dự án; mục này lấy repo mang đúng tên **"Zen Design System"** (`Zen-Design-System/Zen-DS`, của Dizai Studio, Việt Nam) làm chính, liệt kê các dự án trùng tên, rồi so với các design system lớn theo tiêu chí mà Zen lấy làm điểm bán: dùng được với AI agent. Đã clone đầy đủ Zen-DS (HEAD `0e0ff04c` 16/10/2026), cài devDependencies, chạy toàn bộ cổng kiểm của repo và bộ test.

### 7f.1 Trùng tên "Zen"

| Dự án | Là gì | Ghi chú (16/10/2026) |
|---|---|---|
| **`Zen-Design-System/Zen-DS`** | Design system thương mại của **Dizai Studio** (Việt Nam), React 19 + TypeScript, sinh từ thư viện Figma | Mục chính, xem 7f.2 |
| `umami-software/zen` | Design system và bộ component React của **Umami** (analytics mã mở), theo quy ước shadcn, primitive **Base UI**, Tailwind v4 | **MIT**, 58★, 726 commit (721 của Mike Cao, người lập Umami), npm `@umami/react-zen` 0.255.0, ~104 file component, có `SKILL.md` cho agent; tài liệu zen.umami.is |
| `reciprocity/zen-design-system` | Biến, style cho micro-frontend "Zen" của Reciprocity | Dừng từ 11/2020 |
| Zen UI (Flowbase) | Bộ component cho **Webflow**, file Figma bán riêng | Không phải mã mở |
| Zendesk Garden | Design system của Zendesk (`zendeskgarden/react-components`) | Không phải "Zen", hay bị nhầm; Apache-2.0, ~1,1k★ |

### 7f.2 Hồ sơ Zen DS

| Mục | Thông tin (đọc 16/10/2026) |
|---|---|
| Repo | `Zen-Design-System/Zen-DS` · **0★** (shields), 561 commit trong 18 ngày có commit, từ 25/9/2026; Alex Duong 287, commit đồng tác giả Claude 168, `alexduonguiux-hub` 83. Bài LinkedIn có hashtag #zendesignsystem #dizaistudio nhắc đội ngũ Việt Nam; quan hệ giữa các tài khoản và Dizai **chưa xác minh** |
| Nội dung | 67 component có hướng dẫn (đếm bởi `guidelines:check`; Button, input, Table, Dialog, Sidebar, Chat, Chart, app shell…), mỗi component có hướng dẫn Do/Don't và tài liệu props sinh tự động; README ghi **2.179 biến Figma** trên 7 trục chế độ (theme, component theme, density, radius, emphasis, breakpoint, typography), 36 text style, 18 effect style, **1.598 icon**; trang tài liệu "Codebase Platform" và Storybook |
| Lớp cho AI agent | `AGENTS.consumer.md` (đi kèm package, dành cho agent dựng app), `AGENTS.md` (cho agent sửa chính design system), `llms.txt`; **MCP server cục bộ** (`node mcp/server.mjs`, stdio, 11 tool: `list_components`, `get_component`, `get_tokens`, `search_icons`, `list_templates`, `map_figma_component`, `check_spec`, `check_usage`…; không gọi mạng); 8 skill (`zen-component-usage`, `zen-figma-design`, `zen-token-sync`, `zen-responsive-screens`…) |
| Cổng máy | **Usage guard** 205 luật dùng component (có plugin ESLint), kiểm token/text style/icon, đồng bộ hướng dẫn với props, "Figma parity" (`tools/figma-contract`), `verify:package` (đóng gói, cài vào app tạm, type-check, build, kiểm ngân sách kích thước) |
| Giấy phép | **Thương mại, theo số người dùng (seat)**: package `@zen-ds/react` chỉ cài được từ registry riêng `npm.dizai.studio` sau khi đăng nhập tài khoản Zen. Mã nguồn công khai trên GitHub nhưng **không phải mã mở**. `LICENSE.md` (bản 1.0, hiệu lực 8/10/2026) cho phép sửa mã, dùng trong số End Product không giới hạn, cho phép dùng AI agent qua MCP; đầu file ghi **"Draft for legal review… has not yet been reviewed by a lawyer"** |
| npm công khai | `@zen-ds/react@0.1.0` (5/5/2026), ghi **MIT**, maintainer `zen-ds`. Tài liệu của Zen gọi đây là "old public 0.1.0" và cảnh báo thiếu dòng scope trong `.npmrc` thì npm cài nhầm bản này; `npx zen-ds doctor` kiểm điều đó |

**Tự chạy (Node 24.22, `npm ci --ignore-scripts`, 16/10/2026):**

| Lệnh | Kết quả |
|---|---|
| `npx tsc --noEmit -p .` | Sạch |
| `npm run usage:selftest` | 205 luật, mỗi luật bắt được lỗi trong fixture xấu, fixture tốt sạch |
| `npm run usage:check` | Đạt: 464 file, 205 luật, 1 cảnh báo |
| `tokens:check` · `styles:check` · `icons:check` | Đạt, 0 lỗi |
| `guidelines:check` | Hướng dẫn khớp mã: 67 component, 236 union khớp, 85 không phân giải được |
| `node mcp/selftest.mjs` | 11 tool trả lời đúng qua client SDK stdio |
| `npx vitest run` | **1.058 test pass, 24 skip** (70 file) |

**Đánh giá Zen DS:**

- **Điểm mạnh thật, đã kiểm:** tài liệu dành cho agent, MCP cục bộ, và luật dùng component **kiểm bằng máy** (205 luật, có self-test chứng minh mỗi luật bắt được lỗi). Cách này khớp với bài học "skill chỉ khuyên, cổng máy mới chặn" của mục 21 §10c và XIAS (§7d): muốn agent dùng đúng design system thì phải có linter, không chỉ có văn bản hướng dẫn.
- **Rủi ro:** sản phẩm mới khoảng 3 tuần, 0★, chưa có người dùng công khai; mã do một người và agent viết là chính; giấy phép còn là **bản nháp chưa qua luật sư**; phụ thuộc registry riêng và tài khoản của Dizai (mất licence là mất quyền cập nhật). Bản 0.1.0 công khai ghi MIT trong khi bản hiện tại là thương mại: quyền MIT của bản 0.1.0 đã phát hành không tự thu hồi được; muốn dùng hợp pháp bản mới thì phải mua licence.
- **Hợp với ai:** đội ở Việt Nam cần một design system có sẵn Figma + React + lớp cho agent, chấp nhận trả theo seat. Đội cần mã mở thì xem bảng 7f.3.

### 7f.3 Các design system khác, nhìn theo "AI-ready" (shields 16/10/2026)

| Design system | ★ · license | Nền | Lớp cho AI agent (đọc 16/10/2026) |
|---|---|---|---|
| **shadcn/ui** | 126k · MIT | Copy mã vào dự án, Base UI/Radix + Tailwind | MCP server chính thức trong CLI (duyệt, tìm, cài component từ registry), skill, `llms.txt`. Đầy đủ nhất trong nhóm mã mở |
| **Ant Design** | 100k · MIT | Component đầy đủ cho ứng dụng doanh nghiệp | Có MCP theo bài tổng hợp, mức "tài liệu" **(chưa xác minh từ trang chính thức)** |
| **MUI (Material UI)** | 99k · MIT | Material Design | MCP trả tài liệu và ví dụ **(chưa xác minh từ trang chính thức)** |
| **Chakra UI** / **Ark UI** | 41k / 5,4k · MIT | Chakra có style; Ark là headless của cùng đội | MCP có hướng dẫn cho Cursor/VS Code/Claude **(chưa xác minh từ trang chính thức)** |
| **Mantine** | 32k · MIT | Component đầy đủ, hook | Có trong danh sách MCP của bài tổng hợp **(chưa xác minh)** |
| **HeroUI** (tên cũ NextUI) | 31k · Apache-2.0 | React + Tailwind | – |
| **Fluent UI** (Microsoft) | 20k · shields không nhận diện | Fluent 2 | `llms.txt` theo UICentral; không tìm thấy MCP chính thức |
| **Radix Primitives** / **Base UI** | 19k / 11k · MIT | Headless | – |
| **React Spectrum / React Aria** (Adobe) | 16k · Apache-2.0 | Headless + design system Spectrum; mạnh về a11y | – |
| **Material Web** (Google) | 11k · Apache-2.0 | Web component Material 3 | – |
| **Carbon** (IBM) | 9,5k · Apache-2.0 | Web component + React | **Carbon MCP** (public preview, cần IBMid; mã đóng theo bài ngoài) · `llms.txt` |
| **USWDS** | 7,2k | Design system chính phủ Mỹ | – |
| **Polaris** (Shopify) | 6,2k | Đã chuyển sang web component cho app Shopify | – |
| **Primer** (GitHub) | 3,9k · MIT | React + CSS | **`@primer/mcp`** chính thức, stdio cục bộ: token, component, pattern, icon (trang primer.style) |
| **Atlassian Design System** | npm `@atlaskit/*` | React | **`@atlaskit/ads-mcp`** (Early Access) + MCP hosted tại mcp.atlassian.com; Atlassian còn công bố `DESIGN.md` (xem §7c) |
| **GOV.UK Frontend** | 1,5k · MIT | Design system chính phủ Anh, chuẩn a11y | – |
| **Zendesk Garden** | 1,1k · Apache-2.0 | React | – |
| **Zen DS** (Dizai) | 0 · thương mại | React 19 + Figma | MCP cục bộ 11 tool, `AGENTS.consumer.md`, `llms.txt`, **205 luật dùng kiểm bằng máy** |

**Chọn thế nào (cho dự án của chủ kho):**

- **Mặc định cho React + Tailwind:** shadcn/ui (mã nằm trong repo, MCP chính thức, giấy phép MIT). Umami Zen là ví dụ tốt về cách một sản phẩm thật dựng design system riêng trên shadcn + Base UI.
- **Ứng dụng nghiệp vụ nhiều bảng, form:** Ant Design hoặc MUI. Cần a11y chặt (chính phủ, y tế): React Aria/Spectrum hoặc GOV.UK Frontend làm chuẩn tham chiếu.
- **Học cách làm design system "cho agent":** đọc Primer MCP (mã mở, cục bộ) và Zen DS (usage guard có self-test). Hai thứ đáng chép là MCP trả token/component đúng phiên bản đang cài, và linter luật dùng component chạy trong CI, không chỉ trong prompt.
- **Trước khi dùng một design system thương mại** (Zen DS hay bất kỳ): đọc giấy phép bản đã ký, không bản nháp; hỏi rõ chuyện gì xảy ra với End Product khi ngừng trả phí; ghim registry trong `.npmrc` để không cài nhầm package trùng tên trên npm công khai.

**Nguồn §7f:** https://github.com/Zen-Design-System/Zen-DS (clone đầy đủ, HEAD 0e0ff04c; README.md, LICENSE.md, AGENTS.consumer.md, AGENTS.md, .mcp.json, mcp/server.mjs, skills/, package.json; tự chạy tsc, usage/tokens/styles/icons/guidelines check, MCP selftest, vitest) · https://registry.npmjs.org/@zen-ds%2freact (0.1.0, MIT, 5/5/2026) · https://github.com/umami-software/zen · https://zen.umami.is/ · https://registry.npmjs.org/@umami%2freact-zen · https://github.com/reciprocity/zen-design-system · https://webflow.com/libraries/detail/zen-ui · https://vn.linkedin.com/in/tungoc19 · https://primer.style/product/getting-started/foundations/mcp/ · https://carbondesignsystem.com/developing/carbon-mcp/overview/ · https://www.npmjs.com/package/@atlaskit/ads-mcp · https://www.atlassian.com/blog/how-we-build/atlassians-design-md-is-here-what-we-learned-testing-portable-design-context-in-practice · https://state-of-ai-in-design-systems.netlify.app/systems/shadcn-ui · https://uicentral.fyi/blog/ui-component-libraries-with-mcp-servers · https://daily.dev/posts/top-10-best-react-ui-libraries-2026-ai-dx-edition--xtcsp4agl · https://mowgli.ai/blog/mcp-servers-for-ui-design-2026 · shields.io cho số sao các repo trong bảng 7f.3

## 8. Nguồn (mục 1–6)

- https://designrevision.com/blog/best-react-component-libraries · https://designrevision.com/blog/best-tailwind-component-libraries · https://dualite.dev/blogs/best-ui-component-libraries · https://www.uilora.com/blog/uilora/10-best-react-ui-component-libraries-in-2026-ranked-by-a-frontend-team · https://www.techwench.com/best-ui-component-libraries-2026/
- https://www.opensourcealternatives.to/item/penpot · https://openalternative.co/excalidraw · https://www.libhunt.com/compare-penpot-vs-excalidraw · https://storyflow.so/blog/best-excalidraw-alternatives-2026
- https://www.figma.com/resource-library/ai-design-tools/ · https://open-design.ai/blog/best-ai-design-tools/ · https://designtools.fyi/facets/ui-generation · https://github.com/narrowin/awesome-generative-ui · https://dev.to/hadil/24-best-ai-design-tools-for-designers-and-developers-in-2026-i1h
- https://www.tasteskill.dev/ · https://www.x-cmd.com/install/taste-skill/ · https://apito.ai/en/blog/seo/ai-frontend-template-look-taste-skill/ · https://github.com/maxbogo/awesome-ai-tools-for-ui
- https://refactoringui.com/ · https://github.com/klaufel/awesome-design-systems · https://github.com/bradtraversy/design-resources-for-developers · https://designsystemsrepo.com/design-systems/ · https://designsystems.surf/design-systems
- https://github.com/copilotkit/copilotkit · https://github.com/ag-ui-protocol/ag-ui · https://techcrunch.com/2026/05/05/copilotkit-raises-27m-to-help-devs-deploy-app-native-ai-agents/ · https://alatirok.com/best-ai-agent-chat-ui-library/
