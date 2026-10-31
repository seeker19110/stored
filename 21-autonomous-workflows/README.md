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
| **AgentGPT** | 4/2023 | Dừng phát triển 11/2023, công ty pivot 7/2024; **đã archive** (push cuối 29/4/2025, §10d.1) | ~36k |

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
7. **Tối đa N repair cùng failure** (xboss AI Delivery Loop: 3; projects-template: chuỗi đỏ cùng chữ ký) → chuyển WAITING/BLOCKED, không lặp tiếp.
8. **Side effect đối ngoại đi qua outbox** (Sales-Hunter ADR-0010): ghi intent trước khi gọi, lease + fencing token, `outcome_unknown` → reconcile bằng read-back thay vì retry mù, pause mặc định, cooldown sống qua restart; "đã đăng" chỉ tính khi có receipt đọc lại.
9. **Tài liệu trạng thái phải tươi bằng máy**: CI kiểm SHA ghi trong PROGRESS/STATUS là tổ tiên của HEAD và nhánh nêu tên còn tồn tại (xboss, Sales-Hunter) — chống "nhật ký tự khai".

**Từ repo của chủ kho (mục 23):** projects-template đo **DORA baseline trước khi bật tự trị** và có `maintain-run.sh` + `threat-model-maintain-cron.md` cho cron bảo trì; X-Agents có `keeper` (canary dependency, ví dụ urllib3) và **human gate 24h** cho đề xuất đối ngoại; Anthropic đã bỏ `opusplan` (projects-template ADR-0007) nhưng dhcb/xboss vẫn còn trong `settings.json`; Claude Code có **auto mode** và `STOP_HOOK_BLOCK_CAP`; Codex có **Goals** (mục tiêu dài hạn) — so sánh trong `projects-template/docs/reports/2026-10-12-doi-chieu-vong-lap-coding.md`; bài "C compiler bằng nhiều Claude song song" được đối chiếu như ví dụ tự trị có harness mạnh.

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
7. **AI Delivery Loop** (xboss) là state machine đáng chuẩn hoá: Frame → Research → Spec → Ready → Build → Verify → PR → Reconcile; 1 vòng = 1 PR; goal file có risk register + iteration log; PR `feat` phải link spec đã "Approved for implementation".

## 10b. Kiểm ảnh: mariagorskikh/open-instinct, agent cá nhân nhắn qua iMessage (ảnh người dùng gửi, 2026-10-13)

> Ảnh là trang repo GitHub: About "Open Instinct: an open-source Instinct. A personal agent you text on iMessage, with its own computer and a trusted network of other agents. Built on Pi, Inkbox, Maritime and Composio.", 293★, 65 fork, 38 commit, 1 tag, 1 issue, 4 PR, MIT; commit gần nhất `638c657` "Merge pull request #12 from tonydzi/fix/blocked-merchants-scan-all-…" (4 ngày trước) có dấu ✕ đỏ. Đã clone toàn bộ repo (HEAD `79a144a` 11/10/2026), đọc README, `SECURITY.md`, `docs/research/INSTINCT.md`, `packages/core/src/policy.ts`, workflow CI, rồi tự build và chạy test.

### 10b.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 13/10/2026) |
|---|---|
| Repo | `mariagorskikh/open-instinct` · ~324★, 68 fork, **MIT** · 61 commit từ 3/10/2026 (tên đầu là "LibreInstinct") tới 11/10/2026 |
| Tác giả | Maria Gorskikh (~36 commit); người đóng góp khác: mahmoudomarus 7, ishanray 5, aadithyan rajesh 4, Anton Dziatkovskii (tonydzi) 3, Thom Bailly 2 |
| Bản gốc được sao | **Instinct** của Spear Street Technology (Noah Shinn): agent cá nhân thương mại qua iMessage, vòng Series C $1B ở định giá $10B ngày 28/9/2026 (Sequoia, Benchmark, Coatue; theo tin tổng hợp từ Reuters/TechCrunch, chưa đọc bài gốc). README tự gọi bản này là "from-scratch, documented clone", không liên quan tới công ty |
| Kiến trúc | Monorepo pnpm/TypeScript, 11 package: `core`, `gateway`, `server`, `inkbox`, `computer`, `network`, `payments`, `context`, `apps`, `ample`, `cli`; 13 skill |
| Các mảnh ghép | **Inkbox** (số điện thoại iMessage/SMS, email, kênh A2A) · **Maritime** (microVM có desktop Linux riêng cho agent) · vòng agent **Pi** (`earendil-works/pi`, ~115k★; dùng `@earendil-works/pi-ai`, `pi-agent-core`, `pi-coding-agent`, `pi-mcp`) · **Composio** (kết nối app) · **Stripe Link** (thẻ dùng một lần khi mua hộ) |
| Model mặc định | `anthropic/claude-fable-5-1`, dự phòng `anthropic/claude-opus-5-5` (đổi được) |

### 10b.2 Kiểm từng ô trong ảnh

| Ô trong ảnh | Kiểm | Ghi chú |
|---|---|---|
| 293★ · 65 fork · 38 commit | ⚠️ cũ | Nay ~324★, 68 fork (shields 13/10/2026), 61 commit. Repo mới 10 ngày tuổi nên số đổi theo ngày |
| "A personal agent you text on iMessage" | ✅ | Kênh nhắn đi qua Inkbox; ngoài iMessage còn SMS, email và A2A |
| "with its own computer" | ✅ | Mỗi agent có một microVM Maritime với desktop Linux, trình duyệt và shell |
| "a trusted network of other agents" | ✅ | Package `network`: agent nói chuyện với agent qua A2A, phân 6 mức tin cậy (owner/partner/family/friend/contact/stranger) |
| "Built on Pi, Inkbox, Maritime and Composio" | ✅ | Khớp dependency trong `package.json` các package |
| MIT | ✅ | `LICENSE` MIT |
| Commit `638c657` có dấu ✕ đỏ | ⚠️ | Lúc chụp, CI của commit đó đỏ. HEAD hiện là PR #24 (`fix/inkbox-tunnel`); trạng thái CI hiện tại (chưa xác minh) |

**Tổng:** 5✅ / 2⚠️ / 0❌. Mô tả trong ảnh đúng. Hai ⚠️ là số cũ và CI đỏ lúc chụp.

### 10b.3 Điều ảnh không nói (đọc mã và tự chạy)

- **Test thật chạy được.** README ghi 837 test. Tự chạy `pnpm install --frozen-lockfile --ignore-scripts && pnpm build && pnpm -r test` ngày 13/10/2026: **877 test, tất cả pass** (core 221, apps 156, inkbox 141, server 94, payments 66, network 65, gateway 63, computer 43, ample 25, context 3). Chưa chạy `pnpm smoke` (cần tài khoản dịch vụ thật).
- **Quyền được chặn bằng mã, không bằng prompt.** `packages/core/src/policy.ts` kiểm từng lời gọi tool qua `beforeToolCall` theo mức tin cậy của người nhắn, ghi `audit.jsonl`; nội dung từ ngoài được bọc nhãn "untrusted"; `net-guard.ts` chặn SSRF tới địa chỉ nội bộ.
- **`SECURITY.md` tự khai giới hạn rõ:** tool `bash` là shell thật trong VM; chống SSRF chưa chặn được DNS rebinding; email đến không kiểm SPF/DKIM nên có thể bị giả người gửi; `merchantName` trong yêu cầu thanh toán không được đối chiếu với danh sách cho phép/chặn; rate limit chỉ nằm trong bộ nhớ; cookie trình duyệt lưu trong VM; phải tin nền tảng host (Maritime, Inkbox).
- **Cấp quyền tiêu tiền và đọc tin nhắn.** Agent có thể mua hộ bằng thẻ Stripe Link dùng một lần và đọc mọi tin nhắn gửi tới số điện thoại của nó. Đây là chỗ cần đặt hạn mức trước khi thử.
- **CI có cổng bí mật:** build/typecheck/test/smoke, bước "No leftover secrets", workflow quét bí mật trên toàn lịch sử, workflow đẩy image lên GHCR.
- **Trùng tên:** `Merit-Systems/OpenInstinct` (~450★) là dự án khác, không liên quan; README của nó cũng ghi rõ điều này.

### 10b.4 So sánh & dùng thế nào

- **Thuộc nhóm agent cá nhân chạy liên tục**, cùng họ với OpenClaw/Hermes Agent (mục 02) và phần personal agent ở mục 19. Khác biệt: kênh chính là tin nhắn điện thoại, agent có máy riêng, và có mạng agent với mức tin cậy.
- **Đáng mượn cho dự án của chủ kho:** (1) mô hình 6 mức tin cậy kiểm ở `beforeToolCall` + audit log, thay cho luật viết trong prompt; (2) bọc nội dung ngoài thành "untrusted" (khớp ADR "nội dung ngoài là dữ liệu" ở mục 23); (3) `SECURITY.md` liệt kê giới hạn đã biết như một sổ nợ.
- **Chưa nên chạy thật với tiền hay dữ liệu thật:** repo mới 10 ngày, một người viết phần lớn, phụ thuộc bốn dịch vụ trả phí bên ngoài, và còn các lỗ tự khai ở email và thanh toán.

**Nguồn §10b:** https://github.com/mariagorskikh/open-instinct (clone đầy đủ, HEAD 79a144a; README, SECURITY.md, docs/research/INSTINCT.md, packages/core/src/policy.ts, packages/*/package.json, .github/workflows/) · https://trendshift.io/repositories/281812 · https://github.com/earendil-works/pi · https://github.com/Merit-Systems/OpenInstinct · https://aiweekly.co/alerts/instinct-raises-1b-series-c-at-10b-for-personal-ai-agent · https://letsdatascience.com/news/instinct-raises-1-billion-series-c-c9d149f6 · https://officechai.com/ai/ai-agent-startup-instinct-is-now-worth-10-billion-with-just-14-employees/ (Series C của Instinct; WebSearch 13/10/2026) · https://agent37.com/docs/agents-api/instinct

## 10c. Kiểm ảnh "Traditional — the line / AI-native — the loop" (ảnh người dùng gửi, 2026-10-16)

> Ảnh hai nửa. Bên trái là sáu khối đen xếp dọc Plan → Design → Build → Test → Deploy → Maintain, chú thích *"Traditional — the line. One slow loop back is a new release cycle."* Bên phải là sáu vòng tròn quanh một tâm cam "Claude", mũi tên khép kín từ Maintain về Plan, chú thích *"AI-native — the loop. Hours, not weeks, with humans above the loop instigating, directing and governing."*

**Nguồn ảnh:** Figure 2 "The line and the loop" trong **The AI-native SDLC playbook** của Anthropic (blog claude.com, 21/8/2026, Louis Claxton, nhóm Applied AI; bài đọc 40 phút; bản PDF 54 trang, tạo 23/9/2026). Ảnh người dùng gửi trùng nội dung và bố cục với ảnh thứ hai của trang blog (bản người dùng là webp thu nhỏ còn 2000×1266) (`assets.claude.com/75c8e050….png`, 2048×1296). Ảnh trên web **không có alt text** nên công cụ đọc trang bỏ qua nó, chỉ tìm được chú thích trong PDF. Đã đọc toàn văn PDF; bài anh em của Jason Clinton (Deputy CISO), *How Anthropic secures its AI-native SDLC* (21/7/2026), dùng để đối chiếu số liệu.

### 10c.1 Kiểm từng ý trong ảnh

| Ý trong ảnh | Kiểm | Ghi chú |
|---|---|---|
| Sáu giai đoạn Plan · Design · Build · Test · Deploy · Maintain | ✅ | Đúng sáu "stage" của playbook; chính playbook gọi chúng là "non-linear" và gợi ý áp dụng theo thứ tự phụ thuộc giữa các play, không nhất thiết đi vòng |
| "Traditional — the line. One slow loop back is a new release cycle" | ⚠️ | Bên trái là waterfall thuần. Agile/Scrum đã là vòng lặp từ lâu; playbook tự thừa nhận "most organizations sit somewhere between the two columns". Luận điểm thật của playbook hẹp hơn và đúng hơn: **nút cổ chai dời khỏi Build** (Figure 1: build co lại còn vài giờ, các bước người làm quanh nó giữ nguyên độ dài) |
| "Hours, not weeks" | ⚠️ | Là **mục tiêu**, không phải kết quả đo. Playbook chỉ đưa chỉ số dẫn ("intent capture" từ chu kỳ nhiều tuần xuống vài giờ, review PR đầu tiên xuống vài phút), không có case study đo cycle time. Số đo thật nằm ở bài của Clinton và chỉ nói về **khối lượng code**: Claude viết ~80% code được merge ở Anthropic, mỗi kỹ sư ship ~8× code/quý so với 2021–2025, tỷ lệ PR có review góp ý thực chất 16% → 54% |
| "Humans above the loop instigating, directing and governing" | ⚠️ | Chữ trong ảnh và câu kết ("Human judgement stays above it") nói "above", nhưng thân bài nói "humans stay **in** the loop" và đặt người vào **cổng**: chấp nhận `intent.md`/`spec.md`, duyệt `plan.md` trước khi viết code (plan mode chặn sửa file), code owner duyệt PR, người cho phép lên production ("the agent may act up to the production gate and cannot pass it"). Chỉ riêng stage 6 là chạy headless "without a person in the path", và cả ở đó người vẫn triage hàng đợi |
| Claude ở tâm vòng, mũi tên Maintain → Plan | ✅ có điều kiện | Mũi tên khép vòng có cơ chế thật: script **tất định** theo dõi production, vượt ngưỡng thì gọi Claude headless, Claude ghi chẩn đoán thành một `intent.md` mới. Nhưng ảnh đặt Claude ở tâm, còn thứ thật sự nối các giai đoạn là **artifact commit vào git**, và ảnh không vẽ nó (xem 10c.2) |

**Tổng:** 2✅ / 3⚠️ / 0❌. Ảnh không sai, nhưng là ảnh minh hoạ cho một bài hướng dẫn, nói mạnh hơn nội dung bài: "hours, not weeks" chưa có số đo, và "above the loop" bỏ qua các cổng người duyệt mà chính bài coi là bắt buộc.

### 10c.2 Cơ chế thật: vòng quay bằng artifact và cổng, không bằng Claude

Câu then chốt của playbook là chú thích hình ngay sau bảng "The shifts": *"Every stage commits an artifact the next stage can read."* (Figure 3 của PDF là đồ thị phụ thuộc giữa các play.) Chuỗi commit vừa là đầu vào của giai đoạn sau vừa là audit trail.

| Giai đoạn | Artifact commit | Cơ chế | Cổng người / máy |
|---|---|---|---|
| Plan | `intent.md` (proto-spec bằng lời người yêu cầu) | Brainstorm với Claude, template tổ chức (có thể là skill) | Product owner chấp nhận |
| Design | `spec.md` cạnh `intent.md` | Skill chuẩn nội bộ (brand, security, compliance, UX); lo ngại được chuyển cho chủ chính sách | Người chấp nhận spec; tech lead cho việc rủi ro cao |
| Build | `plan.md` (duyệt trước khi có code), rồi diff + test | Plan mode mặc định, `CLAUDE.md` dưới một trang, skill, hook build-time (chặn path bảo vệ, chạy formatter/linter), worktree song song (2–3 phiên), subagent; auto mode chỉ cho việc thường lệ (spec chặt, blast radius nhỏ, đã có test) | Engineer duyệt plan |
| Test | Output test, build log, screenshot diff do Claude chạy và dán | Vòng tự kiểm, subagent verifier, eval liên tục trong CI (bắt đầu với 20–50 task thật) | **Hook chặn agent sửa file test trong lúc sửa lỗi** |
| Deploy | PR kèm kết quả review; quyết định phát hành | `REVIEW.md`, Code Review (research preview), `@claude` sửa theo review, managed settings (ví dụ `requiredMinimumVersion: "2.1.193"`), job CI sandbox, deploy/rollback qua MCP | Code owner; hook approval cho production; rollback phải diễn tập ở staging |
| Maintain | `intent.md` sinh từ ngưỡng bị vượt; file bài học; kết quả quét; bản ghi kênh sự cố | `bands.yaml`: baseline 30 ngày, luật Western Electric; **1σ chỉ log, 2σ Claude đọc để chẩn đoán (tool hạn chế), 3σ được đề xuất PR hoặc runbook đã duyệt trước**; quét định kỳ (Claude Security, mặc định hằng tuần); Claude Tag trực on-call trong Slack | Chủ dịch vụ triage; mỗi sự cố thêm một eval |

Ba nguyên tắc của playbook đáng chép nguyên ý:

1. **Skill là kiểm soát dạng khuyên nhủ, hook là lớp tất định phía sau.** Chính sách phải luôn đúng thì cần hook hoặc review pass, không chỉ skill.
2. **Phát hiện phải tất định;** model chỉ vào cuộc khi đã vượt ngưỡng.
3. **Agent đi được tới cổng production nhưng không được qua.**

**Mâu thuẫn nội bộ nhỏ:** ở stage Test, playbook dặn dùng hook chặn agent sửa file test để agent không thể "làm yếu bài kiểm tra của chính đoạn code nó sửa". Nhưng ví dụ ở stage Maintain lại cho agent "quarantines the flaky test" khi tỉ lệ fail CI vượt 3σ, chỉ dựa vào cổng review. Hai chỗ không hẳn trái nhau (quarantine đi qua PR, không nằm trong một task sửa lỗi), nhưng khi áp dụng nên chọn quy tắc chặt: quarantine test cũng phải có người duyệt riêng, giống quy tắc "không skip/disable test để xanh" ở §9.

### 10c.3 Phản biện bên ngoài

Cả hai bài phản biện tìm được đều do công ty **bán đúng phần chúng chỉ ra là thiếu**, nên cần đọc với dè dặt:

- **Waydev** (Alex Circei, 24/8/2026): thiếu tầng **đo lường**. Mỗi play có "How to measure it", nhưng không nói cách gom và liên kết sáu nguồn dữ liệu. `bands.yaml` cần baseline lịch sử mới báo vượt ngưỡng được. Tốc độ review tăng có thể che tỉ lệ thay đổi gây lỗi tăng về sau.
- **Port** (Yonatan Boguslavski, 28/8/2026): playbook "assumes intent exists". Nó không nói tín hiệu (ticket, cảnh báo) thành `intent.md` thế nào, hay xác định service và chủ sở hữu ra sao. Blast radius cũng không đo được chỉ từ repo vì cần bản đồ phụ thuộc hạ tầng.

Nhận xét độc lập: hai điểm này **khớp với thứ playbook tự ghi là điều kiện tiên quyết**. Bằng chứng governance cần git history, PR metadata, transcript và OpenTelemetry; mỗi artifact cần một "source of truth". Phản biện không bác playbook, chỉ nói phần khó nhất nằm ngoài nó.

### 10c.4 Đối chiếu với kho (ba cột)

| Cơ chế trong playbook | Kho đã có, sâu hơn | Kho đã có, nông hơn | Kho chưa có |
|---|---|---|---|
| Chuỗi `intent → spec → plan → diff → PR` | AI Delivery Loop của xboss (§10 mục 7: Frame → Research → Spec → Ready → Build → Verify → PR → Reconcile, PR `feat` phải link spec đã duyệt); Spec Kit/Kiro (mục 13 §5) | | |
| Hook làm cổng, skill chỉ khuyên | Mục 23 (projects-template: "prompt không phải cơ chế bảo mật", fail closed); mục 03 §8b (hook cưỡng bức ~98% so với chỉ dặn ~60%) | | |
| Harness, kiểm chứng ngoài, giới hạn vòng | §2, §8 của mục này | | |
| Đo trước khi bật tự trị | projects-template đo **DORA baseline** (§8) | | |
| Eval liên tục trong CI, mỗi sự cố thêm một eval | | Mục 07 có công cụ eval, chưa có quy ước "sự cố → eval" | |
| Phát hiện tất định theo **ngưỡng σ** (`bands.yaml`, 1σ/2σ/3σ, Western Electric) gọi agent theo bậc quyền | | | ✅ Mới. Khác cron bảo trì (`maintain-run.sh`) ở chỗ agent chỉ được gọi khi có tín hiệu, và quyền tăng theo độ lệch |
| Managed settings cho tổ chức (`requiredMinimumVersion`, chặn production) | | Mục 12, 23 có `settings.json` cấp project | Cấu hình cấp tổ chức (server-managed) chưa ghi |
| Hook chặn sửa file test trong task sửa lỗi | | Quy tắc "không skip/disable test" (§9) mới ở dạng lời dặn | Hook cụ thể |

### 10c.5 Dùng thế nào

- **Trích dẫn ảnh này như minh hoạ, không như bằng chứng.** Muốn nói về năng suất thì dùng số đo của bài Clinton (80% code, 8×, 16% → 54%) và ghi rõ đó là số nội bộ Anthropic, tự báo cáo.
- **Phần đáng lấy nhất là bảng 10c.2,** không phải hình tròn. Với dự án của chủ kho, thêm hai thứ "chưa có": (1) hook chặn sửa `tests/**` khi task là sửa lỗi; (2) một `bands.yaml` nhỏ cho tỉ lệ fail CI, quyền theo bậc (1σ log, 2σ đọc, 3σ chỉ mở PR), chạy bằng Routine (§3.2).
- **Giữ người ở cổng, không chỉ "ở trên".** Thứ tự an toàn là duyệt plan → code owner duyệt PR → người duyệt production, đúng như thân bài playbook, dù hình vẽ gợi ý ít người hơn.
- Một số tính năng playbook dựa vào vẫn chưa ổn định (đọc 16/10/2026): Code Review là research preview; Claude Security và Claude Tag là public beta; Claude Design là beta.

**Nguồn §10c:** https://claude.com/blog/the-ai-native-sdlc-playbook (21/8/2026; HTML + ảnh `assets.claude.com/75c8e050ace91c2b288498fe45384469cfb00aa2.png`) · PDF "AI Native SDLC Playbook_designv2" (54 trang, link từ trang blog, đọc toàn văn) · https://academy.claude.com/courses/ai-native-sdlc-playbook · https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle (Jason Clinton, 21/7/2026) · https://waydev.co/anthropics-ai-native-sdlc-playbook-has-a-missing-layer-measurement/ · https://www.port.io/blog/anthropic-ai-native-sdlc-playbook

## 10d. Nâng cấp 31/10/2026: rà repo lớn, cập nhật trạng thái và 5 repo mới

> **Cách làm.** (1) Đọc lại số sao, license, trạng thái của 18 mục trong catalog mục 21 bằng GitHub API (31/10/2026); nhiều mục trước đây để trống số sao. (2) Chạy 6 truy vấn GitHub search (`ralph loop`, `durable execution`, `workflow orchestration`, `autonomous coding loop` tạo sau 1/10/2025, `agent orchestrator parallel`, `harness agent`), lọc repo đã có trong kho. Chọn **5 repo** phủ ba tầng của §1: loop trong session, harness dài hạn, durable runtime. Clone `--filter=blob:none`, đọc LICENSE, hook, script loop, CI, grep telemetry. **Không cài, không chạy.**

### 10d.1 Thay đổi trạng thái của repo đã có

| Repo | Thay đổi (GitHub API 31/10/2026) | Hệ quả |
|---|---|---|
| `reworkd/AgentGPT` | **Đã archive** (read-only); push cuối 29/4/2025; 36,3k★, GPL-3.0 | §7 đổi "maintenance mode" thành **archive**. Chỉ còn giá trị lịch sử |
| `yoheinakajima/babyagi` | 22,4k★; push cuối **31/1/2026**; GitHub **không nhận file license** (catalog ghi MIT) | Gần 9 tháng đứng yên. Kiểm lại license trước khi chép mã |
| `githubnext/gh-aw` | Repo đã chuyển sang **`github/gh-aw`** (5.545★, MIT, push 31/10/2026) | Link cũ vẫn chuyển hướng; nên trích `github/gh-aw` |
| `temporalio/temporal` | 24,1k★ (catalog trống) | Bổ sung số |
| `restatedev/restate` | 4,6k★; GitHub `NOASSERTION` (catalog ghi BUSL-1.1) | Không phải mã mở OSI; giữ cờ |
| `inngest/inngest` | 6k★; GitHub `NOASSERTION` (server SSPL chuyển Apache sau 3 năm, theo docs, **chưa xác minh** lại) | Giữ ghi chú "Apache-2.0 (server)" kèm cờ kiểm |
| `dbos-inc/dbos-transact-py` | 1,7k★, MIT | Bổ sung số |
| `activepieces/activepieces`, `windmill-labs/windmill` | 25,3k★ và 18,3k★; GitHub `NOASSERTION` (catalog ghi MIT và AGPL-3.0) | Nhiều khả năng do có phần enterprise license riêng (**chưa xác minh** lại); đọc LICENSE trước khi nhúng |
| `Significant-Gravitas/AutoGPT` | 187,8k★; `NOASSERTION` (MIT + Polyform Shield cho platform) | Như §7 |
| `kestra-io/kestra`, `huginn/huginn` | 30,1k★, 50,2k★, vẫn hoạt động | §6 cập nhật số: Kestra ~28,4k → 30,1k, Huginn ~49k → 50,2k |

### 10d.2 Bảng nhanh 5 repo mới

| Repo | Tầng (§1) | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `OthmanAdi/planning-with-files` | Harness + loop | 27,8k · MIT | 30/10/2026 | Lập kế hoạch bằng file (`task_plan.md`, `findings.md`, `progress.md`) + hook giữ plan qua compaction và chặn dừng sớm | Hook chạy trên mọi Read/Grep |
| `snarktank/ralph` | Loop | 22,1k · MIT | 2/2/2026 | Bản Ralph loop gọn nhất: `ralph.sh` + `prd.json` (`passes`) + `progress.txt` | **`--dangerously-skip-permissions`**, đứng yên 9 tháng |
| `wanshuiyin/Auto-claude-code-research-in-sleep` (ARIS) | Harness nghiên cứu | 18,4k · MIT | 1/11/2026 | 91 skill cho vòng nghiên cứu ML chạy qua đêm: review chéo model, thí nghiệm, viết paper | 834/1.300 commit có trailer Claude |
| `conductor-oss/conductor` | Durable runtime | 32,4k · Apache-2.0 | 30/10/2026 | Engine workflow (gốc Netflix, 2016) nay có task LLM, MCP, A2A, `DO_WHILE` cho agent | Cần Java 21; "agentspan" mới từ 7/2026 |
| `triggerdotdev/trigger.dev` | Durable runtime | 16,7k · Apache-2.0 | 31/10/2026 | Task TypeScript dài không timeout, retry, queue, waitpoint chờ người, cron; tự host bằng Docker/K8s | **PostHog ở MCP CLI, không đọc `DO_NOT_TRACK`** |

### 10d.3 Hồ sơ từng repo

- **`planning-with-files`.** 580 commit từ 3/1/2026, 78 tác giả, v3.27.0 (126 tag), 245 commit từ 1/8. Hỗ trợ ~15 host (thư mục `.codex`, `.cursor`, `.gemini`, `.kiro`, `.hermes`, `.pi`…). Phần đáng học nằm trong `scripts/check-complete.sh --gate` (Stop hook): chỉ chặn dừng khi **đủ 5 điều kiện**: plan ở chế độ gated, phase còn `in_progress`, `stop_hook_active` không bật, **số lần chặn dưới trần `PWF_GATE_CAP` (mặc định 20)**, và **ledger có tiến triển từ lần chặn trước** (không tiến triển thì cho dừng). Code còn ghi chú lỗi cũ (#178: glob `*stop_hook_active*true*` từng khớp nhầm). `attest-plan.sh` khoá `task_plan.md` bằng SHA-256; nếu file bị sửa ngoài ý muốn, hook **từ chối nạp plan vào ngữ cảnh** và báo `[PLAN TAMPERED]`. `PLANNING_DISABLED=1` tắt cho phiên CI. 103 file test. "Crash-proof" trong mô tả ⚠️: thực chất là khôi phục bằng `session-catchup.py` đọc lại file, không có bảo đảm giao dịch. Cài: `/plugin marketplace add OthmanAdi/planning-with-files` rồi `/plugin install planning-with-files@planning-with-files`; agent khác: `npx skills add OthmanAdi/planning-with-files --skill planning-with-files -g`.
- **`snarktank/ralph`** (Ryan Carson). Chỉ 20 commit (7/1–2/2/2026), không tag. `ralph.sh` lặp tối đa `MAX_ITERATIONS` (mặc định 10), mỗi vòng mở **tiến trình mới** (context sạch) chạy `amp --dangerously-allow-all` hoặc `claude --dangerously-skip-permissions --print`; agent chọn story ưu tiên cao nhất có `passes: false` trong `prd.json`, chạy check, commit, ghi `progress.txt`. Dừng khi output có `<promise>COMPLETE</promise>`. Bẫy: chuỗi này cũng có trong chính `CLAUDE.md`/`prompt.md`, và script grep **toàn bộ output** nên agent chỉ cần trích lại hướng dẫn là loop dừng sai; lỗi từng vòng bị nuốt (`|| true`). Hợp làm ví dụ dạy, không hợp chạy trên máy có dữ liệu thật. Bản Claude Code dài hơi hơn đã có ở mục 03 (`frankbria/ralph-claude-code`).
- **ARIS.** 1.300 commit từ 10/3/2026, 116 tác giả, 197 `SKILL.md` (91 skill chính + bản Codex). Mô tả "Markdown-only skills" ⚠️: repo có 11 MCP server (`codex-exec`, `gemini-review`, `claude-review`…), ~50 tool Python (watchdog GPU, hàng đợi thí nghiệm, kiểm trích dẫn). `auto-review-loop`: **`MAX_ROUNDS = 4`**, dừng khi reviewer ở model khác cho **điểm ≥ 6/10 và** verdict `ready`/`almost`; trạng thái lưu file để khôi phục; skill **tự dặn không bọc trong `/loop` hay cron** vì sẽ mất bộ nhớ reviewer và tốn token vô ích. `tools/threat_scan.py` là lớp quét prompt-injection bằng regex, fail-closed, lấy mẫu từ Hermes Agent (MIT, có ghi công). CLI riêng ARIS-Code (Rust, MIT) nằm ở nhánh `aris-code`. Cài: `claude plugin marketplace add wanshuiyin/Auto-claude-code-research-in-sleep` rồi `claude plugin install aris@aris` và `/aris:setup`.
- **`conductor-oss/conductor`.** 6.119 commit từ 7/12/2016, 464 tác giả, v3.34.0-rc1; Orkes giữ nhịp chính (Netflix ngừng bản gốc cuối 2023, **chưa xác minh** ngày). Module `ai/` (từ 2/2026) thêm task `LLM_CHAT_COMPLETE`, `LIST_MCP_TOOLS`, `CALL_MCP_TOOL`, A2A, vector DB; `SWITCH` có `evaluatorType: decision` gọi model để chọn nhánh. Ví dụ agent trong README dùng `DO_WHILE` với điều kiện **`iteration < 10`**: trần vòng nằm trong định nghĩa workflow ✅ đúng guardrail §8. Có ví dụ human-in-loop và cancel. "Chạy trong 60 giây" cần Node + Java 21, CLI tải JAR server về `~/.conductor-cli/`. Telemetry server **chưa kiểm**. Cài: `npm install -g @conductor-oss/conductor-cli` rồi `conductor server start`.
- **`triggerdotdev/trigger.dev`.** 8.610 commit từ 30/11/2022, 167 tác giả, 896 commit từ 1/8. SDK v3 có nhóm module mới cho agent: `chat.ts` (từ 5/2026), `skills.ts`, `subAgentStream.ts`, `steeringContext.ts`, `compactionResponse.ts`, cùng `wait`/waitpoint token cho người duyệt, `schedules` (cron), `idempotencyKeys`, `concurrencyLimits`. LICENSE Apache-2.0 ở gốc và từng package ✅. Tự host: `hosting/docker`, `hosting/k8s`. Telemetry: MCP server trong CLI gửi PostHog (phản hồi người dùng); tắt bằng `--skip-telemetry` hoặc `TRIGGER_TELEMETRY_DISABLED`, **không đọc `DO_NOT_TRACK`** ⚠️. Mặc định SDK kết nối cloud của Trigger.dev. Cài (theo `docs/snippets/step-cli-init.mdx`): `npx trigger.dev@latest init` (nên ghim phiên bản thay `@latest`).

### 10d.4 Vị trí trong bản đồ §1 và §5

| Tầng | Thêm vào | So với đã có |
|---|---|---|
| Loop trong session | `snarktank/ralph`, Stop gate của planning-with-files | Ralph cũ (mục 03) dùng Stop hook; bản snarktank dùng tiến trình mới mỗi vòng |
| Harness dài hạn | planning-with-files, ARIS | Gần với harness Anthropic §2.1 (progress file, feature list `passes`), thêm plan có băm và reviewer khác model |
| Durable runtime | Trigger.dev, Conductor | Trigger.dev cạnh Inngest (TypeScript, có cloud); Conductor cạnh Temporal (JVM, workflow JSON) |

### 10d.5 Mẫu chung rút ra

1. **Stop gate tốt có trần và phát hiện đứng yên**: planning-with-files (20 lần, ledger không đổi thì cho dừng), ARIS (4 vòng), Conductor (`iteration < 10`). Ralph chỉ có trần vòng và điều kiện dừng dễ khớp nhầm.
2. **Không đặt loop trong loop**: ARIS cấm bọc vòng review trong `/loop`/cron; lịch nên kích hoạt *sự kiện bên ngoài* (thí nghiệm xong), không kích hoạt lại cả vòng.
3. **Bảo vệ file trạng thái khỏi bị sửa lén** (băm SHA-256 plan) là bước tiếp theo của "feature list chỉ đổi `passes`" (§2.1).
4. **Reviewer khác model là mặc định mới** (ARIS, codex-plugin-cc ở mục 20 §3t), đúng bài generator–evaluator §2.2, nhưng luôn kèm số vòng tối đa.
5. **Durable runtime đã có primitive cho agent** (waitpoint, chat stream, MCP task); trước khi tự viết harness có trạng thái, xem runtime đã có chưa. Telemetry của CLI vẫn phải kiểm từng cái: `DO_NOT_TRACK` chưa phổ quát.

**Nguồn §10d:** GitHub search API 31/10/2026 (6 truy vấn; `repo:` cho `github/gh-aw`, `yoheinakajima/babyagi`) · `meta_all.json`/`status_all.json` của đợt rà · clone `--filter=blob:none` 31/10/2026, đọc: OthmanAdi/planning-with-files (LICENSE, hooks/hooks.json, scripts/{gate-stop.sh, check-complete.sh, attest-plan.sh}, tests/) · snarktank/ralph (LICENSE, ralph.sh, prompt.md, CLAUDE.md, .claude-plugin/marketplace.json) · wanshuiyin/Auto-claude-code-research-in-sleep (LICENSE, README.md, .claude-plugin/marketplace.json, skills/auto-review-loop/SKILL.md, tools/{watchdog.py, threat_scan.py}, nhánh `aris-code`: LICENSE, cây thư mục) · conductor-oss/conductor (LICENSE, README.md, ai/DECISION_SWITCH.md, cây `ai/examples/`) · triggerdotdev/trigger.dev (LICENSE, README.md, packages/cli-v3/src/{mcp/telemetry.ts, cli/common.ts}, cây packages/trigger-sdk/src/v3/, hosting/) · https://github.com/OthmanAdi/planning-with-files · https://github.com/snarktank/ralph · https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep · https://github.com/conductor-oss/conductor · https://github.com/triggerdotdev/trigger.dev · https://github.com/github/gh-aw · https://github.com/reworkd/AgentGPT

---

## 11. Nguồn

- Mục 23 §2, §4.3, §4.5 (projects-template, xboss, Sales-Hunter; đọc 2026-10-12)
- Anthropic AI-native SDLC (§10c): https://claude.com/blog/the-ai-native-sdlc-playbook (21/8/2026, kèm PDF 54 trang) · https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle (21/7/2026)
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
