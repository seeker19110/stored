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

## 5. Nguồn

- https://en.wikipedia.org/wiki/Model_Context_Protocol · https://github.com/wong2/awesome-mcp-servers · https://github.com/sadekxD/Awesome-MCP · https://uibakery.io/blog/best-mcp-servers
- https://www.mintmcp.com/blog/a2a-vs-mcp · https://crystl.dev/blog/agent-communication-protocols/ · https://stellagent.ai/insights/a2a-protocol-google-agent-to-agent · https://www.flowhunt.io/blog/agentic-ai-foundation-a2a-mcp-standards/ · https://techiehub.blog/what-is-the-a2a-protocol/
- https://github.com/ag-ui-protocol/ag-ui · https://blogs.oracle.com/ai-and-datascience/announcing-agent-spec-for-a2ui-copilotkit-ag-ui · https://aws.amazon.com/blogs/machine-learning/build-generative-ui-for-ai-agents-on-amazon-bedrock-agentcore-with-the-ag-ui-protocol/ · https://learn.microsoft.com/en-us/agent-framework/integrations/ag-ui/
- https://blog.buildbetter.ai/agents-md-vs-cursorrules-vs-claude-skills-2026-comparison/ · https://meshlaunch.com/en/blog/2026-cursor-agent-skills-complete-guide.html · https://codersera.com/blog/agents-md-vs-claude-md-vs-cursor-rules-comparison-2026/ · https://dev.to/creeta/one-skillmd-replaces-claudemd-agentsmd-and-cursorrules-5a70
- §2b (12/10/2026): https://github.com/modelcontextprotocol/python-sdk · https://github.com/modelcontextprotocol/typescript-sdk · https://github.com/modelcontextprotocol/inspector · https://github.com/modelcontextprotocol/registry · https://github.com/modelcontextprotocol/ext-apps · https://github.com/MCP-UI-Org/mcp-ui · https://github.com/agentclientprotocol/agent-client-protocol · https://agentclientprotocol.com/get-started/clients · https://github.com/agentsmd/agents.md · https://agents.md/ · https://github.com/i-am-bee/acp · https://github.com/agntcy
- §2c (12/10/2026): https://github.com/VoltAgent/official-mcp-servers · https://raw.githubusercontent.com/VoltAgent/official-mcp-servers/main/CONTRIBUTING.md · https://repos.ecosyste.ms/api/v1/hosts/GitHub/repositories/VoltAgent%2Fofficial-mcp-servers · https://github.com/orgs/VoltAgent/repositories · https://github.com/VoltAgent/voltagent · https://github.com/PostHog/mcp · https://github.com/semgrep/mcp · https://github.com/browserbase/mcp-server-browserbase · https://github.com/elevenlabs/elevenlabs-mcp · https://github.com/JetBrains/mcp-jetbrains · https://github.com/langfuse/mcp-server-langfuse · https://github.com/ahujasid/mcp-for-blender · https://github.com/google/mcp · https://github.com/modelcontextprotocol/servers · https://github.com/punkpeye/awesome-mcp-servers · https://github.com/wong2/awesome-mcp-servers · https://glama.ai/mcp/servers · https://smithery.ai
