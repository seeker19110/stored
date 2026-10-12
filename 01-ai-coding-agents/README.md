# 01 · AI Coding Agents

> Các agent/trợ lý lập trình chạy trong terminal, IDE hoặc cloud. Số sao ước lượng tại 9–10/2026, đối chiếu từ nhiều nguồn (xem cuối trang).

## 1. Bảng tổng hợp

### 1.1 Mã nguồn mở (CLI / tự host)

| Dự án | Repo | License | ★ (ước lượng) | Điểm nổi bật | Ghi chú |
|---|---|---|---|---|---|
| **OpenCode** | github.com/sst/opencode | MIT | ~210k | CLI/TUI agent đa model, provider-agnostic, LSP tích hợp | Nhiều nguồn xếp #1 nhóm mở (9/2026) |
| **DeepSeek Harness** | github.com/deepseek-ai/deepseek-harness | MIT | ~200k (2 tuần sau 13/8/2026) | Kiến trúc "mọi thứ là plugin": UI, tool call, context injection, cả agent loop đều thay được; hỗ trợ model local | Developer preview, chưa nhận PR ngoài; số sao giữa các nguồn chênh lệch (95k→203k) |
| **OpenAI Codex CLI** | github.com/openai/codex | Apache-2.0 | ~127k | Agent terminal chính thức của OpenAI, sandbox, multi-agent orchestration | Rust rewrite |
| **Gemini CLI** | github.com/google-gemini/gemini-cli | Apache-2.0 | ~107k | Agent terminal của Google, free tier rộng, MCP | |
| **OpenHands** (cũ: OpenDevin) | github.com/OpenHands/OpenHands | MIT | ~90k | Nền tảng agent dev đầy đủ (sandbox Docker, web UI, cloud), nhiều SOTA SWE-bench | Đổi tên từ All-Hands-AI |
| **Cline** | github.com/cline/cline | Apache-2.0 | ~69k | VS Code extension agent, plan/act mode, MCP marketplace | |
| **Aider** | github.com/Aider-AI/aider | Apache-2.0 | ~49k | Pair-programming terminal, repo map, git-native | Commit cuối 5/2026 → phát triển chậm lại |
| **SWE-agent** | github.com/SWE-agent/SWE-agent | MIT | ~20.5k | Princeton; agent-computer interface, giải GitHub issue tự động | Nghiên cứu, bảo trì đều (10/2026) |
| **mini-SWE-agent** | github.com/SWE-agent/mini-swe-agent | MIT | ~8.4k | **100 dòng code**, >74% SWE-bench Verified; là harness chuẩn của Vals leaderboard | Minh chứng "harness đơn giản vẫn mạnh" |
| **Goose** | github.com/block/goose | Apache-2.0 | – | Agent desktop/CLI của Block, MCP-first | |
| **Roo Code / Kilo Code** | github.com/RooCodeInc/Roo-Code | Apache-2.0 | – | Fork Cline, nhiều mode | |

### 1.2 Thương mại / mã đóng

| Sản phẩm | Hãng | Hình thức | Giá tham khảo | Điểm nổi bật |
|---|---|---|---|---|
| **Claude Code** | Anthropic | CLI + IDE + web/cloud | theo gói Claude | Repo ~148k★ nhưng mã đóng; hooks, skills, subagents, plugins (`ralph-loop`), `/loop`, worktree |
| **Cursor** | Anysphere | VS Code fork | Pro $20 / Pro+ $60 / Ultra $200 | Mạnh nhất cho multi-file; cloud agents song song; đọc SKILL.md từ 2.4 (1/2026) |
| **Windsurf → Devin Desktop** | Cognition | IDE | ~$15–20 | Sau khi Cognition mua Windsurf, vận hành dưới tên Devin Desktop (nguồn chưa thống nhất) |
| **Devin** | Cognition | Cloud agent | $20 beta / $500 seat ent. | Agent "kỹ sư phần mềm" đầu tiên |
| **GitHub Copilot** | GitHub/MS | IDE + coding agent | $10 / $19 / $39 | Mặc định cho team GitHub; agent kém Cursor/Claude Code theo review |
| **Google Jules** | Google | Cloud async agent | free 15 task/ngày | Tốt cho test & PR trên repo Python |
| **OpenAI Codex (cloud)** | OpenAI | Cloud agent | trong ChatGPT Plus $20 / Pro $100+ | Chạy song song nhiều task trong sandbox |

### 1.3 Agent workspace / ADE – chạy nhiều coding agent song song (thêm 2026-10-12)

Lớp **không phải agent** mà là "bàn làm việc" bọc các CLI agent ở bảng 1.1/1.2: mỗi agent một pane/worktree, so sánh kết quả, review diff. ★ đọc trên trang GitHub 12/10/2026 trừ khi ghi khác.

| Dự án | Repo | License | ★ | Cách tiếp cận | Ghi chú |
|---|---|---|---|---|---|
| **Personal Jarvis** | github.com/Dodaios/Dodaios (cũ: PersonalJarvis/PersonalJarvis) | Apache-2.0 (≤1.6.0 là MIT) | 183 | "Super-app": ADE nhiều pane + giọng nói/wake word + computer use + agent nền có memory + marketplace | Case study §3c; Python + React, 1 tác giả chính |
| **T3 Code** | github.com/pingdotgg/t3code | MIT | ~27,1k | "Agent harness control surface": điều khiển agent trên máy mình qua web/desktop/mobile | Personal Jarvis mượn code thread/timeline và trang Computers (NOTICE) |
| **Vibe Kanban** | github.com/BloopAI/vibe-kanban | Apache-2.0 | ~28,3k | Bảng kanban, mỗi thẻ = một agent trong worktree riêng | README ghi **đang sunset**, chuyển cho cộng đồng |
| **Orca** | github.com/stablyai/orca | MIT | chưa rõ (10k–43k tùy nguồn) | Fan-out 1 prompt sang nhiều CLI agent, mỗi agent một worktree, chọn bản thắng để merge | Số sao các nguồn lệch nhau ~4× → **(chưa xác minh)** |
| **Claude Squad** | github.com/smtg-ai/claude-squad | AGPL-3.0 | ~8,6k | TUI trên tmux + git worktree, quản lý Claude Code/Codex/OpenCode/Amp | Nhẹ nhất, chỉ terminal |
| **Conductor** | Melty Labs (đóng) | thương mại | – | App Mac, agent song song mỗi cái một worktree, panel review diff | Chỉ macOS (theo bài so sánh, chưa xác minh) |

## 2. Benchmark & cách đánh giá

| Benchmark | Trạng thái 10/2026 | Top |
|---|---|---|
| SWE-bench Verified | **Bão hòa**: Vals ngừng chấm model mới từ 1/9/2026; OpenAI tuyên bố (2/2026) không còn đo được frontier | Claude Opus 5 (mini-SWE-agent) 97.0%, DeepSeek V4 Pro 96.4%, GPT-5.6 Sol 96.2% |
| SWE-bench Pro (Verified) | Benchmark kế nhiệm, khó hơn | Claude Opus 5.5 ~65% (6/10/2026) |
| Khác | SWE-Touch (người dùng sửa code giữa chừng), RoadmapBench (nâng cấp version dài hạn), UTBoost | Đang nổi trong giới học thuật |

**Bài học:** chọn agent theo (1) harness có kiểm soát được không, (2) license, (3) chi phí token, (4) tích hợp MCP/skills; đừng dựa vào số sao.

## 3. Xu hướng kiến trúc đáng chú ý

- **Harness > Model**: các paper 2026 ("Harness Engineering: Source-Code Study of Eleven Systems", "Inside the Scaffold") cho thấy phần lớn chất lượng đến từ vòng lặp, công cụ, quản lý ngữ cảnh.
- **Plugin hóa toàn bộ** (DeepSeek Harness) và **tối giản hóa** (mini-SWE-agent) là 2 cực cùng tồn tại.
- **Cloud/async agents** (Codex cloud, Jules, Cursor cloud agents, Claude Code web) → lập trình viên trở thành người ra đề & review.
- **Memory có cấu trúc** cho agent ("Your Code Agent Can Grow Alongside You", 2026).

## 3b. Case study: Understand-Anything – codebase thành knowledge graph (trending, 2026-10-12)

> Nguồn: ảnh bảng trending người dùng gửi ("Understand-Anything: +2.331 sao/ngày"). Nghiên cứu từ repo (README, cấu trúc, CLAUDE.md), trang org, trendshift, bài Better Stack / Augment Code, các directory skill.

### 3b.1 Hồ sơ nhanh

| Thuộc tính | Giá trị (đọc 2026-10-12) |
|---|---|
| Repo | https://github.com/Egonex-AI/Understand-Anything (URL cũ `Lum1104/Understand-Anything` redirect về đây; mirror `GoodDingo/understand-anything`) |
| Tác giả | Yuxiang Lin · Infinite Universe, Inc. (dòng bản quyền); org **Egonex-AI** ("Understand anything. Understand anyone."), website egonexai.com, 1 repo public, không member public |
| Ngôn ngữ / license | TypeScript, pnpm workspaces, Tree-sitter, Vite, Vitest; **MIT** |
| Số liệu | **85,9k★**, 7,2–7,5k fork, 42 contributor, 857 commit, 117 issue mở, 200 PR mở; cập nhật 10/10/2026 |
| Trending | #1 GitHub Trending TypeScript 4 ngày (21–28/5/2026, lần đầu 23/5); trendshift +6.836★/61 ngày (13/8–12/10), đỉnh 12–14/9 (+227/+240/+241 mỗi ngày); ảnh người dùng gửi ghi +2.331★/ngày (đợt sóng mới) |
| Tagline | "Graphs that teach > graphs that impress" |

### 3b.2 Nó làm gì

- Biến code (hoặc docs, wiki kiểu "Karpathy LLM wiki") thành **knowledge graph tương tác**: node là file/hàm/class, cạnh là import/call/kế thừa; tóm tắt tiếng Anh thường, **guided tour** theo thứ tự phụ thuộc, tìm fuzzy + ngữ nghĩa, **diff impact analysis**, phân lớp (API/Service/Data/UI/Utility), view business logic (domain → flow → step), UI thích ứng persona (junior dev, PM, power user), giải thích 12 pattern ngôn ngữ trong ngữ cảnh; đầu ra đa ngôn ngữ gồm **tiếng Việt** (en, zh, zh-TW, ja, ko, ru, vi).
- Lệnh: `/understand` (lưu `.ua/knowledge-graph.json`; `--language`, `--auto-update` tạo post-commit hook), `/understand-dashboard`, `/understand-chat`, `/understand-diff`, `/understand-explain`, `/understand-onboard`, `/understand-domain`, `/understand-knowledge`.
- Cài: `/plugin marketplace add Egonex-AI/Understand-Anything` → `/plugin install understand-anything`; nền tảng khác qua `install.sh`/`install.ps1` (Codex dùng tiền tố `$`). Hỗ trợ: Claude Code (plugin gốc), Cursor, VS Code + Copilot, Copilot CLI, Codex, OpenCode, OpenClaw, Antigravity, Gemini CLI, Pi Agent, Vibe CLI, Hermes, Cline, KIMI CLI, Trae, Nanobot, Kiro.
- Chia sẻ team: commit graph (trừ `.ua/intermediate/` và `diff-overlay.json`), graph lớn dùng git-lfs; viewer read-only `npx` (Node ≥18) không cần Claude Code.

### 3b.3 Cách hoạt động (điểm đáng học)

| Lớp | Cơ chế | Vì sao quan trọng |
|---|---|---|
| **Tất định** | Tree-sitter trích import/export/định nghĩa/call site/kế thừa; cùng input → cùng output; cũng là cơ sở **incremental** (chỉ phân tích file đổi) | Giảm hallucination cấu trúc, giảm token lần sau |
| **Ngữ nghĩa** | LLM sinh summary, tag, layer, domain mapping, tour, concept callout | Phần "dạy" người đọc |
| **Pipeline đa agent** | project-scanner → file-analyzer (song song tối đa 5 worker, 20–30 file/batch) → architecture-analyzer → tour-builder → graph-reviewer; thêm domain-analyzer, article-analyzer | Chia việc theo vai trò + có **reviewer** kiểm graph (evaluator pattern, mục 03) |
| **Đóng gói** | Cùng một lõi, nhiều thư mục plugin (`.claude-plugin`, `.copilot-plugin`, `.cursor-plugin`) + installer | Mẫu "một skill, nhiều host" (mục 04/20) |

README tự cảnh báo: lần chạy đầu trên codebase lớn **tốn nhiều token**; gợi ý gói subscription hoặc model local (Ollama, mục 10).

### 3b.4 Đánh giá

- **Điểm mạnh:** lai tất định + LLM đúng chỗ; incremental; output kiểm tra được (JSON trong repo); viewer không cần agent; đa host; đa ngôn ngữ (có vi).
- **Rủi ro / lưu ý:** phần lớn bài viết bên ngoài là aggregator/khuyến mãi, chưa có đánh giá độc lập về độ chính xác graph; một trang trending (trendingrepo.com) gắn cờ "có thể star-farming" cho bản owner cũ — **chưa xác minh**, nhưng tốc độ +2k★/ngày sau 5 tháng ra mắt là bất thường và đáng theo dõi (so sánh ADHD, Anatomy, OpenMontage ở mục 03/06/19 đều có đợt sóng tương tự). Chi phí token lần đầu; graph lớn cần lfs; 200 PR mở cho thấy maintainer quá tải.
- **Vị trí trong kho:** công cụ "đọc hiểu codebase" cho coding agent, cùng nhóm với Context7/llms.txt (mục 16) và memory có cấu trúc (mục 10). Đáng thử cho onboarding dự án lạ và review tác động diff trước khi vào Ralph loop (mục 03).

## 3c. Case study: Personal Jarvis (Dodaios) – "super-app" agent cho desktop (ảnh README người dùng gửi, 2026-10-12)

> Nguồn: ảnh chụp README người dùng gửi. Nghiên cứu bằng clone đầy đủ lịch sử (commit `e28f53f`, 11/10/2026), đọc `README.md`, `AGENTS.md`, `NOTICE`, `LICENSE`, `jarvis.toml.example`, `jarvis/safety/*`, `jarvis/core/config.py`, `.github/workflows/`; trang GitHub, PyPI, personaljarvis.ai; tìm HN/Reddit (không thấy thảo luận độc lập).

### 3c.1 Hồ sơ nhanh

| Thuộc tính | Giá trị (đọc 2026-10-12) |
|---|---|
| Repo | https://github.com/Dodaios/Dodaios — **đổi tên từ `PersonalJarvis/PersonalJarvis`** 10–11/10/2026 (PR #525, #526, #530; URL cũ vẫn redirect). PyPI `personal-jarvis` còn trỏ homepage về URL cũ, nhưng attestation bản 3.1.1 ghi repo Dodaios |
| Tác giả | Ruben Lütke (Đức): **5.777/5.839 commit** (~99%); 3 người khác 10–14 commit; 2 commit ký "Claude" |
| Tuổi / nhịp | Commit đầu 19/6/2026 → 105 ngày có commit, đỉnh **264 commit/ngày** (1/7/2026); 71 tag, v3.1.1 (10/10/2026); 378 commit "auto-save WIP via Claude stop-hook" |
| Quy mô | ~664k dòng Python trong `jarvis/` (74 package con), frontend React, 2.564 file `test_*.py`, 23 workflow GitHub Actions, `CHANGELOG.md` 212 KB |
| License | **Apache-2.0** từ 2.0.0 (commit 27/8/2026 "switch from MIT to Apache 2.0"); bản ≤1.6.0 vẫn MIT. Có `TRADEMARK.md` (không liên kết Marvel/Disney…) |
| Số liệu GitHub | 183★, 70 fork, 4 watcher, 33 issue, 56 PR mở; 20 topic (`claude-code`, `computer-use`, `wake-word`, `mcp`…) |
| Cài đặt | `irm …/install.ps1 \| iex` / `curl … install.sh \| bash`, installer .exe/.dmg/AppImage (macOS chưa notarize, Windows chờ SignPath), hoặc `pip install personal-jarvis` + `jarvis serve` (headless, cổng 47821) |

### 3c.2 Nó làm gì (theo README, đã đối chiếu thư mục)

- **Agentic IDE**: nhiều pane terminal thật, mỗi pane chạy một CLI (Claude Code, Codex, OpenCode, Kimi Code, GLM, Grok Build, Antigravity, Cursor CLI, DeepSeek Harness); pane có **call sign T1, T2…** để ra lệnh bằng giọng ("Tell T1 to write the tests"), gửi cùng một task cho nhiều pane rồi so sánh. Dùng subscription có sẵn của người dùng (`jarvis/claude_auth.py`, `codex_auth.py`, `*_quota_state.py`).
- **Jarvis Agents**: agent sống lâu, mỗi agent một chat không kết thúc, ghi chú riêng ("self-learning"), routine theo lịch; mission dài chạy trong **git worktree**, tách worker song song, qua bước review. Có phần chuyển thể từ `NousResearch/hermes-agent` (`third_party/hermes-agent`, MIT).
- **Giọng nói**: wake word tự chọn, hội thoại ngắt lời được, dictation vào mọi app, gọi điện (Twilio); STT/TTS chạy offline được (Silero VAD).
- **Computer use** desktop + trình duyệt; **marketplace** >40 plugin/MCP/skill/CLI; memory dạng **wiki local** có trích dẫn; Routines; Appshots; "Jarvis Verse" 3D; pet trên desktop; kênh Telegram/Discord; CLI `jarvis` + API local.

### 3c.3 Đọc cổng thật thay vì văn xuôi (mục 23, WORKFLOW)

| Tuyên bố README | Code / cấu hình thật | Nhận xét |
|---|---|---|
| "Every action passes a risk check with four levels: safe, monitor, ask and block. Anything that could change your system waits for your approval" | `jarvis/safety/risk_tier.py`: thứ tự **blacklist → whitelist → tier mặc định của tool** (+ hook `risk_tier_for_args`). `config.py`: `approval_mode` mặc định **`"bypass"`**, `default_tier = "safe"`; chỉ tier `ask` mới hỏi | Mặc định là **không hỏi** cho việc do app tự chạy; README nói ngược lại. Docs `safety-and-approvals.md` có thừa nhận kết nối kế thừa "monitor default" chạy không hỏi |
| Blacklist chặn lệnh nguy hiểm | `fnmatch` trên chuỗi `"<tool> <args>"` và `"<args>"`; blacklist mặc định chỉ 5 mẫu (`format *`, `rm -rf /`, `del /f /s /q C:\`…). Docstring ghi audit 8/8/2026 phát hiện **mọi mẫu blacklist mặc định từng "chết"** với `run_shell` | Glob khớp chuỗi dễ né (`rm -rf ~`, khoảng trắng kép, `bash -c`) |
| Lệnh phá huỷ sẽ hỏi trước | `command_impact.py` tách `&&`, `;`, `\|` và xếp loại read/modify/destructive — **nhưng chỉ chạy ở bước 3**; whitelist mặc định có `"git log *"`, `"git diff *"` và **thắng trước** | `fnmatchcase("git log -1; rm -rf ~/x", "git log *") == True` → lệnh nối sau whitelist được hạ xuống `safe`, bỏ qua bộ phân loại (phân tích tĩnh 12/10/2026, **chưa chạy thử trong app**) |
| — | `AGENTS.md` là file hướng dẫn duy nhất; `.claude/{agents,skills}` và `.codex/agents/*.toml` là bản sinh, CI (`scripts/ci/check_agents_md.py`) chặn `CLAUDE.md` | Mẫu "một nguồn, nhiều host" giống mục 04/20 |
| — | `AGENTS.md` §1 "Traps no one guesses": working tree **dùng chung** giữa nhiều phiên agent (cấm `git add -A`); probe vào app thật **tốn tiền thật** (5 lượt test từng tốn $6,82); cấm Chrome headless (từng ghim CPU 100%); mọi reconnect phải jitter (từng cạn cổng ephemeral) | Sổ bẫy cụ thể, có mã AP-n/BUG-n — cùng tinh thần `TRAPS.md` mục 03/23 |

### 3c.4 Đánh giá

- **Điểm mạnh:** gom ADE + voice + computer use + agent nền vào một app local, không cần tài khoản, dùng lại subscription sẵn có; ghi công bên thứ ba cẩn thận (`NOTICE` liệt kê T3 Code, hermes-agent, Silero); `AGENTS.md` là ví dụ tốt về sổ bẫy thực chiến cho codebase do agent viết; có release bot, scorecard, attestation, nhiều workflow smoke đa nền tảng.
- **Rủi ro:** (1) **bus factor = 1** và nhịp 50–260 commit/ngày cho thấy phần lớn code do agent sinh — 664k dòng Python sau ~4 tháng khó audit; (2) mặc định `bypass` + whitelist thắng bộ phân loại lệnh là khoảng hở thật cho app có quyền điều khiển máy (mục 12); (3) cài bằng `curl | bash`/`irm | iex`, binary macOS chưa notarize, Windows chưa ký; (4) đổi tên repo, đổi license MIT→Apache trong 4 tháng → link/PyPI chưa đồng bộ; (5) cộng đồng nhỏ (183★), chưa có review độc lập — phần tính năng đều là **tự công bố**; (6) trùng tên với `open-jarvis/OpenJarvis` (Stanford, ~11k★, Apache-2.0, local-first nhưng thiên về framework + đo hiệu năng/năng lượng) và nhiều fork/mirror `*/PersonalJarvis`.
- **So với nhóm ADE (§1.3):** T3 Code/Orca/Claude Squad chỉ làm "bàn điều phối" và giữ phạm vi hẹp; Personal Jarvis là cực "làm tất cả", gần OpenClaw/Hermes Agent (mục 02) hơn là một IDE. Chọn T3 Code hoặc Claude Squad nếu chỉ cần chạy agent song song; thử Personal Jarvis nếu muốn điều khiển bằng giọng nói, nhưng đặt `approval_mode = "ask"` và xoá whitelist `git log *`/`git diff *` (hoặc chỉ whitelist lệnh không tham số) trước khi giao quyền computer use.
- **Bài học đem về kho:** (a) **call sign cho pane** là giao diện điều phối bằng giọng rẻ mà hiệu quả; (b) allowlist kiểu glob trên chuỗi lệnh phải chạy **sau** bộ tách lệnh nối, không trước (mục 12 §4); (c) stop-hook auto-commit WIP là lưới an toàn, nhưng sinh 378 commit nhiễu → nên squash trước khi merge.

## 4. Nguồn

- https://pinggy.io/blog/best_open_source_cli_coding_agents/
- https://www.morphllm.com/best-ai-coding-agents-2026
- https://www.openhands.dev/blog/open-source-ai-coding-agents
- https://stoneforge.ai/blog/open-source-ai-coding-agents/
- https://andrew.ooo/answers/best-open-source-ai-coding-agent-2026-ranked-guide/
- https://thenewstack.io/deepseek-harness-open-source-plugins/
- https://www.mindstudio.ai/blog/deepseek-harness-coding-agent
- https://github.com/OpenHands/OpenHands · https://github.com/SWE-agent/mini-swe-agent · https://github.com/SWE-agent
- https://arxiv.org/html/2604.03515v2 (Inside the Scaffold) · https://arxiv.org/pdf/2609.00006 (Harness Engineering)
- Understand-Anything: https://github.com/Egonex-AI/Understand-Anything · https://github.com/Egonex-AI · https://trendshift.io/repositories/23482 · https://betterstack.com/community/guides/ai/understand-anything/ · https://www.augmentcode.com/learn/understand-anything-71k-stars · https://mcpmarket.com/tools/skills/understand-anything-code-graph · https://github.com/GoodDingo/understand-anything · understand-anything.com
- Personal Jarvis: https://github.com/Dodaios/Dodaios (clone đầy đủ, commit e28f53f) · https://github.com/PersonalJarvis/PersonalJarvis (URL cũ) · https://pypi.org/project/personal-jarvis/ · https://personaljarvis.ai · https://github.com/alvinreal/awesome-opensource-ai/pull/788 · https://github.com/slavakurilyak/awesome-ai-agents/issues/637
- ADE so sánh: https://github.com/pingdotgg/t3code · https://github.com/BloopAI/vibe-kanban · https://github.com/smtg-ai/claude-squad · https://github.com/open-jarvis/OpenJarvis · https://agentsroom.dev/blog/best-multi-agent-coding-tools · https://www.codeagentswarm.com/en/guides/best-tools-to-run-multiple-ai-coding-agents · https://nimbalyst.com/blog/best-multi-agent-desktop-apps-claude-code-codex-2026/ · https://aitoolsatlas.ai/tools/orca-stably/review (Orca, số sao chưa xác minh)
- https://www.vals.ai/benchmarks/swebench · https://arxiv.org/pdf/2609.08149 (SWE-Bench Pro Verified)
- https://codeant.ai/blogs/best-ai-code-editor-cursor-vs-windsurf-vs-copilot · https://www.developersdigest.tech/blog/ai-coding-tools-pricing-2026 · https://levelop.dev/blog/the-best-ai-coding-agents-in-2026-a-practical-ranking-for-working-developers
