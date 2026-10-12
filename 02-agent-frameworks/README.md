# 02 · Agent Frameworks & LLM Orchestration

> Thư viện để xây agent/multi-agent và ứng dụng LLM. Số sao ước lượng 8–10/2026.

## 1. Bảng tổng hợp

| Framework | Repo | Ngôn ngữ | ★ (ước lượng) | Mô hình tư duy | Khi nào dùng |
|---|---|---|---|---|---|
| **LangChain** | langchain-ai/langchain | Py/TS | ~130k | Chuỗi, tool, retriever; hệ sinh thái lớn nhất | Prototype nhanh, nhiều tích hợp |
| **LangGraph** | langchain-ai/langgraph | Py/TS | ~40k · **34.5M tải/tháng** | Đồ thị trạng thái (state graph), checkpoint, human-in-the-loop | Agent production cần kiểm soát luồng, durable |
| **AutoGen → Microsoft Agent Framework** | microsoft/autogen · microsoft/agent-framework | Py/.NET | ~60k (AutoGen, maintenance) | Hội thoại đa agent; hợp nhất AutoGen + Semantic Kernel, GA 1.0 4/2026 | Doanh nghiệp .NET/Azure |
| **CrewAI** | crewAIInc/crewAI | Py | ~57k · 5.2M tải/tháng | Vai trò (role) + nhiệm vụ + crew | Đội agent theo vai trò, dễ lên |
| **OpenAI Agents SDK** | openai/openai-agents-python | Py/TS | ~29k · 10.3M tải/tháng | Agents, handoffs, guardrails, tracing | Dùng OpenAI/Responses API |
| **LlamaIndex** | run-llama/llama_index | Py/TS | ~48k | Data framework (RAG), workflows | RAG trên dữ liệu doanh nghiệp |
| **Semantic Kernel** | microsoft/semantic-kernel | .NET/Py/Java | ~28k | Plugins, planners | Đang hợp vào Agent Framework |
| **smolagents** | huggingface/smolagents | Py | ~26k | Code-agent tối giản (agent viết Python để hành động) | Nhẹ, HF ecosystem |
| **Haystack** | deepset-ai/haystack | Py | ~20k | Pipeline component hóa | RAG/search production |
| **PydanticAI** | pydantic/pydantic-ai | Py | ~16k | Typed, dependency injection, validation | Team ưa type-safety |
| **Google ADK** | google/adk-python | Py/Java | – | Agent Development Kit, A2A native | Gemini/Vertex |
| **Mastra** | mastra-ai/mastra | TS | – | Agent framework TS, workflows, evals | Next.js/TS stack |
| **OpenClaw** | openclaw/openclaw | TS | **~390k** | Trợ lý cá nhân tự host, nối Discord/Slack/Telegram/WhatsApp, skills module | Agent cá nhân; tác giả Peter Steinberger gia nhập OpenAI 2/2026, dự án về foundation độc lập |
| **Hermes Agent** | NousResearch/hermes-agent | Py | – | Agent mã mở chạy CLI/TUI/Electron + gateway Telegram/Discord/Slack/WhatsApp + ACP cho IDE; skills tự học, memory, `delegate_task` (≤10 con, **không lồng**), kanban, cron, webhook, plugin model-provider | Chủ kho dùng thật (mục 23 §5): provider Antigravity/`claude -p`/Codex CLI, 112 skill; docs `llms.txt` |
| **MetaGPT** | FoundationAgents/MetaGPT | Py | ~70,8k (trang GitHub 12/10/2026) | "Công ty phần mềm" đa vai trò: SOP → PRD/design/code; MGX | Khung "công ty AI" đầu tiên |
| **ChatDev** | OpenBMB/ChatDev | Py | ~34,5k (12/10/2026) | Chat-chain giữa các vai trò CEO/CTO/dev/tester | Nghiên cứu, nhỏ gọn |
| **DeerFlow** | bytedance/deer-flow | Py/TS | ~83,7k (12/10/2026) | Deep research đa agent trên LangGraph, planner + coordinator | X-Agents đối chiếu (mục 23 §3.1) |
| **AG2** (ex-AutoGen fork) | ag2ai/ag2 | Py | – | Fork cộng đồng của AutoGen 0.2 | Tách khỏi Microsoft 11/2024 |
| **CAMEL** | camel-ai/camel | Py | ~13k (nt.) | Role-playing agent, data gen, OWL | Học thuật |
| **agency-swarm** | VRSEN/agency-swarm | Py | – | Agency = agent có vai trò + luồng giao tiếp định nghĩa sẵn | Trên OpenAI Assistants/Agents SDK |
| **gpt-pilot** | Pythagora-io/gpt-pilot | Py/TS | ~33,6k (12/10/2026) | Dev AI theo bước, hỏi người khi kẹt | **Ngừng bảo trì**; cảnh báo mã độc trong `core/telemetry/` (8/2025–6/2026) **(chưa xác minh)** |
| **ruflo** (claude-flow) | ruvnet/ruflo | TS | – | Swarm orchestration cho Claude Code, hive-mind, MCP tools | Nhiều tuyên bố hiệu năng **chưa kiểm chứng** |
| **Paperclip** | paperclipai/paperclip | TS | ~100,5k (12/10/2026) | "Quản lý agent như nhân viên": org chart, budget, heartbeat; `npx paperclipai onboard` | Lớn nhất họ "công ty AI" 2026 |
| **OpenOPC** | HKUDS/OpenOPC | Py | ~1,8k (12/10/2026) | "One-person company": tự dựng org chart, uỷ việc cho Claude Code/Codex/Cursor | Mới, mỏng |
| **OpenCompany** (ex-MachinaOS) | zeenie-ai/OpenCompany | Py + TS | ~995 (12/10/2026) | App desktop/self-host: nhân viên AI = lead + specialist trên canvas, trigger email/chat/lịch, Temporal, 86 SKILL.md | Xem §4; theo dõi, chưa khuyến nghị production |

## 2. Phân tích

- **Sao ≠ dùng thật**: AutoGen nhiều sao nhất nhưng ở chế độ bảo trì; LangGraph ít sao hơn nhưng dẫn đầu mọi chỉ số adoption.
- **Hợp nhất**: Microsoft gom AutoGen + Semantic Kernel; LangChain tách phần agent sang LangGraph; OpenAI tự làm SDK → xu hướng "mỗi nhà cung cấp model có SDK agent riêng + 1–2 framework trung lập".
- **Chuẩn chung thay framework**: MCP (tool), A2A (agent-agent), AG-UI (UI) khiến việc chọn framework ít "khóa chặt" hơn trước.
- **"Công ty AI" là một họ riêng** (MetaGPT, ChatDev, gpt-pilot, agency-swarm, DeerFlow; so sánh trong `X-Agents/docs/reports/2026-10-10-doi-chieu-12-repo-co-che.md`): điểm chung là vai trò + SOP + artifact trung gian; bài học từ X-Agents (mục 23 §3.1) là **model quyết định, code hành động** — mọi trường "đã làm" do code điền, không tin lời khai của model.
- **Hermes Agent** là framework agent cá nhân gần OpenClaw nhất nhưng mở hơn về provider (plugin model-provider, CLI thuê bao làm backend) — xem mục 23 §5.
- **Tiêu chí chọn**: (1) kiểm soát luồng & durable execution (LangGraph), (2) tốc độ lên demo (CrewAI), (3) type-safety (PydanticAI), (4) hệ sinh thái cloud (ADK/Agent Framework), (5) khối lượng phụ thuộc (smolagents).

## 4. Case study: zeenie-ai/OpenCompany – "nhân viên AI" đóng gói thành sản phẩm (link từ người dùng, 2026-10-12)

### Hồ sơ nhanh

| Mục | Giá trị (đọc 2026-10-12, clone nông commit `a09c079`) |
|---|---|
| Repo | zeenie-ai/OpenCompany (tên cũ **MachinaOS**, đổi ~7/2026); npm `@zeenie-ai/opencompany` 0.2.1 (12/9/2026) |
| Tác giả | Zeenie AI (tài khoản cá nhân, 5 repo); gần như toàn bộ commit của `trohitg`, trailer `Co-Authored-By: Claude`; everydev.ai nói 1 nhân sự ở Bengaluru **(chưa xác minh)** |
| License / quy mô | MIT; 995★ · 151 fork · 1.556 commit; commit cuối 11/10/2026; ~183k dòng Python + ~91k dòng TS; 386 file test; `CLAUDE.md` 359 KB (2.835 dòng) |
| Stack | FastAPI + WebSocket, React 19 + React Flow + Tailwind 4, Electron, bun, uv/Python 3.12, SQLite mặc định, **Temporal** nhúng; 14 provider LLM (Anthropic, OpenAI, Gemini, Ollama, LM Studio…) |
| Xu hướng sao | +671/90 ngày (reporank) — ổn định, không viral; **0 thread HN/Reddit** tìm được |

### Cơ chế đáng học

- **Một nhân viên = một workflow**: chủ mô tả việc bằng lời → LLM soạn bản thiết lập (app, giờ làm, quy tắc hỏi trước) → "Hire" tạo workflow chạy nền với trigger Gmail/Telegram/WhatsApp/Stripe/webhook/cron.
- **Topology là ranh giới uỷ quyền** (`docs-internal/agent_teams.md`): lead (`ai_employee`/`orchestrator_agent`) chỉ giao việc cho specialist nối trực tiếp vào handle `input-teammates`, tối đa 2 tầng, không trùng loại specialist trong một đội; mỗi tool node có đúng một agent sở hữu.
- **Task Manager** gắn cố định vào lead: giao việc chỉ qua `assign_task(mission, context, acceptance_criteria, assignee)`; specialist nộp, lead review và trả lại nếu chưa đạt rồi mới báo chủ. Các tool `delegate_to_*` **bị ẩn khỏi model**, lead chỉ thấy roster một dòng/teammate.
- **Context ≠ Memory** (RFC-0002): context = hội thoại backend sở hữu, khoá `(workflow, generation, agent)`, mọi lần kích hoạt nối tiếp cùng hội thoại; memory = tool `simpleMemory` gọi tường minh, người dùng sửa được. Thiết kế journal/epoch/hash-chain trong RFC bị thay bằng store phẳng sau ~2 tháng — "đơn giản thắng".
- **Compaction** tự động ở 0,8 cửa sổ ngữ cảnh thành tóm tắt 5 phần ("lấy cảm hứng từ Claude Code") kèm đếm token và tính chi phí theo `pricing.json`.
- **Skill = SKILL.md** (chuẩn Agent Skills, 86 file/21 domain, ví dụ `employee/chase-late-payments` với 3 mức nhắc nợ, cấm đe doạ/tự giảm giá); "self-improving" = memory + sửa skill + thêm tool có duyệt, **không retrain**.
- **Plugin**: class kế thừa `ActionNode/TriggerNode/ToolNode` với `Params`/`Output` Pydantic dùng chung cho form UI + tool schema LLM + REST spec; restart là có node mới, không sửa frontend. Approval gate "ask first" cho gửi/chi tiền kèm 5 giây undo. CLI agent (Claude Code/Codex/Gemini) chạy qua subprocess — gãy khi CLI đổi flag (issue #132–134).

### Mâu thuẫn & rủi ro

- README "78 skills" nhưng đếm được **86**; "140+ tools" vs docs "110+ nodes" vs mã 171 plugin; README hứa 6 "nhân viên" nhưng chỉ ship 3 template + 4 starter; website kể 6 vai khác và dashboard "$27,342/day" không có bằng chứng; website bán gói Pro/Max trong khi README nói "No subscription".
- `.env` **commit sẵn SECRET_KEY/JWT_SECRET_KEY dev**; binary desktop chưa ký; không SECURITY.md; agent có quyền email/thanh toán/shell trên máy người dùng.
- Bus-factor 1; issue 10/10/2026: job kẹt "working" khi model local không gọi `assign_task` (#145), Gmail trigger giao mission rỗng (#143). cloudnews.tech (4/2026): "còn xa mới plug-and-play".
- Trùng tên với `tinyhumansai/opencompany` (Rust, GPL-3.0, 298★) — dự án khác, vài directory gộp nhầm.

### Bài học cho kho

- Họ "công ty AI" 2026 tách làm hai: *thư viện cho dev* (MetaGPT, ChatDev, CrewAI, agency-swarm) và *sản phẩm end-user chạy nền* (Paperclip, OpenCompany, OpenOPC). OpenCompany là mẫu hiếm có installer 3 OS + Docker 1 container, docs nội bộ 300 file và 3 RFC ở dự án một người.
- Ba pattern đưa sang mục 03: topology = ranh giới uỷ quyền, ẩn tool uỷ quyền khỏi model (chỉ đưa roster), tách context/memory. Cùng ý với X-Agents "model quyết định, code hành động" (mục 23).
- Trạng thái: **theo dõi, chưa khuyến nghị production**; nếu thử: Docker, đổi secret `.env`, dùng model cloud; xem lại sau 3–6 tháng (contributor thứ hai, SECURITY.md, bản ký số).

## 5. Nguồn

- https://www.firecrawl.dev/blog/best-open-source-agent-frameworks
- https://dreaming.press/posts/ai-agent-frameworks-github-ranked-by-stars-2026.html
- https://unifiedplatforms.com/blogs/web-development/agentic-ai-frameworks-compared/
- https://the-agent-report.com/2026/07/ai-agent-frameworks-comparison-2026-langgraph-crewai-autogen/
- https://pickaxe.co/post/top-ai-agent-frameworks · https://pickaxe.co/post/crewai-vs-langgraph-vs-autogen
- https://www.langchain.com/resources/ai-agent-frameworks
- https://cordum.io/blog/langchain-vs-llamaindex-vs-semantic-kernel · https://uvik.net/blog/python-ai-agent-frameworks/
- https://github.com/NousResearch/hermes-agent · https://github.com/FoundationAgents/MetaGPT · https://github.com/OpenBMB/ChatDev · https://github.com/bytedance/deer-flow · https://github.com/ag2ai/ag2 · https://github.com/camel-ai/camel · https://github.com/VRSEN/agency-swarm · https://github.com/Pythagora-io/gpt-pilot · https://github.com/ruvnet/ruflo (đọc qua docs nội bộ của X-Agents/Hermes-Agents, 2026-10-12)
- OpenCompany (đọc 2026-10-12): https://github.com/zeenie-ai/OpenCompany (README, CONTRIBUTING, CLAUDE.md, LICENSE, releases, issues #128 #129 #132–134 #143 #145, `docs-internal/{agent_teams,employee_teams,normal_mode,memory_compaction,agent_context_flow}.md`, RFC-0001..0003, `server/nodes/README.md`, `server/skills/**/SKILL.md`, `client/src/features/home/hire/starters.json`) · https://opencompany.sh · https://docs.opencompany.sh · https://reporank.net/en/repo/zeenie-ai-opencompany.html · https://www.opensourcealternatives.to/item/opencompany · https://cloudnews.tech/machinaos-wants-to-bring-the-ai-personal-assistant-from-the-cloud-to-your-own-server/ · https://www.everydev.ai/developers/zeenie-ai (chưa xác minh) · https://github.com/paperclipai/paperclip · https://github.com/HKUDS/OpenOPC · https://github.com/tinyhumansai/opencompany (trùng tên)
- https://github.com/openclaw/openclaw · https://www.digitalocean.com/resources/articles/what-is-openclaw · https://www.freecodecamp.org/news/how-to-build-and-secure-a-personal-ai-agent-with-openclaw/
