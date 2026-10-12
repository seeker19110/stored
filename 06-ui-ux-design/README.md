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

## 7. Nguồn
- https://designrevision.com/blog/best-react-component-libraries · https://designrevision.com/blog/best-tailwind-component-libraries · https://dualite.dev/blogs/best-ui-component-libraries · https://www.uilora.com/blog/uilora/10-best-react-ui-component-libraries-in-2026-ranked-by-a-frontend-team · https://www.techwench.com/best-ui-component-libraries-2026/
- https://www.opensourcealternatives.to/item/penpot · https://openalternative.co/excalidraw · https://www.libhunt.com/compare-penpot-vs-excalidraw · https://storyflow.so/blog/best-excalidraw-alternatives-2026
- https://www.figma.com/resource-library/ai-design-tools/ · https://open-design.ai/blog/best-ai-design-tools/ · https://designtools.fyi/facets/ui-generation · https://github.com/narrowin/awesome-generative-ui · https://dev.to/hadil/24-best-ai-design-tools-for-designers-and-developers-in-2026-i1h
- https://www.tasteskill.dev/ · https://www.x-cmd.com/install/taste-skill/ · https://apito.ai/en/blog/seo/ai-frontend-template-look-taste-skill/ · https://github.com/maxbogo/awesome-ai-tools-for-ui
- https://refactoringui.com/ · https://github.com/klaufel/awesome-design-systems · https://github.com/bradtraversy/design-resources-for-developers · https://designsystemsrepo.com/design-systems/ · https://designsystems.surf/design-systems
- https://github.com/copilotkit/copilotkit · https://github.com/ag-ui-protocol/ag-ui · https://techcrunch.com/2026/05/05/copilotkit-raises-27m-to-help-devs-deploy-app-native-ai-agents/ · https://alatirok.com/best-ai-agent-chat-ui-library/
