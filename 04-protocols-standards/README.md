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

## 4b. Nâng cấp 31/10/2026: rà repo lớn

> Hai việc. (1) Đọc lại số sao, license, ngày push của mọi repo mục 04 trong catalog bằng GitHub search API (31/10/2026). (2) Tìm repo lớn còn thiếu: 8 truy vấn (topic `mcp`, `a2a`, `mcp-gateway`; từ khoá "model context protocol", "agent protocol", "agent skills specification", "a2ui"; repo tạo sau 1/10/2025). Lọc trùng với toàn catalog, chọn **6 repo** gần chủ đề "giao thức và chuẩn" nhất, clone `--filter=blob:none` đủ lịch sử, đọc LICENSE, manifest, cấu trúc, CI, file nguồn chính và grep telemetry. **Không cài, không chạy script nào.**

### 4b.1 Repo cũ: điều đã đổi

| Repo | Thay đổi (12/10 → 31/10/2026) | Hệ quả |
|---|---|---|
| **Spec MCP** (bản `2026-07-28`) | Changelog chính thức: **bỏ `Mcp-Session-Id` và phiên ở tầng giao thức**, bỏ bắt tay `initialize`, thêm `server/discover`, mỗi request mang version và capability trong `_meta`; bỏ `ping`, `logging/setLevel`; tasks chuyển thành extension | Dòng "MCP Streamable HTTP với `Mcp-Session-Id` (ai-gateway)" ở §2 đã lỗi thời theo spec mới; server/gateway tự viết cần lộ trình sang stateless. Chi tiết ở 4b.3 |
| `prefecthq/fastmcp` | ~23k → **28,3k** (+23%) | Tăng nhanh nhất mục; vẫn là framework Python phổ biến nhất |
| `a2aproject/A2A` | Bảng §1 chưa có số → **26,4k**, push 30/10 | Catalog bổ sung số sao |
| `ag-ui-protocol/ag-ui` | **16,9k**, push 30/10 | Lần đầu ghi số trong README |
| `modelcontextprotocol/servers` | 91,2k → 91,7k; GitHub báo `NOASSERTION` | Không phải đổi license: cả tổ chức đang chuyển MIT → Apache-2.0 (code) và CC-BY-4.0 (docs), file LICENSE là văn bản chuyển tiếp nên GitHub không nhận dạng được. Tương tự `typescript-sdk`, `inspector`, `registry`, `ext-apps` |
| `agentsmd/agents.md` | 24,9k → 25,2k; **commit cuối vẫn 10/9/2026** | Bảy tuần không commit; là quy ước ổn định nên chưa đáng lo, nhưng đừng chờ thay đổi từ repo này |
| `VoltAgent/official-mcp-servers` | 302 → **405** (+34%) | §2c vẫn đúng về cơ chế |
| `VoltAgent/awesome-agent-skills` · `punkpeye/awesome-mcp-servers` | Chưa có số → **36,7k** · 96,2k → 97,1k | Catalog bổ sung số sao |
| SDK, inspector, registry, ACP | Dao động dưới 3% | Không đổi nhận định |

### 4b.2 Bảng nhanh 6 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `modelcontextprotocol/modelcontextprotocol` | Spec MCP | 9,6k · đang chuyển MIT → Apache-2.0 (`NOASSERTION`) | 31/10/2026 | Nguồn gốc spec + schema TS/JSON, 6 bản (2024-11-05 → 2026-07-28 + draft), 48 SEP | README vẫn ghi MIT |
| `agentskills/agentskills` | Spec Agent Skills | 26,8k · Apache-2.0 (docs CC-BY-4.0) | 9/8/2026 | Spec SKILL.md + thư viện kiểm `skills-ref` | Không CI; 12 tuần đứng yên |
| `a2ui-project/a2ui` | Chuẩn Agent → UI | 16,9k · Apache-2.0 | 30/10/2026 | JSON khai báo UI, renderer Lit/Angular/Flutter/Swift/Kotlin, bộ conformance | Vẫn "public preview"; trước là `google/A2UI` |
| `github/github-mcp-server` | MCP server chính chủ | 34,1k · MIT | 28/10/2026 | Server GitHub chính thức (Go), bản hosted `api.githubcopilot.com/mcp/` | Ghi được vào repo nếu không bật `--read-only` |
| `mcp-use/mcp-use` | Framework MCP | 10,8k · MIT | 30/10/2026 | SDK Python/TS dựng MCP server, MCP Apps, agent client | **Telemetry gửi cả câu hỏi và câu trả lời** |
| `agentgateway/agentgateway` | Gateway MCP/A2A | 5,8k · Apache-2.0 | 30/10/2026 | Proxy Rust cho MCP, A2A, LLM; dự án LF Projects do Solo.io dẫn | Hạ tầng nặng (Kubernetes, CEL) |

### 4b.3 Hồ sơ từng repo

- **`modelcontextprotocol/modelcontextprotocol` (spec).** 4.932 commit từ 24/9/2024, 472 tác giả, 977 commit từ 1/5/2026; 6,2% commit có trailer Claude. Schema viết TypeScript trước (`schema/2026-07-28/schema.ts`, 3.197 dòng) rồi xuất JSON Schema. Có quy trình SEP thật: 48 file trong `seps/`, workflow `sep-lifecycle.yml`, `sep-reminder.yml`. `AI_POLICY.md` **bắt buộc khai báo** mọi trợ giúp AI trong PR/issue. Bản `2026-07-28` là đổi lớn nhất từ khi ra mắt: stateless, `subscriptions/listen` thay GET/SSE, mẫu **MRTR** (`input_required`) thay request từ server (sampling, elicitation), mọi kết quả list có `ttlMs`/`cacheScope`, `tools/list` nên trả theo thứ tự cố định để tăng cache hit, client **MUST** kiểm `iss` (RFC 9207). Mâu thuẫn: README ghi "licensed under the MIT License" ❌, LICENSE ghi đang chuyển sang Apache-2.0. Không phải phần mềm để cài; đọc tại modelcontextprotocol.io/specification.
- **`agentskills/agentskills`.** 145 commit, 44 tác giả, Jonathan Hefner (Anthropic) 91 commit; 39% commit có trailer Claude. Gồm spec (`docs/specification.mdx`), hướng dẫn viết và **eval skill** (`evaluating-skills.mdx`, `optimizing-descriptions.mdx`), và `skills-ref` (Python): `validator.py` kiểm đúng các giới hạn spec ghi (name ≤ 64 ký tự, chữ thường, không `--`, khớp tên thư mục; description ≤ 1024; compatibility ≤ 500; chỉ 6 trường frontmatter) ✅. Lệch nhỏ: validator nhận chữ Unicode (i18n), spec ghi "lowercase letters, numbers, and hyphens" ⚠️. README `skills-ref` tự ghi "demonstration purposes only". Repo không có `.github/`, tức **không CI**; test có nhưng không ai chạy tự động. Commit cuối 9/8/2026 chỉ thêm OpenClaw, Hermes Agent vào danh sách client. Kiểm skill: `uvx --from git+https://github.com/agentskills/agentskills#subdirectory=skills-ref skills-ref validate <thư-mục>` **(lệnh suy từ pyproject, chưa chạy)**.
- **`a2ui-project/a2ui`.** 1.696 commit từ 26/9/2025, 110 tác giả, 706 commit từ email `google.com`; không commit nào có trailer Claude (repo dùng `.gemini/`). Spec có 4 bản `v0_8`, `v0_9`, `v0_9_1`, `v1_0` (RC); README ghi bản production là 0.9.1 và "Early stage public preview". Lời "agent chỉ được yêu cầu component có trong catalog tin cậy" có cơ chế thật: `conformance/core/catalog.yaml` và `validator_v*.yaml` định nghĩa bộ test chung cho mọi SDK ✅. Điểm cần canh: **catalog MCP** (`catalogs/mcp/`) cho phép payload UI gọi `callMcpTool` theo tên tool, và component `McpApp` nhúng MCP App vào surface — tức UI do agent sinh có thể kích hoạt tool; host phải tự lọc tool nào được gọi. 19 workflow CI (conformance, eval, kiểm spec). Liên quan AG-UI §1 và mục 06 §7p.6.
- **`github/github-mcp-server`.** 1.200 commit, 194 tác giả, Go; bản v2.0.3 (21/10/2026). Kiểm soát quyền làm tốt: `--toolsets`, `--tools`, `--exclude-tools`, `--read-only` (ưu tiên hơn `--tools`) ✅; **lockdown mode** chỉ trả nội dung public do người có quyền push viết, README tự nói rõ là "best-effort content filter… not an authorization boundary" và miễn trừ `github-actions[bot]`, `copilot`. Chế độ HTTP: `--listen-host` để trống thì **nghe trên mọi interface**; header `X-MCP-Lockdown` chỉ bật thêm được, không tắt được lockdown do người vận hành đặt. Không thấy telemetry trong mã. Cài: `claude mcp add github -e GITHUB_PERSONAL_ACCESS_TOKEN=$GITHUB_PAT -- docker run -i --rm -e GITHUB_PERSONAL_ACCESS_TOKEN ghcr.io/github/github-mcp-server` (thêm `-e GITHUB_READ_ONLY=1` hoặc cờ `--read-only` cho agent không cần ghi).
- **`mcp-use/mcp-use`.** 1.693 commit, 68 tác giả; SDK Python và TypeScript (client, agent, server, inspector, MCP Apps). **Telemetry bật mặc định, gửi tới PostHog EU (`eu.i.posthog.com`, key viết cứng) và Scarf.** `telemetry/events.py` và `telemetry.py` cho thấy sự kiện `mcp_agent_execution` mang **nguyên văn `query` và `response`** của agent, cùng tên tool, model; docs tự ghi "Query and response content" nhưng vẫn gọi là "anonymized" ❌. Tắt bằng `MCP_USE_ANONYMIZED_TELEMETRY=false` (Python không đọc `DO_NOT_TRACK`). Ngoài telemetry, repo hoạt động tốt (CI conformance, e2e inspector, eval SDK). Cài: `pip install mcp-use` hoặc `npm install --save-dev @mcp-use/client`, nhớ đặt biến tắt telemetry trước.
- **`agentgateway/agentgateway`.** 3.180 commit từ 18/3/2025, 307 tác giả, 2.022 commit từ email `solo.io`; `CHARTER.md` xác nhận là "a Series of LF Projects". Rust (15 crate) + controller Go cho Kubernetes Gateway API; proxy MCP, A2A và LLM với RBAC qua CEL, JWT/OAuth, rate limit, guardrail, OpenTelemetry. File `analytics.go` chỉ là lệnh xem log request cục bộ (token, chi phí, TTFT), không gửi ra ngoài ✅. Lời "the first complete connectivity solution" không kiểm được. Bản v1.7.0 (27/10/2026); quickstart chỉ có trên agentgateway.dev **(chưa đọc)**. Chưa kiểm hỗ trợ spec MCP 2026-07-28.

### 4b.4 Mẫu chung rút ra

1. **Chuẩn đã có "cổng máy" đi kèm:** MCP có schema JSON + SEP lifecycle, Agent Skills có `skills-ref validate`, A2UI có bộ conformance YAML dùng chung cho mọi SDK. Dự án dùng chuẩn nên chạy validator chính thức trong CI thay vì tự viết.
2. **MCP đang bỏ trạng thái phiên.** Ai đã dựa vào `Mcp-Session-Id`, SSE resumable hay request từ server (sampling/elicitation) phải chuyển sang handle tường minh và MRTR.
3. **Lọc nội dung chống prompt injection không phải ranh giới quyền:** github-mcp-server nói thẳng điều này về lockdown mode; vẫn cần `--read-only` và token tối thiểu.
4. **Telemetry trong SDK giao thức là rủi ro dữ liệu thật:** mcp-use gửi nguyên văn hội thoại. Đặt biến tắt riêng của từng SDK, đừng chỉ dựa vào `DO_NOT_TRACK`.
5. **License đang chuyển tiếp làm GitHub báo `NOASSERTION`** (cả tổ chức modelcontextprotocol): đọc file LICENSE, đừng đọc nhãn.

**Nguồn §4b (31/10/2026):** GitHub search API (`repo:` cho repo cũ, 8 truy vấn topic/từ khoá) · clone `--filter=blob:none`: modelcontextprotocol/modelcontextprotocol (README.md, LICENSE, AI_POLICY.md, GOVERNANCE.md, `docs/specification/2026-07-28/changelog.mdx`, `schema/*`, `seps/`, `.github/workflows/`), agentskills/agentskills (README.md, `docs/specification.mdx`, `skills-ref/src/skills_ref/validator.py`, `skills-ref/README.md`, `.claude/hooks/session-start.sh`), a2ui-project/a2ui (README.md, `specification/`, `conformance/core/catalog.yaml`, `catalogs/mcp/README.md`, workflows), github/github-mcp-server (README.md mục Toolsets và Lockdown Mode, `cmd/github-mcp-server/main.go`, tag v2.0.3), mcp-use/mcp-use (`libraries/python/mcp_use/telemetry/{telemetry,events}.py`, `libraries/typescript/packages/client/src/telemetry/telemetry.ts`, `docs/python/development/telemetry.mdx`, `libraries/python/mcp_use/agents/mcpagent.py`), agentgateway/agentgateway (README.md, CHARTER.md, `crates/`, `controller/pkg/cli/standalone/analytics.go`) · https://modelcontextprotocol.io/specification · https://github.com/a2ui-project/a2ui · https://agentgateway.dev

## 4c. Nâng trần 2/11/2026: bộ conformance, inspector có eval, chuẩn đóng gói và scanner cho MCP/A2A (yêu cầu người dùng)

> Tìm repo **chưa có trong catalog** ở ba lớp: chuẩn, cổng máy, đầu bảng. GitHub search API 2/11/2026 (`repo:` cho từng repo, 6 truy vấn từ khoá). Clone `--depth 1 --filter=blob:none`, đọc LICENSE, README, manifest, CI, file chính. **Không cài, không chạy.**

**Trần hiện tại:**

- Mục đã có spec (§4b `modelcontextprotocol/modelcontextprotocol`, `agentskills/agentskills`, A2UI), SDK, inspector chính thức, registry (§2b) và một validator nhẹ (`skills-ref`, §4b.3). Tức là đủ để **viết** server, chưa đủ để **chứng minh** server/client đúng spec.
- Chưa có bộ test conformance nào cho MCP hay A2A, nên "hỗ trợ spec 2026-07-28" (§4b.3, agentgateway) vẫn là lời tự nhận.
- Chưa có lớp đóng gói chuẩn (`.mcpb` chỉ được nhắc qua repo của chủ kho, §2) và chưa có scanner bảo mật cho MCP trong mục này (scanner nằm ở mục 12).

| Repo | Lớp | ★ · license (2/11/2026) | Commit cuối | Vì sao nâng trần | Rủi ro |
|---|---|---|---|---|---|
| `modelcontextprotocol/conformance` | Cổng máy (chính thức) | 140 · MIT → Apache-2.0 đang chuyển (`NOASSERTION`; `package.json` vẫn ghi MIT) | HEAD `c37eec8` 1/10/2026 (nhánh khác push 2/11) | Bộ test chính thức cho **cả client và server**: 81 file scenario, kiểm từng message JSON-RPC trên dây với JSON Schema của spec (`wire-schema-valid`); `--requirements 2026-07-28` chạy đúng tập bắt buộc của một bản spec, đóng băng lúc phát hành; `tier-check` chấm SDK theo SEP-1730; có GitHub Action (`action.yml`) và file baseline lỗi đã biết | Bản `0.2.0-alpha.12`, ít sao; scenario tăng nhanh nên chỉ tin `--requirements`, không tin "chạy tất cả" |
| `a2aproject/a2a-tck` | Cổng máy (chính thức) | 57 · Apache-2.0 | 22/10/2026 | TCK cho A2A trên 3 transport (gRPC, JSON-RPC, HTTP+JSON); MUST là lỗi cứng, SHOULD là `xfail`; sinh SUT từ kịch bản Gherkin cho a2a-java/python/jakarta | Rất ít sao; README còn trỏ link spec cũ `google.github.io/A2A` |
| `a2aproject/a2a-inspector` | Cổng máy (thủ công) | 506 · Apache-2.0 | 29/10/2026 | Một binary Go có UI: kiểm agent card v1.0/v0.3 theo spec, ghi và validate từng request/response | Không phải test tự động cho CI; Docker mẫu đã bind `127.0.0.1` ✅ |
| `MCPJam/inspector` | Đầu bảng | 2,3k · Apache-2.0 **trừ phần eval** (`NOASSERTION`) | 2/11/2026 | Inspector + eval chéo 16 cấu hình client (ChatGPT, Claude, Cursor…), OAuth debugger, CLI chạy conformance/e2e/eval trong CI | `server/services` (và `server/routes/mcp/evals.ts` nếu có) dùng **MCPJam EE License** (văn bản giấy phép nằm ở `server/evals/LICENSE`): chạy production cần subscription, dev/test thì được. Telemetry PostHog/Axiom có chính sách "chặt nhất thắng", `DO_NOT_TRACK=1` (hoặc `true`) chỉ tắt telemetry phía server (analytics, báo lỗi Sentry, log Axiom); bản browser phát hành trên npm vẫn gửi usage event lên PostHog, muốn tắt phải build từ source với `VITE_DISABLE_POSTHOG_LOCAL=true` (app desktop dùng `MCPJAM_TELEMETRY_DISABLED=1`) |
| `modelcontextprotocol/mcpb` | Chuẩn đóng gói | 2,2k · MIT → Apache-2.0 đang chuyển | HEAD 22/4/2026 | Spec + JSON Schema manifest (v0.1 → v0.4) và CLI `mcpb init/validate/pack/sign/verify`; tên cũ DXT; Claude Code nhận `.mcpb` trong `mcpServers` của plugin (docs plugins-reference, mục 20 §3v) | Hơn 6 tháng không commit trên `main`; chữ ký tự ký chỉ cảnh báo, không chặn |
| `cisco-ai-defense/mcp-scanner` | Cổng máy (bảo mật) | 1,1k · Apache-2.0 | 28/10/2026 | Quét tool MCP bằng YARA (offline), LLM judge, API Cisco AI Defense; thêm "readiness" tĩnh (timeout, retry), quét gói PyPI/npm trong Docker; có CodeQL, plugin Claude Code | `--stdio-command` **khởi chạy server** để quét; analyzer API gửi mô tả tool lên Cisco; LLM analyzer cần key |

**Stack nâng trần** (lợi ích/công sức giảm dần):

1. Server MCP tự viết: thêm job CI `npx @modelcontextprotocol/conformance server --url … --requirements 2026-07-28 --expected-failures conformance-baseline.yml` (hoặc dùng `action.yml`). Đây là cổng duy nhất biến lộ trình stateless ở §4b.3 thành đo được.
2. Trước khi cài server ngoài (§2c): `mcp-scanner --analyzers yara` (không cần key, không gửi dữ liệu) trên server đã sandbox; kết hợp checklist 3 điểm của §2c và OWASP MCP Top 10 (mục 12).
3. Kiểm tay bằng inspector chính thức (§2b); khi cần đo tool trên nhiều client thì dùng MCPJam, nhưng giữ phần eval trong phạm vi dev/test vì license EE.
4. Phát hành server local: đóng gói `.mcpb` và chạy `mcpb validate` trong CI; ký bằng chứng chỉ thật, đừng dừng ở `--self-signed`.
5. Agent A2A: `a2a-tck` mức MUST trong CI, `a2a-inspector` để soi agent card.
6. Skill: tiếp tục `skills-ref validate` (§4b.3); lint và eval skill chi tiết hơn xem mục 20 §3v.

**Nguồn §4c:** GitHub search API 2/11/2026 (`repo:` từng repo; truy vấn "mcp conformance", "skill validator agent skills", "claude plugin validate") · clone `--depth 1 --filter=blob:none` 2/11/2026: modelcontextprotocol/conformance (LICENSE, README.md, SDK_INTEGRATION.md, package.json, action.yml, `requirements/`, `src/scenarios/`), MCPJam/inspector (LICENSE, `mcpjam-inspector/server/evals/LICENSE`, README.md, `mcpjam-inspector/shared/telemetry-privacy.ts`, `server/utils/__tests__/analytics.test.ts`, workflows), modelcontextprotocol/mcpb (LICENSE, README.md, CLI.md, `schemas/`, package.json), cisco-ai-defense/mcp-scanner (LICENSE, README.md, workflows, `claude-code-plugin/`), a2aproject/a2a-tck (LICENSE, README.md), a2aproject/a2a-inspector (README.md) · https://github.com/modelcontextprotocol/conformance · https://github.com/a2aproject/a2a-tck · https://github.com/a2aproject/a2a-inspector · https://github.com/MCPJam/inspector · https://github.com/modelcontextprotocol/mcpb · https://github.com/cisco-ai-defense/mcp-scanner

<a id="core-protocol-boundaries"></a>

## 4d. Nâng trần 2/11/2026: phiên bản wire và ranh giới uỷ quyền MCP (mở rộng cùng ngày)

> Mở rộng chiều sâu trong cùng đợt 2/11/2026, không phải công bố các repo vừa ra mắt. Hai repo dưới đã có trong catalog: đọc lại LICENSE, CI và nhánh mặc định bằng clone chỉ đọc; SHA đối chiếu GitHub API. Mức bằng chứng **code-read**; không chạy/build repo ngoài, hiệu năng và hành vi thực tế **(chưa xác minh)**. Số sao/trạng thái đọc 2026-11-02; ngày commit tính theo UTC, tách khỏi `pushed_at`.

| Repo đã có | ★ · license (2026-11-02) | HEAD nhánh mặc định | Vai trò đọc sâu |
|---|---|---|---|
| `modelcontextprotocol/python-sdk` | 24.736 · MIT | 2026-10-27 · `d7845c07` | Conformance/version baseline và bảo vệ transport |
| `agentgateway/agentgateway` | 5.872 · Apache-2.0 | 2026-10-30 · `084992d6` | JWT/CEL theo tool. prompt. resource và đường gọi |

**Trần còn thiếu:** §4c đã có bộ conformance/scanner. Cần tách **đúng giao thức**, **xác thực danh tính** và **được quyền thao tác tài nguyên**: một server pass JSON-RPC/schema vẫn có thể cho người dùng đọc dữ liệu tenant khác.

### MCP Python SDK: ghim spec, harness và baseline cùng nhau

- [CI conformance](https://github.com/modelcontextprotocol/python-sdk/blob/d7845c073a2b9ba5ab2817ecf93d3e45ef24cd14/.github/workflows/conformance.yml) ghim `@modelcontextprotocol/conformance@0.2.0-alpha.11`, chạy wire `2025-11-25`, `2026-07-28` và mặc định; có baseline riêng cho từng wire. Bản baseline 2026-07-28 tại SHA này có `client: []`, `server: []`. Đây là **đọc cấu hình**, chưa xác minh artifact/kết quả CI; khi so SDK phải ghi đúng bộ requirements và baseline, không chỉ badge xanh.
- [`MCPServer`](https://github.com/modelcontextprotocol/python-sdk/blob/d7845c073a2b9ba5ab2817ecf93d3e45ef24cd14/src/mcp/server/mcpserver/server.py#L1162) tự bật DNS-rebinding protection cho localhost trong đường SSE được đọc; [`TransportSecurityMiddleware`](https://github.com/modelcontextprotocol/python-sdk/blob/d7845c073a2b9ba5ab2817ecf93d3e45ef24cd14/src/mcp/server/transport_security.py#L48) khi không nhận settings lại dùng protection tắt. Không suy từ giá trị mặc định của model settings ra mọi entrypoint; reverse proxy/host khác phải cấu hình Host/Origin allowlist rõ và thử request giả.
- Auth đòi token verifier khi bật; [bearer middleware](https://github.com/modelcontextprotocol/python-sdk/blob/d7845c073a2b9ba5ab2817ecf93d3e45ef24cd14/src/mcp/server/auth/middleware/bearer_auth.py) và auth settings là phần phải kiểm với issuer/resource URL thực tế. MCP authorization spec cấm kiểu nhận token sai audience rồi chuyển thẳng xuống API. Credential cho upstream là một ranh giới riêng.

### agentgateway: có engine policy chưa có nghĩa đã có policy

- [`McpAuthorizationSet::validate`](https://github.com/agentgateway/agentgateway/blob/084992d6091d671cf845e9cd40b16fed41c1511d/crates/agentgateway/src/mcp/rbac.rs#L54) trả `true` nếu **không có rule**. Vì vậy cài gateway rồi cấu hình JWT chưa tự giới hạn từng tool. Phải thêm policy cho tool/prompt/resource và kiểm người dùng không được phép cả khi list và khi gọi trực tiếp tên đã biết.
- [JWT config](https://github.com/agentgateway/agentgateway/blob/084992d6091d671cf845e9cd40b16fed41c1511d/crates/agentgateway/src/http/jwt.rs#L166) yêu cầu issuer; audience chỉ được ép khi danh sách cấu hình không rỗng. Có mode `Permissive` cho phép request thiếu/sai JWT. Đây là tuỳ chọn chức năng, không phải lỗi tự thân; cấu hình triển khai cần chọn mode và audience đúng với mức tin cậy.
- [Ví dụ MCP authorization](https://github.com/agentgateway/agentgateway/blob/084992d6091d671cf845e9cd40b16fed41c1511d/examples/mcp-authorization/config.yaml) minh hoạ CEL theo `jwt.sub` và `mcp.tool.name`, nhưng có CORS `*` và backend token passthrough. Không chép nguyên ví dụ thành cấu hình production: phải kiểm audience/credential flow tới upstream, origin được phép và network không cho bypass gateway. [CI](https://github.com/agentgateway/agentgateway/blob/084992d6091d671cf845e9cd40b16fed41c1511d/.github/workflows/pull_request.yml) có proxy test/lint đa OS, chưa thay kiểm chính sách nghiệp vụ của người tích hợp.

**Ma trận chọn cổng kiểm**

| Muốn chứng minh | Cổng phù hợp | Chưa chứng minh được |
|---|---|---|
| Message/transport đúng một bản spec | Conformance §4c, ghim harness + requirements | User được phép truy cập dữ liệu nào |
| Token đúng issuer/audience/thời hạn | SDK verifier hoặc gateway JWT với cấu hình thực | Quyền trên tool/resource của tenant |
| Người A không gọi được tool của B | CEL/tool policy + test deny list/call | Nội dung retrieved không có prompt injection |
| Không bypass chính sách | Backend chỉ nhận traffic gateway/credential hợp lệ | Model luôn dùng tool theo mục đích mong muốn |
| Đổi spec/SDK không âm thầm mất tính năng | Ma trận host × transport × spec + baseline diff | Hành vi của host/model chưa nằm trong test |

**Cách ghép:** server nhỏ dùng SDK và auth rõ trước; thêm gateway khi có nhiều upstream, policy/trace tập trung. Khóa đường trực tiếp tới upstream, cấp credential theo audience và phạm vi; chạy conformance cùng negative tests auth, expiry, wrong audience, cross-tenant, gọi tool không có trong list. ghép scanner §4c và guardrail mục 12 cho rủi ro nội dung. Các negative test nêu trên là tiêu chí đánh giá, **(chưa xác minh)** bằng chạy thật trong đợt này.

**Nguồn phần mở rộng:** [1](https://github.com/modelcontextprotocol/python-sdk/blob/d7845c073a2b9ba5ab2817ecf93d3e45ef24cd14/LICENSE) · [2](https://github.com/modelcontextprotocol/python-sdk/blob/d7845c073a2b9ba5ab2817ecf93d3e45ef24cd14/.github/workflows/conformance.yml) · [3](https://github.com/modelcontextprotocol/python-sdk/blob/d7845c073a2b9ba5ab2817ecf93d3e45ef24cd14/.github/actions/conformance/expected-failures.2026-07-28.yml) · [4](https://github.com/modelcontextprotocol/python-sdk/blob/d7845c073a2b9ba5ab2817ecf93d3e45ef24cd14/src/mcp/server/mcpserver/server.py) · [5](https://github.com/modelcontextprotocol/python-sdk/blob/d7845c073a2b9ba5ab2817ecf93d3e45ef24cd14/src/mcp/server/transport_security.py) · [6](https://github.com/modelcontextprotocol/python-sdk/blob/d7845c073a2b9ba5ab2817ecf93d3e45ef24cd14/src/mcp/server/auth/middleware/bearer_auth.py) · [7](https://github.com/agentgateway/agentgateway/blob/084992d6091d671cf845e9cd40b16fed41c1511d/LICENSE) · [8](https://github.com/agentgateway/agentgateway/blob/084992d6091d671cf845e9cd40b16fed41c1511d/crates/agentgateway/src/mcp/rbac.rs) · [9](https://github.com/agentgateway/agentgateway/blob/084992d6091d671cf845e9cd40b16fed41c1511d/crates/agentgateway/src/http/jwt.rs) · [10](https://github.com/agentgateway/agentgateway/blob/084992d6091d671cf845e9cd40b16fed41c1511d/examples/mcp-authorization/config.yaml) · [11](https://github.com/agentgateway/agentgateway/blob/084992d6091d671cf845e9cd40b16fed41c1511d/.github/workflows/pull_request.yml) · [12](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations)

## 4e. Kiểm ảnh "Codex Project Structure" (Ananya Ghosh Chowdhury): bản đồ file cấu hình dự án của OpenAI Codex, đối chiếu mã nguồn (ảnh người dùng gửi, 3/11/2026)

> Ảnh là cây thư mục `your-repo/` gồm `AGENTS.md`, `AGENTS.override.md`, `.agents/skills/deploy/{SKILL.md,scripts/}` và `.codex/{config.toml [mcp_servers.*], agents/*.toml, rules/default.rules, hooks.json, hooks/pre_tool_use.py, environments/environment.toml}`, mỗi nhánh có một hộp giải thích. Tác giả ghi trên ảnh: Ananya Ghosh Chowdhury (@ananyaghoshchowdhury). Đối chiếu với `openai/codex` (Apache-2.0, 132.944★) tại `ac91c14443c11c4279a9305099354e443c6fa7d4` (clone nông 3/11/2026). Docs trong repo (`docs/agents_md.md`, `docs/skills.md`…) chỉ trỏ ra developers.openai.com, nên phần lớn kiểm bằng mã Rust trong `codex-rs/`. **Không chạy Codex.**

| Hộp trong ảnh | Kết quả | Đối chiếu |
|---|---|---|
| **AGENTS.md**: gộp từ gốc tới thư mục hiện tại, file gần hơn thắng; `AGENTS.override.md` thay thế trong thư mục của nó; trần 32 KiB qua `project_doc_max_bytes` | ✅ | `core/src/agents_md.rs:45` `LOCAL_AGENTS_MD_FILENAME = "AGENTS.override.md"`; `config/src/config_toml.rs:77` `DEFAULT_PROJECT_DOC_MAX_BYTES = 32 * 1024`. Thứ tự gộp chưa đọc từng dòng |
| **skills/** trong `.agents/` (không phải `.codex/`); quét từ thư mục hiện tại lên gốc repo; lúc khởi động chỉ nạp name + description; gọi bằng `$deploy` | ✅ phần thư mục | `ext/skills/src/host_roots.rs:27` `AGENTS_DIR_NAME = ".agents"`; cũng có `~/.agents/skills` (`guardian-v2/.../trusted_skills.rs:22`). Cách nạp tiến dần và cú pháp `$tên` theo docs, chưa đọc mã **(chưa xác minh)** |
| **config.toml**: lớp dự án đè `~/.codex/config.toml`; `.codex/` lồng nhau thì gần nhất thắng; bị bỏ qua ở dự án không tin cậy | ✅ | Comment ở `config/src/loader/mod.rs:133–135`: cwd → các thư mục cha → gốc git tìm `./.codex/config.toml`, "loaded but disabled when untrusted" |
| **MCP servers**: STDIO hoặc streamable HTTP; không có `.mcp.json`, server là bảng trong `config.toml`; `codex mcp add`, `codex mcp login` (OAuth) | ✅ | `McpServerTransportConfig::{Stdio, StreamableHttp}`; `cli/src/mcp_cmd.rs:79` `Login(LoginArgs)` |
| **agents/**: mỗi subagent tùy biến là một file TOML; cần name, description, `developer_instructions`; có model, reasoning effort, sandbox riêng; có sẵn default, worker, explorer | ✅ | `agent-roles/src/agent_role_config.rs` kiểm `developer_instructions` không được rỗng; `core/src/agent/role.rs` có `DEFAULT_ROLE_NAME = "default"`, `"explorer"`, `"worker"` |
| **rules/**: `prefix_rule()` viết bằng Starlark theo tiền tố lệnh; kiểm lệnh chạy ngoài sandbox; allow/prompt/forbidden, mức chặt nhất thắng; thử bằng `codex execpolicy check` | ✅ | `execpolicy/src/decision.rs` (`Allow`, `Prompt`, `Forbidden`); `policy.rs:494` lấy `.max()` các quyết định khớp, tức chặt nhất thắng; có `execpolicy/src/execpolicycheck.rs` và lệnh `Execpolicy` trong `cli/src/main.rs:198` |
| **hooks.json**: script cho **12** sự kiện vòng đời; hoặc bảng `[hooks]` trong config.toml; exit code 2 để chặn tool call; phải được duyệt và tin cậy trong `/hooks` | ⚠️ số sự kiện | Tại HEAD có **14** sự kiện: PreModelRequest, PostModelRequest, PreToolUse, PermissionRequest, PostToolUse, PreCompact, PostCompact, SessionStart, SessionEnd, UserPromptSubmit, SubagentStart, SubagentStop, Stop, Interrupt (`app-server-protocol/src/protocol/v2/hook.rs:19`). Exit 2 đúng: `hooks/src/events/{post_tool_use,permission_request}.rs` xử lý `Some(2)` khi handler có quyền tác động. Handler có 4 loại (Command, McpTool, Prompt, Agent), ảnh chỉ nói script |
| Hộp cuối, tiêu đề "**Tokenomics**": môi trường local cho app ChatGPT desktop; setup script chạy với mỗi worktree mới; Actions (Run, Test) trên thanh trên cùng; commit để chia sẻ | ⚠️ sai tiêu đề | Nội dung nói về **local environments** (`.codex/environments/environment.toml`), không liên quan token. App desktop không có mã nguồn mở. Docs chính thức (developers.openai.com/codex/app/local-environments) xác nhận setup script chạy khi tạo worktree, actions nằm trên thanh trên cùng, file commit được. Schema file chỉ thấy trên trang skill cộng đồng **(chưa xác minh)** |

**So với Claude Code (để ai dùng cả hai biết file nào tương ứng):** `AGENTS.md` ↔ `CLAUDE.md` (Claude Code đọc AGENTS.md qua `@import`, §4); `.agents/skills/` ↔ `.claude/skills/` (cùng định dạng SKILL.md); `.codex/config.toml [mcp_servers]` ↔ `.mcp.json`; `.codex/agents/*.toml` ↔ `.claude/agents/*.md`; `.codex/rules/*.rules` (Starlark) ↔ `permissions` trong `.claude/settings.json`; `.codex/hooks.json` ↔ `hooks` trong `settings.json` (Claude Code cũng chặn bằng exit code 2). Khác biệt đáng chú ý: Codex **tắt toàn bộ cấu hình dự án** khi thư mục chưa được tin cậy, và hook dự án phải được duyệt trong `/hooks`. Đây là lớp chặn hữu ích khi clone repo lạ có `.codex/` độc hại.

**Dùng thế nào:** ảnh đúng khoảng 6/8 hộp và là bản đồ nhanh tốt. Trước khi dựa vào số liệu cụ thể (số sự kiện hook, giá trị mặc định), hãy kiểm lại docs chính thức hoặc mã, vì Codex đổi nhanh (hai sự kiện model-request và Interrupt không có trong ảnh).

**Nguồn §4e:** ảnh người dùng gửi 3/11/2026 · clone `--depth 1` https://github.com/openai/codex HEAD `ac91c14443c11c4279a9305099354e443c6fa7d4`: https://github.com/openai/codex/blob/ac91c14443c11c4279a9305099354e443c6fa7d4/codex-rs/core/src/agents_md.rs · https://github.com/openai/codex/blob/ac91c14443c11c4279a9305099354e443c6fa7d4/codex-rs/config/src/config_toml.rs · https://github.com/openai/codex/blob/ac91c14443c11c4279a9305099354e443c6fa7d4/codex-rs/config/src/loader/mod.rs · https://github.com/openai/codex/blob/ac91c14443c11c4279a9305099354e443c6fa7d4/codex-rs/ext/skills/src/host_roots.rs · https://github.com/openai/codex/blob/ac91c14443c11c4279a9305099354e443c6fa7d4/codex-rs/agent-roles/src/agent_role_config.rs · https://github.com/openai/codex/blob/ac91c14443c11c4279a9305099354e443c6fa7d4/codex-rs/core/src/agent/role.rs · https://github.com/openai/codex/blob/ac91c14443c11c4279a9305099354e443c6fa7d4/codex-rs/execpolicy/src/decision.rs · https://github.com/openai/codex/blob/ac91c14443c11c4279a9305099354e443c6fa7d4/codex-rs/execpolicy/src/policy.rs · https://github.com/openai/codex/blob/ac91c14443c11c4279a9305099354e443c6fa7d4/codex-rs/cli/src/mcp_cmd.rs · https://github.com/openai/codex/blob/ac91c14443c11c4279a9305099354e443c6fa7d4/codex-rs/app-server-protocol/src/protocol/v2/hook.rs · https://github.com/openai/codex/blob/ac91c14443c11c4279a9305099354e443c6fa7d4/codex-rs/hooks/src/events/post_tool_use.rs · https://developers.openai.com/codex/app/local-environments · GitHub search API `repo:openai/codex` 3/11/2026.

<a id="factory-protocol-conformance-evidence-2026-11-04"></a>

## 4f. Nâng trần 4/11/2026: phiên bản conformance, mẫu số và license là một phần hợp đồng tích hợp

> Đọc lại MCP Conformance (nhóm Model Context Protocol), `c37eec888e1c6ff140af79987a40008548b7cc5f`, ngày 2026-11-04; **code-read**, không chạy client/server hay bộ test upstream; không cập nhật sao. Nối §4c–§4d; không suy trạng thái chuẩn đã final từ tên một thư mục hay một revision của harness.

**Trần còn thiếu:** có test conformance chưa trả lời “phiên bản wire nào, test nào được tính, có bao nhiêu skipped/expected failures, chứng minh quyền của ứng dụng tới đâu?”. Xưởng phải lưu toàn bộ hợp đồng kiểm này để lần nâng SDK không đổi nghĩa pass âm thầm.

### MCP Conformance: frozen requirements khác toàn bộ suite hiện tại

- [README](https://github.com/modelcontextprotocol/conformance/blob/c37eec888e1c6ff140af79987a40008548b7cc5f/README.md) phân `--suite`, `--spec-version` và `--requirements <revision>`. Requirements đóng băng danh sách cho revision, cố định wire version và thay lựa chọn suite/scenario; harness còn có scenario ngoài phần chấm. Một scenario có ở cả hai revision phải được chạy cho từng wire; pass một phiên bản không suy sang phiên bản khác.
- [Loader requirements](https://github.com/modelcontextprotocol/conformance/blob/c37eec888e1c6ff140af79987a40008548b7cc5f/src/requirements.ts) chỉ nhận các role client/server, chặn khai báo authorization-server vào requirement set. [`requirementsExitCode`](https://github.com/modelcontextprotocol/conformance/blob/c37eec888e1c6ff140af79987a40008548b7cc5f/src/index.ts) lọc scenario được chấm; lỗi ở `not_scored` vẫn báo nhưng không làm exit code của conformance thất bại. Do đó giữ **scored, not-scored, skipped và baseline expected-failure** riêng trong artifact; một tỷ lệ pass không đại diện mọi scenario.
- [Requirement set cụ thể](https://github.com/modelcontextprotocol/conformance/blob/c37eec888e1c6ff140af79987a40008548b7cc5f/requirements/2026-07-28.yaml) cùng bản harness là bằng chứng tái kiểm. Những revision/nhãn draft trong upstream cần được đối chiếu đặc tả đang triển khai trước tích hợp; không tự chuyển production sang draft vì nó xuất hiện trong `list`.
- [LICENSE thực](https://github.com/modelcontextprotocol/conformance/blob/c37eec888e1c6ff140af79987a40008548b7cc5f/LICENSE) ghi quá trình **MIT → Apache-2.0**: đóng góp chưa có đồng ý chuyển vẫn theo MIT; đóng góp code/spec mới theo Apache-2.0; tài liệu trừ specification theo CC-BY-4.0. Không gán nguyên cây là “MIT thuần” hoặc “Apache-2.0 thuần”; kiểm notice khi đóng gói lại.

| Lớp | Công cụ/nguồn so sánh | Phạm vi đúng |
|---|---|---|
| Wire interoperability MCP | MCP Conformance + requirement revision | Message/schema/lifecycle và scenario cụ thể |
| A2A | A2A TCK/Inspector (§4c) | Giao thức A2A; không thay MCP tests |
| Kiểm bề mặt tool | Cisco MCP Scanner (§4c) | Tín hiệu policy/phân tích theo khả năng scanner, không là bằng chứng nghiệp vụ |
| API nghiệp vụ/tenant | OpenAPI + oasdiff (mục 29), test runtime (mục 30/34) | AuthZ, ownership, compatibility và side effect của ứng dụng |

**Chuỗi nâng SDK cho xưởng:** (1) inventory client/server, transport, wire revision và extension sử dụng; (2) ghim SDK, harness SHA, requirements file, exception baseline; (3) chạy role/transport thực sự cần và negative fixture để biết bộ chấm bắt lỗi; (4) lưu checks.json với passed/failed/skipped/not-scored/expected-failure và version; (5) kiểm độc lập access token audience, tenant, quyền từng tool và hành động lặp; (6) thử rollback về SDK/config trước. Harness không tự chứng minh một người dùng có quyền đọc một hồ sơ trong sản phẩm.

**Cổng nhận đề xuất:** không giảm số scenario required ngoài thay đổi revision có duyệt; không biến failure thành baseline chỉ để xanh; mọi exception có phạm vi/owner/hạn xem lại; quyền ứng dụng có ca từ chối truy cập chéo tenant. Đây là tiêu chí tích hợp, chưa chạy trong đợt đọc mã.

**Nguồn kiểm cấu hình:** [CI](https://github.com/modelcontextprotocol/conformance/blob/c37eec888e1c6ff140af79987a40008548b7cc5f/.github/workflows/ci.yml) · [Expected failures](https://github.com/modelcontextprotocol/conformance/blob/c37eec888e1c6ff140af79987a40008548b7cc5f/src/expected-failures.ts). CI chạy kiểm/build/test harness; không chứng nhận một deployment của xưởng.

## 5. Nguồn

- https://en.wikipedia.org/wiki/Model_Context_Protocol · https://github.com/wong2/awesome-mcp-servers · https://github.com/sadekxD/Awesome-MCP · https://uibakery.io/blog/best-mcp-servers
- https://www.mintmcp.com/blog/a2a-vs-mcp · https://crystl.dev/blog/agent-communication-protocols/ · https://stellagent.ai/insights/a2a-protocol-google-agent-to-agent · https://www.flowhunt.io/blog/agentic-ai-foundation-a2a-mcp-standards/ · https://techiehub.blog/what-is-the-a2a-protocol/
- https://github.com/ag-ui-protocol/ag-ui · https://blogs.oracle.com/ai-and-datascience/announcing-agent-spec-for-a2ui-copilotkit-ag-ui · https://aws.amazon.com/blogs/machine-learning/build-generative-ui-for-ai-agents-on-amazon-bedrock-agentcore-with-the-ag-ui-protocol/ · https://learn.microsoft.com/en-us/agent-framework/integrations/ag-ui/
- https://blog.buildbetter.ai/agents-md-vs-cursorrules-vs-claude-skills-2026-comparison/ · https://meshlaunch.com/en/blog/2026-cursor-agent-skills-complete-guide.html · https://codersera.com/blog/agents-md-vs-claude-md-vs-cursor-rules-comparison-2026/ · https://dev.to/creeta/one-skillmd-replaces-claudemd-agentsmd-and-cursorrules-5a70
- §2b (12/10/2026): https://github.com/modelcontextprotocol/python-sdk · https://github.com/modelcontextprotocol/typescript-sdk · https://github.com/modelcontextprotocol/inspector · https://github.com/modelcontextprotocol/registry · https://github.com/modelcontextprotocol/ext-apps · https://github.com/MCP-UI-Org/mcp-ui · https://github.com/agentclientprotocol/agent-client-protocol · https://agentclientprotocol.com/get-started/clients · https://github.com/agentsmd/agents.md · https://agents.md/ · https://github.com/i-am-bee/acp · https://github.com/agntcy
- §2c (12/10/2026): https://github.com/VoltAgent/official-mcp-servers · https://raw.githubusercontent.com/VoltAgent/official-mcp-servers/main/CONTRIBUTING.md · https://repos.ecosyste.ms/api/v1/hosts/GitHub/repositories/VoltAgent%2Fofficial-mcp-servers · https://github.com/orgs/VoltAgent/repositories · https://github.com/VoltAgent/voltagent · https://github.com/PostHog/mcp · https://github.com/semgrep/mcp · https://github.com/browserbase/mcp-server-browserbase · https://github.com/elevenlabs/elevenlabs-mcp · https://github.com/JetBrains/mcp-jetbrains · https://github.com/langfuse/mcp-server-langfuse · https://github.com/ahujasid/mcp-for-blender · https://github.com/google/mcp · https://github.com/modelcontextprotocol/servers · https://github.com/punkpeye/awesome-mcp-servers · https://github.com/wong2/awesome-mcp-servers · https://glama.ai/mcp/servers · https://smithery.ai
