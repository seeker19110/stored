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
- **Thêm từ repo của chủ kho (mục 23, 2026-10-12):** `impeccable` (plugin/skill "taste" được case-study-ft41 ghi trong `ui-ux-intelligence-provider.md`), `nextlevelbuilder/ui-ux-pro-max-skill` (45 file, vendor trong Hermes-Agents), `google-labs-code/design.md` (file DESIGN.md mô tả hệ thiết kế cho agent), `popular-web-designs` (54 design system tóm tắt). xboss có cổng tĩnh `check:contrast` + `check:ui-ux-guard` và Lighthouse CI chặn merge 4 category — "taste" chỉ bền khi có cổng máy đi kèm.

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
| Skill sơ đồ "diagram-as-code" | Mermaid skills (design-doc-mermaid ~44k install), Excalidraw skills (~28.7k install, Kroki/CLI export), Garry Tan `diagram` (Mermaid → Excalidraw editable), `diagram-design` (41 loại, branded) | Sơ đồ 2D trừu tượng; Anatomy là **minh họa vật thể 3D-isometric có mô phỏng** |
| Skill thẩm mỹ frontend | Taste Skill (mục 4 ở trên), Refactoring UI skill, `ibelick/ui-skills` (~9.4k★, directory chứa Anatomy cùng animated-sprites, animation-vocabulary, antfu-design, beautiful-shadows) | Anatomy nằm ở nhánh "visual/craft" của cùng hệ sinh thái |
| Motion/video skills | claude-motion-design, awesome-claude-video-skills (mục 19) | Video/animation thay vì SVG tương tác |

### Nhận xét & bài học

1. **Skill kèm kit + audit + eval** là mẫu đáng học: thay vì chỉ prompt, skill mang theo thư viện hình học không phụ thuộc, script kiểm chứng bằng máy (audit hình học, đếm line end, screenshot 4×) và bộ prompt eval. Đây là "evidence or it's a FAIL" (mục 09) áp vào đồ họa.
2. **Sizing trước khi làm** (Figure/Hero/Epic + ước tính thời gian, hỏi người dùng) là cách kiểm soát chi phí token/thời gian rõ ràng, giống gate `[BLOCKER]`/approval ở mục 09 và 19.
3. **"Truth first"**: readout và chuyển động lấy từ một model số nhỏ → tránh minh họa "đẹp nhưng sai"; tái dùng cho dataviz và explainer.
4. **Rủi ro:** dự án 2 ngày tuổi, 1 contributor chính; build 30 phút–6 giờ mỗi hình rất tốn token; phụ thuộc Chrome headless; chưa có đánh giá độc lập (bài ai.sulat.com không truy cập được, 403). Số sao tăng nhanh nhờ bài đăng X ngày 10/10 và lan sang Weibo.
5. Liên hệ: mục 04 (chuẩn Agent Skills, cài qua `skills` CLI), mục 06 §4 (Taste Skill), mục 19 (motion skills), mục 09 (kiểm chứng bằng máy).

**Nguồn:** https://github.com/wheresryan22/anatomy (README, SKILL.md, releases/v1.0.0, commits) · https://github.com/wheresryan22 · https://github.com/wheresryan22/anatomy-figures · https://x.com/wheresryan22/status/2108948624004526516 · https://www.ui-skills.com/skills/wheresryan22/anatomy · https://www.skills.sh/wheresryan22/anatomy/anatomy · https://skillselion.com/guides/best-diagram-skills-for-claude-code · https://aipptskill.com/blog/ai-diagram-skills-guide/ · https://open-design.ai/skills/diagram/ · https://skillselion.com/guides/diagram-design-skill-claude-code-guide

## 8. Nguồn (mục 1–6)

- https://designrevision.com/blog/best-react-component-libraries · https://designrevision.com/blog/best-tailwind-component-libraries · https://dualite.dev/blogs/best-ui-component-libraries · https://www.uilora.com/blog/uilora/10-best-react-ui-component-libraries-in-2026-ranked-by-a-frontend-team · https://www.techwench.com/best-ui-component-libraries-2026/
- https://www.opensourcealternatives.to/item/penpot · https://openalternative.co/excalidraw · https://www.libhunt.com/compare-penpot-vs-excalidraw · https://storyflow.so/blog/best-excalidraw-alternatives-2026
- https://www.figma.com/resource-library/ai-design-tools/ · https://open-design.ai/blog/best-ai-design-tools/ · https://designtools.fyi/facets/ui-generation · https://github.com/narrowin/awesome-generative-ui · https://dev.to/hadil/24-best-ai-design-tools-for-designers-and-developers-in-2026-i1h
- https://www.tasteskill.dev/ · https://www.x-cmd.com/install/taste-skill/ · https://apito.ai/en/blog/seo/ai-frontend-template-look-taste-skill/ · https://github.com/maxbogo/awesome-ai-tools-for-ui
- https://refactoringui.com/ · https://github.com/klaufel/awesome-design-systems · https://github.com/bradtraversy/design-resources-for-developers · https://designsystemsrepo.com/design-systems/ · https://designsystems.surf/design-systems
- https://github.com/copilotkit/copilotkit · https://github.com/ag-ui-protocol/ag-ui · https://techcrunch.com/2026/05/05/copilotkit-raises-27m-to-help-devs-deploy-app-native-ai-agents/ · https://alatirok.com/best-ai-agent-chat-ui-library/
