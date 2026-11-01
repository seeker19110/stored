# 06 · UI/UX, Design Tools & Design-for-AI

> Thư viện component, công cụ thiết kế mở, công cụ AI sinh giao diện, tài nguyên học UI/UX, và lớp "giao diện cho agent".

## 1. Thư viện component & design system (web)

| Thư viện | Repo | ★ · license (31/10/2026) | Commit cuối | Kiểu | Nhận xét |
|---|---|---|---|---|---|
| **shadcn/ui** | shadcn-ui/ui | ~127k · MIT | 31/10/2026 | Copy-paste source (CLI) trên Tailwind | Mặc định cho React+Tailwind; từ 7/2026 cài mới dùng **Base UI**, vẫn hỗ trợ Radix; 27 layout block (§7h) |
| **MUI** | mui/material-ui | ~99k · MIT | 31/10/2026 | Material Design, đầy đủ | An toàn cho enterprise |
| **Radix UI** | radix-ui/primitives | ~19k · MIT | 14/10/2026 | Headless primitives | Chậm lại sau khi WorkOS mua. Trước ghi "19–35k (nguồn lệch)"; shields đọc thẳng từ GitHub ra 19k |
| **Base UI** | mui/base-ui | ~11k · MIT | 30/10/2026 | Headless, từ team Radix + MUI + Floating UI | Lựa chọn khi bắt đầu mới |
| **Mantine** | mantinedev/mantine | ~32k · MIT | 29/10/2026 | "Batteries included", 100+ component | |
| **Vuetify** | vuetifyjs/vuetify | ~41k · MIT | 31/10/2026 | Material 3 cho Vue | `LICENSE.md` ở gốc là symlink tới `packages/vuetify/LICENSE.md` (MIT), nên GitHub không nhận diện được |
| **Headless UI** | tailwindlabs/headlessui | ~29k · MIT | **13/4/2026** | Headless, Tailwind-native | Hơn 6 tháng không commit (release cuối v2.2.10 ngày 7/4/2026); Tailwind Labs về Shopify 9/2026 (§7h) |
| **daisyUI** | saadeghi/daisyui | ~43k · MIT | 13/10/2026 | Plugin component Tailwind | Template đầy đủ bán riêng (§7h) |
| **Storybook** | storybookjs/storybook | ~91k · MIT | 30/10/2026 | Phát triển/test/doc component cô lập | Chuẩn de-facto |

**Design system tham khảo (doanh nghiệp):** Atlassian, GitHub Primer, GitLab Pajamas, Google Material, IBM Carbon, Shopify Polaris (**Polaris React đã bị archive 11/8/2026, đổi tên `Shopify/polaris-react-archive`; Shopify chuyển sang Polaris Web Components từ 1/10/2025**) (bảng so sánh có cột "AI-ready", MCP, `llms.txt`: §7f.3) — xem `klaufel/awesome-design-systems`, designsystemsrepo.com, designsystems.surf.

## 2. Công cụ thiết kế / canvas mã nguồn mở

| Dự án | Repo | License | ★ (31/10/2026) | Commit cuối | Định vị |
|---|---|---|---|---|---|
| **Excalidraw** | excalidraw/excalidraw | MIT | ~135k | 31/10/2026 | Whiteboard phong cách vẽ tay, self-host |
| **Penpot** | penpot/penpot | MPL-2.0 | ~62k | 30/10/2026 | **Thay thế Figma** mã mở, xuất CSS/HTML thật, Docker self-host |
| **tldraw** | tldraw/tldraw | tldraw license (riêng, cần license thương mại tùy trường hợp) | ~51k | 30/10/2026 | Infinite canvas SDK, gần Figma nhất về cảm giác |
| **Onlook** | onlook-dev/onlook | Apache-2.0 | ~27k | **21/7/2026** | Visual editor cho React/Tailwind, "Cursor cho designer"; hơn 3 tháng không commit trên nhánh chính (commit cuối là bản vá IDOR tRPC), dù vẫn có push ở nhánh khác |
| **OpenDesign** | nexu-io/open-design (open-design.ai) | Apache-2.0 | ~105k | 30/10/2026 | "Collaborative AI design agent workspace"; có dịch vụ trả phí. Hồ sơ §7k, **đọc mã §7q.0: telemetry nội dung bật mặc định, agent chạy bỏ kiểm quyền** |
| **FigCraft** | storytold/figcraft | MIT OR Apache-2.0 | ~4k | 31/10/2026 | Dựng lại Figma bằng Rust nhờ agent, alpha, điều khiển được qua CLI/MCP (§7e) |

## 3. AI sinh giao diện (design-to-code / prompt-to-UI)

| Công cụ | Mở? | ★ (31/10/2026) | Ghi chú |
|---|---|---|---|
| **v0.app** (Vercel) | Đóng | – | Rebrand 1/2026, full-stack sandbox, Git, DB connectors; mạnh nhất ở scaffolding frontend |
| **Lovable** | Đóng | – | Prompt → app full-stack (Supabase) |
| **Bolt.new** (StackBlitz) | Core `bolt.diy` mở (MIT) | `stackblitz-labs/bolt.diy` ~20k (shields), commit cuối 10/2026 | WebContainer trong trình duyệt |
| **Google Stitch** | Đóng | – | Sinh UI + màu/typography/spacing tái dùng |
| **MagicPath** | Đóng | – | Layout + hướng thiết kế trên infinite canvas |
| **Subframe** | Đóng | – | Canvas compose React/Tailwind, export code sạch |
| **Figma Make / AI** | Đóng | – | Tích hợp trong Figma |

Danh sách: `narrowin/awesome-generative-ui` (LLM sinh/compose UI động; 144★, CC-BY-4.0, push cuối 26/10/2026), `maxbogo/awesome-ai-tools-for-ui` (1.002★, không ghi license). Số đọc 31/10/2026 (GitHub API).

## 4. "Taste" cho coding agent – chống giao diện AI generic

- **Taste Skill** (`Leonxlnx/taste-skill`, **~98,9k★**, 6,7k fork, MIT, commit cuối 19/10/2026; trước ghi ~46k★ theo listing): mô tả GitHub hiện nay là "art direction, reference images and a browser check", tức đã thêm bước kiểm trên trình duyệt **(chưa đọc mã, chưa xác minh)**; bộ Agent Skills cho Claude Code/Cursor/Codex; cấm các trope "AI slop": purple mesh gradient, hero căn giữa, 3 card giống nhau, font Inter + ảnh stock; 3 "dial" variance/motion/density; v2 đọc brief (loại trang, đối tượng, vibe) trước khi code.
- **Refactoring UI Skill** (`s0xDk/refactoring-ui-skill`, 646★, MIT): áp quy tắc spacing/typography/color/hierarchy từ sách Refactoring UI, kèm `tokens.css` đã kiểm tương phản. Hồ sơ: §7g.4.
- **Frontend-design skill** của Anthropic (trong marketplace Claude Code, Apache-2.0) + Taste làm lớp "quality enforcement". Hồ sơ: §7g.3.
- Chưa có benchmark độc lập chứng minh hiệu quả; bằng chứng chủ yếu là demo & cộng đồng.
- **Thêm từ repo của chủ kho (mục 23, 2026-10-12):** `impeccable` (~83k★ ngày 19/10/2026, hồ sơ mục 20; plugin/skill "taste" được case-study-ft41 ghi trong `ui-ux-intelligence-provider.md`), `nextlevelbuilder/ui-ux-pro-max-skill` (~137k★; 45 file, vendor trong Hermes-Agents; hồ sơ §7g.2), `google-labs-code/design.md` (~28k★, Apache-2.0; file DESIGN.md mô tả hệ thiết kế cho agent; spec + linter, xem §7c), `popular-web-designs` (54 design system tóm tắt). xboss có cổng tĩnh `check:contrast` + `check:ui-ux-guard` và Lighthouse CI chặn merge 4 category — "taste" chỉ bền khi có cổng máy đi kèm.

## 5. Tài nguyên học UI/UX cho developer

| Tài nguyên | Loại | ★ · license (19/10/2026) | Ghi chú |
|---|---|---|---|
| **Refactoring UI** (Wathan & Schoger) | Sách + video (trả phí) | – | Kinh điển cho dev không phải designer; skill dựa trên sách: §7g.4 |
| **Laws of UX** (Jon Yablonski) | Web miễn phí + sách | – | Nguyên lý tâm lý học (Fitts, Hick, Jakob…) |
| `bradtraversy/design-resources-for-developers` | Awesome list | ~67k · MIT, commit cuối 18/10/2026 | Ảnh, font, màu, template, CSS framework |
| `klaufel/awesome-design-systems` | Awesome list | 907 · CC0-1.0, commit cuối 14/9/2026 | Design system hướng dev |
| Design Systems Gallery / designsystems.surf | Thư viện ví dụ | – | Cảm hứng & chuẩn |
| Material Design 3, Apple HIG, Fluent 2 | Guideline chính thức | – | Layout thích ứng: §7h |

## 6. Lớp giao diện cho agent (Agentic UI / Generative UI)

| Dự án | Repo | ★ · license (31/10/2026) | Commit cuối | Vai trò | Ghi chú |
|---|---|---|---|---|---|
| **CopilotKit** | CopilotKit/CopilotKit | ~38k · MIT | 30/10/2026 | Frontend stack cho agent, tác giả **AG-UI** | Gọi vốn $27M 5/2026; nặng & opinionated, như application framework |
| **assistant-ui** | assistant-ui/assistant-ui | ~13k · MIT | 30/10/2026 | Headless React primitives cho chat/agent | Ghép tốt với Vercel AI SDK |
| **Vercel AI SDK** + **AI Elements** | vercel/ai | ~28k · Apache-2.0 | 30/10/2026 | Toolkit streaming, framework-agnostic; AI Elements = component lắp ráp | Gần tầng transport |
| **AG-UI** | ag-ui-protocol/ag-ui | ~17k · MIT | 30/10/2026 | Giao thức sự kiện agent ↔ UI | AWS AgentCore, MS Agent Framework, Oracle A2UI tích hợp |

**Nhận định:** năm 2026 lựa chọn quyết định bởi giao thức (AG-UI) hơn là bộ component.

> **Cách lấy số §1–§6 (rà lại 31/10/2026; lần trước 19/10/2026):** số sao và license từ GitHub search API (`repo:` từng dự án, làm tròn); `bolt.diy` không hiện trong search (là fork) nên lấy shields. **Ngày commit cuối đọc từ `git clone --depth 1` nhánh mặc định**, không dùng `pushed_at` của API vì trường này đổi cả khi push nhánh khác (Onlook: push 21/10 nhưng commit nhánh chính cuối 21/7). Khi GitHub báo license `NOASSERTION` thì giữ license đã đọc trong file LICENSE (Vuetify, tldraw, Vercel AI). Bảng rà toàn bộ 72 repo GitHub của mục: §7p.1.

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

**Rà lại 18/10/2026 (người dùng gửi lại ảnh "PASSED ALL GATES"):** repo **không đổi** — vẫn HEAD `62092bd`, v2.9.8, 144 commit. Chỉ số sao tăng **1.686 → ~2,0k** (218 fork). Ảnh là reference app `examples/` với nhãn "PASSED ALL GATES" (marketing); nhắc lại §7d.2: README/ảnh tuyên bố 52/52 nhưng tự chạy `accuracy_report.mjs` thật ra 49/52, và "138 design systems" phần lớn chép từ hai kho MIT khác không ghi nguồn. Đánh giá giữ nguyên.

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

## 7g. Bốn skill/kho UI đã được nhắc nhưng chưa có hồ sơ (yêu cầu người dùng, 2026-10-18)

> §4 và §7d nhắc tới `ui-ux-pro-max-skill`, `frontend-design` của Anthropic, "Refactoring UI Skill" và `bergside/awesome-design-skills`, nhưng catalog chưa có dòng nào cho chúng. Mục này lập hồ sơ cả bốn: clone repo ngày 18/10/2026, đếm file và dữ liệu thật, tự chạy test hoặc kiểm số liệu khi có thể, rồi đối chiếu với nguồn ngoài.

### 7g.1 Bảng nhanh

| | `ui-ux-pro-max-skill` | `frontend-design` (Anthropic) | Refactoring UI Skill (`s0xDk`) | `bergside/awesome-design-skills` |
|---|---|---|---|---|
| Bản chất | Kho tra cứu (CSV + BM25) sinh "design system" theo loại sản phẩm, kèm 6 skill phụ | 1 prompt ~70 dòng định hướng thẩm mỹ, chống mặc định | 1 skill quy tắc + token CSS lấy từ sách *Refactoring UI* | 67 cặp `SKILL.md` + `DESIGN.md` theo style, kéo về bằng CLI TypeUI |
| ★ · license (18/10/2026) | ~137k · MIT | `anthropics/claude-plugins-official` ~42k · Apache-2.0 | 646 · MIT | ~3,2k · MIT |
| Hoạt động | 277 commit, v2.15.0, commit cuối 14/10/2026 | Plugin 1.1.0, SKILL.md sửa lần cuối 2–3/9/2026 | 2 commit, cùng ngày 27/8/2026 | 49 commit, 9/3 → 28/6/2026 |
| Có cổng máy? | Có validator dữ liệu + 164 unit test của chính repo; **không** đo bản render | Không; chỉ dặn "tự chụp màn hình để phê bình" | Không; token đã kiểm tương phản sẵn | Không; mục "Quality Gates" là văn bản |
| Đã kiểm | `unittest` 164/164 pass, `validate_data.py` OK, chạy thử 1 truy vấn | 3 bản SKILL.md trong 3 repo giống hệt nhau | Tính lại tỉ lệ tương phản light và dark mode: khớp chú thích | 81% dòng là khung chung; 40/67 màu primary không đạt 4,5:1 với chữ trắng |

### 7g.2 `nextlevelbuilder/ui-ux-pro-max-skill`: kho tra cứu lớn nhất, tạo design system bằng tìm kiếm

| Mục | Thông tin (đọc 18/10/2026) |
|---|---|
| Repo | `nextlevelbuilder/ui-ux-pro-max-skill` · trang GitHub **~137k★**, ~14,6k fork · **MIT** (© 2024 Next Level Builder) · tag mới nhất **v2.15.0** · 277 commit, commit đầu 30/11/2025, cuối 14/10/2026 |
| Tác giả | Viet Tran (`viettranx`) 55 commit, "Goon" 30, Clark Cant 17, Duy 15. README có bản tiếng Việt, ảnh demo có giao diện tiếng Việt; tác giả và đội có vẻ ở Việt Nam **(chưa xác minh danh tính)**. Cùng chủ: `3dviz-pro-max`, goclaw.sh, agentkit.best |
| Phân phối | `npx ui-ux-pro-max-cli init --ai <platform>` cho 19 nền tảng (Claude, Cursor, Copilot, Codex, Gemini, Kiro, OpenClaw…). npm `ui-ux-pro-max-cli`: **72.299** lượt tải trong 17/9–16/10/2026 |
| Bên trong | 7 skill trong `.claude/skills/` (`ui-ux-pro-max` 214 dòng, `design` 333, `ui-styling` 336, `design-system` 248, `brand`, `banner-design`, `slides`). Lõi là `scripts/search.py` + `core.py` (**BM25**) chạy trên 13 file CSV. Dữ liệu được nhân bản 3 lần (`src/`, `cli/assets/`, `.claude/skills/`) và `diff` cho thấy giống nhau |

**Đếm lại các con số trên badge** (từ `data/*.csv` và `catalog-summary.json`):

| Badge/README | Đếm thật | Ghi chú |
|---|---|---|
| "79 searchable UI styles" | ✅ 88 dòng, trong đó 79 "searchable" (50 active + 29 supplemental), 9 deprecated | `catalog-summary.json` giải thích đúng |
| "192 reasoning rules", 192 palette, 192 loại sản phẩm | ✅ đúng 192 dòng mỗi file | Mỗi "rule" là một dòng gợi ý theo loại sản phẩm, không phải luật kiểm được |
| 74 font pairing, 119 UX guideline, 25 loại chart, 22 stack | ✅ khớp | Thêm 1.934 Google Fonts, 105 icon chọn lọc |
| Nguồn dữ liệu | ⚠️ `data-provenance.json` chỉ có **51 bản ghi**, phủ 51/192 profile; 31 bản ghi đang "needs-review" | Phần lớn dữ liệu không ghi nguồn gốc từng dòng |

**Tự chạy (Python 3, 18/10/2026):** `python3 -m unittest discover` **164/164 pass**; `validate_data.py` OK (12 file domain, 22 file stack). Thử truy vấn `"fintech mobile banking app" --design-system` thì nhận về pattern **trang landing** ("Contact Sales / Get Quote", logo carousel, Hero → Proof) chứ không phải màn hình app. Accent là tím `#8B5CF6` với ghi chú "Gold trust + purple tech", trong khi mục AVOID của cùng kết quả ghi "AI purple/pink gradients". Checklist còn yêu cầu `cursor-pointer` và hover cho một app mobile. Đây là một truy vấn, chưa đại diện cho cả kho, nhưng cho thấy BM25 khớp theo từ khóa chứ không hiểu ngữ cảnh mobile.

**Đánh giá:**

- **Điểm mạnh:** dữ liệu lớn, có cấu trúc, tra cứu tất định (cùng câu hỏi ra cùng kết quả), có test và validator thật, hỗ trợ nhiều agent nhất trong nhóm. Hợp làm **nguồn gợi ý** palette, font, style khi chưa có brand.
- **Hạn chế:** không có cổng đo trên bản render. Đây là điểm khác chính với Impeccable (mục 20, engine Rust 59 rule tất định) và XIAS (§7d, 52 cổng trình duyệt), như mục 20 đã ghi. Kết quả có thể tự mâu thuẫn như ví dụ trên. Số sao tăng rất nhanh: agentskill.sh ghi 38,3k (3/2026), Skillselion ghi 112k (30/7/2026), trang GitHub ~137k (18/10/2026).
- **Dùng thế nào:** gọi `search.py` để lấy gợi ý, rồi để người hoặc agent chọn lại theo brief. Không dùng nguyên output làm design system. Ghép với một bộ cổng đo (ví dụ script của XIAS) nếu muốn chặn lỗi tương phản. Mục 23 ghi repo này từng được vendor trong Hermes-Agents (45 file).

### 7g.3 `frontend-design` (Anthropic): prompt ngắn, chính chủ, thay đổi theo thời gian

| Mục | Thông tin (đọc 18/10/2026) |
|---|---|
| Vị trí | `anthropics/claude-code/plugins/frontend-design` (plugin 1.1.0), `anthropics/claude-plugins-official/plugins/frontend-design`, `anthropics/skills/skills/frontend-design`. Cả ba `SKILL.md` **giống hệt nhau** (71 dòng) |
| Tác giả | Prithvi Rajasekaran, Alexander Bricken (Anthropic Applied AI, theo `plugin.json`). Bài blog "Improving frontend design through Skills" ngày 12/11/2025 |
| License | `LICENSE.txt` Apache-2.0 trong `anthropics/skills` |
| Cài | `/plugin marketplace add anthropics/claude-code` rồi `/plugin install frontend-design@claude-code-plugins`; hoặc lấy từ marketplace chính thức. Skill do model tự gọi theo mô tả, không phải lệnh `/` |
| Lịch sử | Thêm 11/11/2025; viết lại 9/6, 17/6 (bump 1.1.0) và 2–3/9/2026 |

**Nội dung bản hiện tại:** vai "design lead của studio", buộc xác định chủ đề, người dùng và việc chính của sản phẩm trước khi thiết kế; quy trình hai lượt (lên plan token màu 4–6 hex, font, layout bằng ASCII wireframe, rồi tự so plan với "bản mặc định" và sửa trước khi code); một phần dài về viết nội dung UI (CTA nói rõ hành động, lỗi không xin lỗi, sentence case). Phần đáng chú ý nhất là danh sách **5 cụm "dấu hiệu AI"** cụ thể: nền kem `#F4F1EA` + serif + accent đất nung `#D97757` (skill tự nhận đây là màu của chính Claude), nền gần đen + một accent xanh axit, layout báo giấy, "bộ card SaaS" bóng `rgba(0,0,0,.1)`, và các chi tiết khuôn như eyebrow viết hoa, chuỗi "A · B · C", mũi tên "→" sau nút.

**Đánh giá:**

- **Điểm mạnh:** ngắn (bài blog ước ~400 token cho bản đầu), chính chủ, cập nhật theo chính những gì model hay lặp lại. Bản 9/2026 còn đảo một phần lời khuyên của bản 11/2025: blog gốc khuyên dùng nền gradient nhiều lớp và animation tải trang, bản mới coi "gradient washes as decoration" và fade-up từng section là dấu hiệu AI.
- **Hạn chế:** không có cổng máy, chỉ dặn tự chụp màn hình để phê bình. Bài blog chỉ có ảnh so sánh, **không có benchmark**. Con số "1,1 triệu lượt cài" xuất hiện ở một số trang tổng hợp nhưng không tìm thấy trên trang chính thức **(chưa xác minh)**. Mục tiêu là "khác biệt", nên với sản phẩm đã có brand phải nói rõ ràng buộc trong prompt (skill có ghi "lời của brief luôn thắng").
- **Dùng thế nào:** bật cho trang mới, landing, prototype. Với ứng dụng nghiệp vụ đã có design system thì design system thắng; ghép thêm cổng đo (XIAS) hoặc detector (Impeccable) nếu cần chặn.

### 7g.4 "Refactoring UI Skill": hai repo trùng tên, chọn bản `s0xDk`

`maxbogo/awesome-ai-tools-for-ui` (mục 08) trỏ tới **`s0xDk/refactoring-ui-skill`**. Tìm web còn ra `lovropodobnik/refactoring-ui-skill` (2 commit ngày 8/1/2026, skill 32 dòng + 5 lệnh `/fix-*`, **không có file LICENSE**) và `booklib-ai/skills/refactoring-ui` (chỉ thấy qua trang tổng hợp, chưa xác minh). Hồ sơ dưới đây là bản `s0xDk`.

| Mục | Thông tin (đọc 18/10/2026) |
|---|---|
| Repo | `s0xDk/refactoring-ui-skill` · **646★**, 62 fork · **MIT** (© 2026 s13k) · **2 commit, cùng ngày 27/8/2026** |
| Bên trong | `SKILL.md` 267 dòng (thang spacing, type, weight, màu HSL, 5 mức bóng, line-height, radius; quy trình; 9 "hard rule") · `references/systems.md` (dựng palette), `diagnose.md` (bảng triệu chứng → cách sửa), `techniques.md` · `assets/tokens.css` (token đầy đủ: thang, ramp xám và primary 9 mức, 3 bộ màu accent, lớp semantic `--surface`/`--text-*`/`--action` và khối dark mode) |
| Bản quyền sách | README ghi không chứa chữ hay hình của sách, chỉ ghi chú và CSS tự viết theo ý tưởng của sách |

**Kiểm token (18/10/2026):** tính lại tỉ lệ tương phản theo WCAG từ các giá trị HSL trong `tokens.css`. Light mode khớp chú thích: `grey-400` 2,67:1 (chỉ dùng cho chữ disabled), `grey-500` 3,91:1 (chỉ chữ lớn), `grey-600` 5,60:1, `grey-900` 13,43:1 so với nền `grey-100`; chữ trắng trên `primary-500` 5,81:1, trên `red/yellow/green-500` lần lượt 6,15 / 4,98 / 6,06:1. **Dark mode (kiểm lại 19/10/2026** bằng script đọc khối `@media (prefers-color-scheme: dark)` và giải `var()`, màu làm tròn về 8-bit như trình duyệt): `--text-primary` 11,22:1, `--text-secondary` 9,95:1, `--text-tertiary` 6,05:1 trên nền và 4,81:1 trên `--surface-raised`, chữ trên `--action` 5,19:1, `--border-strong` 5,03 / 3,99:1; đều khớp chú thích trong file. Tính theo 8-bit, các số light mode ở trên lệch tối đa 0,05 (vd primary-500 5,78:1).

**Đánh giá:**

- **Điểm mạnh:** quy tắc cụ thể đến mức kiểm được (không hai bước spacing nào gần nhau dưới ~25%, chữ lớn theo WCAG là 24px hoặc 18,66px đậm chứ không phải 18px, viền chức năng cần 3:1). Token có sẵn và đúng như chú thích. Có bảng chẩn đoán để sửa UI cũ, điều ít skill "taste" làm.
- **Hạn chế:** chỉ 2 commit, một tác giả, chưa có lịch sử bảo trì. Không có cổng máy; luật nằm trong prompt. Thiên về web/CSS, chưa nói tới mobile native.
- **Dùng thế nào:** hợp làm lớp "hệ thống" bên dưới một skill "taste" (frontend-design hoặc Taste Skill): skill này giữ thang giá trị, skill kia quyết định cá tính. Có thể chép thẳng `tokens.css` làm điểm khởi đầu rồi đổi hue.

### 7g.5 `bergside/awesome-design-skills`: 67 style viết bằng một khuôn

| Mục | Thông tin (đọc 18/10/2026) |
|---|---|
| Repo | `bergside/awesome-design-skills` · trang GitHub **~3,2k★**, 327 fork · **MIT** (© 2026 Bergside) · 49 commit, **tất cả của Zoltán Szőgyényi** (đồng sáng lập Themesberg theo blog của Themesberg, công ty làm Flowbite; quan hệ với Bergside chưa xác minh), 9/3 → 28/6/2026 |
| Bên trong | 67 thư mục trong `skills/`, mỗi thư mục có `SKILL.md` (81–101 dòng, trung vị 83) và `DESIGN.md`; `index.json`; ảnh preview |
| Phân phối | CLI **TypeUI** (`npx typeui.sh pull <slug>`, repo `bergside/typeui.sh`), ghi file vào `.claude/`, `.cursor/skills/`…; npm `typeui.sh` 1.297 lượt tải 17/9–16/10/2026. Trang tổng hợp nhắc tới bản Pro trả phí **(chưa xác minh)** |

**Đo chất lượng (18/10/2026):**

- **Khuôn chung chiếm phần lớn:** cả 67 `SKILL.md` có đúng 13 mục giống nhau (Mission, Brand, Style Foundations… Quality Gates), nằm giữa hai dấu `TYPEUI_SH_MANAGED`. Trung bình **81% số dòng** của mỗi file cũng xuất hiện ở ≥90% các file khác. Phần riêng của từng style chủ yếu là một câu mô tả, tên font và vài mã màu.
- **Màu:** 17/67 style dùng cùng primary `#3B82F6` (blue-500 của Tailwind). Nếu đặt chữ trắng trên nền primary (cách phổ biến cho nút), **40/67** style không đạt 4,5:1. Ví dụ `brutalism` `#DD614C` 3,57:1, `bento` `#FAD4C0` 1,38:1. File không quy định màu chữ trên primary, nên đây là rủi ro khi dùng chứ không hẳn là lỗi file.
- **Tên thương hiệu:** có style đặt theo thương hiệu (`claude`, `codex`, `stitch`, `roku`, `sega`, `pacman`, `tetris`, `ant`…) mà không có ghi chú quan hệ hay tuyên bố không liên kết.
- **Liên hệ:** §7d đã ghi 51 style của XIAS lấy mô tả và màu từ kho này mà không ghi công.

**Đánh giá:** hợp làm **danh mục cảm hứng** hoặc khung để tự viết `SKILL.md` theo style. Muốn có giá trị kiểm chứng thì viết DESIGN.md theo spec Google (§7c) và chạy `lint`; với style có primary sáng, thêm token `on-primary` rõ ràng.

### 7g.6 Xếp vào bức tranh chung

| Lớp | Nên dùng | Vì sao |
|---|---|---|
| Thang giá trị, token nền | Refactoring UI Skill (`s0xDk`) | Quy tắc kiểm được, token đúng chú thích |
| Hướng thẩm mỹ, chống "AI slop" | `frontend-design` (chính chủ) hoặc Taste Skill (§4) | Ngắn, danh sách dấu hiệu cụ thể |
| Gợi ý palette/font theo loại sản phẩm | `ui-ux-pro-max-skill` | Kho dữ liệu lớn, tra cứu tất định, nhưng phải chọn lọc lại |
| Khung style có sẵn | `bergside/awesome-design-skills`, `awesome-design-md` (§7c) | Cảm hứng; tự viết lại cho brand |
| Cổng đo bắt lỗi thật | XIAS (§7d), Impeccable (mục 20) | Hai bộ duy nhất trong kho có đo hoặc detector tất định |

Cả bốn mục trên đều **không có benchmark độc lập**, giống nhận xét ở §4. Bài học của §4 vẫn đúng: "taste" chỉ bền khi có cổng máy đi kèm.

**Nguồn §7g:** https://github.com/nextlevelbuilder/ui-ux-pro-max-skill (clone đủ, 277 commit, HEAD 56ea9cf 14/10/2026; README, skill.json, LICENSE, `src/ui-ux-pro-max/data/*.csv`, `catalog-summary.json`, `data-provenance.json`, `scripts/core.py`; tự chạy `unittest` 164/164, `validate_data.py`, `search.py --design-system` 18/10/2026) · trang GitHub 18/10/2026 (~137k★, ~14,6k fork) · api.npmjs.org `ui-ux-pro-max-cli` (72.299, 17/9–16/10/2026) · skillselion.com/best/plugins-for-frontend-design (112k★, dữ liệu 30/7/2026) · agentskill.sh/@nextlevelbuilder/ui-ux-pro-max (38,3k★, 3/2026) · releasealert.dev/github/nextlevelbuilder/ui-ux-pro-max-skill · https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design (README, plugin.json 1.1.0, SKILL.md; git log) · https://github.com/anthropics/claude-plugins-official (trang GitHub ~42,3k★, 18/10/2026; SKILL.md) · https://github.com/anthropics/skills (`skills/frontend-design/SKILL.md`, LICENSE.txt Apache-2.0) · https://claude.com/blog/improving-frontend-design-through-skills (12/11/2025) · wmedia.es/en/tips/claude-code-frontend-design-skill · claudelog.com/faqs/what-is-frontend-design-skill-in-claude-code · https://github.com/s0xDk/refactoring-ui-skill (clone đủ, 2 commit, HEAD 4887214 27/8/2026; SKILL.md, references/, assets/tokens.css, LICENSE; trang GitHub 646★/62 fork 18/10/2026; tính tương phản light mode) · https://github.com/lovropodobnik/refactoring-ui-skill (clone, 2 commit 8/1/2026, không LICENSE) · vibeindex.ai/skills/booklib-ai/skills/refactoring-ui · https://github.com/maxbogo/awesome-ai-tools-for-ui (README dòng 51) · https://github.com/bergside/awesome-design-skills (clone đủ, 49 commit, HEAD f631a09 28/6/2026; README, LICENSE, `skills/*/SKILL.md`; đo trùng dòng và tương phản 18/10/2026; trang GitHub ~3,2k★/327 fork) · api.npmjs.org `typeui.sh` (1.297, 17/9–16/10/2026) · sourcepulse.org/projects/26797192 · hermesatlas.com/projects/bergside/typeui · vibeindex.ai/collection/bergside/awesome-design-skills · themesberg.com/blog/marketplace/2020-year-in-review

## 7h. Layout mẫu cho web, dashboard và mobile (yêu cầu người dùng, 2026-10-18)

> Người dùng hỏi "layout mẫu cho mobile, web, app". Mục này lập hồ sơ các nguồn **page block, template trang và app shell** có mã dùng được, cộng hai bộ hướng dẫn layout chính thức (Material 3, Apple HIG). Đã clone 21 repo ngày 18/10/2026; số commit, ngày commit cuối và license đọc từ bản clone; số block/trang **đếm bằng `git ls-tree`**, không lấy từ README. Số sao là số làm tròn trên trang GitHub cùng ngày.

### 7h.1 Bảng tổng hợp

| Nhóm | Nguồn | ★ · license | Commit cuối · số commit | Layout thực có trong repo | Stack |
|---|---|---|---|---|---|
| Web | **shadcn/ui Blocks** (`shadcn-ui/ui`) | 125,8k · MIT | 16/10/2026 · 2.571 | 27 block trong `registry/new-york-v4/blocks`: 1 dashboard, 16 sidebar, 5 login, 5 signup; thêm ~70 chart và ~32 calendar block | React, Tailwind v4 |
| Web | **HyperUI** (`markmead/hyperui`) | 12,3k · MIT | 10/10/2026 · 825 | 306 mẫu HTML bản sáng (≈560 file kể cả bản tối): marketing 106, application 163, neobrutalism 37; 12 trang template (analytics dashboard, SaaS landing, portfolio, storefront, support inbox) | HTML + Tailwind |
| Web | **Once UI core** (`once-ui-system/core`) | 268 · MIT | 18/10/2026 · 1.207 | 175 file block trong app docs: Hero 14, Features 18, Sidebar 9, Login 5, Dashboard 3, Pricing, FAQ… | Next.js, SCSS |
| Web | **Preline** (`htmlstreamofficial/preline`) | 6,5k · MIT **+ Preline UI Fair Use License** | 21/8/2026 · 142 | Repo chỉ có 29 plugin JS và 5 template HTML; "204 free blocks" của README nằm trên preline.co, không trong repo | HTML, Tailwind, JS |
| Web | **Flowbite** (`themesberg/flowbite`) | 9,4k · MIT (lõi) | 27/6/2026 · 2.789 | Chỉ trang tài liệu component; Blocks "400+ sections" thuộc bản Pro trả phí | Tailwind, JS |
| Web | **daisyUI** (`saadeghi/daisyui`) | 42,6k · MIT | 13/10/2026 · 3.291 | 61 component CSS, không có trang mẫu; template đầy đủ bán ở daisyui.com/store (vd dashboard từ $69) | Plugin Tailwind |
| Web | **Tailwind Plus** (trước là Tailwind UI) | – · thương mại | – | **Ngừng nhận khách mới** từ khi Tailwind Labs về Shopify (9/9/2026); khách cũ giữ quyền dùng | React/Vue/HTML |
| Dashboard | **shadcn-admin** (`satnaing/shadcn-admin`) | 15,8k · MIT | 11/6/2026 · 323 | 31 route: auth 5 (có OTP), lỗi 5, dashboard, tasks, users, chats, apps, settings 5, help center | Vite, React 19, TanStack Router |
| Dashboard | **next-shadcn-dashboard-starter** (`Kiranism/…`) | 7,1k · MIT | 25/8/2026 · 434 | 28 `page.tsx`: overview, CRUD sản phẩm, users, kanban, chat, billing, 4 form, workspaces | Next 16, React 19, Clerk |
| Dashboard | **Tremor Blocks** (`tremorlabs/tremor-blocks`) | 545 · MIT | **22/1/2025 · 3** | 323 file block trong 28 nhóm: page shell 6, KPI card, bảng, form layout, billing, login, onboarding | Next.js, Tailwind |
| Dashboard | **Tremor** (`tremorlabs/tremor`) | 3,7k · Apache-2.0 | **10/10/2025** · 84 | 39 component (8 loại chart, Tracker, BarList), không có trang | React 18, Recharts 2 |
| Dashboard | **TailAdmin free** (`TailAdmin/free-react-tailwind-admin-dashboard`) | 1,3k · MIT | 15/9/2026 · 90 | 18 trang, chỉ 1 dashboard (ecommerce); bản Pro mới có 7 dashboard | Vite, React 19 |
| Dashboard | **Flowbite Admin Dashboard** (`themesberg/flowbite-admin-dashboard`) | 2,9k · MIT | **20/3/2025** · 89 | 17 trang: auth 5, CRUD 2, layout sidebar/stacked, 404/500, pricing, settings | Hugo, HTML |
| Dashboard | **Refine** (`refinedev/refine`) | 35,9k · MIT | 10/9/2026 · 7.607 | Framework CRUD; 281 thư mục examples, 6 `template-*` (antd, mui, mantine, chakra, headless…), app CRM | React + UI kit tùy chọn |
| Mobile RN | **React Native Reusables** (`founded-labs/react-native-reusables`) | 8,7k · MIT | 27/9/2026 · 1.212 | 32 component (bản NativeWind và Uniwind), 7 block auth (mỗi block có bản Clerk) | React Native, Expo |
| Mobile RN | **Tamagui + Bento** (`tamagui/tamagui`, `code/bento`) | 14,3k · MIT | 17/10/2026 · 18.926 | ~70 file Bento: shell 6 (sidebar, top nav, tab bar, drawer), form layout 5, list 10, ecommerce 4; trang Bento nay ghi "Free, forever" | RN + web |
| Mobile RN | **gluestack-ui v3** (`gluestack/gluestack-ui`) | 5,3k · MIT (chỉ trong `packages/gluestack-ui/LICENSE`, gốc repo không có LICENSE) | 2/9/2026 · 16.582 | 61 component, 3 màn showcase, 4 starter kit (Expo, Expo + Uniwind, monorepo, Next) | RN + web, NativeWind |
| Mobile RN | **NativeWind** (`nativewind/nativewind`) | 8,1k · MIT | 16/10/2026 · 3.373 | Không có layout; lớp Tailwind cho RN mà RNR và gluestack dựa vào (v4 ổn định, v5 RC) | RN |
| Flutter | **flutter/samples** | 19,3k · BSD-3 | 8/10/2026 · 1.925 | Mẫu chính thức; liên quan layout: `material_3_demo`, `cupertino_gallery`, `platform_design`, `compass_app`, `navigation_and_routing` | Flutter |
| Flutter | **Best-Flutter-UI-Templates** (`mitesh77/…`) | 22,8k · MIT | 16/12/2025 · 122 | 5 app demo (hotel booking, fitness, course, drawer, intro animation), 52 file dart, không kiến trúc | Flutter |
| Flutter | **Flutter Responsive Admin Panel** (`abuanwar072/…`) | 7,1k · MIT | 28/7/2026 · 65 | 1 layout responsive (side menu + dashboard), 17 file dart | Flutter |
| Hướng dẫn | **Material 3 canonical layouts** | – | – | 3 layout: list-detail (`ListDetailPaneScaffold`), supporting pane (`SupportingPaneScaffold`, 70/30 ở màn rộng), feed (`LazyVerticalGrid` + `GridCells.Adaptive`) | Compose |
| Hướng dẫn | **Apple HIG: Layout** | – | – | Chọn layout theo size class (không theo thiết bị/hướng xoay), tôn trọng safe area, đổi tab bar sang sidebar khi rộng | SwiftUI/UIKit |
| Cảm hứng | **Mobbin** | – · thương mại | – | Thư viện ảnh chụp app thật, không có mã; Pro khoảng $10/tháng trả theo năm **(chưa xác minh từ trang giá, bị chặn)** | – |

### 7h.2 Điều đã kiểm và rủi ro cần biết

- **License không thuần MIT:**
  - Preline dùng hai license song song; phần Fair Use cấm làm "competing products" và cho tác giả quyền chấm dứt (đã đọc `LICENSE` trong clone).
  - Template `once-ui-system/magic-portfolio` là **CC BY-NC 4.0**, cấm dùng thương mại, dù thư viện core là MIT (đã đọc `LICENSE`).
  - Tremor dùng Apache-2.0 cho component nhưng MIT cho repo blocks.
- **Miễn phí trên README, trả phí khi cần trang hoàn chỉnh:** Preline (bản Pro 740 block theo README), Flowbite Blocks, daisyUI store, TailAdmin Pro. Bản miễn phí của các bộ này thường chỉ là component, không phải trang.
- **Ngừng cập nhật:** Tremor Blocks (3 commit, cuối 1/2025), Tremor (10/2025, còn React 18 + Recharts 2), Flowbite Admin Dashboard (3/2025). Vercel mua Tremor 22/1/2025 và mở miễn phí blocks; từ đó gần như không có commit.
- **Tailwind Plus:** Tailwind Labs về Shopify ngày 9/9/2026, ngừng nhận khách mới cho Tailwind Plus; Tailwind CSS vẫn MIT. Nguồn là nhiều bài báo cùng thuật lại bài "Tailwind Labs is joining Shopify" của Adam Wathan; trang tailwindcss.com/plus chỉ hiện form đăng nhập nên **chưa xác minh từ trang chính thức**.
- **Flutter:** gói `flutter_adaptive_scaffold` đã bị đánh dấu discontinued trên pub.dev (0.3.3+1); layout list-detail thích ứng phải tự dựng bằng `LayoutBuilder` / `NavigationRail` **(chưa xác minh có gói thay thế chính thức)**.
- **Breakpoint Material 3:** compact < 600dp, medium 600–839dp, expanded ≥ 840dp, theo tài liệu adaptive của Android; trang m3.material.io trả 404 khi đọc nên **chưa đối chiếu được trên m3**.
- **Apple HIG:** không đưa số margin cố định cho iOS. Số cụ thể có cho tvOS (safe area 60pt trên/dưới, 80pt hai bên) và visionOS (tâm nút cách nhau ≥ 60pt).

### 7h.3 Chọn theo loại sản phẩm

| Cần | Nên lấy | Ghi chú |
|---|---|---|
| Trang marketing / landing | **HyperUI** (106 block marketing, MIT); dự án Next.js thêm **Once UI core** | Tránh Preline nếu không chấp nhận Fair Use; Tailwind Plus không mua được nữa |
| SaaS dashboard | Khung từ **shadcn/ui blocks** (`npx shadcn add dashboard-01`, `sidebar-07`…) + starter **shadcn-admin** (Vite) hoặc **next-shadcn-dashboard-starter** (Next 16) | Tremor Blocks để tham khảo KPI/chart/billing, không làm nền vì đã ngừng; nhiều CRUD thì cân nhắc **Refine** |
| App mobile React Native | **React Native Reusables** (cùng triết lý shadcn) trên NativeWind/Uniwind; cần shell (tab bar, drawer) thì thêm **Tamagui Bento** | gluestack-ui là phương án thay thế nhiều component hơn |
| App mobile Flutter | **flutter/samples** (`material_3_demo`, `cupertino_gallery`, `compass_app`) + Material 3 canonical layouts | Best-Flutter-UI-Templates chỉ để tham khảo giao diện |
| Chuẩn layout thích ứng | **Material 3 canonical layouts** và **Apple HIG: Layout** | Dùng làm quy ước breakpoint và chuyển tab bar ↔ sidebar |
| Cảm hứng màn hình thật | Mobbin | Chỉ là ảnh, không có mã hay license để tái sử dụng |

Liên hệ với các mục khác: layout chỉ là khung; giá trị màu, khoảng cách và "gu" lấy từ design system (§1, §7f) và skill (§7g). Muốn agent dựng trang từ các block này mà không ra giao diện "khuôn", ghép với cổng đo (§7d) hoặc detector (Impeccable, mục 20).

**Nguồn §7h:** clone 18/10/2026 (`git clone --filter=blob:none`, đếm bằng `git ls-tree` trên HEAD): github.com/{shadcn-ui/ui, markmead/hyperui, once-ui-system/core, once-ui-system/magic-portfolio, htmlstreamofficial/preline, themesberg/flowbite, themesberg/flowbite-admin-dashboard, saadeghi/daisyui, satnaing/shadcn-admin, Kiranism/next-shadcn-dashboard-starter, tremorlabs/tremor, tremorlabs/tremor-blocks, TailAdmin/free-react-tailwind-admin-dashboard, refinedev/refine, founded-labs/react-native-reusables, tamagui/tamagui, gluestack/gluestack-ui, nativewind/nativewind, flutter/samples, mitesh77/Best-Flutter-UI-Templates, abuanwar072/Flutter-Responsive-Admin-Panel-or-Dashboard} (README, LICENSE, package.json; số sao từ trang GitHub cùng ngày) · ui.shadcn.com/blocks · blocks.tremor.so · tamagui.dev/bento · daisyui.com/store · pub.dev/packages/flutter_adaptive_scaffold · tailwindcss.com/plus (chỉ form đăng nhập) · cmswire.com/digital-experience/shopify-acquires-tailwind-labs-to-secure-css-framework · vktr.com/digital-experience/shopify-acquires-tailwind-labs-to-secure-css-framework · pulse2.com/shopify-acquires-tailwind-labs-as-tailwind-css-tops-110-million-weekly-installs · witscode.com/blogs/shopify-acquires-tailwind-labs-what-was-announced · developer.android.com/develop/ui/compose/layouts/adaptive/canonical-layouts · m3.material.io/foundations/layout/canonical-layouts/overview (404) · developer.apple.com/design/human-interface-guidelines/layout (đọc qua developer.apple.com/tutorials/data/design/human-interface-guidelines/layout.json) · mobbin.com/pricing (403; giá theo toolradar.com, pricingsaas.com)

## 7i. Kiểm ảnh: miqdadbadjuber/anti-slop ("antislop"), bộ luật lọc "AI slop" cho UI, nội dung và code (ảnh người dùng gửi, 2026-10-19)

> Ảnh là phần đầu README trên trình duyệt: logo "/antislop", huy hiệu Trendshift "#2 Repository Of The Day" và "#13 Repository Of The Week" (JavaScript), các huy hiệu "license MIT", "version v3.2.20", "Skills 29.7K", tiêu đề "Anti Slop: Rules for AI Coding Agents", câu "A filter, not a style guide", và chữ phủ "THIS FREE RULEBOOK" do người đăng lại thêm vào. Đã clone toàn bộ repo (119 commit), đọc 6 skill, tự chạy script kiểm và smoke test của repo, rồi đối chiếu các con số với Trendshift, skills.sh và npm.

### 7i.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 19/10/2026) |
|---|---|
| Repo | `miqdadbadjuber/anti-slop` · trang GitHub **~6,5k★**, 457 fork, 1 issue mở · **MIT** (© 2026 Miqdad Badjuber) · tag mới nhất **v3.2.21** · 119 commit, 7/8 → 16/10/2026 |
| Tác giả | Miqdad Badjuber (Indonesia, 110 follower, 6 repo công khai, đây là repo duy nhất có sao). 95/119 commit từ ba tên/tài khoản của tác giả; Fajar Hidayat 17 commit |
| Phân phối | `npx antislop-ai` (trình cài hỏi skill, phạm vi, agent) · `npx skills add miqdadbadjuber/anti-slop` · plugin cho Claude Code, Codex, Cursor, Antigravity, Kimi, Cline, Oh My Pi, Pi · file đơn `antislop.md` để dán vào chat. npm `antislop-ai`: **9.992** lượt tải 17/9–16/10/2026 |
| Bên trong | 6 skill: `antislop` (lõi, 724 dòng), `antislop-ui` (311), `antislop-copywriting` (372), `antislop-layoutmobile` (170), `antislop-code` (128, chỉ sửa comment), `antislop-human` (150, kèm `contrast-check.py` và MCP tính tương phản). Lõi có **38 luật R-01…R-38** chia 3 tầng: Hard Gate, Purpose-Gate, Quality Locks; cộng 5 chuẩn "Craftsmanship" và "Delivery Gate" trước khi giao |
| Tác động lên máy | Plugin Claude Code tự khởi động MCP `antislop-contrast` (Node gọi Python chạy `contrast-mcp.py`, stdio). Trình cài chép thư mục skill và ghi một khối có dấu `<!-- antislop:start/end -->` vào `CLAUDE.md` hoặc `AGENTS.md`; lưu chế độ ở `~/.config/antislop/settings.json` |

### 7i.2 Kiểm từng ô trong ảnh

| Ô trong ảnh | Kiểm | Ghi chú |
|---|---|---|
| "#2 Repository Of The Day" (Trendshift, JavaScript) | ✅ | Trang trendshift.io/repositories/137042: hạng 12, 6, **2**, 22 các ngày 7–10/10/2026, ngoài ra "not trending". Là thứ hạng một ngày trong nhóm JavaScript |
| "#13 Repository Of The Week" | ✅ | Có huy hiệu Weekly #13, trang không ghi ngày |
| "license MIT" | ✅ | `LICENSE` MIT; npm `antislop-ai` cũng ghi MIT |
| "version v3.2.20" | ⚠️ cũ | Hiện là **v3.2.21** (tag, `package.json`, npm) |
| "Skills 29.7K" | ⚠️ cũ, dễ hiểu sai | skills.sh nay ghi **32,0K**, là **tổng lượt cài của 6 skill** (từ 4,9K đến 6,3K mỗi skill), không phải số người dùng. Các skill có số gần bằng nhau, khớp với việc trình cài chép cả bộ một lần |
| "A filter, not a style guide: no prescribed colors, fonts, or layouts" | ✅ có lưu ý | Luật không chỉ định màu hay font. R-06 nêu tên "danh sách mặc định" (Inter, Geist, Space Grotesk…) nhưng ghi rõ "None are banned", chỉ yêu cầu ghi lý do. Tuy vậy, phần cảnh báo có đánh dấu một số lựa chọn bố cục phổ biến là dấu hiệu slop khi dùng mặc định: bento grid, dải logo "Trusted by", footer 4 cột, thẻ giá "Most Popular", icon Lucide |
| Bốn ảnh "See the difference" (không có gì / chỉ antislop / chỉ DESIGN.md / cả hai) | ⚠️ | Ảnh minh họa của tác giả, không công bố brief hay prompt để chạy lại, không có benchmark |
| "THIS FREE RULEBOOK" | – | Chữ do người đăng lại thêm, không có trong README |

**Tổng:** 3✅ / 3⚠️ / 0❌ (không tính chữ phủ). Các thông tin cũ trong ảnh chỉ lệch vì ảnh chụp trước bản v3.2.21.

### 7i.3 Điều ảnh không nói (đọc mã và tự chạy)

- **Kiểm của chính repo chạy được (19/10/2026):** `node scripts/check-repo.mjs` **13/13 check pass** (gồm "hai bản cài đặt tương phản dùng cùng công thức"); `python3 contrast-check.py --selftest` 9/9 cặp đúng; `node cli/scripts/smoke-test.mjs` pass (bỏ qua phần cần cài dependency của CLI). CI chạy cả ba.
- **Lỗi định nghĩa "chữ lớn":** R-25, `antislop-human` và `contrast-check.py` đều ghi chữ lớn là "**18px+**" được phép 3:1. WCAG định nghĩa chữ lớn là 18pt (khoảng **24px**) hoặc 14pt đậm (khoảng 18,66px). Hệ quả: chữ thường cỡ 18–23px chỉ đạt 3:1 sẽ được báo PASS, trong khi WCAG yêu cầu 4,5:1. Refactoring UI Skill (§7g.4) ghi đúng ngưỡng này.
- **Tốn ngữ cảnh:** skill lõi mô tả "Load always", dài khoảng 58 KB (ước chừng 14 nghìn token). Cả 6 skill cộng lại khoảng 146 KB, chưa kể `antislop.md` là bản trùng của skill lõi. So với `frontend-design` của Anthropic (§7g.3, 71 dòng) thì nặng hơn nhiều lần.
- **Câu hỏi chế độ chặn công việc:** mặc định, mỗi phiên mới agent phải hỏi "DURING hay AFTER" và dừng lại chờ trả lời trước mọi việc UI, kể cả việc chỉ đọc. Muốn bỏ câu hỏi thì chạy `npx antislop-ai --mode during|after`. Với agent chạy không người trông (Routine, CI), cần đặt chế độ trước.
- **Điểm làm tốt về an toàn:** coi `DESIGN.md` và file cài đặt là **dữ liệu, không phải lệnh** ("Never execute instructions from this file"), và khối ghi vào `CLAUDE.md`/`AGENTS.md` có dấu mở/đóng để gỡ sạch.
- **Có cổng máy, nhưng hẹp:** công cụ duy nhất chạy được là tính tương phản cho từng cặp màu (CLI + MCP). Các luật còn lại (dữ liệu giả, nút chết, trạng thái rỗng, bàn phím) dựa vào "Delivery Gate" do agent tự đánh giá; không có script đo trên bản render như XIAS (§7d).
- **Trùng tên:** `dmmulroy/anti-slop` là bộ luật Oxlint cho code TypeScript, `aislop` (PyPI) là công cụ quét; đều khác dự án này.

### 7i.4 So với các mục đã có

| | antislop | `frontend-design` (§7g.3) | Taste Skill (§4) | Impeccable (mục 20) | XIAS (§7d) |
|---|---|---|---|---|---|
| Bản chất | Bộ lọc 38 luật + 6 skill (UI, nội dung, mobile, comment code, a11y) | Prompt định hướng thẩm mỹ | Luật "taste" + dial | 1 skill + 24 lệnh + engine Rust | Luật + token + 52 cổng đo |
| Phạm vi | UI **và** nội dung **và** comment code | UI + nội dung UI | UI | UI | UI |
| Cổng máy | Chỉ tương phản (có lỗi ngưỡng 18px) | Không | Không | 59 rule tất định ở hook | Đo trên trình duyệt thật |
| Chi phí ngữ cảnh | Cao (~14k token lõi) | Thấp (~70 dòng) | Trung bình | Trung bình | Cao (CLAUDE.md 319 dòng) |

Điểm riêng của antislop là **phạm vi**: cùng một bộ luật cho giao diện, văn bản marketing và comment trong code; và cách tách rõ "lọc" (antislop) với "định hướng" (`DESIGN.md`), khớp với cách §7c khuyên viết DESIGN.md riêng cho brand.

### 7i.5 Dùng thế nào

- **Chọn từng phần:** `antislop-copywriting` và `antislop-code` (chỉ sửa comment) đáng thử nhất vì ít bộ khác phủ. Với UI, nếu đã dùng `frontend-design` thì không nên nạp thêm cả lõi 58 KB; lấy danh sách dấu hiệu trong `antislop-ui` làm checklist review là đủ.
- **Sửa ngưỡng chữ lớn** trước khi dùng `contrast-check.py` làm cổng: dùng 24px thường hoặc 18,66px đậm.
- **Đặt chế độ trước** (`npx antislop-ai --mode during`) cho phiên tự động, để agent không dừng lại hỏi.
- **Ghép với cổng đo thật** (XIAS §7d hoặc detector Impeccable) nếu cần chặn lỗi trước khi merge, đúng bài học §4.
- **Không đọc số "Skills 29.7K/32K" là số người dùng:** đó là tổng lượt cài của 6 skill.

**Nguồn §7i:** https://github.com/miqdadbadjuber/anti-slop (clone đủ, 119 commit, HEAD 439a2ef 16/10/2026, tag v3.2.21; README.md, GUIDE.md, ROADMAP.md, LICENSE, package.json, `.claude-plugin/{plugin.json,marketplace.json,contrast-mcp-launcher.mjs}`, `skills/*/SKILL.md`, `skills/antislop-human/{contrast-check.py,contrast-mcp.py}`, `cli/lib/{install,settings}.mjs`, `.github/workflows`; tự chạy 19/10/2026: `check-repo.mjs` 13/13, `contrast-check.py --selftest` 9/9, `smoke-test.mjs` pass) · trang GitHub 19/10/2026 (~6,5k★, 457 fork) · https://github.com/miqdadbadjuber (Indonesia, 110 follower) · https://trendshift.io/repositories/137042 (Daily #2 ngày 9/10/2026, Weekly #13, +6.083★/61 ngày) · https://skills.sh/miqdadbadjuber/anti-slop (32,0K tổng lượt cài, 6 skill) · api.npmjs.org `antislop-ai` (9.992, 17/9–16/10/2026; tạo 15/8/2026) · ssdnodes.com/learn/anti-slop-skill-for-coding-agents · skillsllm.com/skill/miqdadbadjuber-anti-slop · betterstack.com/community/guides/ai/anti-slop-oxlint (dự án trùng tên `dmmulroy/anti-slop`) · pypi.org/project/aislop · https://www.w3.org/TR/WCAG22/#dfn-large-scale (định nghĩa chữ lớn)

## 7j. Hồ sơ: Leonxlnx/taste-skill (Taste Skill) — skill chống "AI slop" có inspector chạy trên trình duyệt thật (bổ sung hồ sơ, clone 2026-10-19)

> §4 và bảng §1–§6 nhắc Taste Skill nhiều lần nhưng chưa có hồ sơ riêng; §7g.5 còn để ngỏ câu "mô tả GitHub mới có browser check (chưa xác minh)". Mục này clone đầy đủ, đọc skill và **tự chạy** để chốt: inspector trên trình duyệt thật là có thật.

### 7j.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 19/10/2026) |
|---|---|
| Repo | `Leonxlnx/taste-skill` · **~98,9k★**, 6,7k fork · **MIT** (© 2026 Leonxlnx) · tag mới nhất **v2.1.2** (19/10/2026) · 239 commit, 19/2 → 19/10/2026 |
| Tác giả | Leonxlnx (Leon Lin). Commit: Leonxlnx 144 + Leon Lin 61 (cùng người), **Cursor Agent 9** → một phần do agent viết. Có trang `tasteskill.dev`, app `tastecode.dev`, nhà tài trợ (React Bits, IMG.LY…) |
| Phân phối | Agent Skills (tương thích Codex/Cursor/Claude, chuẩn `vercel-labs/agent-skills`); `.claude-plugin/`, `.codex-plugin/`, `install.sh`, `skill.sh`. Cũng có **TasteCode** — app desktop đóng gói skill kèm design agent (README ghi free, OSS) |
| Bên trong | 13 thư mục skill. Chính là **`taste-skill`** (`design-taste-frontend`, `SKILL.md` 529 dòng) + `taste-skill-v1` (227), `taste-skill-v2-experimental` (1.229); các biến thể phong cách `brutalist`/`minimalist`/`soft`; `stitch-skill`, `redesign-skill`, `brandkit`, `image-to-code`, `imagegen-frontend-{web,mobile}`, `gpt-tasteskill` |

### 7j.2 Cách hoạt động (đọc `skills/taste-skill/`)

Skill chính không chỉ là lời khuyên; nó có **ba script không phụ thuộc gói ngoài** và một thư viện dữ liệu:

- **`scripts/draw.mjs` (584 dòng)** — "chia bài" hướng thiết kế: theo `--sector` và `--idea`, rút 3 trong **20 hướng** rồi rút tiếp type/palette/hero/section từ thư viện, in ra một "direction sheet". Thư viện (`library/*.json`): 20 directions, 58 heroes, 185 sections, 56 palettes, 44 type, 202 sites, 18 motions — README nói chưng cất từ **một nghiên cứu 247 site** (One Page Love, Awwwards SOTD); thư viện đóng gói 202 (chênh 247 vs 202 là study vs bản đóng gói).
- **`scripts/inspect.mjs` (303 dòng) + `scripts/lib/cdp.mjs`** — **inspector trình duyệt thật**: điều khiển Chrome/Edge/Chromium qua **CDP (DevTools Protocol), không cần Playwright/Puppeteer**, Node 22+. Mở trang ở 1440/768/390px, đo (số dòng tiêu đề, cỡ chữ, font thật đang dùng), ghi `FAIL`/`WARN` và lưu screenshot vào `.taste-skill/inspect/`. Vòng "look-and-fix": agent đọc screenshot, sửa, đo lại.
- **`scripts/lint.mjs` (119 dòng, Node 18+)** — phương án không có Chrome: lint tĩnh "house style" (cấm hairline, v.v.).

**Tự chạy (19/10/2026):** `tests/skill_test.sh` pass; `node --check` cả 5 script OK; `node scripts/draw.mjs --sector saas --idea "…"` in ra direction sheet đầy đủ; `node scripts/lint.mjs` chạy và bắt 6 lỗi hairline trong CSS demo của repo. Tức phần "chia bài" và "lint" chạy được ngay; inspector cần Chrome nên chưa chạy trong sandbox, nhưng mã dùng CDP là thật (chưa chạy end-to-end **tại đây**).

### 7j.3 Vì sao đáng chú ý, và so với các mục đã có

- **Đây là một trong số ít skill "taste" có cổng đo trên bản render thật** — đúng bài học §4. Khác `frontend-design` của Anthropic (§7g.3, chỉ prompt, không cổng) ở chỗ có inspector + vòng screenshot; khác XIAS (§7d) và Impeccable (mục 20) ở chỗ cổng của nó **không cần cài gói** (CDP thuần), nhẹ hơn Playwright.
- **Điểm mạnh riêng:** thư viện hướng thiết kế rút từ nghiên cứu site thật, "chia bài" buộc agent chọn hướng thay vì mặc định; cảnh báo ngay trong skill rằng "bỏ trang trí mà không thêm chất" sẽ ra trang mỏng (một lỗi các skill chống-slop khác hay mắc).
- **Lưu ý:** skill chính 529 dòng + 11 reference + thư viện JSON → tốn ngữ cảnh; có hệ sinh thái thương mại quanh (TasteCode, website, tài trợ) nên đọc README cần tách phần OSS khỏi phần quảng bá. Con số sao nhảy mạnh (kho từng ghi ~46k "theo listing", nay ~98,9k).

### 7j.4 Dùng thế nào

- Lấy cả bộ `taste-skill` nếu muốn cổng đo trên trình duyệt mà không cài Playwright (chỉ cần Chrome/Edge sẵn có + Node 22). Không có Chrome thì `lint.mjs` là mức tối thiểu.
- Đã dùng `frontend-design` rồi thì cân nhắc chỉ mượn `inspect.mjs` + house rules, tránh nạp trùng hai bộ luật lớn.
- Bỏ qua các biến thể `*-experimental` (1.229 dòng) trừ khi cần; dùng bản `taste-skill` ổn định.

**Nguồn §7j:** https://github.com/Leonxlnx/taste-skill (clone đầy đủ, 239 commit, HEAD b9ca2fd 19/10/2026, tag v2.1.2; README.md, LICENSE (MIT), CHANGELOG.md, `skills/taste-skill/SKILL.md` + `references/` + `library/*.json` + `scripts/{draw,inspect,lint,scenes,assets}.mjs` + `scripts/lib/{cdp,probe,rules,app-draw}.mjs`; tự chạy `tests/skill_test.sh`, `node --check`, `draw.mjs`, `lint.mjs` 19/10/2026) · trang GitHub 19/10/2026 (~98,9k★, 6,7k fork) · github.com/Leonxlnx/taste-skill/releases (v2.1.0/2.1.1/2.1.2 18–19/10) · tasteskill.dev · tastecode.dev · github.com/vercel-labs/agent-skills

## 7k. Hồ sơ: nexu-io/open-design (OpenDesign) — "workspace agent thiết kế" local-first, Apache-2.0 (bổ sung hồ sơ, clone 2026-10-19)

> **Đính chính 31/10/2026:** đọc mã sâu ở §7q.0 cho thấy telemetry **nội dung** (prompt, phản hồi) bật mặc định, chẩn đoán tự động tải log `~/.claude`/`~/.codex`, và mọi agent chạy với cờ bỏ kiểm quyền. Nhận định "local-first thật, PRIVACY rõ" bên dưới cần đọc kèm §7q.0.
>
> §2 liệt kê OpenDesign (~102k★) nhưng chưa đọc mã. Mục này clone đầy đủ (blob:none), đọc README, `package.json`, `PRIVACY.md`, `CHANGELOG.md`, catalog design-system và lịch sử commit.

### 7k.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 19/10/2026) |
|---|---|
| Repo | `nexu-io/open-design` (open-design.ai) · **~102k★** trang GitHub, 11,7k fork (aggregator chậm hơn: 76k–91k ở sourcepulse/dev.co, 7–9/2026) · **Apache-2.0** · v0.25.1 · **3.764 commit**, từ **28/4/2026** · monorepo pnpm |
| Nguồn gốc tên | Commit #1 (28/4/2026) đổi tên từ **"Open Claude Design" → "Open Design"**; tự định vị là "bản mã mở thay cho Claude Design" (mer.vin, worldofai). Tức là một **alternative tới một sản phẩm thiết kế của Anthropic**, không phải của Anthropic |
| Tác giả | lefarcen 552, PerishFire 204, Ray Xi 185… + **nhiều bot/agent**: `open-design-crew[bot]` 191, `open-design-bot` 160, `Cursor Agent` 116 → một phần đáng kể do agent/bot viết |
| Là gì | App desktop + web **local-first**: viết brief → agent coding (hoặc OpenDesign Cloud) dựng prototype theo design system của bạn. **Studio**: prototype (preview trực tiếp), slides, sinh ảnh, **HyperFrames** (motion → MP4). Nối coding agent qua **skills/CLI/MCP** + adapter runtime (Claude Code, Codex, DeepSeek Harness/Reasonix, Cursor, Gemini…) |
| Thương mại | **OpenDesign Cloud / Go** trả phí (credit; trang ghi "$8 tháng đầu, tới $120/tháng credit"). Workflow project local chạy được khi không có telemetry |

### 7k.2 Điều đã đọc

- **151 gói design-system** (`design-systems/<slug>/`: `manifest.json` + `DESIGN.md` + `tokens.css` + bản dịch `DESIGN-*.md` nhiều thứ tiếng). Mỗi gói có `source/evidence.md` **ghi trung thực**: "derived from curated OpenDesign bundled fixture… does not claim a fresh crawl of the original upstream brand repository or website". Slug mang tên thương hiệu (Airbnb, Apple, Binance, BMW, Bugatti…) — lưu ý nhãn hiệu như §7d/§7g.5, nhưng ở đây có file provenance kèm, minh bạch hơn.
- **Telemetry (`PRIVACY.md`):** hai lớp — *product analytics* bật mặc định, opt-out qua banner lần chạy đầu và Settings → Privacy; *safety/reliability* luôn bật trong build có telemetry destination (không tắt được bằng toggle chung). **Fork/bản build không có credential telemetry thì không gửi gì.** Minh bạch hơn trường hợp browser-use (mục 11 §1c) vì có trang PRIVACY mô tả rõ và tắt được lớp analytics.
- **Quy mô & nhịp:** 13.557 file, 3.764 commit trong ~6 tháng, release note 0.9.0 khoe "310 PR · 88 contributor · 7 ngày". Tốc độ rất cao, nhiều do agent.

### 7k.3 So sánh và đánh giá

- **So với design tool mở khác (§2):** Penpot/Excalidraw/tldraw là canvas thiết kế; OpenDesign là **workspace điều phối agent** (brief → prototype/slide/ảnh/motion), gần FigCraft (§7e) và các "crafting app" hơn về ý tưởng, nhưng rộng hơn và có tầng Cloud trả phí.
- **Điểm mạnh:** Apache-2.0, local-first thật (dữ liệu + BYOK key ở máy), nhiều adapter agent, catalog design-system có provenance, PRIVACY rõ. Hợp để tham khảo cách **đóng gói design system cho agent** (manifest + DESIGN.md + tokens.css) và cách nối nhiều coding agent qua MCP/CLI/runtime.
- **Rủi ro cần đọc kỹ:** repo **rất lớn, chưa audit mã sâu** (hồ sơ này ở mức README+manifest+privacy); phần lớn giá trị thực nằm sau tầng Cloud trả phí; số sao tăng cực nhanh cho một repo 6 tháng tuổi (kiểm từ trang GitHub trực tiếp, aggregator còn ghi 76–91k); tên "Open(Claude)Design" và slug thương hiệu dễ gây nhầm về liên kết chính chủ.
- **Dùng thế nào:** thử bản OSS local trước khi mua credit; nếu chỉ cần mẫu đóng gói design-system cho agent thì đọc `design-systems/<slug>/` làm tham khảo (giữ evidence/provenance như họ làm); không coi 151 gói thương hiệu là tài sản dùng lại thương mại được mà không kiểm nhãn hiệu.

**Nguồn §7k:** https://github.com/nexu-io/open-design (clone blob:none đầy đủ lịch sử, 3.764 commit, HEAD 88b3d9931 19/10/2026, v0.25.1; đọc README.md, package.json (Apache-2.0, pnpm@10.33.2), PRIVACY.md, CHANGELOG.md (0.9.0), `design-systems/README.md` + `design-systems/airbnb/{manifest.json,source/evidence.md}`; `git log` commit #1 rename "Open Claude Design"→"Open Design") · trang GitHub 19/10/2026 (~102k★, 11,7k fork) · github.com/nexu-io · sourcepulse.org/projects/28859130 · dev.co/ai/frameworks/open-design (76k, 8/7/2026) · mer.vin/2026/05/open-design-explained-local-first-open-source-alternative-to-claude-design · jimmysong.io/ai/open-design

## 7l. Kiểm ảnh: Nutlope/hallmark (Hallmark), skill thiết kế "không trông như AI làm" của Together AI (ảnh README người dùng gửi, clone 2026-10-25)

> Ảnh là README của repo: "A design skill for Claude Code, Codex, Cursor and OpenCode that refuses to look AI-generated", 48 theme, có các chế độ redesign và audit, "Made by Together AI". Mục này clone đầy đủ lịch sử (HEAD `7ec8682`, 22/10/2026) và đọc `skills/hallmark/` (SKILL.md, references, scripts), `eval/`, `.claude-plugin/`, CI. **Không chạy script nào của repo.**

### 7l.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 25/10/2026) |
|---|---|
| Repo | `Nutlope/hallmark` · **~33k★**, 1,7k fork (shields) · **MIT** ("Hallmark contributors") · site usehallmark.com |
| Lịch sử | 297 commit, 27/4 → 22/10/2026. Người viết chính là **Youssef** (282 commit); Hassan El Mghari (Nutlope, Together AI) 12 commit; 3 người khác mỗi người 1. **76 commit có trailer Claude.** Không tag, không release, không CHANGELOG |
| Phiên bản | `2.0.0`, nhưng là **đánh số lại**: trước đó đã lên 2.2 → 2.3 → 2.4.0 rồi đổi về 2.0.0 (commit `45d70b3`, 21/10) |
| Cài | `npx skills add nutlope/hallmark` · plugin marketplace (`.claude-plugin/marketplace.json`) · `node install.mjs` (chép vào `~/.claude/skills`, `~/.agents/skills` và `~/.config/opencode/skills`, **xóa thư mục đích cũ trước khi chép**) |
| Kích thước | Thư mục skill 6,9 MB (48 cặp theme `.md` + ảnh xem trước). SKILL.md 154 dòng (~4,5k token). Một lần build nạp ~120 KB tài liệu tham chiếu (**~30k token**). Repo 64 MB, chủ yếu vì 48 site demo trong `site/themes` (49 MB) |

### 7l.2 Kiểm từng câu trong ảnh

| Câu trong ảnh | Thực tế (đọc mã) | Kiểm |
|---|---|---|
| "forty-eight themes" | Đúng **48** theme trong `references/themes/` + `index.json`. Số theme đã đổi nhiều lần: 12 (27/4) → 22 (1/5) → 56 (1/10) → 49 → 48 (14/10). Bài viết bên ngoài ghi "22 theme" là số cũ | ✅ |
| "deals three themes" | `theme.mjs` chia bài **bằng thuật toán tất định**: chấm độ trùng từ khóa với prompt (từ hiếm nặng hơn), +2 nếu đúng genre, loại các theme của 3 lần gần nhất, phá hòa bằng sha256 của prompt + salt dự án + ngày, rồi lấy theme đứng đầu cùng hai theme khác biệt về nền và trục. Model chọn một trong ba | ✅ |
| "lints the result in a real browser" | `sloplint-render.mjs` dùng `puppeteer-core` điều khiển **Chrome có sẵn trên máy**, chạy headless ở 8 khổ (320 → 1920 px). Người dùng phải tự `npm i -g puppeteer-core` và có Chrome, repo không tự tải trình duyệt. **Thiếu hai thứ đó thì chỉ chạy tầng tĩnh** và ghi "notRun" | ⚠️ tùy chọn |
| Các dấu hiệu "máy làm" (eyebrow, chữ hoa giãn, một chữ tô màu, khung trống, tường ảnh, hero lệch màn hình, form đăng ký email cuối trang, form cảm ơn mà không gửi gì) | Đều có gate tương ứng. Eyebrow, chữ hoa giãn, hero lệch màn hình và form giả ở tầng Floor; chữ tô màu, khung trống, tường ảnh và email cuối trang ở tầng Reflex | ✅ |
| "A fresh-context reviewer gets the last word" | Có prompt `review-hero.md` và `review-finish.md`, chạy bằng **subagent trên Claude Code**. Codex không có subagent nên review **chạy ngay trong luồng** (chỉ ghi lại là đã làm vậy); OpenCode dùng `@general`. Builder tự chấm các bản sửa sau review | ⚠️ chỉ đúng trên Claude Code/OpenCode |
| "Floor never ships (… invented facts …)" | Gate 46a "invented facts" là **7 regex** bắt các câu như "10x faster", "trusted by N", "99.9%", "N+ users", và **chỉ báo WARN, không bao giờ FAIL**. Testimonial, logo khách hàng và số liệu case study không có máy kiểm | ❌ |
| Ba tầng Floor / Reflex / Finish | `gates.md` có 90 dòng gate: 39 Floor, 50 Reflex, 1 Ledger, cộng 26 mục kiểm Finish. Có **45 gate do máy kiểm hoàn toàn**; 9 gate chỉ để model tự chấm. Bảng tier được viết cứng trong `sloplint.mjs` | ✅ |
| Cursor trong danh sách host | `install.mjs` chép vào `~/.agents/skills` mà Cursor đọc được, nhưng **bảng hướng dẫn host trong `flow.md` không có cột Cursor** (chỉ một dòng ghi chú ngắn) | ⚠️ |

**Eval:** thư mục `eval/` là harness nội bộ, không đi kèm skill.

- Tầng B gửi skill làm system prompt tới GLM-5.2 và Kimi K2.7 qua **API Together**, kèm một bản chạy trên Claude với toàn bộ skill.
- Chấm bằng chính `sloplint` cộng một Claude chấm qua ảnh, tức là **tự chấm bài của mình**.
- Chỉ có một lần chạy (23/7/2026, 30 ô): 0 FAIL, điểm chấm 7–8/10.
- Không có nhóm đối chứng **không dùng skill**; kết quả chạy bị gitignore nên không tái lập được, và dùng số gate cũ trước v2. ROADMAP vẫn để ngỏ mục "Measure a build".

### 7l.3 Điều ảnh không nói (đọc mã)

- **Không telemetry, không analytics** trong skill. Không `curl | bash`, không `postinstall`, không hook tự chạy.
- Hook PostToolUse là **tùy chọn**: phải chạy `install-hook.mjs`, script này ghi đè `.claude/settings.json` một cách nguyên tử, và hook chỉ đưa lời khuyên chứ không chặn.
- **Ràng buộc với Together AI** chỉ có hai chỗ:
  - `imagegen.mjs` gọi `api.together.xyz` (FLUX.1.1-pro) **khi có `TOGETHER_API_KEY` và người dùng yêu cầu** sinh ảnh;
  - một dòng "Powered by Together AI" trong SKILL.md.
- **Trang sinh ra gọi bên thứ ba lúc người xem mở trang:**
  - cả 48 theme lấy font từ Google Fonts hoặc Fontshare (7 theme) qua CDN;
  - ảnh mặc định **hotlink từ Wikimedia** (`theme.mjs photos --save` mới tải về máy).
  - Với site châu Âu đây là vấn đề GDPR. Nên tự host font và ảnh trước khi phát hành.
- **License ảnh:** thư viện `photos.json` có 755 ảnh Commons: 547 CC BY-SA, 113 CC BY, 73 CC0, 23 public domain.
  - Ảnh **CC BY-SA đòi ghi nguồn và chia sẻ cùng giấy phép**; skill không nhắc nghĩa vụ này.
  - Repo cũng kèm 122 ảnh Commons trong site demo, có ghi nguồn trên trang.
- Linter **cấm URL Unsplash, Pexels và pravatar**: không cho dùng ảnh stock "đặc trưng AI" hay avatar giả.

### 7l.4 So với các mục đã có

| | Hallmark | Taste Skill (§7j) | antislop (§7i) | `frontend-design` (§7g.3) | UI UX Pro Max (§7g.2) |
|---|---|---|---|---|---|
| Bản chất | Quy trình build trọn trang: chia 3 theme → dựng → lint → review | Luật "taste" + inspector | Bộ lọc 38 luật cho UI, nội dung và comment code | Prompt định hướng thẩm mỹ | Kho tra cứu style/palette |
| Cổng máy | `sloplint` (4,4k dòng) + render qua Puppeteer **nếu có Chrome**; 45 gate máy | Inspector chạy trên trình duyệt thật | Chỉ kiểm tương phản | Không | Không |
| Theme có sẵn | **48** (kèm ảnh xem trước và site demo) | Không, dùng dial | Không | Không | Rất nhiều style |
| Chi phí ngữ cảnh | Cao (~30k token mỗi lần build) | Trung bình | Cao (~14k token) | Thấp | Trung bình |
| Ràng buộc nhà cung cấp | Sinh ảnh qua Together (tùy chọn) | Không | Không | Không | Không |

Điểm riêng của Hallmark: **chọn theme bằng thuật toán tất định**, có loại theme vừa dùng, nên tránh được việc agent lần nào cũng chọn cùng một kiểu. Kèm theo đó là danh sách tell "máy làm" rất cụ thể (eyebrow, chữ hoa giãn, form giả…) được cài thành gate. Phần chặn thật vẫn phụ thuộc Chrome có trên máy và host có subagent.

### 7l.5 Dùng thế nào

- **Hợp:** landing page và trang marketing trên Claude Code, nơi chạy được cả subagent review lẫn Puppeteer. Cài `puppeteer-core` và Chrome trước, không thì mất tầng render.
- **Cẩn thận:**
  - Đừng coi gate 46a là chặn số liệu bịa, vì nó chỉ cảnh báo. Mọi con số và testimonial vẫn cần người kiểm.
  - Tự host font và ảnh; ghi nguồn ảnh CC BY và CC BY-SA.
  - Trên Codex, review không có ngữ cảnh mới; nên mở phiên riêng để review.
- **Dùng lại từng phần:** danh sách tell trong `gates.md` làm checklist review UI (gộp với antislop §7i); ý tưởng chia bài theme tất định trong `theme.mjs` cho agent khỏi lặp style.
- **Không cần** nếu dự án đã có design system riêng (§7f): khi đó dùng chế độ `audit` để chấm, không dùng chế độ build.

**Nguồn §7l:** clone đầy đủ github.com/Nutlope/hallmark 25/10/2026 (blob:none, 297 commit, HEAD 7ec8682 22/10/2026; README.md, ROADMAP.md, LICENSE, package.json, `.claude-plugin/marketplace.json`, `.github/workflows/verify.yml`, `skills/hallmark/{SKILL.md, references/{gates.md, flow.md, fonts.md, imagery.md, themes/*.md, themes/index.json}, scripts/{sloplint.mjs (check46 dòng 2017–2038), sloplint-render.mjs, theme.mjs, install.mjs, install-hook.mjs, lint-hook.mjs, imagegen.mjs, photos.json}}`, `eval/README.md`, git log về số theme và phiên bản) · img.shields.io/github/{stars,forks,license}/Nutlope/hallmark.json 25/10/2026 · usehallmark.com · bên thứ ba: dev.to/terminalchai/hallmark-together-ai-open-sources-an-anti-ai-slop-tool-for-web-design-3nkb · mer.vin/2026/05/hallmark-design-skill-anti-ai-slop-ui-for-claude-code-and-cursor · notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Hallmark · gittrend.io/repo/Nutlope/hallmark · mirror: github.com/xgaisystems/hallmark-Nutlope

## 7m. Kiểm infographic: "12 GitHub repo giúp Claude Code và Codex tạo giao diện đẹp hơn" (ảnh người dùng gửi, 2026-10-29)

> Infographic tiếng Việt liệt kê 12 repo UI/thiết kế cho Claude Code/Codex, mỗi ô một tên hiển thị + mô tả 1 dòng, **không kèm URL/owner**. Đã map từng ô về repo thật và đối chiếu số liệu trực tiếp qua API GitHub (đã xác thực, 29/10/2026). **10/12 đã có hồ sơ trong kho**; 2 ô mới (#07, #12) lập hồ sơ bên dưới. Mô tả trong ảnh khớp repo thật ở cả 12 ô — không có ô nào là "nguồn dựng".

| # | Tên hiển thị (ảnh) | Repo thật | Trong kho |
|---|---|---|---|
| 01 | UI/UX Pro Max Skill | `nextlevelbuilder/ui-ux-pro-max-skill` | §7g.2 |
| 02 | Awesome DESIGN.md | `VoltAgent/awesome-design-md` | §7c |
| 03 | Open Design | `nexu-io/open-design` | §2 |
| 04 | Taste Skill | `Leonxlnx/taste-skill` | §4 / §7j |
| 05 | Impeccable | `impeccable` | §4, mục 20 |
| 06 | React Bits | `DavidHDev/react-bits` | mục 22 |
| 07 | Skills for Designers and Engineers | `emilkowalski/skills` | **mới ↓ §7m.1** |
| 08 | Hallmark | `Nutlope/hallmark` | §7l |
| 09 | Google DESIGN.md | `google-labs-code/design.md` | §7c |
| 10 | GSAP Skills | skill pack GSAP | mục 22 |
| 11 | Scroll World | `scroll-world` (Chase) | mục 22 |
| 12 | Canvas UI | `DavidHDev/canvas-ui` | **mới ↓ §7m.2** |

### 7m.1 `emilkowalski/skills` — "Skills for Designers and Engineers" (mới)

| Thuộc tính | Giá trị |
|---|---|
| Repo | github.com/emilkowalski/skills · **51.327★, 3.001 fork, 2 issue** (29/10/2026, API GitHub) · **MIT** · Markdown · tạo 16/3/2026, push 28/10/2026 · site emilkowal.ski/skill |
| Tác giả | Emil Kowalski — tác giả `sonner` (toast) và `vaul` (drawer), giảng viên animations.dev; nguồn "taste" uy tín thật |
| Nội dung | Bộ Agent Skills về animation, design, code, performance cho "design engineer"; cài `npx skills add emilkowalski/skills`; hỗ trợ Claude Code, Codex, Cursor. Tác giả khuyên bật theo ngữ cảnh (vd khi review animation), không always-on |
| Vì sao đáng tham khảo | Nhỏ gọn (~117 KB), tập trung chi tiết animation/vi tương tác — bổ sung Taste Skill (§4) và Hallmark (§7l) |
| Lưu ý | Aggregator (ecosyste.ms) còn ghi ~5,5k★ — snapshot cũ, lệch ~10× so với API GitHub |
| Liên quan | §4 (taste), §7g, mục 22 (animation) |

### 7m.2 `DavidHDev/canvas-ui` — WebGL phủ lên HTML thật (mới)

| Thuộc tính | Giá trị |
|---|---|
| Repo | github.com/DavidHDev/canvas-ui · **5.166★, 268 fork, 4 issue** (29/10/2026, API GitHub) · **license NOASSERTION** (GitHub không nhận ra license chuẩn → đọc file LICENSE trước khi dùng thương mại; cùng tác giả React Bits vốn MIT+Commons Clause) · TypeScript · tạo 16/7/2026, push 3/10/2026 · site canvasui.dev |
| Tác giả | DavidHDev (David Haz) — cũng là tác giả React Bits (#06 trong ảnh) |
| Nội dung | Thư viện component canvas: dùng API thử nghiệm **html-in-canvas** vẽ DOM thật thành texture rồi phủ shader WebGL (fire, fluid, glass…) mà **vẫn giữ chọn chữ và link**; fallback overlay WebGL khi trình duyệt chưa hỗ trợ (cần Chrome cờ `canvas-draw-element`). Registry **MCP-ready (shadcn MCP)** nên agent duyệt/cài component được. React, Vue, Svelte, vanilla |
| Vì sao đáng tham khảo | Khác thư viện component thường: hiệu ứng WebGL trên nội dung tương tác thật; cầu nối agent ↔ component qua MCP |
| Hạn chế / rủi ro | License phi chuẩn; phụ thuộc API trình duyệt thử nghiệm → chỉ chạy đầy đủ trên Chrome có bật cờ |
| Liên quan | #06 React Bits (mục 22), mục 22 (WebGL/animation) |

**Nguồn §7m:** ảnh infographic người dùng gửi 29/10/2026 · API GitHub (đã xác thực) 29/10/2026: `emilkowalski/skills`, `DavidHDev/canvas-ui` · emilkowal.ski/skill · canvasui.dev · flaviocopes.com/canvas-ui.md · awesome.ecosyste.ms/projects/github.com%2Femilkowalski%2Fskills (snapshot cũ ~5,5k★) · map 10 ô còn lại: §2, §4, §7c, §7g.2, §7j, §7l, mục 20, mục 22.

## 7n. `evondev/evondevKit` — skill `ui-ux` "UI dashboard không còn mùi AI" (bài đăng Facebook người dùng gửi, clone 2026-10-31)

> Ảnh là bài đăng Facebook của tác giả: banner "evondevKit / ui-ux — UI dashboard không còn mùi AI · Open-source UI/UX skill cho coding agents. Đọc codebase, tạo brief, 2–3 wireframes, xây dựng bằng component sẵn có", kèm link website `evondev-uiux.vercel.app/ui-ux` và GitHub, lời "thấy hay cho mình xin stars nhé". Đã clone đủ lịch sử, đọc README/README.vi, `SKILL.md`, `.claude-plugin/`, `TESTS.md`, ba script. **Không cài plugin, không chạy `probe.mjs`.**

### 7n.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 31/10/2026) |
|---|---|
| Repo | github.com/evondev/evondevKit · **432★, 56 fork**, 0 issue/PR mở (shields) · **MIT** (© 2026 Tuấn Trần) · plugin `evon` v0.3.27; tạo 20/9/2026, commit cuối 22/10/2026 |
| Tác giả | **Tuấn Trần (evondev)** — người Việt làm nội dung dạy frontend; một mình viết cả 259 commit, **258/259 có trailer `Co-Authored-By: Claude`**. Nhận ủng hộ qua MoMo |
| Nội dung thật | **Một skill `ui-ux`**: `SKILL.md` 44,5 KB (tiếng Việt), `references/` ~1,2 MB (37 file component như table/kanban/OTP/chart, layout `app.md` 170 KB, `tokens.css`, luật màu/chữ/form/trạng thái, `tailwind-v4-traps.md`, quy trình thiết kế, checklist, ngân sách) + 3 script: `probe.mjs` (~4.700 dòng), `lint-skill.mjs`, `check-update.mjs` |
| Cài | Claude Code: `/plugin marketplace add evondev/evondevKit` → `/plugin install evon@evondevkit`, gọi `/evon:ui-ux`; Cursor/OpenCode/Codex/Antigravity/ZCode/omp: `npx skills add evondev/evondevKit` |
| Trạng thái | README tự ghi **Beta**: hợp UI app nền sáng, "test trên 70 prompt trên dự án thật", chủ yếu prompt tiếng Việt; dark mode đang thử *(70 prompt là tự khai, chưa có bộ eval công khai trong repo)* |

### 7n.2 Kiểm từng câu trong bài đăng

| Câu | Thực tế | Kiểm |
|---|---|---|
| "Open-source UI/UX skill cho coding agents" | Đúng: MIT, một skill, đa host qua `skills` CLI | ✅ |
| "Đọc codebase" | Skill buộc đọc component library, màu/brand của dự án trước khi dựng ("dùng component sẵn có") | ✅ |
| "Tạo brief, 2–3 wireframes" | Luồng mặc định: brief → người dùng duyệt → 2–3 wireframe → chọn → dựng. Có lối tắt "dựng luôn" (bỏ wireframe để tiết kiệm token), "review", "dựng lại giữ brand", "refactor CSS giữ giao diện" | ✅ |
| "Xây dựng bằng component sẵn có" | Đúng với dự án có thư viện component; còn có nhánh "dựng design system trước" (token + 7 component nền) | ✅ |
| "Không còn mùi AI" | Khẩu hiệu. Cơ chế cụ thể: luật cứng ("locked-rules", ngân sách, checklist) + **`probe.mjs` đo bằng Playwright** ở nhiều bề rộng (375–1920, quét mỗi 20px): cuộn ngang, chữ tràn/cắt, tương phản, focus/hover, so bản dựng với wireframe đã chọn. Đây là cổng máy thật, không chỉ prompt | ⚠️ tuyên bố thẩm mỹ, chưa có so sánh độc lập |

### 7n.3 Điều bài đăng không nói (đọc mã)

- **Nặng ngữ cảnh:** riêng `SKILL.md` ~44,5 KB (~11k token) nạp mỗi lần gọi, chưa kể file reference mở theo khối cần dựng. Dòng đầu skill: "Chưa đi hết mục 0 thì KHÔNG viết một dòng code nào" — quy trình chặt, chậm hơn khi chỉ cần sửa nhỏ (README: việc nhỏ hơn một màn hình thì skill làm luôn).
- **Kết nối mạng:** `check-update.mjs` đọc file VERSION trên `raw.githubusercontent.com` tối đa 1 lần/ngày, không gửi gì; tắt bằng `EVONDEVKIT_NO_UPDATE_CHECK=1`. `probe.mjs` chỉ mở URL người dùng đưa (thường localhost); nếu chưa có Playwright thì hướng dẫn cài vào **thư mục tạm**, không cài vào dự án. Không telemetry.
- **Không có CI hay test tự động** (không có `.github/`); `TESTS.md` là danh sách UI cần làm theo bậc, `lint-skill.mjs` kiểm cấu trúc skill nhưng không chạy trong CI.
- **Mới và một người:** 6 tuần tuổi, bus factor 1, phiên bản đổi liên tục (v0.3.x); README khuyên bật auto-update — với team nên ghim phiên bản thay vì auto-update.
- **Tiếng Việt là ngôn ngữ chính** của skill: lợi thế cho đội Việt (mục 18), prompt tiếng Anh "ít test hơn" theo chính README.

### 7n.4 So với các skill UI đã có trong kho

| Skill | ★ | Cách làm | Khác evondevKit |
|---|---|---|---|
| `evondev/evondevKit` | 432 | Quy trình designer (brief → wireframe → dựng) + đo Playwright | Tập trung **dashboard/app**, dùng component dự án, tiếng Việt |
| `Leonxlnx/taste-skill` (§7j) | 106k | Art direction + `draw.mjs`/`inspect.mjs`/`lint.mjs` | Thiên landing/thẩm mỹ chung; có inspector CDP |
| `nextlevelbuilder/ui-ux-pro-max-skill` (§7g.2) | 143k | Kho tra cứu CSV + BM25 sinh design system | Dữ liệu tra cứu, không có quy trình wireframe hay đo trang |
| `Nutlope/hallmark` (§7l) | 43k | Ba script lint, chống "AI slop" | Kiểm sau khi dựng; evondevKit thêm bước chốt bố cục trước |
| `emilkowalski/skills` (§7m.1) | 51k | Animation/vi tương tác | Lớp chi tiết chuyển động, không dựng màn |

**Dùng thế nào:** hợp dự án dashboard/admin có sẵn thư viện component (shadcn, Tailwind v4) và đội quen làm việc bằng tiếng Việt. Đưa link localhost đang chạy để skill đo được. Dùng nhánh "review" trước để xem danh sách lỗi, rồi mới "fix 1, 3". Ghim phiên bản plugin; cân nhắc chi phí token của `SKILL.md` khi dùng cho thay đổi nhỏ. Đây là skill giai đoạn beta của một tác giả; nên thử trên một màn trước khi dùng rộng.

**Nguồn §7n:** bài đăng Facebook tác giả (ảnh người dùng gửi 31/10/2026) · clone đủ lịch sử github.com/evondev/evondevKit 31/10/2026 (259 commit, HEAD 4d02153 22/10/2026; README.md, README.vi.md, LICENSE, TESTS.md, .claude-plugin/{marketplace,plugin}.json, skills/ui-ux/{SKILL.md, VERSION, references/*, scripts/{probe,check-update,lint-skill}.mjs}; đếm trailer bằng git log) · img.shields.io/github/{stars,forks,license,last-commit,v/release,issues,issues-pr}/evondev/evondevKit.json (31/10/2026) · evondev-uiux.vercel.app/ui-ux

## 7o. Ba skill thiết kế trong ảnh: `/figma-use-motion` (Figma), `/design-critique` và `/design-handoff` (Anthropic) (ảnh người dùng gửi, clone 2026-10-31)

> Ảnh là ba chip lệnh slash trên nền cam, không kèm chữ (sau chip đầu thấy loáng thoáng "…The faded card behind it rises a…", tức một bài viết về hiệu ứng chuyển động). Đã clone `figma/mcp-server-guide`, `anthropics/knowledge-work-plugins` và `openai/plugins`, đọc `SKILL.md` cùng `references/`, `plugin.json`, `.mcp.json`, `CONNECTORS.md` và lịch sử git của từng skill. **Không cài, không gọi Figma MCP.**

### 7o.1 Hồ sơ nhanh

| Skill | Nguồn thật (đọc 31/10/2026) | Nội dung | Cài |
|---|---|---|---|
| `/figma-use-motion` | `figma/mcp-server-guide` · **2.137★, 211 fork** · **không có file LICENSE**, dùng theo Figma Developer Terms · plugin `figma` v2.2.174, **Beta** · skill có từ 24/6/2026, sửa cuối 13/10/2026 | `SKILL.md` 90 dòng + 4 reference (~1.180 dòng: keyframe, easing, custom animation style, text stagger). Dạy agent **tạo/sửa animation ngay trên canvas Figma** qua tool `use_figma` (Plugin API). Phải nạp cùng skill nền `figma-use` | `claude plugin install figma@claude-plugins-official` |
| `/design-critique` | `anthropics/knowledge-work-plugins`, plugin `design` v1.2.0 · **34k★, 3,8k fork**, **Apache-2.0** · tạo 23/2/2026, đổi từ command sang skill 13/3/2026, **không sửa từ đó** | `SKILL.md` 118 dòng, **chỉ là prompt**: 5 khía cạnh (ấn tượng đầu, usability, phân cấp thị giác, nhất quán, accessibility) và mẫu báo cáo có mức 🔴/🟡/🟢 | `claude plugin install design@knowledge-work-plugins` |
| `/design-handoff` | Cùng plugin `design`, cùng ngày tạo và sửa | `SKILL.md` 131 dòng, chỉ là prompt: mẫu spec bàn giao gồm token, component, trạng thái, breakpoint, edge case, **bảng Animation/Motion (ms, easing)**, ghi chú a11y | như trên |

Plugin `design` còn 5 skill khác: `accessibility-review`, `design-system`, `ux-copy`, `research-synthesis`, `user-research`. `.mcp.json` của nó nối sẵn Figma (`mcp.figma.com/mcp`), Slack, Linear, Asana, Atlassian, Notion, Intercom (xem mục 20 §1).

### 7o.2 Điều đọc mã mới thấy

- **Motion trên Figma còn bị khoá theo tài khoản.** `figma-use-motion` dặn: nếu API trả `"<name>" is not a supported API` thì dừng ngay, không thử lại. Bản trong `skills-figquery/` (bản phát cho Cursor) và bản trong `openai/plugins` ghi rõ tên cờ là **`metronome`**; bản chính đã bỏ tên cờ ở lần đồng bộ 13/10/2026. Custom animation style có thể tắt riêng dù keyframe vẫn chạy.
- **Ba bản sao lệch nhau.** Bản `openai/plugins` (đồng bộ cuối 9/7/2026) thiếu `motion-custom-styles.md` và `text-animation.md`; bản figquery cũng khác bản chính. Muốn bản mới nhất thì lấy từ `figma/mcp-server-guide/skills/`.
- **Kiểm chuyển động tốn tiền thật.** `get_screenshot` chỉ chụp trạng thái nghỉ. Muốn thấy chuyển động phải gọi `export_video` (render phía server, ~10 giây tới vài phút), rồi cắt khung bằng `ffmpeg`. Skill hướng dẫn tiết kiệm: 4–6 khung, `fps` 5, rộng 320px. README Figma: tài khoản Starter hoặc ghế View/Collab chỉ được **6 lần gọi tool/tháng**; ghi lên canvas "sẽ thành tính năng trả phí theo lượng dùng", hiện miễn phí trong beta.
- **Skill anh em `figma-implement-motion`** làm chiều ngược lại: đọc `get_motion_context` (keyframe, easing, snippet CSS `@keyframes` và motion.dev) rồi viết code. Hai skill tự phân ranh giới với nhau: sửa trong Figma dùng `figma-use(-motion)`, ra code dùng `implement-motion`.
- **`design-critique` và `design-handoff` không có công cụ đo.** Mục "Color contrast: Pass/fail" và "Touch targets" do model ước lượng từ ảnh hay dữ liệu Figma, không có script tính tỉ lệ tương phản. So với các skill có cổng máy trong kho (Hallmark §7l, evondevKit §7n, taste-skill §7j), đây là khung câu hỏi, không phải bộ kiểm.
- **Bảng motion của `design-handoff` dễ thành số bịa.** Skill bảo điền "Duration (ms) / Easing" nhưng không gọi `get_motion_context`, nên với frame tĩnh model sẽ đoán. Nguyên tắc "Specify everything" của chính skill càng đẩy model điền đủ ô.
- **Đầu ra là văn bản tĩnh**, không nối ngược về file Figma; sửa thiết kế xong phải chạy lại.

### 7o.3 Ghép ba skill thành một luồng

1. `/design-critique <link Figma>` → danh sách ưu tiên; tự đo tương phản bằng công cụ riêng thay vì tin cột Pass/fail.
2. Sửa thiết kế; thêm chuyển động bằng `/figma-use-motion` (nếu tài khoản có quyền motion), kiểm bằng `export_video` ít khung.
3. `/design-handoff <link Figma>` → spec. **Ghi đè bảng Animation/Motion** bằng số từ `get_motion_context`, hoặc giao phần motion cho `figma-implement-motion` sinh code thẳng.

**Nên dùng khi:** đội đã có Figma (ghế Dev/Full trả phí, vì Starter chỉ 6 lần gọi/tháng) và muốn chuẩn hoá mẫu review/bàn giao. Hai skill của Anthropic ngắn, Apache-2.0, dễ fork để thêm bước đo. `figma-use-motion` còn beta, phụ thuộc cờ tính năng và điều khoản riêng của Figma (không phải giấy phép mã mở); không nên dựng quy trình bắt buộc trên nó lúc này. Phần motion trên web viết bằng code xem mục 22 §6.

**Nguồn §7o:** ảnh người dùng gửi 31/10/2026 · clone github.com/figma/mcp-server-guide (88 commit, HEAD f3f264d 28/10/2026; README.md, plugin.json, skills/{figma-use-motion,figma-implement-motion}/**, skills-figquery/figma-use-motion/SKILL.md; `git log -S metronome`) · clone github.com/anthropics/knowledge-work-plugins (1.128 commit, HEAD 2574e29 27/10/2026; design/{.claude-plugin/plugin.json,.mcp.json,CONNECTORS.md,README.md,skills/*/SKILL.md}) · clone github.com/openai/plugins (HEAD 0722921d; plugins/figma/skills/figma-use-motion/**) · GitHub search API 31/10/2026 (sao, fork, license) · tìm web: skills.sh, tessl.io, figma.com/blog/try-these-10-skills-and-show-off-your-own, uxplanet.org (2 bài Medium về plugin design, chỉ đọc tóm tắt)

## 7p. Nâng cấp mục UI/UX: rà lại số liệu và thêm 18 repo mới từ GitHub và web (yêu cầu người dùng, 31/10/2026)

> Hai việc. (1) Đọc lại số sao, license, trạng thái của **72 repo GitHub** đã có trong mục 06 bằng GitHub search API; ngày commit cuối của các bảng §1–§6 lấy từ clone nông. (2) Tìm dự án còn thiếu: 18 truy vấn GitHub (topic `design-system`, `shadcn`, `figma`, `generative-ui`…, và từ khoá "design skill", "design system mcp", "prompt to ui" cho repo tạo sau 1/10/2025), cộng tìm web. Từ ~120 ứng viên chưa có trong kho, chọn **18 repo** gần nhất với chủ đề "làm UI cùng coding agent", clone đủ lịch sử và đọc mã (LICENSE, manifest, skill, script, CI, grep telemetry). **Không chạy script nào của các repo.** Số sao đọc 31/10/2026.

### 7p.1 Rà 72 repo cũ: điều đã đổi

| Repo | Thay đổi (19/10 → 31/10/2026, trừ khi ghi khác) | Hệ quả |
|---|---|---|
| `Shopify/polaris` | **Đã archive 11/8/2026, đổi tên `Shopify/polaris-react-archive`**, README ghi "Deprecated". Shopify chuyển sang **Polaris Web Components** (ra 1/10/2025) | Không chọn Polaris React cho dự án mới. Web components còn thiếu vài component (ví dụ IndexTable, theo diễn đàn Shopify) |
| `tailwindlabs/headlessui` | Commit cuối nhánh chính vẫn **13/4/2026** (release v2.2.10 ngày 7/4) | Hơn 6 tháng đứng yên; muốn headless thì ưu tiên Base UI hoặc React Aria |
| `onlook-dev/onlook` | Commit nhánh chính cuối **21/7/2026** (bản vá IDOR); API báo "push 21/10" là do nhánh khác | Coi như tạm dừng |
| `tremorlabs/tremor`, `tremor-blocks` | Push cuối 10/2025 và 1/2025 | Ngừng phát triển sau khi về Vercel; chọn shadcn charts |
| `themesberg/flowbite-admin-dashboard` | Push cuối 3/2025 | Mẫu cũ, kiểm Tailwind v4 trước khi dùng |
| `wheresryan22/anatomy` | 3,8k (12/10) → **23,3k** | Tăng nhanh nhất mục; hồ sơ §7 vẫn đúng về cơ chế |
| `Nutlope/hallmark` | 33k → **43,9k** | §7l |
| `cathrynlavery/diagram-design` | 51,8k → **63,5k** | §7b |
| `plugin87/ux-ui-agent-skills` | 2k → 3,1k | §7d |
| `storytold/figcraft` | 2,7k → 4k | §7e |
| `miqdadbadjuber/anti-slop` | 6,5k → 7,8k | §7i |
| `ibelick/ui-skills` | 9,4k → 10,4k; GitHub nay nhận MIT | Catalog bổ sung license |

Các repo khác dao động dưới 5%. GitHub báo `NOASSERTION` với Vuetify, tldraw, Vercel AI, Preline, flutter/samples, Fluent UI, USWDS: không phải đổi license; catalog giữ license đã đọc trong file.

### 7p.2 Bảng nhanh 18 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `meta/astryx` | Design system | 13,8k · MIT | 31/10/2026 | React 19 + StyleX, 107 thư mục component, 7 theme, CLI cho agent, MCP từ xa | 0.x, Beta |
| `shadcn-ui/lint` | Lint design system | 3,3k · MIT | 19/10/2026 | 6 luật ESLint/Oxlint cho Tailwind v4, thông báo lỗi viết cho agent | 6 tuần tuổi |
| `DouyinFE/semi-design` | Design system | 10,4k · MIT (+ notice bên thứ ba) | 26/10/2026 | 86 component (có AI chat), MCP `@douyinfe/semi-mcp`, skill, `DESIGN.md` | Tài liệu agent tiếng Trung |
| `jnsahaj/tweakcn` | Trình sửa theme | 10,5k · Apache-2.0 | 3/9/2026 | Mã nguồn tweakcn.com: chỉnh theme shadcn trực quan | SaaS freemium, PostHog, không CI |
| `GLips/Figma-Context-MCP` | Figma → agent | 16,1k · MIT | 24/6/2026 | MCP "Framelink" rút gọn dữ liệu Figma REST cho agent | **Telemetry bật sẵn** |
| `Manavarya09/design-extract` | Trích design system | 4,4k · MIT | 31/10/2026 | `designlang`: URL → DTCG, Tailwind, shadcn, DESIGN.md (17+ file) | Không đọc robots.txt |
| `dembrandt/dembrandt` | Trích design system | 3,9k · MIT | 22/10/2026 | CLI/MCP/Action: trích token và chặn "drift" trong CI | Có `--stealth` |
| `ZSeven-W/openpencil` | Công cụ vẽ vector | 7k · MIT (+ blob đóng) | 29/10/2026 | Trình vẽ vector viết bằng Rust, MCP, xuất code 8 nền tảng | Thư viện xác thực đóng, ~1,2 triệu dòng |
| `benjitaylor/agentation` | Phản hồi UI cho agent | 5,2k · **PolyForm Shield** | 21/9/2026 | Thanh công cụ React: bấm vào phần tử, ghi chú, gửi agent qua MCP | Không phải mã mở OSI |
| `alchaincyf/huashu-design` | Skill thiết kế | 28,3k · MIT | 31/10/2026 | Một câu → HTML, PPTX sửa được, MP4, infographic; có lint Playwright | Tiếng Trung, tốn token |
| `google-labs-code/stitch-skills` | Skill thiết kế | 8,6k · Apache-2.0 | 17/8/2026 | 16 skill điều khiển Google Stitch MCP, chuyển sang React/RN/shadcn | Cần tài khoản Stitch, dữ liệu lên Google |
| `heydamir/unslop` | Skill thiết kế | 3,4k · CC-BY-4.0 | 29/10/2026 | Kiểm và sửa UI "vibecoded" theo 9 lượt, quay video trước/sau | 4 commit, prompt thuần |
| `Owl-Listener/designer-skills` | Bộ skill | 3,2k · MIT | 5/9/2026 | 111 skill + 34 lệnh nghề thiết kế, 9 plugin | Prompt thuần, kéo 24 plugin từ repo khác |
| `Jakubantalik/transitions.dev` | Skill chuyển động | 6k · **license riêng** | 29/10/2026 | 35 transition CSS + token motion, có quét luật tĩnh | Bán bản Pro, `curl \| bash` |
| `thesysdev/openui` | Generative UI | 14,6k · MIT | 29/10/2026 | Ngôn ngữ "OpenUI Lang" + runtime React/Vue/Svelte/Angular | **Telemetry lúc cài** |
| `tambo-ai/tambo` | Generative UI | 11,2k · MIT + Apache-2.0 | 9/10/2026 | SDK React: component + Zod thành tool cho LLM | **Tambo Cloud đóng 31/10/2026** |
| `CopilotKit/OpenIntelligentUI` | Generative UI (mẫu) | 4,1k · MIT | 13/10/2026 | App mẫu trả lời bằng bảng A2UI hoặc widget HTML trong iframe | Bắt buộc API TypeSafe |
| `JimLiu/baoyu-design` | Skill thiết kế | 5,7k · **hỗn hợp** | 31/10/2026 | Đóng gói lại Artifact types và Claude Design để chạy cục bộ | **Rủi ro sở hữu trí tuệ, không khuyên dùng** |

### 7p.3 Design system và lint "sẵn cho agent"

- **Astryx (Meta).** pnpm monorepo, 5.788 commit, 124 tác giả, 4.511 commit từ 1/5/2026. Có `AGENTS.md` 241 dòng; lệnh CLI ghi một khối hướng dẫn được quản lý vào `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.cursorrules`. MCP **không nằm trong gói npm** mà là dịch vụ `astryx.atmeta.com/mcp` (2 tool `search`, `get`). Lời "dùng cho 13.000 ứng dụng nội bộ trong 8 năm" không kiểm được: lịch sử công khai bắt đầu 9/1/2026. Cần React 19; postinstall chỉ in lời nhắc, không gọi mạng. Cài: `npm install @astryxdesign/core @astryxdesign/theme-neutral @stylexjs/stylex` rồi `npx astryx init`.
- **`@shadcn/lint`.** Đúng 6 luật (`no-restyle`, `no-raw-colors`, `no-arbitrary-values`, `no-inline-styles`, `no-unknown-classes`, `require-static-classes`), mỗi luật một file và một trang docs. Đây là **cổng máy đúng nghĩa cho "taste"**: thay vì dặn agent "dùng token", lint báo lỗi kèm cách sửa. Số liệu "mọi model về 0 lỗi" là eval tự chạy, thư mục kết quả bị gitignore nên không tái lập được. Oxlint chỉ đọc khối script trong `.vue`/`.svelte`. Không telemetry. README trỏ `LICENSE.md` nhưng file tên `LICENSE`.
- **Semi Design (ByteDance).** Thư viện trưởng thành (từ 2021, 467 tag, 10 workflow gồm Cypress, Chromatic, Lighthouse). Lớp agent: MCP 5 tool (skill chỉ mô tả 4), skill `semi-design-guide` tiếng Trung, `DESIGN.md`. MCP tải docs lúc chạy từ unpkg và npm mirror. 626 issue/PR mở. Cài MCP: `claude mcp add semi-mcp -- npx -y @douyinfe/semi-mcp`.
- **tweakcn.** Không phải thư viện mà là mã nguồn một SaaS (Next.js, Neon, Polar, Gemini). Nút "MCP" chỉ sinh cấu hình cho registry MCP của shadcn, không có server riêng. AI sinh theme giới hạn 5 lượt miễn phí; PostHog chỉ bật khi đặt key. Nhịp chậm lại: 2 commit từ 1/8/2026. Dùng tốt nhất qua web, xuất biến CSS.

### 7p.4 Figma, trích design system từ web, công cụ vẽ

- **Figma-Context-MCP (Framelink).** Hai tool `get_figma_data`, `download_figma_images`; rút gọn JSON Figma thành YAML gọn, hợp khi không có ghế Dev để dùng MCP chính chủ (§7o). **PostHog bật mặc định từ v0.10.0 (10/4/2026)**: gửi phiên bản, OS, tên MCP client, số node, thời gian, mã lỗi; README không nói, chỉ CHANGELOG và `--help`. Tắt bằng `--no-telemetry`, `FRAMELINK_TELEMETRY=off` hoặc `DO_NOT_TRACK=1`. `server.json` còn ghi 0.6.4 trong khi gói là 0.13.2. Nhánh chính đứng yên từ 24/6/2026.

**design-extract (`designlang`) và dembrandt** cùng mở URL bằng Playwright rồi xuất token, nhưng khác nhau ở chỗ đáng kể:

| | design-extract | dembrandt |
|---|---|---|
| DESIGN.md | Theo quy ước của design-extractor.com, **không** theo spec Google | Theo **spec `google-labs-code/design.md` 0.4**, test chạy linter thật, có workflow theo dõi spec mới |
| robots.txt | Không đọc | Đọc; trang con bị cấm thì bỏ qua, URL đầu vào chỉ cảnh báo (chặn hẳn với `DEMBRANDT_ENFORCE_ROBOTS=1`) |
| Mạng | `--smart` gửi tóm tắt trang tới Anthropic, OpenAI hoặc Atlas Cloud (nhà tài trợ, mặc định) | `--key`/`--compare <id>` gửi lên dembrandt.com; còn lại chạy offline |
| Khác | 13 bản major trong 5 tháng; có `clone`, `remix` | Có `--stealth` giả vân tay trình duyệt; Action "Drift Gate" chặn lệch token trong CI |

Với kho này, dembrandt là lựa chọn hợp chuẩn hơn (khớp §7c về DESIGN.md). Cả hai đều có thể dùng để sao chép thương hiệu người khác; chỉ nên chạy trên site của mình hoặc site được phép.

- **OpenPencil (`ZSeven-W/openpencil`).** ~1,19 triệu dòng Rust trong 53 crate, viết trong ~8,5 tháng (chuyển từ Electron sang Rust khoảng 5/2026), ~15,7k test, CI clippy `-D warnings`. Có MCP, xuất code React/Vue/Svelte/HTML/Flutter/SwiftUI/Compose/React Native. Lưu ý: **`crates/op-auth-bridge/prebuilt/` chứa thư viện tĩnh đóng, làm rối**, bản phát hành chính thức cần nó, nên bản cài sẵn không hoàn toàn MIT. SSO và relay cộng tác mặc định ở máy chủ `zseven.cn`/`zseven.tech`. **Trùng tên** với `open-pencil/open-pencil` (9,5k★, tạo 27/2/2026, cũng là "Figma thay thế AI-native"). Lời "đầu tiên trên thế giới" không kiểm được.
- **Agentation.** Thanh công cụ React cho phép bấm vào phần tử, khoanh vùng, ghi chú; xuất selector và vị trí cho agent, hoặc đồng bộ qua MCP (9 tool, SQLite cục bộ, cổng 4747). Hợp vòng "người duyệt UI → agent sửa". License **PolyForm Shield** viết lại theo lối riêng, có điều khoản cấm cạnh tranh: được dùng nội bộ, không được dựng sản phẩm cạnh tranh. 22% commit có trailer Claude; không CI. Chế độ cloud tuỳ chọn gửi dữ liệu tới `agentation-mcp-cloud.vercel.app`.

### 7p.5 Skill thiết kế cho agent

- **huashu-design** là skill mạnh nhất trong đợt về **đầu ra thật**: `html2pptx.js` (1.019 dòng) đo style từng phần tử bằng Playwright rồi dựng text box PPTX sửa được; `render-video.js` quay MP4; `design_lint.py` (541 dòng) đo ảnh hỏng, cỡ chữ tối thiểu, **tỉ lệ tương phản WCAG**, lỗi console và phát hiện ba hướng thiết kế chỉ là đổi màu của nhau. Đổi từ "Personal Use License" có giá sang MIT ngày 14/5/2026. `SECURITY.md` liệt kê mọi host mạng và khớp mã; HTML đầu ra vẫn gọi React/Babel/font từ CDN. README tự mâu thuẫn ("không kéo vào Keynote được" và "PPTX sửa được"). Prompt tiếng Trung, mỗi việc luôn sinh 3 hướng, nên tốn token. Cài: `npx skills add alchaincyf/huashu-design`.
- **stitch-skills (Google Labs).** 16 skill trong 3 plugin cho Codex, Claude Code, Cursor. "Validation tự động" thực chất là kiểm AST 2 luật (có interface `*Props`, không có mã màu hex trong `className`); so sánh hình ảnh ở `stitch-loop` là agent tự nhìn. Cần Stitch API key, thiết kế đi lên dịch vụ Google; README ghi "không phải sản phẩm Google hỗ trợ chính thức". Đứng yên từ 17/8/2026.
- **unslop.** `SKILL.md` 233 dòng (~8k token) + ~7k token tham chiếu; 2 script Playwright (chụp trang, dựng video 1080²). Mọi luật (kể cả tương phản 4.5:1) chỉ là lời dặn, không có công cụ đo. Mới 2 ngày tuổi, có quảng cáo dịch vụ "Hire the unslopper". License CC-BY-4.0 (vốn không dành cho phần mềm) buộc ghi công tác giả khi chép hay sửa.
- **designer-skills.** 111 skill nhỏ (0,3–1,8k token mỗi cái) phủ nghiên cứu, design system, chiến lược UX, design ops. CI chỉ kiểm cấu trúc frontmatter. Marketplace kéo thêm 24 plugin từ 4 repo khác qua `git-subdir`, nên con số "273 skill" phụ thuộc repo ngoài. CHANGELOG nói đã gắn tag v1.0.0 nhưng repo không có tag nào. Cài cả bộ sẽ đưa 111 mô tả skill vào ngữ cảnh.
- **transitions.dev.** 35 file transition CSS (README lúc ghi 12, lúc 18; `SKILL.md` ghi 32), có guard `prefers-reduced-motion`. `agent/lib/rules.mjs` là luật tĩnh thật (thời lượng lệch thang, thiếu reduced-motion) nhưng test chỉ chạy khi publish. License riêng: dùng và sửa tự do, **cấm phân phối lại thư viện**; template/theme cần gói trả phí. `npx transitions-refine live --llm` chạy **`curl https://cursor.com/install | bash`**; agent trả phí gửi mã nguồn lên `api.transitions.dev`. Liên quan mục 22 §6.
- **baoyu-design: không khuyên dùng.** `NOTICE.md` tự ghi phần lấy từ Anthropic "not MIT… Anthropic has published no license for it… this project grants none". Repo chứa system prompt của Claude Design (`references/upstream-system-prompt.md`), `provenance.json` cho thấy prompt được trích từ bundle JavaScript phía client, kèm 49 skill dựng sẵn, font icon Anthropicons và editor dựng lại dạng bundle rút gọn 6,3 MB, rồi phát lại lên npm qua 4 gói `dsh-claude-*`. Rủi ro gỡ bỏ và pháp lý cao; mã bundle không kiểm được. Kho chỉ ghi nhận để tránh, không trích nội dung.

### 7p.6 Generative UI: ba cách và một dịch vụ vừa đóng

| | OpenUI (Thesys) | Tambo | OpenIntelligentUI (CopilotKit) |
|---|---|---|---|
| Định dạng | Ngôn ngữ riêng **OpenUI Lang** (dòng lệnh kiểu `root = Card([...])`), spec v1.0 có EBNF và fixture | Không có spec UI: component đăng ký bằng Zod thành tool cho LLM | Bảng **A2UI** + widget HTML/JS do LLM sinh chạy trong iframe |
| Giao thức | Stream qua **AG-UI** (gói langchain), hồ sơ A2UI thử nghiệm | Sự kiện **AG-UI**, client MCP đầy đủ | AG-UI qua CopilotKit |
| Phụ thuộc dịch vụ | Mẫu mặc định gọi `api.thesys.dev`; có mẫu tự host | Client mặc định `api.tambo.co`, **ngừng 31/10/2026**, xoá dữ liệu 30/11 | **Bắt buộc** router Jev của TypeSafe, không có đường lui |
| Telemetry | **`postinstall` của `lang-core` gửi PostHog khi cài**, mọi gói runtime kéo theo; tắt `OPENUI_TELEMETRY_DISABLED=1` hoặc `DO_NOT_TRACK=1` | CLI gửi PostHog; tắt `TAMBO_TELEMETRY_DISABLED` | Gửi `telemetry.copilotkit.ai`; tắt `COPILOTKIT_TELEMETRY_DISABLED=1` |
| Độ chín | 1.076 commit, 60 tác giả, ~143 file test, CI đầy đủ | 5.573 commit, CI đầy đủ, nhưng việc gần nhất là chuẩn bị đóng cloud | 162 commit, không release, dùng bản prerelease CopilotKit |

Nhận định: "chuẩn mở" của OpenUI do một công ty kiểm soát; bảng so sánh "1x so với A2UI 3x" không có dữ liệu trong repo. Tambo vẫn tự host được (Docker + Postgres) nhưng tương lai bảo trì không rõ, không nên chọn cho dự án mới. Với kho này, hướng an toàn vẫn là AG-UI + bộ component (§6) và MCP Apps (mục 04).

### 7p.7 Mẫu chung rút ra

1. **"Agent-ready" đã thành tính năng tiêu chuẩn của design system** (Astryx, Semi, và trước đó Zen DS §7f): `AGENTS.md`, MCP tra cứu component, `DESIGN.md`. Cái phân biệt là có **cổng máy** hay không: `@shadcn/lint`, Drift Gate của dembrandt, `design_lint.py` của huashu đo được; unslop, designer-skills, design-critique (§7o) chỉ dặn.
2. **Telemetry bật sẵn ngày càng phổ biến** ở công cụ cho agent: Framelink MCP (lúc chạy), OpenUI (lúc cài), CopilotKit. Đặt `DO_NOT_TRACK=1` trong môi trường CI/agent chặn được cả ba.
3. **License "gần mở"** nhiều lên: PolyForm Shield (Agentation), license riêng cấm phân phối lại (transitions.dev), CC-BY cho mã (unslop), blob đóng trong repo MIT (OpenPencil). Đọc file LICENSE, đừng tin nhãn GitHub.
4. **Phụ thuộc dịch vụ có thể biến mất**: Tambo Cloud đóng đúng ngày khảo sát. Ưu tiên mẫu tự host được và ghim endpoint.
5. **Sao tăng nhanh không phải tín hiệu chất lượng**: 4 repo trong đợt có dưới 6 tuần tuổi hoặc một người viết gần hết.

**Nguồn §7p:** GitHub search API 31/10/2026 (`repo:` cho 72 repo cũ và 18 repo mới; 18 truy vấn topic/từ khoá) · shields.io cho `stackblitz-labs/bolt.diy` · clone nông nhánh mặc định 20 repo của §1–§6 (ngày commit) · clone `--filter=blob:none` 18 repo mới, đọc: astryx (LICENSE, README, AGENTS.md, packages/cli/{scripts/postinstall.mjs, foundation/agent-docs/agent-docs.mjs}, apps/docsite/src/app/mcp/route.ts), shadcn-ui/lint (packages/lint/src/rules/*, docs/evals.md, SETUP.md), tweakcn (lib/posthog.ts, mcp-dialog.tsx, lib/ai/providers.ts, lib/constants.ts), semi-design (LICENSE, ecosystem/semi-mcp/src/tools/index.ts, ecosystem/semi-ui-skills/SKILL.md, DESIGN.md), Figma-Context-MCP (src/telemetry/client.ts, server.json, CHANGELOG.md), agentation (LICENSE, mcp/src/server/http.ts, skills/*), huashu-design (LICENSE và lịch sử license, SECURITY.md, scripts/{design_lint.py, html2pptx.js, render-video.js}), baoyu-design (LICENSE, NOTICE.md, references/upstream-sync/provenance.json — chỉ đọc đầu file), stitch-skills (react-components/scripts/validate.js, workflows), unslop (SKILL.md, scripts/*), designer-skills (CHANGELOG.md, .claude-plugin/marketplace.json, lint.yml), transitions.dev (LICENSE, agent/lib/rules.mjs, refine/bin/cli.mjs), openui (packages/lang-core/{package.json, src/telemetry/install.ts}, spec/*), tambo (README.md, SELF-HOSTING.md, packages/client/src/tambo-client.ts, các LICENSE/NOTICE), OpenIntelligentUI (apps/agent/src/visualization_router.py, docs/telemetry.md), design-extract (src/formatters/design-md.js, src/classifiers/smart.js), dembrandt (lib/robots.ts, lib/formatters/markdown.ts, smoke.yml), openpencil (crates/op-auth-bridge/{NOTICE, prebuilt/}, op-codegen/src/codegen_targets.rs) · Web: infoq.com/news/2026/10/shopify-web-components, community.shopify.dev/t/is-polaris-shopify-com-going-to-be-shut-down/26216, github.com/Shopify/polaris-react-archive (release notes), releases.sh (Headless UI), infoq.com/news/2026/09/meta-astryx-design-system, opensourceforu.com/2026/06/meta-open-sources-astryx, tambo.co/blog/posts/tambo-is-shutting-down (link trong README, chưa mở)

## 7q. Đọc mã kỹ: open-design, open-pencil, Ionic, Lucide (yêu cầu người dùng, 31/10/2026)

> OpenDesign đã có hồ sơ mức README ở §7k (19/10); open-pencil, Ionic, Lucide là repo lớn còn thiếu sau §7p. Mỗi repo clone đủ lịch sử (blob:none), đọc mã, CI, tài liệu nội bộ; **không cài, không chạy script**. Số sao từ GitHub search API 31/10/2026.

### 7q.0 `nexu-io/open-design`: đọc mã sâu (bổ sung §7k)

| Mục | Thông tin (HEAD `12d970eac`, 30/10/2026) |
|---|---|
| Repo | **105.186★**, 11.992 fork, 572 issue + **759 PR mở** · 3.831 commit trên `main` từ 28/4/2026 · tag mới nhất `open-design-v0.26.1` (22/10) **không nằm trên `main`** (vẫn ghi 0.25.1); tag không ký; CHANGELOG dừng ở 0.9.0 (5/2026); 2.819 nhánh remote |
| Ai viết | 485 tên tác giả; bot `open-design-crew[bot]` 224, `open-design-bot` ~205, `Cursor Agent` 116; 124 commit có trailer Claude, 78 Cursor |
| Kiến trúc | pnpm monorepo: daemon Express 5 + SQLite, web Next.js 16, desktop **Electron 41** (không có Rust/Tauri). ~1,85 triệu dòng TS/TSX (~931k là test); riêng `server.ts` 18.961 dòng. 169 skill, 115 design template, 501 manifest plugin, **152 gói design system** (README ghi 151) |
| Luồng chạy | Web gọi `POST /api/runs` → ghép system prompt (prompt gốc + DESIGN.md + skill + memory) → **spawn CLI agent ngoài** (`shell:false`, cwd là thư mục project) → stream SSE → agent ghi file → xem trong iframe. Có đường BYOK không cần CLI (Anthropic, OpenAI, Azure, Google, Ollama) |

**Phát hiện nặng (đã tự kiểm lại các dòng in đậm trong mã):**

- ❌ **Mọi agent đều chạy với kiểm quyền tắt, gắn cứng trong mã**: Claude Code `--permission-mode bypassPermissions` (`runtimes/defs/claude.ts:116`), Codex `workspace-write` + mạng, và **`danger-full-access` tự động trên Windows/WSL**; Cursor `--force --trust`; Copilot `--allow-all-tools`; Amp `--dangerously-allow-all`; Qwen/Qoder/Trae `--yolo`; Antigravity `--dangerously-skip-permissions`… Brief, file nhập hay skill độc có thể chạy mọi thứ với quyền người dùng.
- ❌ **Telemetry và chia sẻ nội dung mặc định bật**: `applyTelemetryDefaults` đặt `{metrics: true, content: true}` khi chưa có cấu hình (`app-config.ts:732-738`) → prompt, phản hồi, input/output tool gửi về Langfuse qua relay `telemetry.open-design.ai`. Kênh "safety/reliability" gửi PostHog **không kiểm consent và không có công tắc** (khớp PRIVACY.md); README:239 lại nói "consent-gated".
- ❌ **Chẩn đoán tự động tải lên file `*.log` trong `~/.claude`, `~/.codex/log` và thư mục log OpenCode** (`packages/diagnostics/src/agent-logs.ts:120-175`, có bước che bớt), bật mặc định ở bản cài mới; PRIVACY.md không nói rõ việc tải log của CLI bên thứ ba. Mã nguồn relay nằm ở repo riêng.
- ⚠️ **Updater tự viết chỉ so hash lấy từ cùng feed**, không kiểm chữ ký riêng; gói "launcher payload" sau khi giải nén bị **`xattr -dr com.apple.quarantine`** (`updater/payload.ts:159`), tức bỏ qua Gatekeeper cho mã tải về. Bộ cài thì có ký và notarize.
- ⚠️ **API key lưu JSON plaintext** (`app-config.json`, `.od/media-config.json`, file sau không đặt quyền `0o600`); không dùng keychain hay `safeStorage`.
- ⚠️ Daemon bind `127.0.0.1:7456`, từ chối bind ra ngoài khi thiếu `OD_API_TOKEN` (tốt), nhưng **request từ loopback bỏ qua token**, request **không có header Origin được cho qua**, không có allowlist Host chung → có khả năng bị DNS rebinding với route GET **(chưa xác minh khai thác được)**. Docker image đặt `0.0.0.0`.
- ⚠️ **Prompt gốc tự ghi nguồn**: `packages/contracts/src/prompts/official-system.ts` dòng 4: *"Adapted from claude.ai/design's 'expert designer' prompt — same identity, workflow, and content philosophy"*; mặc định màu `#D97757`. Không tìm thấy URL tài sản hay bundle trích từ Anthropic (khác baoyu-design §7p.5), nhưng vẫn là rủi ro điều khoản/sở hữu trí tuệ. Có chế độ "Website Clone" dặn model chép "assets, fonts, and copy faithfully".
- ⚠️ Gói design system mang tên thương hiệu (Stripe, Linear…): `evidence.md` chỉ nói "derived from the curated OpenDesign bundled fixture" (vòng tròn), không có tuyên bố nhãn hiệu; không kèm file font thương mại.
- ⚠️ Dịch vụ model trả phí **AMR là lựa chọn "Officially recommended" mặc định khi onboarding**, trong khi README nói "We don't ship an agent". Bản build từ mã nguồn không có key thì PostHog/relay không gửi, trừ luồng analytics AMR gắn cứng `amr-api.open-design.ai` **(chưa xác minh có gửi ở bản build nguồn)**.
- ✅ Iframe xem trước mặc định không có `allow-same-origin`; cửa sổ Electron `contextIsolation`, `sandbox`, chặn `window.open`; không `eval` trong daemon; CI 55 workflow, ~3.000 file test, Playwright `@critical` và visual.

**Kết luận:** đánh giá §7k ("local-first thật, PRIVACY rõ") cần sửa: lõi chạy cục bộ nhưng **mặc định gửi cả nội dung prompt và log agent ra ngoài**, và mọi agent chạy không kiểm quyền. Nếu dùng: tắt cả hai lớp telemetry trong Settings ngay lần đầu (lớp safety vẫn gửi), chạy trong máy ảo/container riêng không có thư mục `~/.claude`, `~/.codex` thật, không mở brief/skill từ nguồn lạ, ưu tiên đường BYOK; không dùng bản Docker trên mạng chung khi chưa đặt token.

### 7q.1 `open-pencil/open-pencil` (OpenPencil, TypeScript): khác hẳn `ZSeven-W/openpencil` ở §7p.4

| Mục | Thông tin |
|---|---|
| Repo | 9.510★, 1.000 fork, 167 issue/PR mở · tạo 27/2/2026 · **3.404 commit**, HEAD 31/10/2026 · tag mới nhất v0.16.0 (14/10/2026) · openpencil.dev |
| Tác giả | Danila Poyarkov (`dannote`) viết **~89%** commit; 70 tên tổng cộng. Chỉ 19 commit (0,56%) có trailer Claude, nhưng đó là **do quy định**: CONTRIBUTING cấm ghi AI là đồng tác giả, CI chặn, `.claude/settings.json` tắt attribution; việc dùng AI khai trong mẫu PR |
| License | `LICENSE` MIT, nhưng `REUSE.toml` đặt **phần Cloud (`packages/cloud/**`, `src/cloud/**`…) theo Apache-2.0**; có NOTICE cho Kiwi (evanw), luật lint lấy từ `dmmulroy/anti-slop`. **Không có blob nhị phân đóng** (khác ZSeven) |
| Không liên quan ZSeven | 0 commit chung, không trùng tác giả, không nhắc tên nhau; cùng đọc file `.pen` của Pencil.dev nên trùng hướng, không phải fork |

**Kiến trúc.** TypeScript ~587k dòng (trong đó ~259k là test), Vue ~61k, vỏ desktop **Tauri v2** (Rust ~5k dòng). Vẽ bằng **Skia qua `canvaskit-wasm`** trên WebGL, layout bằng Yoga WASM. Định dạng gốc là chính **`.fig` của Figma** (Kiwi + Zstd + ZIP), cũng mở `.pen`, `.jam`, draw.io, Mermaid; xuất SVG, PDF, PPTX, HTML, ảnh, JSX/Tailwind, Storybook. Cộng tác P2P bằng **Yjs qua WebRTC (Trystero)**, báo hiệu qua MQTT công cộng và TURN công cộng `openrelay.metered.ca`.

**Tài liệu nội bộ trung thực hơn README** (như FigCraft §7e): `fig-reader.md` ghi độ trung thực trên toàn bộ corpus "chưa xong"; `export.md` liệt kê lỗ hổng (tên, liên kết style, override); `validation.md` nói chưa có quy trình so hình tự động với Figma; ma trận roadmap ghi prototyping, smart animate, version history "Not modeled".

**AI.** BYOK qua Vercel AI SDK (Anthropic, OpenAI, Google, DeepSeek, OpenRouter, endpoint tương thích); **127 tool** `defineTool`; MCP stdio và HTTP. MCP HTTP làm đúng: bind `127.0.0.1:7600`, **bearer token ngẫu nhiên mặc định**, `eval` tắt trừ khi `OPENPENCIL_MCP_EVAL=1`, giới hạn thư mục bằng `OPENPENCIL_MCP_ROOT` (riêng stdio không áp các giới hạn này, SECURITY.md tự ghi). Gọi Claude Code/Codex/Gemini qua ACP, **không truyền cờ bỏ quyền**; yêu cầu quyền hết giờ thì tự từ chối.

**Rủi ro đọc mã thấy:**

- ❌ **Chat AI trong app desktop bật tool `eval` mặc định**: chạy JavaScript do model viết bằng `new AsyncFunction` ngay trong webview chính, không duyệt, không cô lập; webview đó có quyền Tauri ghi/xoá file `**`, spawn một số tiến trình, `csp: null`. Prompt injection trong file thiết kế hay nội dung web có thể dẫn tới xoá/ghi file **(suy ra từ đọc mã, chưa thử khi chạy)**. Tắt `eval` trong Settings → AI tools khi mở file lạ.
- ⚠️ Đăng nhập ChatGPT **dùng lại client ID OAuth của Codex CLI** và gọi `chatgpt.com/backend-api/codex`: vùng xám điều khoản, có thể hỏng bất kỳ lúc nào.
- ⚠️ Bản build chính thức **gửi ping ẩn danh hằng ngày mặc định** (phiên bản, OS, arch, không ID); thống kê dùng là opt-in. Tắt bằng Settings → Privacy, `OPENPENCIL_TELEMETRY=0` hoặc `DO_NOT_TRACK`. Khớp CHANGELOG.
- ⚠️ CI rất dày (commitlint, oxlint, typecheck, jscpd ngưỡng 0, test 9 nhóm, Cloud e2e 3 backend) nhưng **548 file e2e Playwright của editor không chạy trong workflow nào** tìm được.
- ✅ Cập nhật tự động ký minisign, `requireSignedVersion: true`; bản macOS ký Developer ID và notarize; artifact có attestation. Bản Windows có vẻ chưa ký Authenticode **(chưa xác minh)**.
- Bus factor ~1; 881 commit từ 1/9/2026.

**So sánh nhanh:**

| | open-pencil | ZSeven-W/openpencil (§7p.4) | FigCraft (§7e) | Penpot |
|---|---|---|---|---|
| Ngôn ngữ | TS/Vue + Tauri | Rust | Rust | Clojure(Script) |
| License | MIT + Apache-2.0 (Cloud), sạch | MIT + thư viện xác thực đóng | MIT/Apache-2.0 | MPL-2.0 |
| File Figma | Đọc/ghi `.fig` gốc, chưa trọn vẹn (tự ghi) | Không kiểm | "Best effort" | Qua plugin |
| AI | BYOK, 127 tool, MCP, ACP; **eval bật sẵn** | MCP, ACP | CLI/MCP | Không gốc AI |

**Dùng thế nào:** hợp để đọc/chuyển `.fig`/`.pen` không giao diện qua CLI hoặc MCP (giữ token, eval tắt, đặt `OPENPENCIL_MCP_ROOT` hẹp). Dùng bản web PWA nếu không muốn cấp quyền file của desktop. Luôn giữ file `.fig` gốc. Chưa thay được Figma cho prototype hay lịch sử phiên bản.

### 7q.2 `ionic-team/ionic-framework` (Ionic 9): khỏe, MIT, nhưng do OutSystems nắm

| Mục | Thông tin |
|---|---|
| Repo | **52.734★**, 13.295 fork, 439 issue + 76 PR mở · từ 2013 · 14.820 commit, HEAD 30/10/2026 · **v9.0.10** (v9.0.0 ra 19/8/2026), phát hành vá **mỗi tuần** |
| Ai làm | 12 tháng qua 508 commit: bot ~35% (renovate, release bot), **nhân viên Ionic/OutSystems ~59%** (4–6 người), cộng đồng ~6% |
| License | MIT sạch ("Drifty Co."), không CLA |
| Kinh doanh | Blog Ionic 11/2/2025: **ngừng bán mới mọi sản phẩm thương mại** (Appflow, Identity Vault, Portals…); Appflow chạy tới 31/12/2027; Framework và Capacitor "vẫn miễn phí và mở", là lõi mobile của OutSystems |

**Kiến trúc.** Lõi web components viết bằng **Stencil** (`@stencil/core` ^4.44), bọc cho Angular, React, Vue (kèm router riêng) và SSR Angular; 97 thư mục component (~60–70 component dùng được: datetime, modal, sheet, segment, refresher, item-sliding…). Hai "mode" giao diện **iOS và Material** chọn tự động theo nền tảng (64 file SCSS mỗi mode). Capacitor chỉ là phụ thuộc phát triển, phát hiện lúc chạy. v9 cần Angular 18+, React 18/19, Vue 3.5+, iOS 16+, Capacitor 7+; **`@ionic/react-router` chưa hỗ trợ React Router 7**.

**Cổng chất lượng mạnh:** 424 spec Playwright e2e/screenshot, 213 unit test, **7.436 ảnh chuẩn** so hình, **axe-core** trong 37 file e2e, chạy trên Mobile Chrome/Safari/Firefox; CI chia 20 shard screenshot, bắt buộc check tổng; CodeQL; chạy thử hằng đêm với bản Stencil mới.

**Sẵn cho agent ở mức vừa:** có **`ionicframework.com/docs/llms.txt`** (~46 KB, mỗi trang có bản `.md`) và `core/api.txt` (API công khai, 2.109 dòng); repo **không có** `AGENTS.md`/`CLAUDE.md`, **không có MCP chính chủ** (chỉ bản cộng đồng).

**Telemetry:** framework không gửi gì. **Ionic CLI bật telemetry mặc định**: Google Analytics (mã UA cũ) + POST `api.ionicjs.com/events/metrics` kèm lệnh, đối số, UUID máy, `ionic info`, token nếu đăng nhập; tắt `ionic config set -g telemetry false` (tự bỏ khi CI hoặc không TTY). CLI gần như ngủ (commit cuối 3/2025); dùng Vite/Angular CLI + Capacitor trực tiếp cũng được.

**Đang chuẩn bị:** nhánh `next` (hơn 590 commit) thêm theme "ionic" (58 file SCSS) và phụ thuộc **`outsystems-design-tokens`**; blog v9 hẹn "Modular Ionic" quý 2/2027, tức sắp đổi lớn theo design system của OutSystems.

**Dùng thế nào:** hợp đội web (nhất là Angular) cần một mã cho iOS/Android/PWA qua Capacitor, app nội bộ nhiều form và danh sách. Ghim v9, tắt hoặc bỏ CLI, không dựa vào Appflow/Identity Vault/Portals (thay bằng Capawesome, Capgo, Codemagic). Cho agent đọc `docs/llms.txt` và `core/api.txt`. Không hợp app cần cảm giác native thật hay nhiều animation; so với React Native Reusables, Tamagui, Flutter ở §7h.

### 7q.3 `lucide-icons/lucide`: bộ icon mặc định của shadcn, license thật là ISC + MIT

| Mục | Thông tin |
|---|---|
| Repo | **25.427★**, 1.666 fork, 392 issue/PR mở · fork từ Feather (commit đầu 8/6/2020 "fork") · 3.120 commit, HEAD 30/10/2026 · **v1.66.0** (v1.0.0 ngày 23/3/2026) |
| Nhịp | 779 commit/12 tháng, tăng dần (160 trong 10/2026); **95 bản phát hành/năm**: cron hằng ngày tự tăng minor khi có icon mới (qua bước duyệt) |
| Người phát hành | Chỉ 3 người (`ericfennis`, `karsa-mistmere`, `jguddas`) được chạy release (khoá trong workflow) |
| Nội dung | **2.015 icon** (README còn ghi "1600+"), mỗi icon có JSON tags/categories (43 category); 277 alias tên cũ (274 đánh dấu deprecated, chưa có ngày gỡ); 14 gói (React, Vue, Svelte, Angular, Solid, RN, static, Astro, lab…) |

**License (lý do GitHub báo `NOASSERTION`).** File `LICENSE` gồm **ISC** cho Lucide **cộng toàn văn MIT của Feather (Cole Bemis) áp cho 115 icon gốc Feather**, liệt kê theo tên cũ (vẫn tồn tại qua tên mới hoặc alias). README và badge chỉ ghi "ISC". Dùng gói npm là đủ điều kiện (gói chép `LICENSE` vào); chép SVG thô thì phải kèm `LICENSE`. Ghi trong hồ sơ tuân thủ là **`ISC AND MIT`**. Đã **gỡ toàn bộ icon thương hiệu** (27/11/2025); workflow tự đóng issue xin logo; cần logo thì dùng Simple Icons (CC0).

**Cổng chất lượng.** Prettier + svgo ép thuộc tính gốc (24×24, `stroke-width` 2, đầu nét tròn), ESLint kiểm SVG (chỉ `currentColor`/`none`, không style inline), lint tên file, schema JSON, cspell; cả 2.015 SVG đúng viewBox và nét. Quy tắc hình học (khoảng cách, bo góc, lưới) **chỉ người duyệt**, có comment xem trước tự động; không có so hình pixel. Chuỗi cung ứng tốt: **npm provenance qua OIDC**, publish `--ignore-scripts`, action ghim SHA, `permissions: {}` mặc định. Không gói nào có postinstall, không telemetry (trang docs dùng OpenPanel, dữ liệu ở EU).

**Cho agent.** Có `llms.txt` (vitepress-plugin-llms) nhưng **trang icon bị loại** ("Not working, need investigation"); endpoint công khai `lucide.dev/api/tags`, `/api/icons/[name]`; **không có MCP chính chủ** (bản cộng đồng nhỏ, < 60★). Agent chọn icon tốt nhất qua tags trong `icons/*.json`.

**Điểm cần sửa ở README:** "1600+" (thực 2.015); "ISC" (thực ISC + MIT); ghi chú v1 "giảm 32,3% (11,4 MB → 1 MB)" tự mâu thuẫn (11,4 → 1 là ~91%).

**Tránh "giao diện Lucide mặc định"** (dấu hiệu "AI slop" mà Hallmark §7l, anti-slop §7i nhắc): Phosphor (6 độ đậm, duotone), Material Symbols (trục biến thiên, Apache-2.0), Iconoir (nét 1,5px, MIT), Heroicons solid/mini, Radix Icons (15px). Tabler gần như giống Lucide nên không giúp. Iconify cho phép đổi bộ sau một API (mỗi bộ giữ license riêng; Remix Icon dùng license riêng, cần đọc trước). Nếu giữ Lucide: đổi `strokeWidth` (1,5) và cỡ qua `LucideProvider` của v1.

**Dùng thế nào:** mặc định an toàn về pháp lý, bảo trì tốt; import từng icon, tránh `DynamicIcon` (kéo toàn bộ icon vào bundle); **ghim phiên bản** (phát hành gần như mỗi ngày) và không dùng URL CDN `@latest` như docs gợi ý. Khớp X-Templates `UX-VISUAL-010` (một bộ icon duy nhất).

**Nguồn §7q:** open-design (HEAD 12d970eac; README.md, PRIVACY.md, apps/daemon/DIAGNOSTICS.md, apps/daemon/src/{server.ts, app-config.ts, analytics.ts, daemon-startup.ts, origin-validation.ts, media/config.ts, langfuse-trace.ts, integrations/{telemetry-relay,vela}.ts, runtimes/{registry,agent-process}.ts, runtimes/defs/{claude,codex,cursor-agent,amr}.ts}, packages/contracts/src/prompts/official-system.ts, packages/diagnostics/src/agent-logs.ts, apps/web/src/{analytics/client.ts, analytics/error-tracking.ts, components/FileViewer.tsx}, apps/desktop/src/main/{runtime.ts, updater.ts, updater/payload.ts}, design-systems/{stripe,agentic,linear-app}/*, .github/workflows/{ci,release-stable}.yml, deploy/Dockerfile) · clone `--filter=blob:none` 31/10/2026: open-pencil (HEAD 9da768cf; README.md, LICENSE, REUSE.toml, SECURITY.md, CONTRIBUTING.md, CHANGELOG.md, .claude/settings.json, desktop/{tauri.conf.json, capabilities/default.json, src/credentials.rs, src/system/env.rs}, .github/workflows/{ci,build,app,heavy-tests}.yml, packages/mcp/src/{server.ts, server/lifecycle.ts, transport/origins.ts}, packages/core/src/tools/{analyze/eval/wrap.ts, registry/core.ts}, src/app/ai/{tools/catalog.ts, agents/acp/permission.ts, providers/chatgpt/oauth.ts}, src/app/telemetry/{config,state}.ts, src/app/collab/transport/trystero.ts, packages/docs/development/{roadmap,fig-reader}.md, packages/fig/docs/{export,validation}.md; so sánh lịch sử với ZSeven-W/openpencil) · ionic-framework (HEAD b01d379; LICENSE, README.md, BREAKING.md, lerna.json, core/{package.json, stencil.config.ts, playwright.config.ts, api.txt}, core/src/global/ionic-global.ts, .github/workflows/build.yml, nhánh `next` core/package.json) + ionic-cli (packages/@ionic/cli/src/lib/{telemetry,config,command}.ts) · lucide (HEAD a630cec; LICENSE, README.md, BRAND_LOGOS_STATEMENT.md, icon.schema.json, eslint.config.js, prettier-plugin-lucide-svg.mjs, .github/workflows/{ci,release,linting-icons,lint-code,close-issue-with-banned-phrases}.yml, docs/guide/version-1.md, docs/privacy.md, docs/.vitepress/config.ts) · ionic.io/blog/important-announcement-the-future-of-ionics-commercial-products · ionic.io/blog/announcing-ionic-framework-9 · ionicframework.com/docs/llms.txt (200) · GitHub search API 31/10/2026

## 7r. Quét các repo lớn còn lại liên quan UI/UX (yêu cầu người dùng, 31/10/2026)

> Sau §7p–§7q còn ~100 ứng viên từ các truy vấn GitHub. Bỏ repo lạc chủ đề (Cal.com, Nextcloud, Plausible, DocuSeal, supermemory…), giữ **46 repo** liên quan UI/UX từ ~5k★, chia 4 nhóm. Mỗi repo clone `--filter=blob:none` (đủ lịch sử nhánh mặc định), đọc LICENSE, manifest, CI, grep telemetry, kiểm 2–3 lời README; phiên bản npm đối chiếu `registry.npmjs.org/<gói>/latest`. **Không cài, không chạy script.** Số sao GitHub search API 31/10/2026; "12t/3t" = số commit trong 12 tháng / 3 tháng qua.

### 7r.1 Công cụ và skill thiết kế dùng AI

| Repo | ★ · license | Commit cuối | Là gì | Đánh giá |
|---|---|---|---|---|
| `JCodesMore/ai-website-cloner-template` | 38,3k · MIT | 5/10/2026 | Starter Next.js + một skill `/clone-website` (61 dòng) cho agent dựng lại bất kỳ URL nào | ⚠️ Skill **dặn dùng chữ, font, ảnh, SVG thật của site gốc**; README có mục "Not Intended For" nhưng skill không có bước kiểm ToS/bản quyền/nhãn hiệu. Rủi ro pháp lý dồn cho người dùng |
| `wandb/openui` | 22,7k · Apache-2.0 | 30/6/2026 | App tự host "kiểu v0": mô tả → HTML → React/Svelte/Web Components (FastAPI + LiteLLM/Ollama) | ⚠️ Gần như ngừng (commit chức năng cuối 15/9/2025, 2026 chỉ có Renovate). **Weave tự bật khi có `WANDB_API_KEY` hoặc chỉ cần có mục `api.wandb.ai` trong `~/.netrc`** → prompt có thể bị trace lên W&B không hỏi (`server.py` dòng 584–603) |
| `ConardLi/garden-skills` | 13,4k · MIT (không ghi chủ sở hữu) | 25/10/2026 | 6 skill; `web-design-engineer` 492 dòng (~9k token) + 29 "style recipe" | ⚠️ "Executable browser acceptance harness" thực ra là văn bản; **phát lại dưới MIT một file 73 KB tự nhận là system prompt "Claude Design"** (`dist/prompts/…`), nguồn gốc không rõ (cùng loại rủi ro với baoyu-design §7p.5) |
| `lnkiai/m3e-canvas` | 9,9k · MIT (+ NOTICE Apache-2.0) | 22/10/2026 | Vẽ màn Material 3 Expressive trên trình duyệt, nối thành luồng, xuất prompt cho coding agent | ✅ Tĩnh, không server, link chia sẻ nằm ở fragment URL, có vitest + CI. ⚠️ **API key lưu plaintext trong localStorage**; 7 tuần tuổi, 27% commit trailer Claude |
| `MengTo/threeui` | 7k · MIT | 1/9/2026 | Phần Community của catalog shader/Three.js thương mại ThreeUI, gói `@designcodeio/threeui` | ⚠️ Open-core (nút "Get Pro"), README ghi 50 component nhưng báo cáo đồng bộ ghi 43; demo tải từ threeui.com, CDN, Supabase |
| `twostraws/SwiftUI-Agent-Skill` | 6,4k · MIT | 26/10/2026 | Skill "SwiftUI Pro" của Paul Hudson: viết/duyệt SwiftUI theo API mới, HIG, accessibility | ✅ Gọn (~1,5k token, 12 file tham chiếu nạp theo bước). ⚠️ "Sự thật nền tảng" cứng (iOS 27, Xcode 27.1) sẽ cũ nhanh |
| `kaankiziltug/logo-design-skill` | 5,6k · MIT (trừ thư viện logo) | 20/10/2026 | Quy trình brief → concept → SVG → kiểm → bộ giao; 9 script Python | ⚠️ **Kèm 1.432 SVG logo của công ty thật** (TRADEMARKS.md: MIT không áp dụng, "chỉ để tham khảo"); `render_png.py` cần renderer ngoài dù README nói "không phụ thuộc" |
| `miurla/morphic` | 9,2k · Apache-2.0 | 28/10/2026 | Answer engine kiểu Perplexity, câu trả lời stream một spec JSON thành component (generative UI) | ✅ Trưởng thành (1.889 commit, CI lint/test/build/eval), **mọi telemetry (PostHog, Vercel, Langfuse) chỉ bật qua biến môi trường**. Mẫu tham khảo generative UI tốt hơn các repo §7p.6 |
| `bernaferrari/FigmaToCode` | 5,3k · **GPL-3.0** | 5/8/2026 | Plugin Figma chuyển tất định (không AI) sang HTML/React/Svelte/Tailwind/Flutter/SwiftUI | ✅ `manifest.json` không xin quyền, `networkAccess: none`. ⚠️ GPL nếu fork/nhúng (mã sinh ra thường không bị GPL ràng, **chưa xác minh pháp lý**) |
| `evolus/pencil` | 9,9k · **GPL-2.0** | 22/10/2026 | Công cụ wireframe Electron lâu đời **của Evolus (Việt Nam)**; v4.0.0 (20/10/2026) thêm **MCP server** cho AI vẽ lên canvas | ❌ README nói MCP "chỉ trên loopback 127.0.0.1" nhưng `app/tools/api-server.js` gọi `server.listen(port)` **không truyền host** (nghe mọi interface), `cors origin '*'`, **không xác thực, bật mặc định cổng 1919** **(đọc mã, chưa thử khi chạy)**; Electron 16 (2021, hết hỗ trợ); 530 issue mở; CI chỉ còn AppVeyor Node 6 |
| `ParthJadhav/Tkinter-Designer` | 10,3k · BSD-3-Clause | 16/10/2026 | Đọc Figma qua REST API, sinh mã GUI Tkinter | ⚠️ Gần như đứng từ 2022 (tag cuối v1.0.7 1/2023), CI dùng installer Poetry đã bị gỡ |

**Đáng chú ý cho mục 18:** Pencil là một trong số ít công cụ thiết kế mã mở do đội Việt Nam làm còn được cập nhật; nên báo lỗi MCP cho Evolus, và khi dùng thì tắt MCP (`pencil.mcp.enabled`) hoặc chặn cổng 1919.

### 7r.2 Thư viện React và tiện ích UI

| Repo | ★ · license | 12t / 3t | Bản mới nhất | React 19 | Tài sản cho AI | Đánh giá |
|---|---|---|---|---|---|---|
| `react-bootstrap/react-bootstrap` | 22,6k · MIT | 31 / 19 | 2.10.10 (5/2025); v3 vẫn beta | ✅ | – | ⚠️ Chỉ khi đã dùng Bootstrap; phát hành chậm, một người bảo trì |
| `uber/baseweb` | 9k · MIT | 49 / 9 | 18.2.0 (tag dừng ở v13, 2023) | dải peer mở, chưa kiểm | – | ❌ README: **"limiting our engagement with this repository"**; CI chỉ build, **không chạy test** (dù có 823 file test); khoá vào Styletron |
| `rsuite/rsuite` | 8,7k · MIT | 1.081 / 996 | 6.2.5 | ✅ (CI 18/19) | **MCP `@rsuite/mcp`, skill, `AGENTS.md`** | ✅ Hợp admin nhiều dữ liệu (~120 component); ghim minor vì vừa ra v6, một người chính |
| `grommet/grommet` | 8,4k · Apache-2.0 | 169 / 102 | 2.58.0 | ✅ | `copilot-instructions.md` (cho người đóng góp) | ⚠️ HPE đứng sau, chú trọng a11y (jest-axe, Chromatic), nhưng phụ thuộc styled-components; 494 issue mở |
| `primefaces/primereact` | 8,3k · MIT (các bản cũ) | 63 / 8 | 10.9.9 | ✅ | – | ❌ README: **"no longer under active development… security fixes only"**, chuyển sang PrimeUI (license bản mới chưa rõ); **xoá toàn bộ workflow CI ngày 21/9/2026** |
| `arco-design/arco-design` | 5,8k · MIT | 87 / 10 | 2.66.18 | qua adapter, CI chỉ React 18 | – | ⚠️ Ổn định nhưng chậm, Less, tài liệu Trung trước |
| `cosscom/ui` (coss ui, trước là Origin UI) | 10,8k · MIT (2 dòng copyright nên GitHub báo NOASSERTION) | 279 / 59 | không version (qua registry shadcn) | **bắt buộc** 19.2 + Next 16 | **`AGENTS.md`, `llms.txt`, skill** | ✅ Design system của Cal.com trên **Base UI + Tailwind v4**; chỉ 6 file test |
| `elastic/eui` | 6,4k · **SSPL-1.0 / Elastic License 2.0** | 566 / 196 | 123.3.0 | ❌ (chỉ 17/18) | `AGENTS.md`, `CLAUDE.md` | ❌ Ngoài hệ Elastic: **không phải license OSI** (đổi từ Apache-2.0 ngày 8/7/2021); dù vậy a11y tốt nhất nhóm (46 test Cypress + axe) |
| `react-hook-form/react-hook-form` | 44,9k · MIT | 493 / 240 | 7.91.0 (v8 beta) | ✅ | – | ✅ Chuẩn de facto cho form, 0 phụ thuộc runtime |
| `bvaughn/react-virtualized` | 27,1k · MIT | 11 / 11 | 10.0.0 (18/10/2026, viết lại TS) | chỉ v10 | – | ⚠️ README tự khuyên dự án mới dùng `react-window` (cùng tác giả) hoặc TanStack Virtual |
| `usablica/intro.js` | 23,5k · **AGPL-3.0 + license thương mại** | 104 / 41 | 8.6.0 | không áp dụng | – | ⚠️ Dự án thương mại **phải mua license**; thay bằng driver.js hoặc react-joyride (MIT) |

**Ghi nhận:** hai thư viện của công ty lớn đã rút lui công khai (Base Web của Uber, PrimeReact của PrimeTek) nhưng vẫn còn hàng nghìn sao; sao không nói gì về tình trạng bảo trì. Hai bẫy license: EUI (SSPL/ELv2) và intro.js (AGPL + bản thương mại). Không gói nào trong nhóm có postinstall hay telemetry.

### 7r.3 Vue, Angular và mobile

| Repo | Nền | ★ · license | 12t / 3t | Bản mới nhất | Tài sản cho AI | Đánh giá |
|---|---|---|---|---|---|---|
| `vueComponent/ant-design-vue` | Vue | 21,7k · MIT (3 khối MIT gộp nên GitHub báo NOASSERTION) | 12 / 0 | 4.2.6 (**11/2024**) | – | ❌ Thực tế không bảo trì: 10/12 commit gần nhất là docs/quảng cáo; nhánh `feat/vapor` chưa phát hành. **Workflow bắt mọi PR phải có trailer Co-Authored-By của Claude/Copilot/Cursor/Codex** |
| `tusen-ai/naive-ui` | Vue 3 | 18,6k · MIT | 184 / 52 | 2.45.3 (8/2026) | `AGENTS.md` | ✅ Hợp admin/dashboard Vue; 712 issue mở, phụ thuộc một người chính |
| `unovue/shadcn-vue` | Vue 3.5 + Tailwind v4 | 10,8k · MIT | 284 / 43 | CLI 2.9.0 (28/10/2026) | **`llms.txt`, MCP trong CLI, bộ skill Claude** | ✅ Mặc định cho Vue + Tailwind; sẵn cho agent nhất nhóm |
| `unovue/reka-ui` (trước là Radix Vue) | Vue (headless) | 6,9k · MIT | 455 / 150 | 2.11.0 (5/10/2026) | `CLAUDE.md`, `llms.txt` | ✅ Lớp nền của shadcn-vue và Nuxt UI; nhánh v3 sẽ có thay đổi phá vỡ |
| `NG-ZORRO/ng-zorro-antd` | Angular 22 | 9,2k · MIT | 288 / 60 | 22.1.2 (10/2026) | **`AGENTS.md`, `.claude/`, 7 skill, cấu hình MCP (Angular CLI, ESLint), `llms.txt` + `llms-full.txt`** | ✅ Lựa chọn cho Angular; major phải khớp major Angular |
| `ant-design/ant-design-mobile` | React (mobile web) | 12,1k · MIT | 51 / 9 | 5.43.0 (9/2026) | – | ⚠️ Ổn định cho H5 nhưng chậm lại, toolchain cũ |
| `akveo/react-native-ui-kitten` | React Native | 10,7k · MIT | 193 / 145 | 6.2.1 (10/2026) | `AGENTS.md`, `CLAUDE.md`, MCP thiết bị | ⚠️ **Hồi sinh 2026** (179/193 commit một người), README nói chạy New Architecture RN 0.81 **(chưa xác minh)** |
| `wix/react-native-calendars` | React Native | 10,3k · MIT | 3 / 0 | 1.1314.0 (1/2026) | – | ⚠️ Chuẩn de facto nhưng gần như đứng; tự thử trên New Architecture |
| `necolas/react-native-web` | RN → web | 22,2k · MIT | 77 / 77 | 0.21.4 (10/2026) | – | ⚠️ Nghỉ 11 tháng rồi hồi sinh 25/9/2026 dưới người dẫn mới; **0.22 có thay đổi phá vỡ** — ghim 0.21.x |
| `pure-admin/vue-pure-admin` | Mẫu admin Vue | 20,7k · MIT | 72 / 3 | v7.0.0 (4/2026) | – | ⚠️ 0 test, phụ thuộc rất nặng; dùng bản `pure-admin-thin` |
| `jd-opensource/taro-ui` | Taro (mini-program) | 4,7k · MIT | 108 / 4 | 3.4.2 (9/2026) | `SKILL.md` tiếng Trung | ⚠️ Chỉ khi đã dùng Taro 3; Taro 4 còn thử nghiệm, tài liệu chỉ tiếng Trung |

**Ghi nhận:** ba repo từng bị coi là bỏ (UI Kitten, react-native-web, taro-ui) đã hồi sinh năm 2026 nhưng đều dựa vào một người; ant-design-vue và react-native-calendars thì ngược lại, sao cao nhưng thực tế chỉ còn bảo trì tối thiểu. Các thư viện Vue/Angular đang **cạnh tranh bằng tài sản cho agent** (llms.txt, MCP, skill), giống xu hướng §7p.7.

### 7r.4 Hạ tầng design system, web components, tiện ích và danh sách

| Repo | ★ · license | 12t / 3t | Bản mới nhất | Tài sản cho AI | Đánh giá |
|---|---|---|---|---|---|
| `stenciljs/core` | 13,1k · MIT (đoạn NOTICE thêm vào nên GitHub báo NOASSERTION) | 257 / 77 (nhánh `v5` thêm 451 commit) | 4.45.2; v5.0.0-beta.27 | `CLAUDE.md` (v5) | ⚠️ Trình biên dịch web components dưới Ionic (§7q.2). **CLI v4 bật telemetry mặc định** gửi `api.ionicjs.com` (tắt `npx stencil telemetry off`; bỏ qua khi CI); **v5 gỡ hẳn telemetry**. Một người chính |
| `BuilderIO/mitosis` | 14,5k · MIT | 17 / 4 | 0.14.2 | – | ⚠️ Viết một lần, biên dịch ra ~20 framework; vẫn 0.x, nhịp giảm mạnh (143 → 17 commit/năm), CLI phụ thuộc `gluegun: "latest"` |
| `Tencent/omi` | 13,3k · MIT (bọc trong notice kiểu Tencent) | 15 / 6 | 7.7.14 (tag dừng ở 7.7.0, 2024) | – | ⚠️ Không có CI chạy được; chỉ đáng dùng cùng TDesign; dự án mới chọn Lit hoặc Stencil |
| `chakra-ui/panda` | 6,2k · MIT | 1.094 / 436 | 2.4.0 (lõi v2 viết lại bằng Rust/Oxc) | **`AGENTS.md`, skill, MCP `@pandacss/mcp`, `llms.txt`** | ✅ CSS-in-JS không runtime, CI đầy đủ (cả cargo-deny, clippy); phụ thuộc một người (Segun Adebayo) |
| `chakra-ui/zag` | 5,2k · MIT | 884 / 230 | 1.47.0 | `AGENTS.md`, `CLAUDE.md`, `context7.json`, `llms-*.txt` | ✅ 51 "máy trạng thái" component (dialog, combobox, date-picker…) cho 6 framework; lớp logic của Ark UI, Chakra v3, Skeleton v5; 69 e2e Playwright |
| `primer/css` | 13k · MIT | 179 / 70 (152 là dependabot) | 22.3.3 | – | ⚠️ README: **"This project is in KTLO mode"** (chỉ giữ chạy) từ 25/9/2025; dự án mới dùng Primer React hoặc `@primer/primitives` (vẫn sống) |
| `skeletonlabs/skeleton` | 6,1k · MIT | 313 / 11 | 5.0.1 (8/2026) | `.claude/skills` (cho người đóng góp), llms | ⚠️ Tailwind v4 + Zag; chậm hẳn sau v5.0, PR bảo mật của Renovate chưa merge từ cuối 8/2026 |
| `knadh/oat` | 5,6k · MIT | 273 / 26 | 1.0.1 (31/10/2026) | – | ✅ cho công cụ nhỏ: HTML/CSS ngữ nghĩa ~10 KB, 0 phụ thuộc (Kailash Nadh, CTO Zerodha); **không có test** |
| `golden-layout/golden-layout` | 6,7k · MIT | 9 / 0 | v2.6.0 (**2022**) | – | ❌ cho dự án mới: 4 năm không release, v3 chưa ra |
| `dicebear/dicebear` | 10k · MIT (mã) | 665 (nhánh 11.x) | 10.7.0; 11.0.0-rc.2 | llms | ✅ Avatar tất định, lõi cho 7 ngôn ngữ. ⚠️ **Mỗi style có license riêng**: CC BY 4.0 (adventurer, big-smile, micah, personas… phải ghi công), CC0 (lorelei, notionists, pixel-art…), avataaars/bottts license riêng "free for commercial use" (không phải mã mở). Nhánh mặc định là RC |
| `ekmas/neobrutalism-components` | 5,6k · MIT | 55 / 53 | (registry shadcn) | – | ⚠️ README ghi "no longer maintained" từ 7/2025 tới 11/9/2026 rồi viết lại trên Base UI; không CI, không test |
| `birobirobiro/awesome-shadcn-ui` | 20,7k · MIT | 502 / 208 | – | – | ✅ ~548 mục có cột ngày, CI kiểm link (lychee); 10 link thử: 0 chết, 2 trỏ repo đã archive, 1 đổi tên; có chỗ quảng cáo trả phí |
| `aniftyco/awesome-tailwindcss` | 15,2k · CC0-1.0 | 21 / 4 | – | – | ✅ ~74 link chọn lọc, đã gỡ thư viện không miễn phí; CONTRIBUTING **cấm bài gửi do AI viết và bài trả phí**; 1/10 link chết (`tailwindcss.com/discord`) |

### 7r.5 Mẫu chung rút ra từ 46 repo

1. **Sao không phản ánh bảo trì.** Sáu repo trên 9k★ đang ở chế độ duy trì hoặc rút lui công khai (Base Web, PrimeReact, Primer CSS "KTLO", ant-design-vue, golden-layout, react-native-calendars). Dấu hiệu đọc được ngay: banner trong README, bảng hỗ trợ trong `SECURITY.md`, CI có chạy test hay không, tag có khớp `package.json` hay không.
2. **Bẫy license ẩn sau nhãn GitHub.** `NOASSERTION` thường chỉ là MIT kèm notice (Stencil, Omi, coss ui, ant-design-vue), nhưng cũng có thể là SSPL/ELv2 (EUI) hay AGPL + thương mại (intro.js); và license theo **từng tài sản** (style DiceBear, logo trong logo-design-skill, thư viện Pencil GPL). Luôn đọc file.
3. **Tài sản cho agent thành tiêu chí chọn thư viện**: shadcn-vue, ng-zorro, rsuite, Panda, Zag, coss ui có `llms.txt`/MCP/skill; thư viện cũ hơn thì không. Hợp với X-Templates `UX-DS-019`.
4. **Máy chủ MCP cục bộ của app desktop là bề mặt tấn công mới**: Pencil (nghe mọi interface, CORS `*`, không xác thực, bật mặc định) đối lập với open-pencil (127.0.0.1, token ngẫu nhiên, eval tắt) §7q.1.
5. **Telemetry trong CLI dựng sẵn** (Stencil v4, Ionic CLI) và **trace ngầm** (wandb/openui qua `~/.netrc`) tiếp tục là thứ phải tắt chủ động; bổ sung bảng §2 của [X-TEMPLATES.md](../X-TEMPLATES.md).

**Nguồn §7r:** clone `--filter=blob:none` 46 repo ngày 31/10/2026, đọc qua `git show HEAD:<file>`: LICENSE/NOTICE, `package.json`/`pyproject.toml`, README, workflow CI, các file nêu trong bảng (ví dụ `evolus/pencil` app/tools/api-server.js; `wandb/openui` backend/openui/server.py dòng 584–603; `primefaces/primereact` README.md, SECURITY.md; `uber/baseweb` README.md, .github/workflows/pr-check.yml; `elastic/eui` LICENSE.txt; `usablica/intro.js` license.md; `stenciljs/core` src/cli/telemetry/telemetry.ts, nhánh v5 V5_PLANNING.md; `dicebear/dicebear` nhánh 9.x packages/@dicebear/*/LICENSE; `ConardLi/garden-skills` dist/prompts/; `kaankiziltug/logo-design-skill` TRADEMARKS.md) · `registry.npmjs.org/<gói>/latest` · GitHub search API 31/10/2026.

## 8. Nguồn (mục 1–6)

- https://designrevision.com/blog/best-react-component-libraries · https://designrevision.com/blog/best-tailwind-component-libraries · https://dualite.dev/blogs/best-ui-component-libraries · https://www.uilora.com/blog/uilora/10-best-react-ui-component-libraries-in-2026-ranked-by-a-frontend-team · https://www.techwench.com/best-ui-component-libraries-2026/
- https://www.opensourcealternatives.to/item/penpot · https://openalternative.co/excalidraw · https://www.libhunt.com/compare-penpot-vs-excalidraw · https://storyflow.so/blog/best-excalidraw-alternatives-2026
- https://www.figma.com/resource-library/ai-design-tools/ · https://open-design.ai/blog/best-ai-design-tools/ · https://designtools.fyi/facets/ui-generation · https://github.com/narrowin/awesome-generative-ui · https://dev.to/hadil/24-best-ai-design-tools-for-designers-and-developers-in-2026-i1h
- https://www.tasteskill.dev/ · https://www.x-cmd.com/install/taste-skill/ · https://apito.ai/en/blog/seo/ai-frontend-template-look-taste-skill/ · https://github.com/maxbogo/awesome-ai-tools-for-ui
- https://refactoringui.com/ · https://github.com/klaufel/awesome-design-systems · https://github.com/bradtraversy/design-resources-for-developers · https://designsystemsrepo.com/design-systems/ · https://designsystems.surf/design-systems
- https://github.com/copilotkit/copilotkit · https://github.com/ag-ui-protocol/ag-ui · https://techcrunch.com/2026/05/05/copilotkit-raises-27m-to-help-devs-deploy-app-native-ai-agents/ · https://alatirok.com/best-ai-agent-chat-ui-library/
