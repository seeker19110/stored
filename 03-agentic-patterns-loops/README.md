# 03 · Agentic Patterns, Loops & Harness/Context Engineering

> Các mẫu thiết kế vòng lặp agent, kỹ thuật vận hành agent tự trị, và cách quản lý ngữ cảnh. Đây là phần "lý thuyết + thực hành" nền cho mọi mục khác.

## 1. Định nghĩa cốt lõi (Anthropic, *Building Effective Agents*, 12/2024)
>
> "Agents are typically just LLMs using tools based on environmental feedback in a loop."

Phân biệt **workflow** (luồng LLM + tool được code định sẵn) và **agent** (LLM tự quyết định luồng). Khuyến nghị: bắt đầu từ mẫu đơn giản nhất, chỉ thêm tự trị khi có lợi ích đo được.

### 5 workflow pattern

| Pattern | Ý tưởng | Ví dụ |
|---|---|---|
| Prompt chaining | Chuỗi gọi LLM tuần tự, có gate kiểm tra giữa các bước | Viết outline → kiểm tra → viết bài |
| Routing | Phân loại input rồi chuyển tới prompt/model chuyên biệt | Hỗ trợ khách hàng: hoàn tiền / kỹ thuật |
| Parallelization | Sectioning (chia việc độc lập) hoặc Voting (chạy nhiều lần lấy đa số) | Review code bằng nhiều góc nhìn |
| Orchestrator–workers | Orchestrator tự chia task động, giao worker, tổng hợp | Sửa code nhiều file, tìm kiếm đa nguồn |
| Evaluator–optimizer | Một LLM sinh, một LLM chấm, lặp | Dịch văn học, tìm kiếm nhiều vòng |

## 2. Hình dạng vòng lặp agent

| Mẫu | Nguồn gốc | Cơ chế | Ưu / nhược |
|---|---|---|---|
| **ReAct** | Yao et al. 2022 (Princeton/Google) | Thought → Action → Observation lặp | Linh hoạt, dễ debug / thiếu cái nhìn toàn cục, có thể lạc đường |
| **Plan-and-Execute** | LangChain, BabyAGI | Planner lập kế hoạch, executor thực thi, planner sửa lại | Hiệu quả cho task phụ thuộc nhiều bước / tốn vòng lập kế hoạch |
| **Reflexion** | Shinn et al. 2023 | Thêm tự phê bình sau mỗi lần thử, lưu vào memory | Cải thiện qua lần thử / cần tiêu chí đánh giá rõ |
| **LATS / Tree-of-Thought** | 2023 | Tìm kiếm cây trên các bước suy luận | Mạnh với bài toán tìm kiếm / đắt |
| **Generator–Evaluator (long-running)** | Anthropic (long-running agents note) | Tách sinh & đánh giá, handoff bằng artifact, reset ngữ cảnh | Nền cho agent chạy nhiều giờ |

Khảo sát học thuật: *The Landscape of Emerging AI Agent Architectures* (arXiv 2404.11584) kết luận thành công phụ thuộc **planning + self-correction**.

## 3. Ralph Wiggum loop – vòng lặp tự trị cho coding agent

- **Tác giả:** Geoffrey Huntley (7/2025). Dạng thuần túy:

  ```bash
  while :; do cat PROMPT.md | claude ; done
  ```

- **Nguyên lý:** mỗi vòng là một session mới; "bộ nhớ" duy nhất là **file trong repo** (plan, test, progress). Agent lặp cho tới khi tiêu chí hoàn thành đạt.
- **Phiên bản Anthropic:** plugin `ralph-loop` trong repo `anthropics/claude-code` dùng **Stop hook** chặn việc kết thúc session và nạp lại prompt (giữ ngữ cảnh trong 1 session); kết thúc bằng promise string + giới hạn số vòng. Claude Code cũng có `/loop`, `/goal`, `/batch` (chưa xác minh trên docs chính thức).
- **Khi nào hội tụ:** prompt chính xác + tiêu chí **kiểm chứng được** (tests pass, lint sạch, build ok). Prompt mơ hồ → lạc.
- **Phê bình:** phù hợp greenfield; để loop tự merge/tag là rủi ro khi người khác phụ thuộc vào output (orbi.build: "passed 28 tests, then failed review").
- **Triển khai cộng đồng:** `frankbria/ralph-claude-code` (exit detection thông minh), nhiều guide tại awesomeclaude.ai, paddo.dev.
- **Phản biện từ repo của chủ kho (projects-template PR #287 "ba cổng máy cho /auto-complete", xboss, 2026-10-12 — mục 23 §2.2):** `<promise>` string (và `/goal`) là **lời khai của model**, không phải bằng chứng. Thay bằng: (1) Stop hook đọc **file trạng thái** do script/CI điền (test, lint, build) chứ không đọc output của model; (2) **chuỗi đỏ cùng chữ ký** — cùng một failure lặp N lần (xboss: 3 repair) thì dừng và báo BLOCKED thay vì lặp tiếp; (3) **trần số vòng** (`STOP_HOOK_BLOCK_CAP`, mặc định 8 ở projects-template) + fingerprint sha256 để Stop hook không chạy lại cổng tĩnh trên cùng diff; (4) **evidence gate**: muốn kết thúc phải nêu đường dẫn bằng chứng tồn tại thật.
- **Vòng đời hook Claude Code dùng thật** (bảng từ `projects-template/.claude/settings.json`, xboss, dhcb): `SessionStart` (nạp PROGRESS.md + git state, `additionalContext`) · `PreToolUse` (`permissionDecision: deny|ask` — risk-zone gate "fact-forcing": lần đầu sửa file vùng rủi ro phải nêu 4 dữ kiện; protect-config; block `curl | sh`) · `PostToolUse` (telemetry, nhắc file dùng chung) · `Stop` (cổng tĩnh theo file đổi, đọc `stop_hook_active` để tránh đệ quy) · `SubagentStop` · `PreCompact`; mọi hook có biến env tắt có chủ đích và **có test** (`tests/claude-hooks.test.ts`). Kho trước đây chỉ biết Stop hook của Ralph.
- **Xem thêm mục 21 (Autonomous Workflows):** `/loop` đã được xác minh trên docs chính thức (cron 5 trường, jitter, hết hạn 7 ngày, tối đa 50 task, `loop.md`); Routines cloud (≥1 giờ, trigger lịch/API/GitHub); hai bài harness dài hạn của Anthropic (11/2025, 3/2026).

## 4. Context engineering & harness engineering

| Khái niệm | Nội dung | Nguồn |
|---|---|---|
| Context engineering (Anthropic, *Effective Context Engineering for AI Agents*) | Ngân sách ngữ cảnh là kỷ luật kỹ thuật: viết / chọn / nén / cô lập ngữ cảnh qua trajectory dài | anthropic.com, philschmid.de |
| Bài học Manus | Rebuild framework 4 lần; **KV-cache hit rate** là metric quan trọng nhất; đừng để agent tự viết lại todo.md (tốn ~30% token) → dùng planner sub-agent, inject khi cần | philschmid.de part 2, Medium |
| Harness engineering (OpenAI/Anthropic thuật ngữ) | Harness = hệ thống cho phép model hành động như agent: repo map, AGENTS.md, runtime control, sandbox | arXiv 2609.00006, 2606.20683, preprints 202603.1756 |
| MemoHarness / structured memory | Harness tự học từ kinh nghiệm | arXiv 2607.14159, 2603.13258 |
| Think in Code / Code execution with MCP | Model viết code lọc dữ liệu trong môi trường thực thi, chỉ đưa kết quả vào context (Anthropic 11/2025: 150k → 2k token; Cloudflare "Code Mode"); đóng gói thành plugin: **context-mode** (§8b), RTK, claude-mem, Serena | anthropic.com/engineering/code-execution-with-mcp, §8b |

## 5. Multi-agent coding song song (thực hành 2026)

- **Git worktrees** cho mỗi agent (`claude --worktree`): tránh ghi đè file, tranh chấp git index, port dev-server. Không bao phủ state chia sẻ (DB, API ngoài) → serialize các bước đó.
- **Phân cấp primitive (Claude Code):** subagents (trong session) · agent teams (giữa session, thử nghiệm) · background agents · `/batch` cho thay đổi cơ học lớn.
- **Hợp đồng giao diện:** sinh OpenAPI/spec trước khi chạy song song để tránh drift (mầm của "spec-driven development").
- **Giới hạn:** thêm agent chỉ khi còn sức review; 4–5 agent → RAM; 10+ → ngân sách context mỗi agent.
- **Công cụ ADE (agent workspace):** T3 Code, Orca, Vibe Kanban (sunset), Claude Squad, Conductor, Personal Jarvis — bảng mục 01 §1.3. Personal Jarvis đặt **call sign T1/T2…** cho từng pane để giao việc bằng giọng nói và gửi cùng task tới nhiều pane để so sánh (mục 01 §3c).
- **Hướng dẫn:** `FlorianBruniaux/claude-code-ultimate-guide` (agent-teams.md), thepromptshelf.dev (6 pattern), developersdigest.tech.
- **Bẫy đã mắc thật (mục 23, 3 repo độc lập cùng ghi):** **subagent không có tool Agent** — subagent không lồng subagent (Claude Code; Hermes `delegate_task` cũng ≤10 con, không lồng) → mô hình "coordinator gọi worker" chỉ chạy khi *phiên chính* dispatch; coordinator viết thành subagent sẽ im lặng không làm gì (xboss TRAPS §7). projects-template thêm **trần 5 subagent** đồng thời.
- **Điều phối 3 tầng, chọn theo 2 trục** (projects-template `orchestration-3-tier.md`, xboss `CLAUDE.md` bảng `route:`): phiên chính viết đặc tả → coordinator (model mạnh, effort thấp) → worker theo **độ phức tạp × độ kín của đặc tả** (`complex-implementer` Opus·high / `spec-executor` Opus·low / `standard-worker` Sonnet / `mechanical-worker` Haiku); luật cứng "thiếu đặc tả thì hỏi". `scripts/model-capability-tiers.json` tách tier khỏi tên model vendor.
- **Hợp đồng giao việc cho subagent** (Sales-Hunter `SUBAGENT-TASK-CONVENTION.md`): mỗi task pack ghi `model_tier` **T0–T4** (T4 = người duyệt trước merge; side effect mạng/publish/ToS ≥ T3), enum `external_side_effects` (none / ingest-network / publish / account-change), subagent **không tự nâng tier**; **nhánh A** (1 việc lớn = 1 remote branch, subtask = commit, tiết kiệm cold-start) là mặc định, **nhánh B** (mỗi subtask một worktree) chỉ khi song song thật và path không chồng.
- **Học từ repo ngoài theo 3 cột** (`adopt-from-outside.md`): với mỗi cơ chế của repo ngoài ghi *đã có & sâu hơn / đã có nhưng nông hơn / chưa có*; **"grep cổng đang chạy, đừng đọc văn xuôi"** (đọc `settings.json`, hook, CI thay vì README); kiểm mâu thuẫn README↔file; cảnh báo nguồn do AI dựng.
- **Uỷ quyền trong đội agent (OpenCompany, mục 02 §4, 2026-10-12):** (1) **topology = ranh giới uỷ quyền** — lead chỉ giao việc cho agent nối trực tiếp, tối đa 2 tầng, mỗi tool có đúng một chủ; (2) **ẩn tool `delegate_to_*` khỏi model**, chỉ đưa roster một dòng/teammate và một tool `assign_task(mission, context, acceptance_criteria)` → giảm nhiễu chọn tool; (3) lead review kết quả specialist, trả lại nếu chưa đạt, rồi mới báo người; (4) **context** (hội thoại backend sở hữu, nối tiếp qua mọi lần kích hoạt) tách khỏi **memory** (tool gọi tường minh, người sửa được); compaction ở 0,8 cửa sổ. Bẫy thật: model local không gọi `assign_task` → job kẹt "working" mãi (issue #145) — cần timeout/no-progress detection (mục 21).
- **Kỷ luật sổ sách**: `TRAPS.md` (bẫy đã mắc thật: ngày/PR/cách rà/chốt chặn) tách khỏi ADR; `/hoc` (xboss) xếp bài học theo **mức bền**: máy kiểm được & lặp ≥2 → cổng CI; bẫy → TRAPS; theo vùng file → rule path-scoped; quy trình → skill; toàn dự án → CLAUDE.md; kiến trúc → ADR.

## 6. Checklist thiết kế agent loop (rút ra)

1. Tiêu chí dừng **kiểm chứng được bằng máy** (test, lint, type-check, build).
2. Trạng thái bền trong **file/repo**, không trong "trí nhớ" của session.
3. Giới hạn vòng lặp + exit detection + nhật ký tiến độ.
4. Tối ưu KV-cache: prefix ổn định, chỉ append, tránh sửa đầu prompt.
5. Tách generator/evaluator; evaluator nên có công cụ độc lập.
6. Cô lập tài nguyên (worktree, sandbox) khi chạy song song.
7. Người review ở cuối vòng; không để loop tự merge vào main.
8. Tín hiệu dừng do **code điền** (file trạng thái, exit code, `verified_by`), không do model khai; chuỗi đỏ cùng chữ ký ≥3 → BLOCKED.
9. Không giả định subagent lồng được subagent; dispatch từ phiên chính; ghi `model_tier` và side effect cho mỗi việc giao.

## 8. Case study: ADHD – Parallel Divergent Ideation (link từ người dùng, 2026-10-12)

| Thuộc tính | Giá trị (đọc 2026-10-12) |
|---|---|
| Repo | https://github.com/UditAkhourii/adhd · npm `adhd-agent` · docs adhd.mintlify.site · preprint adhdstack.github.io (v0.1, 25/5/2026) |
| Mô tả | "A skill for coding agents. Tree-of-thought with pruning, built on the Claude & Codex Agent SDK" |
| Tác giả | Udit Akhouri (Raj) – "Independent AI Researcher", IIT Patna; từng ở Emora Health, Malpani Ventures; 125 followers; repo liên quan: neuroarxiv (434★, check prior art trên arXiv), quicksilver, brane-code, branerail, cdaf |
| ★ / forks / commit | 4.4k ★ · ~300–314 forks · 74 commit · 2 contributor · 12 issue mở; +864★ trong 61 ngày (13/8–12/10/2026), đỉnh 19/8 (+122), đang chậm lại |
| License | MIT |
| Ngôn ngữ | TypeScript (~600 dòng core), Node 18+; cài `npx skills add UditAkhourii/adhd` hoặc `npm i -g adhd-agent` |

### Cơ chế (từ `SKILL.md` và preprint)

- **Vấn đề nhắm tới:** *premature convergence* – LLM chọn phương án hợp lý đầu tiên rồi "đánh bóng" nó.
- **Phase 1 – Diverge (không critic):** chọn 5 trong 15 "cognitive frame" (hardware engineer, regulator, 10-year-old, competitor, biology, logistics, game design, markets, inversion, $0/1h, infinite budget/10y, remove load-bearing assumption, speedrunner, ant colony, 3am on-call); spawn **5 Agent/Task call song song, cô lập** (không thấy nhau → tránh anchoring), mỗi nhánh trả JSON 6 ý tưởng ngắn. Với bài code: 4 frame code/design + 1 wild.
- **Phase 2 – Focus (critic bật):** 1 call chấm novelty/viability/fit (0–10, trọng số 0.35/0.40/0.25), gắn cờ **trap** (ý tưởng hấp dẫn nhưng chi phí ẩn); 1 call cluster theo "góc nhìn"; 3 call song song **deepen** top-3 (sketch, rủi ro chịu tải, bước đầu tiên, ý con).
- **Output cố định:** Brief → Wide set (cluster + chip `[N7 V8 F9]`) → Converge (shortlist 2–4, ★ non-obvious pick, traps riêng) → Focus → Provocation.
- **Gate tiền kiểm:** chỉ chạy khi bài **mở, rủi ro cao, cách hỏi mở**; bỏ qua với syntax/lookup/"quick/standard/one-line". ~10 call/run, 30–90 giây, **5–10× chi phí** single-shot.
- **Anti-pattern tác giả nêu:** hội tụ giả dạng phân kỳ; ý lạ mà không hội tụ; chạy "song song" tuần tự; không dám chốt.
- **Khác ToT (Yao 2023):** nhánh **cô lập** (ToT chia sẻ context), phân nhánh bằng **đổi vantage point** chứ không phải đổi bước kế tiếp, generator/critic là **2 call tách biệt** với system prompt đối lập.

### Bằng chứng & phê bình

| Nguồn | Nội dung |
|---|---|
| EVALS.md / preprint (tự báo cáo) | 6 bài kỹ thuật (LRU cache, LLM hang CLI, rate limiter + leader election, bug 0.1%, tách monolith Rails, đặt tên feature-flag); judge = LLM "skeptical staff engineer" (không nêu model); ADHD thắng 5/6; Δ: breadth +4.17, novelty +5.17, **trap detection +7.67**, actionability +3.00, builder usefulness +0.83 |
| Hạn chế tác giả tự nhận | judge cùng họ model (familiarity bias); mẫu 6 bài; frame viết tay có thể trùng ý; actionability bị **confound** do ADHD có schema output còn baseline không; chỉ bài engineering |
| The New Stack (6/2026) | Tiêu đề: *"gave Claude Code 'ADHD'… thinks 2x better now. Outside experts want more proof."* Tác giả nói với báo: "good for brainstorming and planning, **not coding**" |
| dudarik.com (5/6, cập nhật 7/7/2026) | "2×" chưa được tái lập độc lập; testdouble/han review 8 vòng nêu câu hỏi phương pháp (issues #16–18); chi phí tăng theo N, thêm độ trễ trước khi code |
| ADOPTERS.md (16 entry, tự duy trì) | Đáng tin nhất là entry có PR merge: repowire (#313), mythify, godaudits, godplans (có **control arm** và từ chối một số tính năng), han; `multi` port đa model (mỗi frame một họ model); phần còn lại là fork/cài đặt |

### Bài học cho kho này

1. Là hiện thân gọn của **parallelization (sectioning) + evaluator-optimizer** trong 5 pattern của Anthropic (mục 1), dùng đúng cho bài *open-ended* chứ không phải thực thi.
2. **Cô lập context giữa các nhánh** là điểm thiết kế đáng tái dùng khi chạy subagent song song (mục 5): subagent không nên thấy output nhau nếu muốn đa dạng.
3. Tách generator/critic bằng call riêng + rubric số + trap list → mẫu tốt cho "design review" trước khi vào Ralph loop.
4. Rủi ro: chi phí 5–10×, bằng chứng tự báo cáo với judge cùng model; nên tự chạy A/B trên bài của mình (bench/results.json có transcript đầy đủ) và kiểm tra `han` review trước khi đưa vào quy trình team.
5. Liên hệ: mục 04 (SKILL.md), mục 07 (LLM-as-judge), mục 17 (frame = persona prompting có chủ đích "distort perspective, not supply expertise").

**Nguồn:** https://github.com/UditAkhourii/adhd (README, SKILL.md, EVALS.md, ADOPTERS.md) · https://adhdstack.github.io/ · https://github.com/UditAkhourii · https://trendshift.io/repositories/39300 · https://thenewstack.io/claude-code-adhd/ · https://dudarik.com/en/blog/adhd/ · https://explainx.ai/skills/UditAkhourii/adhd/adhd · https://futureagi.com/blog/what-is-tree-of-thoughts-prompting-2026/ · https://arxiv.org/html/2605.06040v1 (Novelty-based ToT) · https://arxiv.org/html/2605.28566v2 (ToT as heuristic search)

## 8b. Case study: context-mode – giữ output tool ngoài cửa sổ ngữ cảnh (link từ người dùng, 2026-10-12)

> Nguồn: link https://github.com/mksglu/context-mode. Nghiên cứu bằng clone đầy đủ lịch sử (v1.0.169, 2.228 commit): `README.md`, `BENCHMARK.md`, `CLAUDE.md`, `LICENSE`, `stats.json`, `src/executor.ts`, `src/server.ts`, `src/cli.ts`, `hooks/core/{routing,formatters}.mjs`, `.github/workflows/`; trang GitHub; thread HN #47193064; so với bài Anthropic *Code execution with MCP* và các tool cùng loại.

### Hồ sơ nhanh

| Thuộc tính | Giá trị (đọc 2026-10-12) |
|---|---|
| Repo | https://github.com/mksglu/context-mode · npm `context-mode` · plugin marketplace Claude Code (`/plugin marketplace add mksglu/context-mode`) |
| Tác giả | Mert Köseoğlu: ~1.371/2.228 commit; 544 commit là bot `ci: update install stats`; ~6 contributor có 15–36 commit |
| Tuổi / nhịp | Commit đầu 23/2/2026, 229 ngày có commit, 198 tag (v1.0.x) |
| Quy mô | ~26,7k dòng TypeScript trong `src/`; adapter cho **17 client** (Claude Code, Codex, Gemini CLI, Copilot VS Code/JetBrains/CLI, Cursor, OpenCode, KiloCode, OpenClaw, Kiro, Zed, Pi, OMP, Antigravity…) |
| License | **Elastic License 2.0** (source-available, **không phải OSI open source**): được dùng/sửa/phân phối, cấm cung cấp dưới dạng dịch vụ hosted/managed |
| Số liệu | **26,8k★**, 1,9k fork, 104 watcher, 173 issue + 172 PR mở; HN #1 (570 điểm, 107 bình luận) |
| Badge "users" | `stats.json`: "671.8k+ users" = **lượt tải npm (626,3k) + marketplace (45,5k)** → là số lượt cài, không phải số người dùng. Dải logo "Used across teams at" (Microsoft, Google, Meta…) đều link `#`, không có bằng chứng **(chưa xác minh)** |

### Cơ chế (đọc code)

| Lớp | Cơ chế | Điểm đáng học |
|---|---|---|
| **Think in Code** | Tool MCP `ctx_execute` / `ctx_execute_file` / `ctx_batch_execute` chạy script ở 12 ngôn ngữ; chỉ **stdout** vào context | Cùng ý tưởng với bài *Code execution with MCP* của Anthropic (4/11/2025, 150k → 2k token, −98,7%) và "Code Mode" của Cloudflare: model viết code lọc dữ liệu thay vì đọc dữ liệu thô |
| **Knowledge base** | `ctx_index` / `ctx_fetch_and_index` chia markdown theo heading vào **SQLite FTS5**; tìm bằng BM25 (Porter) + trigram, gộp bằng **Reciprocal Rank Fusion**, rerank theo khoảng cách từ, sửa lỗi gõ Levenshtein; cache URL TTL 24h; dọn sau 14 ngày | RAG lexical không cần vector DB (so mục 10) |
| **Định tuyến cưỡng bức** | Hook `PreToolUse` **deny** `curl`/`wget`, HTTP inline (`fetch('http`, `requests.get(`…), `WebFetch`; Bash có output >20 dòng và Read để phân tích được chuyển sang `ctx_*`. Với Claude Code, `formatters.mjs` dùng deny + lý do thay vì `updatedInput` (comment ghi CC v2.1.x bỏ qua rewrite lệnh Bash) | Có hook: ~98% tiết kiệm theo tác giả; chỉ có file hướng dẫn (Zed, Antigravity): ~60%, "~60% compliance" |
| **Progressive throttling** | `ctx_search` lần 1–3 bình thường, 4–8 giảm kết quả + cảnh báo, **từ 9 trở đi chặn** và bắt dùng `ctx_batch_execute` | Ngân sách gọi tool cứng, không chỉ dặn trong prompt |
| **Session continuity** | 5–6 hook (PostToolUse, UserPromptSubmit, Stop, PreCompact, SessionStart) ghi sự kiện (file sửa, git, task, lỗi, quyết định) vào SQLite; sau compaction **không đổ lại** mà index FTS5 rồi truy xuất theo BM25; không `--continue` thì xoá dữ liệu phiên cũ | Tách "context" và "memory" giống OpenCompany (mục 5) và claude-mem |
| **Redaction** | `posttooluse.mjs` che `token`, `secret`, `password`, `api_key`, `cookie`… trong `tool_input` của `mcp__*` trước khi lưu DB | Nên có ở mọi hook ghi log |

### Đối chiếu tuyên bố với code (đọc cổng thật, mục 23)

| Tuyên bố | Thực tế | Nhận xét |
|---|---|---|
| "Raw data stays in a **sandboxed** subprocess… processed in **complete isolation**" (mục Privacy) | `executor.ts` `#buildSafeEnv`: copy **toàn bộ** `process.env` rồi bỏ một denylist (`BASH_FUNC_*`, `COMPlus_*`, `GIT_SSH_COMMAND`, `GIT_ASKPASS`…); có `shell: true`; không giới hạn filesystem/mạng; mặc định **không có timeout** (issue #406, để host lo) | "Sandbox" chỉ là **ranh giới tiến trình + ranh giới context**, không phải sandbox bảo mật. Chính mục Security của README thừa nhận: "not a full OS sandbox — treat approving any execution tool as approving arbitrary code". Hai mục README mâu thuẫn nhau |
| "Credential passthrough… without exposing them to the conversation" | Đúng là token (`GITHUB_TOKEN`, AWS…) không in vào context, nhưng script do model viết **có** quyền dùng chúng | Thành ra rủi ro prompt injection → exfiltration giống Bash |
| Chặn `curl`/`WebFetch` vì "tốn context" | Hook đẩy truy cập mạng từ tool host (Bash/WebFetch, có thể nằm trong sandbox và luật quyền của host) sang tool MCP `ctx_execute` "full network access", chạy trong tiến trình MCP server. Dự án từng phải vá đúng kiểu thoát này cho file (#852, `ctx_execute_file` giới hạn trong project root) | **Phân tích tĩnh, chưa kiểm chứng trên từng host**: với host sandbox Bash nhưng không sandbox MCP server, cài context-mode có thể **nới** ranh giới mạng/FS. README khuyên "keep host-level sandboxing enabled" nhưng không nói sandbox host có phủ tiến trình MCP hay không. Lớp an toàn bù lại: đọc lại luật `deny` của `.claude/settings.json` và áp vào `ctx_*`, tách lệnh nối `&&`/`;`/`\|` trước khi so (đúng thứ tự mà Personal Jarvis làm sai, mục 01 §3c) |
| "Nothing leaves your machine. No telemetry" | Không tìm thấy telemetry trong `src/`; có gọi `registry.npmjs.org/context-mode/latest` để kiểm phiên bản; `ctx insight` chỉ **mở trình duyệt** tới `context-mode.com/insight` (dashboard hosted B2B: "per-engineer productive rate… CTO, EM, CISO, FinOps") | Đúng về dữ liệu, nhưng đang hình thành mô hình **open-core**: lõi ELv2 + dashboard thương mại |
| "315 KB → 5.4 KB, 98%"; "session từ ~30 phút thành ~3 giờ" | `BENCHMARK.md`: 21 kịch bản, đo **byte vào context**, không đo chất lượng câu trả lời; tác giả nói trên HN "We haven't run formal benchmarks on answer quality yet". Có kịch bản chỉ tiết kiệm 13% (Playwright network requests) | Con số giảm byte là thật nhưng không chứng minh agent làm việc tốt hơn |

### Phản biện bên ngoài (HN #47193064, 570 điểm)

- **Mất thông tin:** benchmark giả định model luôn viết đúng code tóm tắt; hook quá hung hăng với output nhỏ; "information preservation is a real issue".
- **Phạm vi:** một người thử thấy hook **không chặn được response của MCP server bên thứ ba** — chỉ áp cho tool có sẵn và CLI wrapper (tác giả phản bác, chưa ngã ngũ). README hiện chỉ "nhắc lại" (re-inject) hướng dẫn bọc MCP ngoài vào `ctx_execute` mỗi 10 lần gọi (`CONTEXT_MODE_EXTERNAL_MCP_NUDGE_EVERY`).
- **Lựa chọn khác:** subagent (cô lập context sẵn có trong Claude Code), redirect output ra file, CLI thay MCP, RTK; "stats say subagents didn't benefit from it".
- **Trình bày:** vài người nghi bài đăng và phản hồi do LLM viết; claim "Bun nhanh 3–5×" không liên quan vì LLM mới là nút cổ chai.

### So sánh với công cụ cùng mục tiêu (★ trang GitHub 12/10/2026)

| Công cụ | ★ | License | Cách giảm context | Khác context-mode |
|---|---|---|---|---|
| **context-mode** | 26,8k | ELv2 | Chạy code + index FTS5 + hook chặn/chuyển tool + khôi phục phiên | Bao trọn nhiều lớp, cưỡng bức qua hook |
| **RTK** (rtk-ai/rtk) | 83,1k | Apache-2.0 | Binary Rust, hook viết lại `git status` → `rtk git status`, lọc/gộp/cắt/khử trùng output CLI; lưu output đầy đủ khi lệnh lỗi | Chỉ lọc output lệnh shell, không đổi tool, không cần MCP; README tự nói 90% output bash **không** có nghĩa là giảm 90% hoá đơn |
| **claude-mem** (thedotmack) | 99,9k | Apache-2.0 | 5 hook ghi lại phiên, AI nén thành observation, SQLite FTS5 + Chroma, 4 tool MCP truy xuất 3 lớp | Tập trung **memory giữa các phiên**; có Cloud Sync tuỳ chọn (cmem.ai) |
| **Serena** (oraios) | ~30,2k | GPL-3.0 (SolidLSP MIT) | Tool MCP mức **symbol** qua LSP (>40 ngôn ngữ): tìm/sửa theo hàm/class thay vì đọc cả file | Giảm context khi **đọc code**, không phải khi xử lý log/web |
| **Code execution with MCP** (Anthropic) / **Code Mode** (Cloudflare) | – | mẫu thiết kế | Đưa MCP server thành API code, agent viết code gọi và lọc trong môi trường thực thi | Là **nguyên lý** gốc; Anthropic nhấn mạnh cần sandbox + giới hạn tài nguyên + giám sát — đúng phần context-mode còn mỏng |
| **Có sẵn trong Claude Code** | – | – | Subagent (context riêng, chỉ trả tóm tắt), `/compact`, chuyển output dài ra file | Không cài thêm, không thêm bề mặt tấn công |

### Bài học cho kho này

1. **Ngân sách context là cổng máy, không phải lời dặn:** hook chặn + throttling cứng (lần 9 bị chặn) hiệu quả hơn "hãy tiết kiệm" trong `CLAUDE.md` (~98% so với ~60% theo tác giả, chưa có đánh giá độc lập).
2. **Think in Code** đáng áp dụng ngay **không cần cài gì**: với log/CSV/test output, bảo agent viết script in ra kết quả tổng hợp thay vì `cat`. Đây là cùng một kỹ thuật với bài của Anthropic.
3. **Đừng gọi tiến trình con là sandbox.** Muốn cô lập thật thì dùng sandbox của host hoặc E2B/Daytona/container (mục 11); và kiểm tra xem plugin MCP có đưa tool ra **ngoài** sandbox của host không (mục 12).
4. **Đo chất lượng, không chỉ đo byte:** trước khi áp cho team, chạy A/B trên vài task thật (pass@1, số lượt sửa, chi phí) có/không có context-mode — giống khuyến nghị cho ADHD (§8).
5. **License ELv2** ổn cho dùng nội bộ, nhưng không được đóng gói thành dịch vụ hosted; ghi vào checklist chọn tool (mục 09).
6. Liên hệ: mục 10 (FTS5/BM25/RRF, memory), mục 11 (sandbox), mục 12 (allowlist + tách lệnh nối), mục 20 (plugin marketplace), mục 01 §1.3 (ADE).

**Nguồn:** https://github.com/mksglu/context-mode (clone đầy đủ, v1.0.169) · https://www.npmjs.com/package/context-mode · https://news.ycombinator.com/item?id=47193064 · https://www.anthropic.com/engineering/code-execution-with-mcp · https://github.com/rtk-ai/rtk · https://github.com/thedotmack/claude-mem · https://github.com/oraios/serena · context-mode.com/insight

## 8c. Kiểm ảnh "How AI Agents Work: Agent = model + a harness that runs a loop" (ảnh người dùng gửi, 2026-10-13)

> Sơ đồ một trang: Trigger → khung **Harness** chứa vòng 1 Build context → 2 LLM decides → ◇ "Answer now / goal met?" → 3 Act (tools) → 4 Observe → quay lại 1; bên trái là Memory (ngắn hạn = cửa sổ ngữ cảnh, dài hạn = lưu/truy xuất), Guardrails, Observability + Evals; đầu ra là answer / action taken / handoff.

**Nguồn ảnh:** không ghi tác giả hay logo; không tìm thấy bài gốc đã đánh chỉ mục (13/10/2026). Chữ "LLM" ở dòng "turns an LLM into a working agent" bị vỡ ký tự, dấu hiệu thường gặp của ảnh do model sinh ảnh tạo ra **(chưa xác minh)**. Công thức "Agent = Model + Harness" xuất phát từ bài *The Anatomy of an Agent Harness* (Vivek Trivedy, LangChain, 3/2026): harness là mọi code, cấu hình và logic thực thi không phải là model. DataCamp ghi rõ đây là mô hình tư duy, không phải chuẩn.

### Từng khối: đúng tới đâu

Ký hiệu: ✅ đúng · ⚠️ đúng nhưng thiếu ý quan trọng · ❌ sai.

| Khối | Ảnh nói | Đánh giá | Bổ sung / đọc sâu |
|---|---|---|---|
| Công thức | Agent = model + harness chạy vòng lặp | ✅ | Khớp Anthropic (*Building Effective Agents*: LLM dùng tool trong vòng lặp dựa trên phản hồi môi trường) và Simon Willison ("tools in a loop to achieve a goal") — §1 |
| Trigger | user · event · schedule · another agent | ✅ | Lịch/cron và webhook: mục 21 (`/loop`, Routines) |
| 1 · Build context | system prompt, tool schema, lịch sử, memory truy xuất, kết quả tool trước | ⚠️ | Thiếu **quản lý cửa sổ**: compaction/tóm tắt khi đầy, giữ output tool lớn ngoài cửa sổ, prefix ổn định cho KV/prompt cache — §4, §8b, checklist §6 mục 4 |
| Memory | ngắn hạn = cửa sổ ngữ cảnh; dài hạn lưu/truy xuất (tự động hoặc qua tool) | ✅ | Trạng thái bền nên nằm trong file/repo chứ không trong phiên — checklist §6 mục 2; mục 10 §4 |
| 2 · LLM decides | suy luận, chọn hành động | ✅ | — |
| ◇ Answer now / goal met? | nhánh Yes → trả lời (có thể ngay vòng 1, 0 tool), No → gọi tool | ⚠️ | Trên thực tế không có bước kiểm riêng: harness đọc **output của model** — có khối tool call thì chạy tool, không có thì dừng (Claude API: `stop_reason` = `tool_use` hay `end_turn`). "Goal met?" vì vậy là **lời khai của model**. Thiếu hai nhánh dừng do harness quyết: hết **max steps/budget/token** (khối Guardrails không nối vào vòng) và **tiêu chí dừng kiểm bằng máy** (test, lint, exit code) — checklist §6 mục 1, 3, 8 |
| 3 · Act (tools) | web search, code, file, API, DB, memory search, MCP, sub-agent | ⚠️ | Model chỉ **sinh lời gọi có cấu trúc**, harness mới thực thi (trừ server tool) → đây là chỗ đặt kiểm quyền và sandbox (mục 11 §3, mục 12). Thiếu gọi tool **song song** và lỗi tool trả lại thành observation |
| 4 · Observe | kết quả quay lại ngữ cảnh, vòng chạy 0+ lần | ✅ | Output tool thường chiếm phần lớn cửa sổ → §8b (context-mode) |
| Guardrails | quyền, người duyệt, max steps · budget, lỗi & retry, bọc mọi hành động | ✅ (nội dung) | Đặt đúng chỗ: hook trước/sau mỗi tool (PreToolUse/PostToolUse) — mục 20, mục 23; nhưng sơ đồ vẽ tách khỏi vòng nên không thấy nó **chặn** được nhánh nào |
| Observability + Evals | trace, log, chi phí, độ trễ; "output có tốt không?" | ⚠️ | Eval chủ yếu chạy **ngoài** vòng runtime (bộ test offline, CI, replay), vẽ trong harness dễ hiểu nhầm là tự đánh giá lúc chạy. Trace theo chuẩn OpenTelemetry GenAI — mục 07 |
| Final output | answer · action taken · handoff | ✅ | Handoff sang người/agent khác: mục 02, mục 04 (A2A) |

**Tổng:** 7 ✅, 4 ⚠️, 0 ❌. Ảnh đúng ở mức "agent chạy thế nào" và đáng dùng để giải thích cho người mới; chỗ yếu nhất là nút dừng: nó gợi ý agent tự biết đã xong, trong khi harness tốt dừng theo **ngân sách** và **kiểm bằng máy**.

### Thiếu so với harness thật (2026)

- **Bền và chạy lại được:** checkpoint/resume sau crash, idempotency của tool có tác dụng phụ — mục 21 (durable execution).
- **Cô lập:** sandbox/worktree cho tool chạy code và cho subagent song song — mục 11 §3, §5 ở trên.
- **Phân lớp hướng dẫn:** system prompt + file luật repo (`AGENTS.md`/`CLAUDE.md`) + skill nạp theo nhu cầu — mục 04 (Agent Skills), mục 20.
- **Nội dung ngoài là dữ liệu:** kết quả web/tool có thể chứa prompt injection; ảnh không nhắc — mục 12 §1.

**Dùng ảnh thế nào:** tốt làm hình minh hoạ vòng ReAct có harness (§2); khi thiết kế thật thì đọc kèm checklist §6, đặc biệt mục 1 (dừng bằng máy) và mục 8 (tín hiệu dừng do code điền, không do model khai).

## 9. Nguồn (mục 1–7)

- Mục 23 §2.1–2.4, §4.3, §4.5 (projects-template, xboss, Sales-Hunter; đọc clone nông 2026-10-12)
- https://www.anthropic.com/research/building-effective-agents
- https://docs.spring.io/spring-ai/reference/api/effective-agents.html (diễn giải lại 5 pattern)
- https://atlan.com/know/ai-agent/what-is-an-agent-loop/ · https://blogs.oracle.com/developers/what-is-the-ai-agent-loop-the-core-architecture-behind-autonomous-ai-systems
- https://servicesground.com/blog/agentic-reasoning-patterns/ · https://arxiv.org/pdf/2404.11584 · https://arxiv.org/pdf/2509.08646
- https://arxiv.org/pdf/2603.05344 (Building Effective AI Coding Agents for the Terminal)
- https://github.com/anthropics/claude-code/blob/main/plugins/ralph-wiggum/README.md · https://github.com/frankbria/ralph-claude-code
- https://www.theregister.com/2026/01/27/ralph_wiggum_claude_loops/ · https://awesomeclaude.ai/ralph-wiggum · https://paddo.dev/blog/ralph-wiggum-autonomous-loops/ · https://orbi.build/blog/ralph-loop-claude-code
- https://www.philschmid.de/context-engineering-part-2 · https://snowan.gitbook.io/study-notes/ai-blogs/how-to-build-agent-harness
- https://arxiv.org/pdf/2609.00006 · https://arxiv.org/pdf/2606.20683 · https://arxiv.org/pdf/2607.14159 · https://www.preprints.org/manuscript/202603.1756
- https://github.com/FlorianBruniaux/claude-code-ultimate-guide/blob/main/guide/workflows/agent-teams.md · https://thepromptshelf.dev/blog/claude-code-multi-agent-orchestration-patterns-2026/ · https://www.developersdigest.tech/blog/git-worktrees-claude-code-parallel-agents-guide · https://www.aakashx.com/blog/parallel-claude-code-agents/
- §8c ảnh "How AI Agents Work" (13/10/2026): https://langchain.com/blog/the-anatomy-of-an-agent-harness (Vivek Trivedy, 3/2026) · https://www.datacamp.com/blog/agent-harness · https://addyosmani.com/blog/agent-harness-engineering/ · https://blogs.oracle.com/developers/the-agent-loop-decoded-three-levels-every-agent-engineer-must-know · https://strandsagents.com/docs/learning/how-agents-really-work/ · https://www.anthropic.com/research/building-effective-agents · https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview (stop_reason, server tool)
