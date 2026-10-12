# 21 · Autonomous Workflows: từ vòng lặp trong session đến routine chạy không người trực

> Mục này mở ra từ yêu cầu "autonomous workflow" (2026-10-12). Gom bốn tầng thường bị gọi chung một tên: **(a)** vòng lặp tự trị trong một session (Ralph loop, `/loop`), **(b)** harness cho agent chạy nhiều giờ/nhiều context window (hai bài của Anthropic), **(c)** lập lịch & kích hoạt không cần người mở session (Routines, Desktop tasks, GitHub Actions, gh-aw), **(d)** hạ tầng thực thi bền (Temporal, Inngest, DBOS, Restate, LangGraph) và nền tảng automation mã nguồn mở. Kèm lịch sử AutoGPT/BabyAGI, các kiểu hỏng và guardrail. Liên quan: mục 03 (patterns & loops), 05 (n8n/Dify), 13 (GitHub Actions, CI), 12 (bảo mật), 07 (eval).

---

## 0. Tóm tắt 60 giây

- "Autonomous workflow" năm 2026 không còn là một agent chạy vô hạn kiểu AutoGPT 2023, mà là **vòng lặp có ràng buộc** (giới hạn vòng, ngân sách, điều kiện dừng, kiểm chứng đầu-cuối) đặt trong **harness** có bộ nhớ ngoài (progress file, feature list JSON, git) và chạy trên **trigger** (cron, API, sự kiện GitHub).
- Anthropic công bố hai bài harness: **26/11/2025** (initializer agent + coding agent, `claude-progress.txt`, feature list JSON chỉ được sửa trường `passes`, test đầu-cuối bằng Puppeteer) và **24/3/2026** (planner + generator + evaluator, sprint contract, context reset vs compaction). Bài sau tự nhận: khi model mới ra, **nhiều thành phần harness trở nên thừa** (bỏ reset, bỏ sprint với Opus 4.5/4.6).
- Claude Code có ba cách lập lịch chính thức: **Cloud Routines** (chạy trên hạ tầng Anthropic, tối thiểu 1 giờ, không cần máy bật, trigger lịch/API/GitHub), **Desktop scheduled tasks** (máy của bạn, tối thiểu 1 phút), **`/loop`** (trong session, cron 5 trường, jitter, hết hạn sau 7 ngày, tối đa 50 task/session).
- Ở tầng repo, **GitHub Agentic Workflows (gh-aw)** biên dịch markdown + frontmatter thành workflow GitHub Actions `.lock.yml`, agent mặc định read-only và mọi ghi đi qua job `safe-outputs`.
- Ở tầng hạ tầng, bài toán "agent chạy nhiều giờ, chờ người duyệt, không mất trạng thái khi crash" được giải bằng **durable execution**: Temporal (rộng nhất), Restate (một binary), Inngest/Vercel Workflow (durable function cạnh app TypeScript), DBOS (Postgres), LangGraph checkpoint (khi agent đã là graph).
- Kiểu hỏng kinh điển: runaway loop (một tool lỗi bị gọi 400 lần trong 5 phút), chi phí phi mã, drift khỏi mục tiêu, tuyên bố "xong" quá sớm. Guardrail tối thiểu: giới hạn vòng, phát hiện không-tiến-triển, **spend circuit breaker** (cảnh báo 80% / bóp 90% / dừng 100%), cổng người duyệt theo mức rủi ro, kiểm chứng ngoài.

---

## 1. Bốn tầng của một "autonomous workflow"

| Tầng | Câu hỏi nó trả lời | Công cụ tiêu biểu | Mục liên quan |
|---|---|---|---|
| **Loop trong session** | Làm sao để agent không dừng sớm, tự lặp đến khi đạt điều kiện? | Ralph Wiggum loop (Stop hook), `/loop`, `/goal`, `ScheduleWakeup`, Monitor | 03 |
| **Harness dài hạn** | Làm sao giữ trí nhớ & chất lượng qua nhiều context window? | Anthropic harness (initializer/coding agent; planner/generator/evaluator), progress file, feature list JSON, git, browser test | 03, 07 |
| **Trigger & lập lịch** | Ai đánh thức agent khi không có người? | Claude Routines, Desktop tasks, GitHub Actions `schedule`, gh-aw, Channels/webhook | 13 |
| **Thực thi bền (durable)** | Nếu crash lúc giờ thứ 3, hoặc chờ người duyệt 2 ngày thì sao? | Temporal, Restate, Inngest, DBOS, Vercel Workflow, LangGraph checkpointer | 02 |
| **Automation no/low-code** | Không viết code nhưng cần pipeline có AI step? | n8n, Activepieces, Windmill, Kestra, Huginn, Dify | 05 |

Nguyên tắc chung rút ra: **loop** quyết định *khi nào dừng*, **harness** quyết định *nhớ gì và kiểm chứng gì*, **trigger** quyết định *khi nào bắt đầu*, **durable runtime** quyết định *sống sót thế nào*.

---

## 2. Hai bài harness của Anthropic (đọc gốc, 2026-10-12)

### 2.1 "Effective harnesses for long-running agents" (Justin Young, 26/11/2025)

- **Vấn đề:** agent làm việc qua nhiều context window mất trí nhớ giữa các session. Compaction giúp một phần, nhưng ngay cả Opus 4.5 chạy loop với prompt cao cấp ("xây bản clone claude.ai") vẫn ôm quá nhiều việc một lúc, hết context giữa chừng, để lại code dang dở không tài liệu; session sau có khi tuyên bố "xong" quá sớm.
- **Thiết kế:**
  - **Initializer agent** chạy một lần: viết `init.sh` (khởi động dev server), tạo `claude-progress.txt`, commit git đầu tiên.
  - **Coding agent** chạy mọi session sau: làm **một** feature tăng dần, để lại ghi chú có cấu trúc cho session kế.
  - **Feature list JSON** >200 feature đầu-cuối, ban đầu tất cả `failing`; agent **chỉ được sửa trường `passes`**. Chọn JSON thay vì Markdown vì model ít "vô tình viết đè" hơn.
  - **Git** với commit mô tả rõ để revert; **test đầu-cuối bằng trình duyệt** (Puppeteer MCP) như người dùng thật, vì unit test + curl bỏ sót lỗi (hạn chế: agent không thấy alert modal native).
- **Context reset:** mỗi session bắt đầu trắng; agent tự định vị bằng `pwd`, đọc progress file + `git log`, xem feature list, chạy `init.sh` và một smoke test trước khi làm mới. Chính bước này bắt được bug session trước để lại.
- **Kết quả:** định tính (không số liệu): cấu trúc ngăn one-shot và kết thúc sớm; browser test bắt được bug không thấy trong code. Câu hỏi mở: một agent tổng quát vs. nhiều agent chuyên QA; tổng quát hóa ngoài web app.

### 2.2 "Harness design for long-running application development" (Prithvi Rajasekaran, Anthropic Labs, 24/3/2026)

- **Generator–evaluator** (cảm hứng GAN): tách agent sinh và agent chấm. Dễ tinh chỉnh evaluator cho "khó tính" hơn là bắt generator tự phê bình. Với frontend: 4 tiêu chí (chất lượng thiết kế, độc đáo, tay nghề, chức năng), nặng về thiết kế + độc đáo để tránh output chung chung; evaluator dùng Playwright tương tác trang thật; 5–15 vòng, tới 4 giờ.
- **Hệ 3 agent full-stack:** **Planner** nở prompt ngắn thành product spec (deliverable + thiết kế cấp cao, tìm chỗ thêm tính năng AI) → **Generator** xây theo sprint trên React/Vite/FastAPI/SQLite-Postgres, tự đánh giá, dùng git → **Evaluator** bấm qua app như user, test API & DB, đánh trượt sprint dưới ngưỡng cứng. Giao tiếp qua **file**.
- **Sprint contract:** trước mỗi sprint, generator đề xuất sẽ làm gì + cách xác minh; evaluator duyệt tới khi hai bên đồng ý. Cầu nối giữa spec cao cấp và hiện thực kiểm thử được.
- **Reset vs. compaction:** reset = context trắng + handoff có cấu trúc (sạch nhưng thêm phức tạp, token, độ trễ); compaction = tóm tắt tại chỗ (liền mạch nhưng không dọn context). Sonnet 4.5 có "context anxiety" (vội kết thúc) nên reset là bắt buộc.
- **Số liệu:** retro game maker — chạy đơn 20 phút/$9 nhưng runtime game không chạy; harness đầy đủ 6 giờ/$200, chơi được. DAW (harness V2, Opus 4.6) ~3h50/$124,70; QA agent bắt lỗi kéo clip không hoạt động, ghi âm stub.
- **Thay đổi theo model:** Opus 4.5 gần như hết context anxiety → bỏ reset, chạy một session + compaction tự động. Opus 4.6 lập kế hoạch và tự debug tốt hơn → bỏ sprint, evaluator chỉ chấm một lượt cuối. Evaluator chỉ đáng tiền khi task vượt ngưỡng model làm ổn một mình.
- **Bài học:** đọc trace trên task thực tế; tách việc + agent chuyên biệt nơi còn dư địa; **mỗi thành phần harness mã hóa một giả định về điều model chưa làm được** — model mới ra thì phải xét lại, bỏ phần không còn chịu lực, thêm phần mới.

> **Góc nhìn kho:** đây là bằng chứng rõ nhất rằng harness là *tài sản có hạn sử dụng*. Ghi ngày và model vào mỗi harness nội bộ; đặt lịch "xét lại harness" mỗi khi đổi model.

---

## 3. Claude Code: ba cách lập lịch chính thức (docs code.claude.com, đọc 2026-10-12)

| | Cloud **Routines** | **Desktop** scheduled tasks | **`/loop`** (session) |
|---|---|---|---|
| Chạy ở | Cloud do Anthropic quản lý | Máy bạn | Máy bạn |
| Cần máy bật / session mở | Không / Không | Có / Không | Có / Có |
| Bền qua restart | Có | Có | Khôi phục khi `--resume` (trừ ngoại lệ) |
| Truy cập file local | Không (clone mới) | Có | Có |
| MCP | Connector cấu hình theo task | File cấu hình + connector | Kế thừa session |
| Hỏi quyền | Không (tự trị) | Cấu hình theo task | Kế thừa session |
| Khoảng cách tối thiểu | **1 giờ** | 1 phút | 1 phút |

Gợi ý chính thức: Cloud cho việc phải chạy tin cậy không cần máy; Desktop khi cần file/tool local; `/loop` để poll nhanh trong phiên.

### 3.1 `/loop` và cron trong session (chi tiết đáng nhớ)

- Ba chế độ: `/loop 5m <prompt>` (cron cố định), `/loop <prompt>` (Claude tự chọn khoảng 1 phút–1 giờ theo quan sát, in lý do; có thể dùng tool **Monitor** để stream thay vì poll), `/loop` trần (prompt bảo trì mặc định: tiếp việc dở → chăm PR của nhánh: review, CI đỏ, conflict → dọn dẹp; hoặc `loop.md` ở `.claude/loop.md` / `~/.claude/loop.md`, tối đa 25.000 byte, sửa là có hiệu lực vòng sau).
- Có thể lặp một skill: `/loop 20m /review-pr 1234`; chỉ chạy skill mà Claude được phép tự gọi (skill `disable-model-invocation: true`, lệnh built-in, MCP prompt chỉ thành text).
- Tool nền: `CronCreate` / `CronList` / `CronDelete`; cron 5 trường chuẩn vixie (không hỗ trợ `L`, `W`, `?`, tên `MON`); **tối đa 50 task/session**; ID 8 ký tự; giờ địa phương.
- **Jitter** có chủ đích để tránh dồn API: task định kỳ chạy **trễ** tới nửa khoảng cách, tối đa 30 phút (hàng giờ/ngày: trễ 0–30 phút); riêng `*/5 * * * *` chạy **sớm 15 giây** (4m45s) để tận dụng prompt cache 5 phút; one-shot đúng `:00`/`:30` chạy sớm tới 90 giây → muốn đúng giờ thì đặt lệch (`3 9 * * *`).
- **Hết hạn 7 ngày** cho task định kỳ (chạy lần cuối rồi tự xóa) — chặn loop bị quên. Dừng loop tự điều nhịp bằng `Esc` hoặc Claude gọi `ScheduleWakeup stop:true`; nếu một vòng không hẹn lại, hệ thống hẹn dự phòng ~20 phút rồi kết thúc.
- Giới hạn: chỉ bắn khi Claude Code đang chạy và rảnh; không bù lượt bỏ lỡ; background session giữ `/loop` sống không cần terminal; tắt toàn bộ bằng `CLAUDE_CODE_DISABLE_CRON=1`.

### 3.2 Cloud Routines

- Research preview **14/4/2026**. Trigger: lịch (cron), gọi HTTP API, sự kiện GitHub (issue/PR); tạo từ CLI bằng `/schedule` (từ v2.1.225 gắn được GitHub trigger vào routine có sẵn; API trigger/token vẫn chỉ trên web — nguồn thứ cấp).
- Chạy tự trị, không hỏi quyền, clone repo mới mỗi lần; connector cấu hình theo routine. Nguồn thứ cấp nói routine tính vào hạn mức subscription và giới hạn **5/15/25 lượt tự động/ngày** theo gói — **chưa xác minh trên docs**.
- Khác biệt với `/loop`: không kế thừa session, nên prompt phải **tự đủ** (standalone); phù hợp "mỗi sáng triage issue", "mỗi PR mới chạy security review", "webhook từ CI đẩy lỗi vào".

### 3.3 Gắn với Ralph loop (mục 03)

Ralph Wiggum loop giải bài "không cho agent dừng" trong một session (Stop hook nạp lại prompt, promise string + max vòng). `/loop` giải bài "quay lại định kỳ". Routines giải bài "không cần người". Ba thứ xếp chồng được: Routine mỗi giờ → mở session → trong session chạy Ralph loop tới khi test xanh → push → Routine kế kiểm tra CI.

---

## 4. GitHub Agentic Workflows (`githubnext/gh-aw`)

| Thuộc tính | Giá trị (2026-10-12) |
|---|---|
| Định dạng | Markdown + YAML frontmatter (trigger, permissions, tools, engine); thân markdown là nhiệm vụ cho agent |
| Biên dịch | `gh aw compile` → `.lock.yml` chạy như GitHub Actions thường |
| Engine | GitHub Copilot, Claude Code, OpenAI Codex, Google Gemini, Pi |
| An toàn | Job agent **read-only & sandbox mặc định**; mọi ghi lên GitHub đi qua job **`safe-outputs`** (đệm, kiểm tra, áp dụng với quyền hẹp); lời khuyên: xem lại permissions/tools/network/file sinh ra trước khi deploy, vẫn cần người giám sát |
| Use case gợi ý | triage issue, review PR, điều tra CI fail, bảo trì docs, phân tích dependency, báo cáo repo — **bổ sung** chứ không thay CI/CD tất định |
| Số liệu | ~5,4k★, 584 fork, 18.545 commit, MIT; advisory **GHSA-8h78-hpm7-29gg** ảnh hưởng `>=0.83.3,<0.85.4` (đã rút) |
| Tài nguyên | docs theo task, quickstart, workshop `githubnext/gh-aw-workshop` |

**Nhận xét:** gh-aw là hiện thực hóa "prompt-as-workflow" trên CI: cùng ý tưởng với plugin markdown (mục 20) nhưng ở tầng repo và có cơ chế ghi an toàn — một mẫu tốt để tham chiếu khi tự thiết kế agent chạy trên GitHub Actions (quyền tối thiểu + ghi gián tiếp).

---

## 5. Durable execution cho agent chạy lâu

| Nền tảng | Mô hình | Hợp khi | Lưu ý |
|---|---|---|---|
| **Temporal** | Workflow + Activity, worker chạy dài | Cần Signals/Updates/Worker Versioning, đa ngôn ngữ, quy mô lớn | Nền tảng rộng nhất; không hợp serverless (cần worker sống lâu) |
| **Restate** | Durable functions, một binary tự host | Muốn đơn giản vận hành | Mới hơn, hệ sinh thái nhỏ hơn |
| **Inngest** | Durable function qua HTTP endpoint | App TypeScript/serverless | Cloud free 50k execution, Pro từ $99/tháng (nguồn thứ cấp) |
| **Vercel Workflow** | Durable function trong Vercel | Đã ở Vercel/Next.js | Khóa nền tảng |
| **DBOS** | Thư viện + Postgres làm sổ cái | Postgres đã là DB chính | DBOS Pro ~$99/tháng (nguồn thứ cấp) |
| **LangGraph** | Checkpointer theo node của graph | Agent đã là LangGraph graph | Checkpoint async mặc định có thể mất checkpoint mới nhất khi crash cứng → chỉnh sang sync |

- Kết hợp phổ biến: **LangGraph cho suy luận + Temporal cho orchestration** với agent có side effect. Các nguồn so sánh phần lớn do vendor viết (LangChain, Cordum, bài gần Temporal) — đọc có đối chiếu.
- Điểm chung với harness Anthropic: cả hai **ngoại hóa trạng thái** (sổ cái/checkpoint hay progress file + git); khác nhau ở độ "cứng": durable runtime bảo đảm replay chính xác, harness chỉ bảo đảm "đủ để agent định vị lại".

---

## 6. Nền tảng automation mã nguồn mở có AI step

| Dự án | License | ★ (ước lượng, nguồn thứ cấp) | AI/agent |
|---|---|---|---|
| **n8n** (mục 05) | Sustainable Use (source-available, không OSI) | — | AI Agent node, LangChain nodes |
| **Activepieces** | MIT | ~24,7k | Agent-first; ~400 MCP server / 700+ pieces (số khác nhau theo nguồn) |
| **Kestra** | Apache-2.0 | ~28,4k | AI Agents & RAG là task type; có MCP server riêng; YAML declarative |
| **Windmill** | AGPL-3.0 | ~18k | AI sinh script/flow; code-first |
| **Huginn** | MIT | ~49k | "Agent" kiểu Ruby, tiền LLM; vẫn là chuẩn self-host lâu năm |
| Airflow / Prefect | Apache-2.0 | — | Pipeline dữ liệu theo lịch; không agent-native |

---

## 7. Lịch sử: làn sóng AutoGPT 2023 và bài học

| Dự án | Ra đời | Tình trạng 2026 | ★ |
|---|---|---|---|
| **AutoGPT** (Toran Bruce Richards) | 3/2023 | Chuyển thành nền tảng builder agent (block-based) | >187k (nguồn thứ cấp) |
| **BabyAGI** (Yohei Nakajima) | 4/2023 | Bản gốc archive 9/2024; chuyển sang framework "functions" thực nghiệm | — |
| **AgentGPT** | 4/2023 | Dừng phát triển 11/2023, công ty pivot 7/2024; maintenance mode | ~35k |

- Loop gốc: tạo task → ưu tiên → thực thi, ba vai trò prompt trên GPT-4. Bài học thống nhất: **độ tin cậy là nút thắt** — chạy không giám sát thì drift, lặp cùng subgoal, đốt token, không biết output đúng hay sai; không học qua lần chạy. Hệ quả: production chọn thiết kế **có giám sát + ràng buộc** thay vì tự trị toàn phần, chính là hướng Anthropic harness, Ralph loop có max vòng, và Routines không kế thừa session.
- Khảo sát kiến trúc (arXiv 2404.11584) xếp ReAct, RAISE, Reflexion, AutoGPT+P, LATS cùng nhóm single-agent; thành công phụ thuộc planning + self-correction (mục 03).

---

## 8. Kiểu hỏng và guardrail

**Kiểu hỏng hay gặp (2026):** hallucinated tool call; kế hoạch nhiều bước gãy giữa chừng; prompt injection từ nội dung lấy về; **runaway cost** do loop (ví dụ vendor: tool scrape trả rỗng bị gọi lại 400 lần/5 phút); suy giảm âm thầm khi đổi model; tuyên bố xong sớm (Anthropic 2025).

**Guardrail tối thiểu cho một workflow tự trị:**

1. **Giới hạn vòng** (max iterations) + **phát hiện không tiến triển** (vòng lặp không sinh thông tin mới → thoát).
2. **Ngân sách token/tiền là hard stop**, không phải dashboard: **spend circuit breaker** cảnh báo 80% / bóp 90% / dừng 100% (arXiv 2606.03115, SPOQ); OWASP LLM06 xếp "unbounded consumption" là rủi ro hàng đầu (mục 12).
3. **Cổng người duyệt theo mức rủi ro** thay vì bắt duyệt mọi bước (lãng phí chú ý người review): allow-list tool, hành động phá hủy/đối ngoại phải qua gate (so sánh: `/loop` trần chỉ push/xóa khi transcript đã cho phép; gh-aw ghi qua `safe-outputs`).
4. **Kiểm chứng ngoài**: evaluator riêng, browser test, feature list chỉ đổi `passes` (mục 2), "evidence or it's a FAIL" (mục 09).
5. **Hạn sử dụng**: 7 ngày của `/loop`, tối đa 50 task, sprint contract, ghi model + ngày vào harness.
6. **Observability** (mục 07): trace mỗi vòng, đếm tool call lặp, chi phí theo run.

**Giới hạn năng lực (để đặt kỳ vọng):** METR ước độ dài task agent hoàn thành tự trị (50% tin cậy) tăng gấp đôi ~**7 tháng** trong 6 năm; agent gần 100% với task người làm <4 phút nhưng <10% với task >4 giờ (số từ nguồn thứ cấp dẫn METR 2025, có bản cập nhật 5/2026 — kiểm tra metr.org). Lỗi cộng dồn: 95%/bước × 30 bước ≈ 21% chạy sạch (0,95³⁰) — lý do phải chia nhỏ + kiểm chứng từng bước.

---

## 9. Agent tự sửa CI / từ issue ra PR

- Lớp sản phẩm: Claude Code (GitHub Action + Routines + `/loop` prompt bảo trì "chăm PR"), GitHub Copilot coding agent, Devin, Jules (mục 01). Cơ chế chung: trigger sự kiện (CI đỏ, comment review) → agent đọc log → sửa tối thiểu → push → chờ CI lại; cần quy tắc "không skip/disable test để xanh", "không rewrite history nhánh người khác", giới hạn số vòng re-run.
- Dự án cộng đồng tìm được chủ yếu là demo cá nhân (self-healing-ci-agent…), chưa có chuẩn mở; coi là tham khảo mẫu, không phải thư viện production.

---

## 10. Phân tích & khuyến nghị cho kho này

1. **Chọn tầng trước khi chọn tool:** việc trong phiên → `/loop`/Ralph; việc hằng ngày không máy → Routines; việc theo sự kiện repo → gh-aw hoặc GitHub Action; việc có side effect + chờ người nhiều ngày → Temporal/Restate/DBOS.
2. **Mẫu harness tối thiểu** cho project nội bộ: `init.sh` + `progress.md` + `features.json` (chỉ đổi `passes`) + commit nhỏ + smoke test đầu session + evaluator riêng khi task vượt ngưỡng model.
3. **Mọi loop phải có 4 số**: max vòng, ngân sách, timeout, ngày hết hạn. Không có bốn số này thì chưa phải workflow tự trị, mới là demo.
4. **Routine prompt phải tự đủ** và **chỉ đề xuất** với hành động đối ngoại (đồng bộ với skill `call-prep` ở mục 20: scheduled run only proposes).
5. **Xét lại harness khi đổi model** — mỗi guardrail là một giả định về điểm yếu của model cũ.
6. Có thể đóng gói checklist mục 09 + prompt bảo trì `loop.md` thành một plugin (mục 20) để chạy bằng Routine mỗi sáng.

---

## 11. Nguồn

- Anthropic: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents (26/11/2025) · https://www.anthropic.com/engineering/harness-design-long-running-apps (24/3/2026) · https://www.anthropic.com/engineering/building-effective-agents
- Claude Code docs: https://code.claude.com/docs/en/scheduled-tasks · https://code.claude.com/docs/en/routines · https://code.claude.com/docs/en/desktop-scheduled-tasks · https://code.claude.com/docs/en/github-actions · https://code.claude.com/docs/en/goal · https://code.claude.com/docs/en/channels
- Routines (thứ cấp): prosperinai.substack.com, makerkit.dev, claudefa.st, alexdunlop.com, automatonagency.com, swapbiswas.com, apito.ai
- gh-aw: https://github.com/githubnext/gh-aw · https://github.com/githubnext/gh-aw-workshop
- Durable execution: hackernoon.com (LangGraph/DBOS/Inngest/Temporal), zenml.io (8 Inngest alternatives), langchain.com/resources/langgraph-vs-temporal, cordum.io, cadenya.com, appliedtechnologyindex.com, skill.re, arXiv 2607.19297
- Automation OSS: pinggy.io, lyzr.ai, dev.to/badass_tech, automationatlas.io, blog.n8n.io (2 bài), emergent.sh, usecarly.com, aidiscoverywire.com
- AutoGPT/BabyAGI/AgentGPT: futureagi.com, datacamp.com/tutorial/agentgpt, medium.com/@roseserene, fastcompany.com, bairesdev.com, ibm.com/think/topics/evolution-of-ai-agents, lilianweng.github.io/posts/2023-06-23-agent, arXiv 2404.11584
- Failure modes & guardrail: atlan.com/know/ai-agent/what-is-an-agent-loop, openempower.com, medium.com/@Quaxel (12 guardrails), blogs.oracle.com, arXiv 2606.03115 (SPOQ), blog.traversaal.ai (spend circuit breaker), watchtoweragents.com, sqmagazine.co.uk (METR), withtai.com, arXiv 2509.08646, arXiv 2603.05344
- Harness (thứ cấp): preprints.org/manuscript/202603.1756, gist 0xK8oX, pub.towardsai.net, ai-eval.org, ai-heroes.co, theaiautomators.com, victorinollc.com, agentsdesign.dev, arXiv 2607.14159 (MemoHarness)
- Self-healing CI (demo cộng đồng): github.com/Adityaraj1005/self-healing-ci-agent và các PR "self-heal CI" tìm thấy qua search
