# 04 · Protocols & Standards cho hệ sinh thái Agent

> Các giao thức/định dạng mở giúp agent nói chuyện với tool, với agent khác, với UI và với hướng dẫn của dự án.

## 1. Bản đồ giao thức

| Lớp | Giao thức | Chủ quản | Mốc | Vai trò |
|---|---|---|---|---|
| Agent ↔ Tool/Data | **MCP** (Model Context Protocol) | Anthropic → Agentic AI Foundation (AAIF, Linux Foundation, 12/2025) | 11/2024 ra mắt; >10k server production (2026) | Chuẩn kết nối tool, resource, prompt |
| Agent ↔ Agent | **A2A** (Agent2Agent) | Google → Linux Foundation (6/2025) | v1.0 3/2026, v1.0.1 5/2026; >150 tổ chức (4/2026) | Task state, long-running, agent card; có nguồn nói chuyển vào AAIF 20/8/2026 **(chưa xác minh)** |
| Agent ↔ UI | **AG-UI** (Agent-User Interaction) | CopilotKit | 2025–2026; AWS AgentCore, MS Agent Framework, Oracle Agent Spec/A2UI tích hợp | Stream sự kiện agent → frontend, generative UI |
| Agent ↔ Kỹ năng | **Agent Skills / SKILL.md** | Anthropic → chuẩn mở agentskills.io (18/12/2025) | Ra mắt 16/10/2025; OpenAI, Microsoft hỗ trợ trong ~48h; ~40 sản phẩm (Copilot, VS Code, Gemini CLI, Cursor 2.4) | Gói hướng dẫn + script tải theo nhu cầu |
| Agent ↔ Dự án | **AGENTS.md** | OpenAI → Agentic AI Foundation (Linux Foundation), repo `agentsmd/agents.md` | 2025; hơn 60k dự án (12/10/2026) | File hướng dẫn chung cho nhiều tool |
| Editor ↔ Coding agent | **ACP** (Agent Client Protocol) | Zed → `agentclientprotocol/` | Schema v1.25.0 (9/10/2026) | Một giao thức để editor (Zed, JetBrains, Neovim, Emacs) gọi coding agent bất kỳ |
| (legacy) | `.cursorrules` → `.cursor/rules/*.mdc` | Cursor | – | Đã lỗi thời; chuyển sang skills/AGENTS.md |

## 2. MCP chi tiết

- **Repo chính:** `modelcontextprotocol/servers` (~91,2k★, 12/10/2026) – 7 reference server: Everything, Fetch, Filesystem, Git, Memory, Sequential Thinking, Time; README nay ghi "not production-ready", bỏ mục Official Integrations và trỏ sang MCP Registry.
- **SDK/framework:** `prefecthq/fastmcp` (~23k★, Python), SDK chính thức TS/Python/Java/C#/Kotlin.
- **Server phổ biến nhất (theo nhiều roundup):** GitHub, Context7 (docs), Playwright (browser), Filesystem/Fetch, Tavily (search).
- **Danh sách:** `punkpeye/awesome-mcp-servers` (96,2k★), `VoltAgent/official-mcp-servers` (chỉ server chính chủ, xem §2c), `wong2/awesome-mcp-servers` (ngừng nhận PR), `sadekxD/Awesome-MCP`.
- **Rủi ro:** prompt injection qua tool output, quyền truy cập quá rộng → cần allowlist và sandbox.
- **Đóng gói & tính năng ít dùng (từ repo của chủ kho, mục 23):** `.mcpb` — manifest đóng gói MCP server một-click cho Claude Desktop (Dhcb-Tools `tools/mcpb/manifest.json`); **MCP prompts + completion** và WebMCP declarations (`@modelcontextprotocol/server` 2.0.0-beta, REA `docs/mcp-prompts.md`); MCP Streamable HTTP với `Mcp-Session-Id` (ai-gateway). Mẫu thiết kế: "MCP tool là agent-computer interface" — ít tool, tên tham số tra được (`parameters_of`), không đoán; cho model local chỉ lộ ≤8 tool (`--group`).

## 2b. Repo chính thức & SDK đã xác minh (2026-10-12)

| Repo | ★ (12/10) | License | Phát hành / hoạt động gần nhất | Vai trò & điểm chất lượng | Lưu ý |
|---|---|---|---|---|---|
| **modelcontextprotocol/python-sdk** | 24,6k | MIT | v2.3.0 (2/10/2026), commit 12/10 | SDK Python chính thức cho MCP server/client: stdio, Streamable HTTP, SSE; có hướng dẫn chuyển lên v2 | v2 có thay đổi phá vỡ; bỏ Python 3.10 từ 12/10/2026 |
| **modelcontextprotocol/typescript-sdk** | 13,6k | Apache-2.0 (code mới) / MIT (code cũ) | 2.3.1 (5/10/2026) | Hiện thực spec 2026-07-28; tách gói server/client, middleware Express/Fastify/Hono | v2 tách gói; v1.x chỉ còn sửa lỗi và bảo mật |
| **modelcontextprotocol/inspector** | 11,1k | đang chuyển MIT → Apache-2.0 | 2.10.1 (8/10/2026) | Công cụ test MCP server dạng UI và CLI (dùng được trong CI và vòng phản hồi của agent); secret lưu vào keychain hệ điều hành | Không có keychain thì `secrets.json` không mã hoá; v1 chỉ còn vá bảo mật |
| **modelcontextprotocol/registry** | 7,3k | Apache-2.0 (một phần đang chuyển MIT/CC-BY-4.0) | tag v1.8.1 (6/8/2026) | Registry chính thức của cộng đồng cho MCP server, do MCP Registry WG (Stacklok, PulseMCP…) vận hành; API đóng băng ở v0.1 từ 10/2025 | README vẫn ghi "preview", dữ liệu có thể bị reset; chưa GA |
| **modelcontextprotocol/ext-apps** | 2,9k | Apache-2.0 | 2.0.3, commit 25/9/2026 | Extension chính thức **MCP Apps**: spec + SDK nhúng UI vào host (ChatGPT, Claude, VS Code, Goose, Postman); spec 2026-01-26 ổn định | Mức hỗ trợ khác nhau giữa các host; thay thế `MCP-UI-Org/mcp-ui` (5,2k★) |
| **agentclientprotocol/agent-client-protocol** (ACP của Zed) | 4,4k | Apache-2.0 | Schema v1.25.0 (9/10/2026) | Giao thức nối editor bất kỳ với coding agent bất kỳ; client: Zed, JetBrains, Neovim, Emacs, extension VS Code; SDK 5 ngôn ngữ | Trùng tên với ACP của IBM (đã archive); schema v2 còn alpha |
| **agentsmd/agents.md** | 24,9k | MIT | commit 10/9/2026 | Định dạng mở AGENTS.md, hơn 60k dự án dùng; do Agentic AI Foundation (Linux Foundation) quản; Codex, Cursor, Copilot hỗ trợ | Là quy ước, không phải schema; repo chủ yếu là website (38 commit) |

**Nhận xét:**

- **Hai giao thức "ACP" khác nhau:** Agent **Client** Protocol (Zed, nay ở `agentclientprotocol/`, nối editor với coding agent, đang hoạt động; Jupyter AI ở mục 15 dùng giao thức này) và Agent **Communication** Protocol (IBM, `i-am-bee/acp`, **archive 27/8/2025, đã nhập vào A2A**). Bảng §1 và §3 đã sửa theo.
- MCP TypeScript SDK v2 đã nhắm spec 2026-07-28; REA đang dùng `@modelcontextprotocol/server` 2.0.0-beta (§2) nên cân nhắc lên 2.3.x ổn định.
- AGNTCY ("Internet of Agents", Linux Foundation) không có repo chủ lực, mọi repo dưới 400★ — chưa đáng theo dõi.

## 2c. Danh mục MCP server "chính thức": VoltAgent/official-mcp-servers (ảnh người dùng gửi, 2026-10-12)

| Mục | Thông tin (12/10/2026) |
|---|---|
| Repo | `VoltAgent/official-mcp-servers` · 302★, 45 fork, MIT, tạo 1/10/2026, 26 commit |
| Lời hứa | "A curated directory of 280+ official MCP servers from the companies behind the products. No unofficial forks, no abandoned projects." |
| Thực tế | README có **297 mục** trong 14 nhóm (badge "286" là số gõ tay; badge "Last update today" chỉ là ngày commit cuối, không nói gì về các server); 202 mục là repo GitHub, 95 mục chỉ trỏ tới docs hoặc endpoint hosted |
| Cơ chế kiểm | **Không có kiểm tra tự động** (repo không có `.github/`); README tự ghi "curated, not audited"; CONTRIBUTING nhận cả "a widely used open source project", nên "official" không tuyệt đối |
| Chủ list | VoltAgent (framework agent TypeScript, `VoltAgent/voltagent` 10,8k★); list có cả MCP server của chính họ. Cùng chủ: awesome-design-md (120k★), awesome-agent-skills (36k★), awesome-claude-code-subagents (26k★) |

**Kiểm 201 repo GitHub trong list** (metadata ecosyste.ms, trạng thái archive xác nhận trực tiếp trên GitHub):

- **11 repo đã archive (5,5%)**: `PostHog/mcp`, `semgrep/mcp`, `browserbase/mcp-server-browserbase`, `elevenlabs/elevenlabs-mcp`, `tinybirdco/mcp-tinybird`, `e2b-dev/mcp-server`, `axiomhq/mcp-server-axiom`, oxylabs-mcp, `box-community/mcp-server-box`, `chargebee/agentkit`, `incident-io/incidentio-mcp-golang` — phần lớn vì hãng đã chuyển sang **server hosted (remote MCP)** hoặc gộp vào monorepo.
- **Khoảng 21 repo không push hơn 6 tháng** (15 repo chắc chắn, 6 repo **chưa xác minh**), ví dụ `langfuse/mcp-server-langfuse` (2/2025), `JetBrains/mcp-jetbrains` (README ghi "Deprecated… no longer maintained").
- **Không chính chủ hoặc trái luật của list:** `ahujasid/blender-mcp` (nay chuyển hướng sang `ahujasid/mcp-for-blender`) tự ghi "third-party… not made by Blender"; `google/mcp` tự ghi "not an officially supported Google product"; 4 repo gần như 0★ (Invompt, Desearch, bestax, BulkPublish) được merge ngay tuần đầu dù luật cấm "brand new projects".

**Bối cảnh các danh mục khác:** `punkpeye/awesome-mcp-servers` 96,2k★ (~4.200 dòng, không lọc chính chủ); `modelcontextprotocol/servers` 91,2k★ — README **đã bỏ mục "Official Integrations"**, chỉ còn 7 reference server ghi "not production-ready" và trỏ sang MCP Registry (§2b); `wong2/awesome-mcp-servers` 4,4k★ ngừng nhận PR (chuyển sang mcpservers.org); Glama ghi 97.619 server, Smithery 26.257+ server. List của VoltAgent lấp đúng khoảng trống "server chính chủ" mà repo chính thức đã bỏ.

**Cách dùng:** coi là điểm khởi đầu tìm server của chính hãng, nhưng trước khi cài vẫn tự kiểm 3 điều: (1) repo không archive và còn commit; (2) owner đúng là hãng; (3) hãng đã có bản hosted (remote MCP) thay cho repo local chưa — xu hướng 2026 là server local bị archive để chuyển sang endpoint hosted. Tra metadata ở MCP Registry chính thức khi có.

## 3. MCP vs A2A

| | MCP | A2A |
|---|---|---|
| Kết nối | Agent ↔ tool/data | Agent ↔ agent |
| Trạng thái | Phần lớn stateless | Task state tường minh, long-running |
| Khi dùng | Hầu hết ứng dụng, bắt đầu từ đây | Multi-agent vượt ranh giới tổ chức |
| Bổ sung | ACP (IBM) — đã archive 27/8/2025 và nhập vào A2A; ANP | |

## 4. SKILL.md vs AGENTS.md vs CLAUDE.md vs .cursorrules

- **SKILL.md**: YAML frontmatter (name, description) + hướng dẫn + file đính kèm; nạp "progressive disclosure" khi tác vụ khớp. Đặt tại `.claude/skills/`, `.agents/skills/`, `.cursor/skills/`, `.codex/skills/`.
- **AGENTS.md**: hướng dẫn luôn-nạp cho toàn repo, trung lập tool. Khuyến nghị cho team đa tool; skills là lớp bổ sung "gọi được".
- **CLAUDE.md**: tương đương AGENTS.md trong Claude Code (hỗ trợ import, phân cấp thư mục).
- **.cursorrules**: legacy; chuyển đổi = thêm frontmatter + đưa vào thư mục skills/rules.
- **Bộ file cho đa harness** (quan sát trong 19 repo của chủ kho, 2026-10-12): `CLAUDE.md` dùng `@import` để trỏ về AGENTS.md; bridge mỏng `GEMINI.md`, `.clinerules`, `.windsurfrules`, `.cursor/rules/*.mdc`, `.github/copilot-instructions.md` chỉ chứa một dòng "đọc AGENTS.md"; **Antigravity** dùng `.agents/rules/*.md`, `.agents/workflows/*.md`, `.agents/mcp_config.json` và `.agents/skills/`; Hermes Agent đọc SKILL.md có `metadata.hermes`; Codex đọc `AGENTS.md` + `.codex/skills/`. Bẫy thật: `next dev` ghi đè `AGENTS.md` (case-study-ft41) → giữ bản gốc trong `docs/` và kiểm bằng script.
- **Danh sách:** `VoltAgent/awesome-agent-skills` (1000+ skills), `spencerpauly/awesome-cursor-skills`, `PatrickJS/awesome-cursorrules`.

## 5. Nguồn

- https://en.wikipedia.org/wiki/Model_Context_Protocol · https://github.com/wong2/awesome-mcp-servers · https://github.com/sadekxD/Awesome-MCP · https://uibakery.io/blog/best-mcp-servers
- https://www.mintmcp.com/blog/a2a-vs-mcp · https://crystl.dev/blog/agent-communication-protocols/ · https://stellagent.ai/insights/a2a-protocol-google-agent-to-agent · https://www.flowhunt.io/blog/agentic-ai-foundation-a2a-mcp-standards/ · https://techiehub.blog/what-is-the-a2a-protocol/
- https://github.com/ag-ui-protocol/ag-ui · https://blogs.oracle.com/ai-and-datascience/announcing-agent-spec-for-a2ui-copilotkit-ag-ui · https://aws.amazon.com/blogs/machine-learning/build-generative-ui-for-ai-agents-on-amazon-bedrock-agentcore-with-the-ag-ui-protocol/ · https://learn.microsoft.com/en-us/agent-framework/integrations/ag-ui/
- https://blog.buildbetter.ai/agents-md-vs-cursorrules-vs-claude-skills-2026-comparison/ · https://meshlaunch.com/en/blog/2026-cursor-agent-skills-complete-guide.html · https://codersera.com/blog/agents-md-vs-claude-md-vs-cursor-rules-comparison-2026/ · https://dev.to/creeta/one-skillmd-replaces-claudemd-agentsmd-and-cursorrules-5a70
- §2b (12/10/2026): https://github.com/modelcontextprotocol/python-sdk · https://github.com/modelcontextprotocol/typescript-sdk · https://github.com/modelcontextprotocol/inspector · https://github.com/modelcontextprotocol/registry · https://github.com/modelcontextprotocol/ext-apps · https://github.com/MCP-UI-Org/mcp-ui · https://github.com/agentclientprotocol/agent-client-protocol · https://agentclientprotocol.com/get-started/clients · https://github.com/agentsmd/agents.md · https://agents.md/ · https://github.com/i-am-bee/acp · https://github.com/agntcy
- §2c (12/10/2026): https://github.com/VoltAgent/official-mcp-servers · https://raw.githubusercontent.com/VoltAgent/official-mcp-servers/main/CONTRIBUTING.md · https://repos.ecosyste.ms/api/v1/hosts/GitHub/repositories/VoltAgent%2Fofficial-mcp-servers · https://github.com/orgs/VoltAgent/repositories · https://github.com/VoltAgent/voltagent · https://github.com/PostHog/mcp · https://github.com/semgrep/mcp · https://github.com/browserbase/mcp-server-browserbase · https://github.com/elevenlabs/elevenlabs-mcp · https://github.com/JetBrains/mcp-jetbrains · https://github.com/langfuse/mcp-server-langfuse · https://github.com/ahujasid/mcp-for-blender · https://github.com/google/mcp · https://github.com/modelcontextprotocol/servers · https://github.com/punkpeye/awesome-mcp-servers · https://github.com/wong2/awesome-mcp-servers · https://glama.ai/mcp/servers · https://smithery.ai
