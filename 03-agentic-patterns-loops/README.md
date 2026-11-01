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
- **Phân cấp primitive (Claude Code):** subagents (trong session) · agent teams (giữa session, thử nghiệm; kiểm docs 31/10/2026 ở §8f) · background agents · `/batch` cho thay đổi cơ học lớn.
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
| **claude-mem** (thedotmack; hồ sơ đầy đủ mục 10 §4e) | 99,9k | Apache-2.0 | 5 hook ghi lại phiên, AI nén thành observation, SQLite FTS5 + Chroma, 4 tool MCP truy xuất 3 lớp | Tập trung **memory giữa các phiên**; có Cloud Sync tuỳ chọn (cmem.ai) |
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

### Cập nhật 2026-10-16: kiểm ảnh README người dùng gửi

> Ảnh chụp đầu README trên GitHub: banner "99% SAVINGS · CLAUDE CODE" (não pixel), nút "Watch demo · YouTube", mục **Install** ("Platforms are grouped by install complexity…"), khối Claude Code với điều kiện "Claude Code v1.0.33+", lệnh `/plugin marketplace add` + `/plugin install context-mode@context-mode` và `/context-mode:ctx-doctor`. Đối chiếu bằng clone lại repo ngày 16/10/2026.

| Chi tiết trong ảnh | Kiểm chứng | Nhận xét |
|---|---|---|
| Banner "**99% SAVINGS**" | Không phải ảnh của README: đó là thumbnail (`img.youtube.com/vi/QUHrntlfPo4/maxresdefault.jpg`) của video *"Claude Code is Expensive. This MCP Server Fixes It (Context Mode)"* trên kênh **Better Stack** (oEmbed YouTube), gắn vào README từ commit `bab2f0a2` (5/4/2026) | Văn bản README vẫn ghi **98%** (315 KB → 5,4 KB). 99% chỉ là mức của vài kịch bản đơn lẻ (Playwright snapshot, git log, JSON 7,5 MB). Con số trên banner là của bên thứ ba, làm tròn lên, và vẫn chỉ đo **byte**, không đo chất lượng |
| "Platforms are grouped by install complexity. Hook-capable… automatic routing enforcement. Non-hook… one-time routing file copy" | Có từ commit `4bbbd46a` (21/3/2026). Bảng cuối README: nền tảng không có hook là Zed và Antigravity IDE, phải chép tay file hướng dẫn, chỉ "~60% saved" so với "~98%" khi có hook | Khớp với phần "Định tuyến cưỡng bức" ở trên: có hook thì cưỡng bức bằng máy, không có hook thì chỉ là lời dặn |
| "Prerequisites: Claude Code v1.0.33+" | Nguồn cộng đồng ghi plugin/`/plugin` ra public beta ở bản 1.0.33; bài công bố của Anthropic và docs hiện tại (`code.claude.com/docs/en/plugins`) không ghi số phiên bản **(chưa xác minh)** | Đây là mức tối thiểu để **cài** plugin. Hành vi hook lại được chỉnh theo CC v2.1.x (comment trong `formatters.mjs`), nên bản cũ hơn có thể cài được nhưng không chắc định tuyến đúng |
| `/context-mode:ctx-doctor` để kiểm tra | Có thật: `skills/ctx-doctor/SKILL.md` gọi tool MCP `ctx_doctor`, fallback `node cli.bundle.mjs doctor` (`src/cli.ts`); kiểm runtime, hook, FTS5, đăng ký plugin, phiên bản npm/marketplace | Nên chạy ngay sau khi cài, vì hook hỏng thì plugin âm thầm rơi về mức ~60% |
| Hoạt động kể từ lần đọc 12/10 | Thêm **6 commit**, đều là bot `ci: update install stats`; vẫn v1.0.169 (tổng 2.234 commit) | Không đổi code, mọi phân tích ở trên vẫn đúng |
| Số liệu | **29,9k★**, 2,1k fork, 110 watcher (trang GitHub 16/10/2026; 12/10 là 26,8k★). `stats.json`: "686k+ users" = npm 633,6k + marketplace 52,3k | Badge "users" vẫn là **lượt cài**, không phải số người dùng |

**Kết luận:** ảnh không có thông tin mới về cơ chế. Điểm cần nhớ khi trích dẫn: dùng **98% (đo byte, tác giả tự báo cáo)** thay vì "99%" của banner YouTube.

**Nguồn bổ sung:** https://www.youtube.com/watch?v=QUHrntlfPo4 (oEmbed: Better Stack) · https://code.claude.com/docs/en/plugins · https://anthropic.com/news/claude-code-plugins · https://morphllm.com/claude-code-plugins (1.0.33, nguồn cộng đồng)

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

## 8d. Kiểm ảnh "Agentic AI Architecture: How Autonomous AI Systems Think, Decide & Act" (ảnh người dùng gửi, 2026-10-13)

> Infographic dọc 5 tầng: Users/Clients → ① Access, Security & Governance → ② Agent Orchestration Framework (Session/State, "ReAct Loop" Perceive → Think → Decide → Act → Learn, Memory Manager, Planner) → ③ Data & Knowledge (ingestion, processing, vector store, hybrid search, knowledge graph) → ④ Action & Tool Execution (Tool Marketplace/Registry + 6 nhóm tool) → ⑤ Observability & Continuous Improvement → Business Outcomes.

**Nguồn ảnh:** chỉ ghi "© 2026. All rights reserved." và khẩu hiệu "People × Data × AI × Real Impact", không có tên tác giả; không tìm thấy bài gốc đã đánh chỉ mục (13/10/2026). Bố cục và nội dung trùng mô-típ phổ biến "sense → plan → decide → execute → learn" của nhiều blog vendor (Tredence, TechJockey…).

### Từng tầng: đúng tới đâu

Ký hiệu: ✅ đúng · ⚠️ đúng nhưng thiếu ý quan trọng · ❌ sai hoặc thiếu hẳn.

| Tầng / ô | Ảnh nói | Đánh giá | Bổ sung / đọc sâu |
|---|---|---|---|
| Users / Clients | web, mobile, Slack/Teams, API bên thứ ba | ✅ | Thiếu trigger không có người (cron, webhook, agent khác) như ảnh §8c; mục 21 |
| ① Access, Security & Governance | API gateway → authN/authZ → rate limit → validation & guardrails → audit log; IdP SSO/OAuth2/SAML/OIDC | ⚠️ | Đúng cho cửa vào, nhưng guardrail chỉ đặt ở cửa vào. Rủi ro chính của agent nằm **sau** cổng: prompt injection đi vào qua tài liệu/kết quả tool (OWASP LLM01, ASI01), agent hành động thay người dùng nên cần quyền **theo từng tool**, ít nhất có thể (ASI03; MCP dùng OAuth 2.1 cho việc này), guardrail cả ở đầu ra và trước mỗi lời gọi tool. Rate limit theo request không thay được **ngân sách token/chi phí mỗi lượt chạy** — mục 12 §1 |
| ② "ReAct Loop": Perceive → Think → Decide → Act → Learn | gọi đây là ReAct | ❌ (nhãn) | ReAct (Yao và cộng sự, 2022) là xen kẽ **Thought → Action → Observation**; không có bước "Learn". Năm bước trong ảnh là vòng sense–plan–act cổ điển. Agent không tự cải thiện trong lúc chạy: "học" thật là ghi memory (có kiểm soát) hoặc eval/tinh chỉnh **ngoài** runtime. Vòng cũng không có điều kiện dừng (xem §8c và checklist §6 mục 1) — §2 |
| ② Memory Manager | short-term, long-term, episodic, semantic | ⚠️ | Trộn hai trục (thời gian và loại). Khung CoALA (Sumers và cộng sự, 2023) chia working memory + long-term gồm episodic, semantic, **procedural** (kỹ năng, quy trình, file luật — chính là `SKILL.md`/`AGENTS.md`). Thiếu kiểm soát ghi memory: memory bị đầu độc là ASI06 — mục 10 §4, mục 12 |
| ② Session/State, Planner/Task Decomposer | quản lý phiên, chia việc | ✅ | Thiếu checkpoint/resume khi lỗi giữa chừng (durable execution, mục 21) |
| **Tầng model** | không có | ❌ (thiếu hẳn) | Sơ đồ "AI nghĩ, quyết định, hành động" mà không có ô LLM nào. Kiến trúc thật có lớp model: gateway/router, fallback giữa nhà cung cấp, chọn model theo việc, prompt cache, ngân sách token — LLM gateway ở mục 10, mục 23 |
| ③ Data & Knowledge | ingestion → cleaning/chunking/embedding/enrichment/metadata → vector store (Pinecone, Weaviate, Qdrant, Milvus, pgvector) → hybrid search; KG tuỳ chọn | ⚠️ | Năm vector store đều là sản phẩm thật, hybrid search là mặc định đúng. Thiếu: **rerank**; **lọc quyền theo tài liệu lúc truy xuất** (không có thì RAG làm lộ tài liệu người hỏi không được xem); đồng bộ tăng dần và xoá. Mũi tên vẽ dữ liệu chảy *vào* tool registry, trong khi thực tế retrieval là **một tool** agent gọi — mục 10 §3b |
| ④ Tool Marketplace / Registry + 6 nhóm tool | ERP/CRM, DB, sandbox, REST/GraphQL, email/chat, browser/file/search | ⚠️ | Danh mục hợp lý nhưng không nhắc **MCP** (chuẩn kết nối tool phổ biến nhất 2026) hay A2A cho agent–agent. Thiếu **người duyệt** trước hành động không đảo ngược được (gửi email, ghi DB, thanh toán); sandbox chỉ ghi ở ô code execution, trong khi browser/file system cũng cần cô lập — mục 04, mục 11 §3, mục 12 (ASI02 tool misuse) |
| ⑤ Observability & Continuous Improvement | tracing, metrics, eval, alert, cost | ✅ | Đủ ý. Hai điểm bổ sung: trace nên theo chuẩn OpenTelemetry GenAI; eval chủ yếu chạy **offline** (bộ test, CI, replay) chứ không phải tự chấm lúc chạy. "Continuous improvement" không có mũi tên quay về đâu — mục 07 |
| Business Outcomes | productivity, decisions, compliance, growth, impact | ⚠️ | Khẩu hiệu, không có chỉ số đo; không giúp gì cho thiết kế |
| Đa agent | không có | ⚠️ | Ảnh chỉ vẽ một agent; không có handoff, supervisor/worker hay A2A — mục 02, mục 04 |

**Tổng:** 3 ✅, 6 ⚠️, 2 ❌. Ảnh đúng ở mức **danh mục khối** (hầu hết ô tồn tại thật), nhưng hai lỗi nặng: gọi vòng sense–plan–act là "ReAct" và **không có tầng model**. Ngoài ra bảo mật chỉ đặt ở cửa vào, trong khi rủi ro đặc thù của agent nằm ở dữ liệu và tool phía sau cổng.

**Dùng ảnh thế nào:** được làm checklist "đã nghĩ tới khối này chưa" khi trình bày cho người không chuyên. Khi thiết kế thật: thêm tầng model; đổi nhãn vòng lặp cho đúng (Thought → Action → Observation, có điều kiện dừng bằng máy); dời guardrail và kiểm quyền vào **mỗi lời gọi tool**; thêm lọc quyền lúc truy xuất. So với ảnh §8c ("How AI Agents Work"), ảnh §8c ít khối hơn nhưng vẽ vòng lặp đúng hơn.

**Nguồn §8d:** https://arxiv.org/abs/2210.03629 (ReAct, Yao et al.) · https://arxiv.org/abs/2309.02427 (CoALA, Sumers et al.) · https://genai.owasp.org/llmrisk/llm01-prompt-injection/ · https://genai.owasp.org (OWASP Top 10 for Agentic Applications, mục 12) · https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization (OAuth 2.1) · https://opentelemetry.io/docs/specs/semconv/gen-ai/ · https://www.tredence.com/blog/agentic-ai-architectures · https://www.techjockey.com/blog/?p=60555 · https://www.anthropic.com/research/building-effective-agents

## 8e. Kiểm bài viết "Claude Code có Advisor Tool": model chính hỏi ý model mạnh hơn ở điểm quyết định (bài người dùng gửi, đối chiếu docs 2026-10-31)

> Bài tiếng Việt người dùng gửi mô tả Advisor Tool: Main Model (ví dụ Sonnet) làm việc thường ngày, Advisor Model (ví dụ Opus) được tham vấn ở thời điểm quan trọng; Claude tự quyết khi nào gọi; advisor nhận toàn bộ lịch sử gồm tool call và kết quả; khác subagent; đang experimental, cần Anthropic API. Đã đối chiếu với **docs Claude Code** (code.claude.com/docs/en/advisor), **docs Claude API** (platform.claude.com/…/advisor-tool) và **blog Anthropic** "The advisor strategy" (9/4/2026), đọc 31/10/2026. Chưa chạy thử trong phiên.

### 8e.1 Nó là gì (theo docs chính thức)

| Mục | Claude Code | Claude API |
|---|---|---|
| Trạng thái | **Experimental**; cần Claude Code v2.1.98+ (`/advisor` ở `-p`/SDK/desktop/Remote Control cần v2.1.260+) | **Beta**, header `advisor-tool-2026-03-01`, tool `type: "advisor_20260301"`, `name: "advisor"`, `model: "<advisor>"` |
| Bật | `/advisor opus` (lưu vào `advisorModel`), setting `"advisorModel": "opus"`, cờ `claude --advisor opus` (không hiện trong `--help`); tắt `/advisor off`; vô hiệu hẳn `CLAUDE_CODE_DISABLE_ADVISOR_TOOL=1` | Thêm vào mảng `tools`; tùy chọn `max_uses` (trần mỗi request), `max_tokens` (≥ 1024, khuyên 2048), `caching` |
| Cơ chế | Server tool chạy trên hạ tầng Anthropic, có cho cả gói subscription lẫn API | Executor phát `server_tool_use` với **input rỗng**; server tự dựng transcript → một lượt suy luận riêng trên model advisor với system prompt của Anthropic → trả `advisor_tool_result`; tất cả trong một request `/v1/messages` |
| Advisor thấy gì | **Toàn bộ hội thoại**, gồm mọi tool call và kết quả | System prompt, định nghĩa tool, các lượt trước, tool result, phần text executor đã viết; **advisor không có tool, không có context management**, thinking của nó bị bỏ, chỉ trả lời khuyên (thường 400–700 token text) |
| Ghép cặp | Advisor phải **xếp hạng ≥ model chính**; ví dụ Sonnet 4.6 chính nhận Fable/Opus/Sonnet/Haiku 5.5; Opus 5/5.5 chính chỉ nhận Fable hoặc Opus 5+; Haiku 4.5 gọi được advisor nhưng không làm advisor được | Advisor phải ≥ Sonnet 4.6 và ≥ năng lực executor; cặp sai trả 400 |

### 8e.2 Kiểm từng ý trong bài

| Ý trong bài | Docs nói | Kiểm |
|---|---|---|
| Anthropic đang thử nghiệm trong Claude Code | "experimental… behavior, pricing, and availability may change" | ✅ |
| Sonnet làm việc thường, Opus đánh giá quyết định khó | Đúng cặp "Sonnet main + Opus advisor" trong bảng gợi ý; ngoài ra Haiku+Opus, Opus+Opus, Fable+Fable, Sonnet+Sonnet | ✅ |
| Advisor không thay model chính, chỉ đưa nhận định | Advisor không có tool, chỉ trả văn bản khuyên | ✅ |
| Claude tự quyết thời điểm: trước khi chọn kiến trúc, khi lỗi lặp lại, trước khi kết luận xong | Gần nguyên văn docs; "model-driven rather than rule-based". **Không có setting để giới hạn hay ép số lần gọi** trong Claude Code — chỉ nhắc bằng prompt ("consult the advisor before you continue"); API mới có `max_uses` | ✅ (thiếu ý không có trần) |
| Advisor nhận toàn bộ lịch sử, gồm tool call và kết quả | Đúng | ✅ |
| Xử lý lại toàn bộ context tốn thêm token | Đúng: trong Claude Code **lượt đọc của advisor không được cache**, mỗi lần gọi đọc lại toàn transcript. API có tham số `caching` (hòa vốn khi ≥ ~3 lần gọi/hội thoại) | ✅ |
| Model chính có thể không theo advisor nếu kết quả thực thi mâu thuẫn | Docs: Claude "surfaces the conflict rather than following the guidance unconditionally" | ✅ |
| Khác subagent | Bảng so sánh chính thức: advisor = điểm quyết định giữa task; subagent = chạy cả subtask; `opusplan` = Opus khi plan mode rồi Sonnet thực thi; `/model` = đổi từ request sau | ✅ |
| Tiết kiệm chi phí so với chạy model mạnh suốt | Docs: "typically costs less"; blog: Sonnet 4.6 + Opus 4.6 advisor **+2,7 điểm % SWE-bench Multilingual, chi phí/task −11,9%**; Haiku 4.5 + Opus **41,2% BrowseComp so với 19,7%** khi chạy một mình, rẻ hơn Sonnet 85%/task nhưng điểm thấp hơn 29%. Số do Anthropic tự đo | ✅ (số của nhà cung cấp, chưa xác minh độc lập) |
| Yêu cầu Anthropic API, giới hạn model, thêm chi phí | Đúng; **gói subscription**: advisor tính vào hạn mức sử dụng của gói (Fable advisor tính vào usage credits trên một số gói) | ✅ |

**Tổng:** bài đúng cả 10 ý, không có ý sai; thiếu vài chi tiết vận hành ở dưới.

### 8e.3 Điều bài không nói

- **Tắt telemetry thì mất advisor:** Claude Code bật advisor qua feature flag tải từ Anthropic; đặt `DISABLE_TELEMETRY` (hay biến tắt tải flag tương tự) thì advisor **luôn tắt**. Máy đã tắt telemetry vì chính sách công ty sẽ không dùng được.
- **Không chạy trên Bedrock/Vertex/Foundry.** Hai trang docs lệch nhau về AWS: docs Claude Code ghi không có trên *Claude Platform on AWS* và *Google Cloud's Agent Platform*, còn docs API liệt kê beta trên *Claude Platform on AWS* và *Claude Models on Google Cloud (Anthropic managed)* — tức API có, nhưng Claude Code chưa hỗ trợ đường đó **(lệch tài liệu, chưa xác minh)**. Qua LLM gateway (`ANTHROPIC_BASE_URL`) chỉ chạy nếu gateway chuyển nguyên request.
- **Lời khuyên có thể bị mã hóa:** với advisor đời mới (Opus 5/5.5, Sonnet 5.5, Fable 5/5.1, Haiku 5.5…) API trả `advisor_redacted_result` — executor đọc được nhưng **client không đọc được**. Muốn log/kiểm lời khuyên dạng chữ phải dùng advisor đời cũ (docs gợi ý Opus 4.8). Trong Claude Code, `Ctrl+O` chỉ hiện lời khuyên "khi advisor trả văn bản đọc được".
- **Cặp không hợp lệ bị bỏ lặng lẽ:** nếu API từ chối cặp, Claude Code gửi lại request **không kèm advisor** mà không báo lỗi; advisor xếp hạng thấp hơn model chính thì không được gắn. Subagent kế thừa advisor và tự kiểm cặp theo model của mình.
- **Không làm hỏng prompt cache của model chính:** bật/tắt `/advisor` giữa phiên giữ nguyên prefix cache (khác với đổi `/model`).
- **Lỗi advisor không làm hỏng request:** `overloaded`, `prompt_too_long` (transcript vượt context của advisor), `too_many_requests`… → executor chạy tiếp không có lời khuyên; transcript hiện "Advisor unavailable (…)" hoặc "Advisor declined…".

### 8e.4 Vị trí trong các pattern của kho và dùng thế nào

- Đây là biến thể **evaluator / generator–evaluator** (§1, §2) nhưng **đồng bộ, theo yêu cầu của chính executor**, và evaluator **không có tool** — chỉ đọc transcript, khác khuyến nghị §6 điểm 5 ("evaluator nên có công cụ độc lập"). Vì vậy advisor không thay được test/CI: nó cùng nhìn một transcript với executor, có thể chia sẻ cùng giả định sai (đúng như bài kết luận).
- So với "Santa Method"/"Council" của ECC (mục 07, mục 20 §3l) — hai reviewer độc lập cùng rubric: advisor rẻ hơn (một lượt, không tool) nhưng không độc lập về dữ kiện.
- **Dùng khi:** task dài nhiều bước (refactor lớn, debug lặp), muốn chất lượng gần model mạnh mà phần lớn lượt chạy model rẻ. Cặp khởi đầu: Sonnet chính + Opus advisor. Trong `CLAUDE.md` có thể ghi "gọi advisor sau khi đọc code định hướng, và một lần trước khi báo xong (sau khi đã ghi file/commit)" — đúng mẫu thời điểm docs API khuyên.
- **Không dùng khi:** task ngắn, hỏi–đáp một lượt, hoặc mọi lượt đều cần model mạnh (đổi `/model` thì hơn). Theo dõi chi phí bằng `/usage`; dùng qua API thì đặt `max_uses` và `max_tokens: 2048`.

**Nguồn §8e:** bài viết tiếng Việt người dùng gửi 31/10/2026 · https://code.claude.com/docs/en/advisor (đọc 31/10/2026: enable, pairing table, cost, prompt caching, requirements, compare) · https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool (đọc 31/10/2026: tool parameters, how it works, response format, model compatibility, usage and billing, caching, limitations, best practices) · https://claude.com/blog/the-advisor-strategy (9/4/2026; số benchmark do Anthropic tự đo) · bên thứ ba (không dùng làm căn cứ): claudelog.com/faqs/what-is-advisor-in-claude-code · docs.litellm.ai/docs/completion/anthropic_advisor_tool (LiteLLM tự dựng vòng lặp cho Bedrock/Vertex, không phải hỗ trợ gốc)

## 8f. Kiểm bài viết "Claude Code Agent Teams: team developer AI thực thụ" (bài người dùng gửi, đối chiếu docs 2026-10-31)

> Bài tiếng Việt người dùng gửi: Agent Teams cho nhiều agent tự nhận việc, làm song song, nhắn tin trực tiếp; ví dụ vai Team Lead / Frontend / Backend / Review; mỗi teammate có context riêng, nhắn tin peer-to-peer, task list chung, model riêng; bật bằng `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 claude`; khác subagent; cảnh báo xung đột file và chi phí token. Đã đối chiếu với docs chính thức **code.claude.com/docs/en/agent-teams** (đọc 31/10/2026). Chưa chạy thử trong phiên.

### 8f.1 Kiểm từng ý trong bài

| Ý trong bài | Docs nói | Kiểm |
|---|---|---|
| Tính năng thử nghiệm, bật bằng `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` | Đúng: "experimental and disabled by default"; đặt qua biến môi trường **hoặc** `"env"` trong `settings.json` | ✅ |
| Nhiều agent làm song song, trao đổi trực tiếp không qua agent trung tâm | Teammate nhắn nhau theo tên qua `SendMessage`; người dùng cũng nhắn thẳng được bất kỳ teammate nào | ✅ |
| Vai Team Lead / Frontend / Backend / Review | **Không có vai dựng sẵn.** Chỉ có **lead** (phiên chính, cố định suốt phiên) và **teammate**; vai do prompt người dùng đặt, hoặc dùng lại định nghĩa subagent (`.claude/agents/…`) làm teammate. Docs dùng ví dụ "UX / kiến trúc / devil's advocate", "security / performance / test coverage" | ⚠️ ví dụ, không phải tính năng |
| Mỗi teammate có context window riêng | Đúng; teammate nạp CLAUDE.md, MCP, skill như phiên thường, **không** nhận lịch sử hội thoại của lead, chỉ nhận prompt giao việc | ✅ |
| Shared task list: tự nhận việc, theo dõi dependency, cập nhật tiến độ | Đúng: 3 trạng thái pending / in progress / completed, task phụ thuộc hiện "blocked" và tự mở khi task trước xong; tự nhận dùng **file locking** chống tranh chấp | ✅ |
| Model khác nhau cho từng teammate | Đúng; thứ tự chọn: model nêu trong prompt → `model` của định nghĩa subagent → `CLAUDE_CODE_SUBAGENT_MODEL` → model của lead. Model và fast mode của teammate **cố định khi spawn** | ✅ |
| Khác subagent: subagent làm xong trả kết quả về agent chính | Bảng so sánh chính thức khớp; thêm: subagent được Claude đặt tên cũng nhắn nhau được | ✅ |
| Việc phụ thuộc nhau / sửa cùng file dễ xung đột, tốn token | Docs: "two teammates editing the same file leads to overwrites"; token **tăng tuyến tính** theo số teammate; việc tuần tự nên dùng một phiên hoặc subagent | ✅ |

**Tổng:** 7/8 ý đúng; ý về các vai chỉ là ví dụ prompt, không phải tính năng có sẵn.

### 8f.2 Điều bài không nói (cần biết trước khi bật)

- **Bật lên là đổi cả subagent thường:** khi bật, mọi lần Claude gọi Agent tool **có `name`** (không phải fork, không có `isolation`) sẽ tạo **teammate** thay vì subagent, **không hỏi xác nhận** — Claude tự đặt tên subagent nên team có thể hình thành dù không yêu cầu. Muốn quay lại: đặt biến về `0` (có hiệu lực ngay, không cần phiên mới; managed/project settings có thể ghi đè).
- **Chỉ phiên tương tác:** ở `-p` và Agent SDK không spawn teammate.
- **Quyền:** teammate **kế thừa chế độ quyền của lead** (trừ `dontAsk`); lead chạy `--dangerously-skip-permissions` thì **mọi teammate cũng vậy**; không đặt quyền riêng lúc spawn được. Prompt xin quyền của teammate hiện ở phiên lead. Plan của teammate (khi lead ở plan mode) **được tự duyệt** ngay, lead không xem, trừ khi người dùng tự chuyển teammate sang plan mode.
- **An toàn tin nhắn giữa agent:** tin từ agent khác được đánh dấu là từ phiên Claude, không phải người dùng — teammate không thể duyệt quyền thay người dùng hay chuyển việc bị từ chối cho teammate khác; ở auto mode, classifier kiểm từng tin trước khi giao.
- **Lưu trữ cục bộ:** mailbox `~/.claude/teams/{team}/inboxes/{agent}.json`, config `~/.claude/teams/{team}/config.json` (xóa khi phiên kết thúc), task list `~/.claude/tasks/{team}/` (**giữ lại** theo `cleanupPeriodDays`). Không có cấu hình team cấp dự án.
- **Hook làm cổng chất lượng:** `TeammateIdle`, `TaskCreated`, `TaskCompleted` — exit 2 để giữ teammate làm tiếp hoặc chặn tạo/hoàn thành task. Đây là chỗ đặt kiểm tra máy (test, lint) thay vì tin teammate tự báo xong.
- **Giới hạn hiện tại:** `/resume`/`/rewind` **không khôi phục** teammate in-process; trạng thái task có thể trễ (teammate quên đánh dấu xong làm kẹt task phụ thuộc); một team mỗi phiên; **không có team lồng nhau**; lead cố định; teammate in-process không chạy subagent nền; split pane cần tmux hoặc iTerm2 (`it2`), không chạy trong terminal VS Code, Windows Terminal, Ghostty.
- **Chi phí cache:** request của teammate in-process có cache TTL **5 phút** mặc định (kể cả gói subscription); đặt `subagentPromptCacheTtl: "1h"` để giữ lâu hơn, ghi cache 1 giờ tính giá cao hơn.
- **Khuyến nghị kích thước:** bắt đầu **3–5 teammate**, khoảng 5–6 task mỗi teammate; mới dùng thì bắt đầu bằng việc **nghiên cứu/review** (không sửa code) trước khi để team cùng viết code. Lead đôi khi tự làm thay thay vì chờ teammate, hoặc dừng sớm — phải nhắc.

### 8f.3 Vị trí trong các pattern của kho

- Đây là **orchestrator–workers + parallelization** (§1) có thêm kênh **peer-to-peer** và **task list có khóa** — gần mô hình "công ty AI" của OpenCompany (mục 02 §4: topology là ranh giới ủy quyền, lead giao việc qua task manager) nhưng Claude Code **không giới hạn ai nhắn ai**.
- Ví dụ "giả thuyết cạnh tranh" trong docs (5 teammate cố bác bỏ giả thuyết của nhau) là biến thể đa tác tử của **ADHD** (§8, ý tưởng phân kỳ song song) áp vào debug, chống hiện tượng neo vào giả thuyết đầu.
- So với **Advisor Tool** (§8e): advisor là một model đọc transcript và khuyên, không tool; teammate là phiên Claude Code đầy đủ có tool. So với các bộ quy trình ở mục 20 (superpowers `dispatching-parallel-agents`, gsd-core "mỗi executor context 200k sạch", mattpocock `implement-spec`): các bộ đó dựng song song bằng subagent; Agent Teams đưa cơ chế này vào sản phẩm, có task list và mailbox chung.
- **Dùng khi:** review nhiều góc nhìn, debug có nhiều giả thuyết, tính năng chia được theo **tập file không giao nhau** (frontend/backend/test). **Không dùng khi:** việc tuần tự, cùng sửa một file, hoặc tác vụ nhỏ — một phiên hoặc subagent rẻ hơn. Luôn thêm hook `TaskCompleted` chạy test trước khi cho đánh dấu xong.

**Nguồn §8f:** bài viết tiếng Việt người dùng gửi 31/10/2026 · https://code.claude.com/docs/en/agent-teams (đọc 31/10/2026: enable, compare with subagents, display modes, specify teammates and models, assign and claim tasks, hooks, how Claude starts agent teams, architecture, permissions, messages between agents, context and communication, token usage, best practices, troubleshooting, limitations)

## 8g. Nâng cấp 31/10/2026: rà repo lớn

> Hai việc. (1) Đọc lại sao, license, trạng thái của các repo mục 03 bằng GitHub search API (31/10/2026). (2) Tìm repo lớn còn thiếu về vòng lặp agent, harness và context engineering: 4 truy vấn (`agent harness`, `agent loop`, `context engineering`, `ralph loop`) cộng ứng viên từ truy vấn của mục 01/02, lọc bỏ repo đã có trong `data/projects.json` (GSD đã có ở mục 20 §3r). Chọn **7 repo**, clone `--filter=blob:none` (lịch sử) và `--depth 1` (đọc/grep mã): LICENSE, manifest, hook, script cổng dừng, CI, grep telemetry/host mạng; đếm commit, tác giả, trailer `Co-Authored-By: Claude`. **Không cài, không chạy script nào của repo.**

### 8g.1 Repo cũ: điều đã đổi

| Repo | Thay đổi (→ 31/10/2026) | Hệ quả |
|---|---|---|
| `frankbria/ralph-claude-code` | Catalog chưa có số → **9,7k★**, MIT, push 31/10 | Bổ sung sao và license |
| `FlorianBruniaux/claude-code-ultimate-guide` | Chưa có số → 6,3k★, **CC-BY-SA-4.0**, push 31/10 | Nội dung chia sẻ cùng điều kiện: trích dài phải giữ CC-BY-SA |
| `mksglu/context-mode` | 26,8k (12/10) → **33k★**; GitHub báo `NOASSERTION` | Vì GitHub không nhận ELv2; license trong file vẫn Elastic-2.0 (§8b) |
| `oraios/serena` | ~30,2k → 31k★; GitHub báo `NOASSERTION` | Do repo có hai license (GPL-3.0 + phần SolidLSP MIT), không phải đổi license |
| `rtk-ai/rtk` | 83,1k → 85,1k★ | |
| `UditAkhourii/neuroarxiv` | Push cuối 17/9/2026 | Đứng yên 6 tuần; `adhd` vẫn push 25/10 |

### 8g.2 Bảng nhanh 7 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `shareAI-lab/learn-claude-code` | Học harness | 79,6k · MIT | 27/10/2026 | 17 chương `s01`→`s17`, mỗi chương một `code.py` dựng lại một khối của Claude Code | Mã dạy học: denylist chuỗi, `max_turns` mặc định không giới hạn |
| `headroomlabs-ai/headroom` | Nén ngữ cảnh | 78,5k · Apache-2.0 | 30/10/2026 | Nén output tool, log, RAG, file trước khi tới LLM; proxy, MCP, `wrap` cho 15 agent | **Beacon bật sẵn** (tôn trọng `DO_NOT_TRACK`); có bản Enterprise |
| `Yeachan-Heo/oh-my-claudecode` | Gói harness | 40,5k · MIT | 31/10/2026 | 19 agent, ~50 skill, `autopilot`, `ralph` có cổng test theo baseline, `team` | Worker team chạy `--dangerously-skip-permissions`; 29,6% commit có trailer Claude |
| `OthmanAdi/planning-with-files` | Pattern lập kế hoạch | 27,8k · MIT | 30/10/2026 | Kế hoạch 3 file trên đĩa + hook mọi lượt; cổng Stop có trần và phát hiện đứng yên | Benchmark do tác giả tự chạy, dữ liệu thô không trong repo |
| `snarktank/ralph` | Ralph loop | 22,1k · MIT | 1/2/2026 | Bản Ralph tối giản: `ralph.sh` 113 dòng + `prd.json` | Dừng bằng chuỗi `<promise>COMPLETE</promise>`; bỏ qua quyền; đứng yên 9 tháng |
| `muratcankoylan/Agent-Skills-for-Context-Engineering` | Bộ skill kiến thức | 18,3k · MIT | 11/10/2026 | 18 skill về context, harness, memory, multi-agent, eval | Prompt thuần, ~5k dòng SKILL.md |
| `cobusgreyling/loop-engineering` | Pattern vận hành loop | 11,7k · MIT | 31/10/2026 | 8 pattern loop quanh repo (triage, PR babysitter, CI sweeper…) với mức tự chủ L1/L2, ngân sách, kill switch | CLI npm `@cobusgreyling/loop` |

### 8g.3 Hồ sơ từng repo

- **learn-claude-code.** 248 commit từ 21/2/2026, 68 tác giả; README 3 ngôn ngữ, `web/` minh hoạ, CI (`ci.yml`, `test.yml`) và 10+ file test cho ranh giới vòng lặp, compaction, team, cron, goal loop. Mỗi chương là một file Python độc lập chỉ cần `anthropic`, `python-dotenv`, `pyyaml`: `s01_agent_loop/code.py` 153 dòng, đến `s17_goal_loop/code.py` 903 dòng. Luận điểm: "agency đến từ model, sản phẩm agent = model + harness" (khớp §8c). ⚠️ Là mã dạy học, đừng chép vào sản phẩm: s01 chặn lệnh nguy hiểm bằng **so khớp chuỗi con** (`"rm -rf /"`, `"sudo"`…) rồi chạy `subprocess.run(shell=True)`, lách được dễ dàng; s17 đặt `MAX_TURNS` mặc định 0 nghĩa là **không giới hạn**. Cài: `git clone` rồi `pip install -r requirements.txt`.
- **Headroom.** 3.436 commit từ 6/1/2026, 377 tác giả, v0.42.0, **21% commit có trailer Claude**. Cùng nhóm "giữ rác ngoài cửa sổ ngữ cảnh" với context-mode/RTK (§8b) nhưng rộng hơn: `ContentRouter` chọn bộ nén theo loại (JSON → SmartCrusher, code → nén theo AST, văn bản → model `Kompress-v2-base` tải từ Hugging Face), bản gốc lưu cục bộ để model gọi `headroom_retrieve` (giống tính "đảo ngược được" của context-mode). `headroom learn` đọc phiên lỗi rồi ghi bài học vào `CLAUDE.local.md` (mặc định) hoặc `CLAUDE.md`/`AGENTS.md`. ⚠️ Câu mở đầu "same answers" mạnh hơn số liệu trong chính README (ví dụ SQuAD v2 đạt 97% khi nén 19%). ⚠️ `wrap`/`deploy` sửa cấu hình của agent khác; `unwrap` để gỡ. Beacon ẩn danh **bật sẵn** (tỉ lệ nén, provider, model, OS), README nói rõ, tắt bằng `HEADROOM_TELEMETRY=off`, `DO_NOT_TRACK=1` hoặc `HEADROOM_OFFLINE=1`. Cài: `uv tool install --python 3.13 "headroom-ai[all]"`.
- **oh-my-claudecode (OMC).** 5.974 commit từ 9/1/2026, 194 tác giả, gói npm `oh-my-claude-sisyphus` v5.7.24; **29,6% commit có trailer Claude**. Cùng tác giả với `oh-my-codex` và Gajae-Code (mục 01 §3i). ✅ Đáng học: `ralph` không chỉ tin chuỗi hứa của model mà có **`omc ralph verify --write-baseline`** ghi baseline test, các lần sau chỉ coi lỗi *mới* là thất bại (exit 1), kèm reviewer `architect`/`critic`/`codex`, trần mặc định 10 vòng (`src/hooks/ralph/loop.ts`). Đây là bản hiện thực gần với phản biện ở §3 (cổng đọc kết quả máy). ⚠️ `src/team/model-contract.ts` khởi động worker Claude với **`--dangerously-skip-permissions`**. `postinstall` chỉ build module native trên macOS, không gọi mạng. Cài: hai lệnh `/plugin` trong Claude Code theo README, hoặc `npm i -g oh-my-claude-sisyphus`.
- **planning-with-files.** 580 commit từ 3/1/2026, 78 tác giả, v3.27.0; cấu hình cho ~15 host (Claude, Codex, Cursor, Gemini, Kiro, OpenCode, Pi…). Mẫu "Manus": `task_plan.md`, `findings.md`, `progress.md` trên đĩa, hook `SessionStart`/`UserPromptSubmit`/`PreToolUse` nạp lại kế hoạch mỗi lượt. ✅ Cổng Stop (`scripts/check-complete.sh --gate`) đúng các nguyên tắc §6: **chỉ bật khi plan có file `.mode` chứa `gate`**, trần `PWF_GATE_CAP` mặc định 20 lần chặn, và **cho dừng nếu ledger không tiến** kể từ lần chặn trước (chống lặp vô ích); `PLANNING_DISABLED=1` để tắt cho phiên CI. ⚠️ Huy hiệu "96,7% vs 6,7%" đo **độ tuân thủ quy trình** (có tạo đủ file hay không), không đo chất lượng; benchmark 7 phương pháp (77 lượt) do tác giả tự chạy, dữ liệu thô "không theo dõi trong repo" (`docs/evals.md` tự ghi). Cài: `/plugin marketplace add OthmanAdi/planning-with-files`.
- **snarktank/ralph** (Ryan Carson). 20 commit, 5 tác giả, đứng yên từ 1/2/2026. `ralph.sh` lặp tối đa 10 vòng, mỗi vòng chạy `amp --dangerously-allow-all` hoặc `claude --dangerously-skip-permissions --print`, dừng khi output chứa `<promise>COMPLETE</promise>`. Đây chính là dạng mà §3 phê bình (dừng theo lời khai của model, bỏ cổng quyền). Giá trị còn lại: định dạng `prd.json` (user story có `passes: true/false`) và `progress.txt` làm bộ nhớ giữa các vòng. Dùng để học, chạy thì nên trong sandbox.
- **Agent-Skills-for-Context-Engineering.** 214 commit từ 20/12/2025, 13 tác giả, v2.3.0. 18 skill (context fundamentals/degradation/compression/optimization, memory, multi-agent, tool design, harness engineering, self-improvement loop, long-horizon prompting…), ~5k dòng `SKILL.md`, 13 script Python minh hoạ. README trích hai paper có nhắc tới repo (arXiv 2601.21557 và một survey trên OpenReview) **(chưa đọc paper)**. Là tài liệu dạng skill, không có cổng máy. Cài (README): `/plugin marketplace add muratcankoylan/Agent-Skills-for-Context-Engineering` trong Claude Code, hoặc chép thư mục skill cần dùng.
- **loop-engineering.** 621 commit từ 9/6/2026, 50 tác giả, bot GitHub Actions commit nhiều nhất (repo tự vận hành bằng chính các loop của nó). Khác các repo trên ở chỗ nói về **vận hành loop quanh repo** (mục 21) chứ không phải vòng lặp trong một phiên: mỗi pattern có nhịp chạy, mức tự chủ tuần đầu (L1 chỉ báo cáo, L2 thận trọng) và ước chi phí. ✅ Cơ chế máy đọc được: `gate.yaml` (denylist đường dẫn `.env`, `secrets/`, `migrations/`, `auth/`, `payments/`…, `maxFiles: 10`, allowlist auto-merge chỉ docs/test), `loop-budget.md` (số lượt/ngày, token/ngày, số sub-agent mỗi lượt), kill switch bằng label `loop-pause-all`, `STATE.md` làm bộ nhớ. Cài: `npx @cobusgreyling/loop init . --pattern daily-triage --tool claude`.

### 8g.4 Mẫu chung rút ra

1. **Cổng dừng đã tiến hoá khỏi "promise string"**: snarktank/ralph (2/2026) vẫn tin chuỗi của model; OMC (baseline test, chỉ lỗi mới mới tính) và planning-with-files (trần 20 + dừng khi không tiến) đã chuyển sang cổng đọc trạng thái do máy ghi, khớp §3 và §6 mục 8.
2. **Kế hoạch trên đĩa + hook nạp lại mỗi lượt** là mẫu sống sót qua `/clear` và compaction (planning-with-files, `STATE.md` của loop-engineering, `progress.txt` của Ralph).
3. **Nén ngữ cảnh đã thành sản phẩm lớn** (Headroom 78,5k★, RTK 85,1k★, context-mode 33k★). Cả ba giữ bản gốc để truy lại; cần đo chất lượng trả lời chứ không chỉ % token tiết kiệm.
4. **"Bỏ qua quyền" vẫn là mặc định ngầm** của loop và team (Ralph, worker của OMC): chạy trong container/worktree tách biệt là điều kiện tối thiểu.
5. **Ngân sách và kill switch phải là file máy đọc** (`gate.yaml`, `loop-budget.md`, label tạm dừng) thay vì lời dặn trong prompt.

**Nguồn §8g:** GitHub search API 31/10/2026 (4 truy vấn mục 03 + truy vấn chung mục 01/02) · `meta_all.json`/`status_all.json` (GitHub API 31/10/2026) · clone `--filter=blob:none` và `--depth 1` 7 repo, đọc: learn-claude-code (README.md, LICENSE, requirements.txt, `s01_agent_loop/code.py`, `s17_goal_loop/code.py`, `tests/`, `.github/workflows/`) · headroom (README.md, LICENSE, `headroom/telemetry/beacon.py`, cấu trúc `crates/`, `plugins/`) · oh-my-claudecode (README.md, LICENSE, package.json, `scripts/postinstall-contained-fs.mjs`, `src/hooks/ralph/loop.ts`, `src/team/model-contract.ts`, `agents/`, `skills/`) · planning-with-files (README.md, LICENSE, `hooks/hooks.json`, `scripts/{gate-stop,check-complete}.sh`, `docs/evals.md`, `skills/planning-with-files/`) · snarktank/ralph (README.md, LICENSE, ralph.sh, prompt.md, prd.json.example) · Agent-Skills-for-Context-Engineering (README.md, LICENSE, `skills/*/SKILL.md`) · loop-engineering (README.md, LICENSE, gate.yaml, loop-budget.md, `scripts/`, `patterns/`)

## 8h. Kiểm bài đăng "Claude Code: 10,69 triệu token nhưng chỉ tốn $9,93 — bí mật là prompt caching" (bài người dùng gửi, đối chiếu docs 1/11/2026)

> Bài đăng mạng xã hội tiếng Việt, không ghi nguồn case study gốc **(chưa xác minh nguồn)**. Đối chiếu bảng giá và tài liệu prompt caching chính thức qua skill tham chiếu Claude API (bản lưu 6/10/2026; trang nguồn: platform.claude.com/docs/en/about-claude/pricing và …/build-with-claude/prompt-caching).

### 8h.1 Kiểm từng câu

| Câu trong bài | Thực tế | Kiểm |
|---|---|---|
| Giá Claude Opus 5.5: input $4, cache read $0,20, output $20 / 1M token | Khớp bảng giá. Bài **không nhắc giá ghi cache**: 1,25× input ($5/1M) với TTL 5 phút, 2× ($8/1M) với TTL 1 giờ | ✅ (thiếu một dòng) |
| Cache read rẻ hơn 20 lần input | Đúng **riêng cho Opus 5.5** (0,05×). Đa số model khác là ~0,1× (10 lần); Fable 5.1 là 0,025× | ✅ có điều kiện |
| 10,69M token, 9,45M là cache read (~88%), chi phí $9,93 thay vì $45,84 | **Khớp nội bộ**: 9,45M × $0,20 = $1,89; tính 9,45M theo giá input thì thêm 9,45 × ($4 − $0,20) = $35,91, và $9,93 + $35,91 = $45,84. Phần còn lại 1,24M token tốn $8,04 — khớp với khoảng 0,12–0,19M token output cộng ~1,05–1,1M input/ghi cache | ✅ số học; nguồn gốc số liệu chưa xác minh |
| "Bí mật" là tận dụng prompt caching | Trong vòng lặp agent, mỗi lượt gửi lại toàn bộ lịch sử; Claude Code **tự đặt cache** nên 80–90% cache read là bình thường, không phải mẹo riêng. Con số "10,69M token" chủ yếu là **cùng một ngữ cảnh được đọc lại nhiều lần**, không phải 10,69M token nội dung mới | ⚠️ cách trình bày phóng đại |
| "$45,84 nếu không cache" | Phép so sánh vẫn giữ phần phụ phí ghi cache (1,25×) trong cả hai vế; không cache thì phần đó tính giá input thường, nên con số "không cache" thật thấp hơn một chút | ⚠️ gần đúng |
| Cache phụ thuộc prefix nhất quán, thời hạn và model; đổi model giữa phiên làm mất cache | Đúng: khớp **theo tiền tố từng byte** (thứ tự `tools` → `system` → `messages`); TTL mặc định 5 phút, mỗi lần đọc làm mới; **cache gắn với model**, đổi model là ghi lại từ đầu. Đổi tool, đổi system prompt, bật/tắt thinking, đổi `effort` ở cấp request cũng làm mất cache | ✅ |
| Phiên quá dài có thể giảm chất lượng | Hợp lý (ngữ cảnh nhiễu). Cân đối: compaction/context editing giữ phiên, nhưng mỗi lần nén là ghi cache mới | ✅ nhận định chung |

### 8h.2 Điều bài không nói

- **Gói thuê bao (Pro/Max) không tính tiền theo token**: con số đô la kiểu này thường là "giá API tương đương" do công cụ như `ccusage` tính từ log của Claude Code **(chưa xác minh bài dùng công cụ nào)**. Chỉ người dùng API key mới thật sự trả số tiền đó.
- **Tiền tố quá ngắn không được cache**: tối thiểu 512 token trên các model thế hệ mới (Opus 5.5…), 4.096 trên Opus 4.6 và Haiku 4.5; ngắn hơn thì không lỗi, chỉ không cache.
- **Kẻ phá cache âm thầm**: ngày giờ trong system prompt, JSON không sắp thứ tự, tập tool thay đổi, xoá rồi chèn lại "nhắc nhở" giữa hội thoại. Cách kiểm: `usage.cache_read_input_tokens` phải tăng đều qua các lượt; nếu luôn ~0 là có thứ làm hỏng tiền tố.
- **Chọn TTL**: các request cách nhau dưới 5 phút thì giữ TTL 5 phút (rẻ nhất, tự làm mới); khoảng 5–60 phút mới đáng trả 2× cho TTL 1 giờ.
- **Mô hình đa model làm mất cache**: router chuyển Opus ↔ Sonnet giữa phiên đánh đổi giá token lấy việc ghi cache lại. Cách đúng là giữ vòng chính trên một model và giao việc rẻ cho subagent.
- **Đo chi phí theo việc hoàn thành**, không theo request: rẻ mỗi lượt mà cần nhiều lượt hơn thì không rẻ.

### 8h.3 Liên hệ trong kho

Advisor Tool (§8e) và Agent Teams (§8f) đều ảnh hưởng cache (model khác, phiên khác); `DISABLE_TELEMETRY` tắt luôn Advisor (§8e). X-Templates đã có luật chọn model theo tầng (`LOOP-ORCH-019`) và ngân sách ngữ cảnh (`context-and-token-budget.md`); bài học "đổi model giữa phiên làm mất cache, đo `cache_read_input_tokens`" là đầu vào cho đợt trích kế tiếp.

**Nguồn §8h:** bài đăng tiếng Việt người dùng gửi 1/11/2026 · skill tham chiếu Claude API (bảng model và giá lưu 6/10/2026; `shared/prompt-caching.md`: kinh tế cache, TTL, tối thiểu theo model, bảng làm mất cache) · trang nguồn ghi trong skill: platform.claude.com/docs/en/about-claude/pricing.md, platform.claude.com/docs/en/build-with-claude/prompt-caching.md (không tải lại trong phiên này).

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
