# 06 · UI/UX, Design Tools & Design-for-AI

> Thư viện component, công cụ thiết kế mở, công cụ AI sinh giao diện, tài nguyên học UI/UX, và lớp "giao diện cho agent".

## 1. Thư viện component & design system (web)

| Thư viện | Repo | ★ (2026) | Kiểu | Nhận xét |
|---|---|---|---|---|
| **shadcn/ui** | shadcn-ui/ui | ~115–121k | Copy-paste source (CLI) trên Tailwind | Mặc định cho React+Tailwind; từ 7/2026 cài mới dùng **Base UI**, vẫn hỗ trợ Radix |
| **MUI** | mui/material-ui | ~93k | Material Design, đầy đủ | An toàn cho enterprise |
| **Radix UI** | radix-ui/primitives | ~19–35k (nguồn lệch) | Headless primitives | Chậm lại sau khi WorkOS mua |
| **Base UI** | mui/base-ui | ~10.6k | Headless, từ team Radix + MUI + Floating UI | Lựa chọn khi bắt đầu mới |
| **Mantine** | mantinedev/mantine | ~28k | "Batteries included", 100+ component | |
| **Vuetify** | vuetifyjs/vuetify | ~41k | Material 3 cho Vue | |
| **Headless UI / DaisyUI** | tailwindlabs/headlessui · saadeghi/daisyui | – | Tailwind-native | |
| **Storybook** | storybookjs/storybook | – | Phát triển/test/doc component cô lập | Chuẩn de-facto |

**Design system tham khảo (doanh nghiệp):** Atlassian, GitHub Primer, GitLab Pajamas, Google Material, IBM Carbon, Shopify Polaris — xem `klaufel/awesome-design-systems`, designsystemsrepo.com, designsystems.surf.

## 2. Công cụ thiết kế / canvas mã nguồn mở

| Dự án | Repo | License | ★ | Định vị |
|---|---|---|---|---|
| **Excalidraw** | excalidraw/excalidraw | MIT | ~134k | Whiteboard phong cách vẽ tay, self-host |
| **Penpot** | penpot/penpot | MPL-2.0 | ~61k | **Thay thế Figma** mã mở, xuất CSS/HTML thật, Docker self-host |
| **tldraw** | tldraw/tldraw | tldraw license | ~51k | Infinite canvas SDK, gần Figma nhất về cảm giác |
| **Onlook** | onlook-dev/onlook | Apache-2.0 | – | Visual editor cho React/Tailwind, "Cursor cho designer" |
| **OpenDesign** | open-design.ai | – | – | Agent-native design tool |

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

## 8. Nguồn (mục 1–6)

- https://designrevision.com/blog/best-react-component-libraries · https://designrevision.com/blog/best-tailwind-component-libraries · https://dualite.dev/blogs/best-ui-component-libraries · https://www.uilora.com/blog/uilora/10-best-react-ui-component-libraries-in-2026-ranked-by-a-frontend-team · https://www.techwench.com/best-ui-component-libraries-2026/
- https://www.opensourcealternatives.to/item/penpot · https://openalternative.co/excalidraw · https://www.libhunt.com/compare-penpot-vs-excalidraw · https://storyflow.so/blog/best-excalidraw-alternatives-2026
- https://www.figma.com/resource-library/ai-design-tools/ · https://open-design.ai/blog/best-ai-design-tools/ · https://designtools.fyi/facets/ui-generation · https://github.com/narrowin/awesome-generative-ui · https://dev.to/hadil/24-best-ai-design-tools-for-designers-and-developers-in-2026-i1h
- https://www.tasteskill.dev/ · https://www.x-cmd.com/install/taste-skill/ · https://apito.ai/en/blog/seo/ai-frontend-template-look-taste-skill/ · https://github.com/maxbogo/awesome-ai-tools-for-ui
- https://refactoringui.com/ · https://github.com/klaufel/awesome-design-systems · https://github.com/bradtraversy/design-resources-for-developers · https://designsystemsrepo.com/design-systems/ · https://designsystems.surf/design-systems
- https://github.com/copilotkit/copilotkit · https://github.com/ag-ui-protocol/ag-ui · https://techcrunch.com/2026/05/05/copilotkit-raises-27m-to-help-devs-deploy-app-native-ai-agents/ · https://alatirok.com/best-ai-agent-chat-ui-library/
