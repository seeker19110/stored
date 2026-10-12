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

- **Repo chính:** `modelcontextprotocol/servers` (~87k★) – reference servers: Everything, Fetch, Filesystem, Git, Memory, Sequential Thinking, Time.
- **SDK/framework:** `prefecthq/fastmcp` (~23k★, Python), SDK chính thức TS/Python/Java/C#/Kotlin.
- **Server phổ biến nhất (theo nhiều roundup):** GitHub, Context7 (docs), Playwright (browser), Filesystem/Fetch, Tavily (search).
- **Danh sách:** `wong2/awesome-mcp-servers`, `sadekxD/Awesome-MCP`, `punkpeye/awesome-mcp-servers`.
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
