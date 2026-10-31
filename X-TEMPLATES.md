# Thư viện cho X-Templates

> Kho `stored` là **nguồn tham khảo** cho khung [`seeker19110/X-Templates`](https://github.com/seeker19110/X-Templates) (v3.29.0, đọc 2026-10-31).
> X-Templates định kỳ trích "phần mới" của kho theo khoảng commit (`research/YYYY-MM-DD-stored-delta-extraction.md`), đối chiếu ba cột
> *sâu hơn / nông hơn / chưa có* và chỉ biến cột 2–3 thành ID yêu cầu. File này làm phía `stored` của hợp đồng đó: chỉ cách đọc kho,
> tổng hợp chéo các hồ sơ, và **bản bàn giao đã đối chiếu sẵn với ID thật của X-Templates**. Bản máy-đọc-được: [`data/xt-handoff.json`](data/xt-handoff.json).

## 1. Hợp đồng đọc kho

| X-Templates cần | `stored` cung cấp ở đâu | Ổn định thế nào |
|---|---|---|
| Danh sách công cụ để lọc theo loại/license/sao | `data/projects.json` (+ `.csv`), trường `category`, `license`, `stars`, `notes`, `section` | `scripts/check_catalog.py` chạy trong CI; mỗi số có ngày đọc trong `notes` |
| Lý do và bằng chứng cho một yêu cầu | Hồ sơ trong `NN-…/README.md`, neo `NN §x` (ví dụ `11 §1h.2`) | Mục chỉ được **thêm**, không đánh số lại; đính chính ghi tại chỗ kèm ngày |
| Phần mới kể từ lần trích trước | `git log <commit trước>..HEAD` + `SOURCES.md` mục "Bổ sung YYYY-MM-DD…" | Mỗi đợt một PR, message commit liệt kê mục mới |
| Bài học đã map sẵn sang ID | `data/xt-handoff.json` + §4 file này | Kiểm schema trong `check_catalog.py`; mỗi bài học có `stored_ref`, `xt_ids`, `column`, `date` |

**Quy ước cột** (giống X-Templates `research/2026-10-30-stored-delta-and-web.md`): `deeper` = X-Templates đã có và sâu hơn; `shallower` = đã có nhưng
thiếu ý; `missing` = chưa có; `not_adding` = cân nhắc và không đề xuất. Chỉ `shallower`/`missing` có `proposal`. ID mới **không đánh số sẵn** —
X-Templates tự cấp số khi thêm (trần 4 MUST/module, ADR-0004); đề xuất ở đây mặc định **SHOULD**.

**Mức tin cậy:** dữ kiện trong hồ sơ đọc từ mã/clone ghi ngày; điều chưa kiểm ghi **(chưa xác minh)**. Số sao không phải bằng chứng chất lượng
(X-Templates `SEC-SUPPLY-026`).

## 2. Tổng hợp chéo: dữ liệu rời máy của công cụ cho coding agent (đọc mã 2026-10-30/31)

`DO_NOT_TRACK=1` **không đủ** — một số công cụ bỏ qua nó, một số chỉ tắt bằng cờ dòng lệnh. Đây là đầu vào cho X-Templates `SEC-INFRA-018`.

| Công cụ (hồ sơ) | Mặc định | Tắt bằng | `DO_NOT_TRACK` | Kênh khác cần biết |
|---|---|---|---|---|
| caveman (20 §3g, §3g.6) | Usage event bật (lưu IP 90 ngày) | `caveman telemetry off` | ✅ | Auto gửi prompt lên Caveman Cloud |
| claude-mem (10 §4e) | PostHog bật | `npx claude-mem telemetry disable`, `CLAUDE_MEM_TELEMETRY=0` | ✅ | Model nén nhận transcript, tiêu quota gói; installer mời đăng nhập cmem.ai |
| codegraph (16 §2f) | Bật, allowlist trường công khai | `codegraph telemetry off`, `CODEGRAPH_TELEMETRY=0`, `--no-telemetry` | ✅ (tắt cả update check) | Update check GitHub 1 lần/ngày |
| chrome-devtools-mcp (11 §1e) | Usage statistics gửi Google | **chỉ cờ** `--no-usage-statistics` | ❌ không thấy trong README | CrUX nhận URL trace (`--no-performance-crux`) |
| browser-use (11 §1c) | PostHog bật | `ANONYMIZED_TELEMETRY=false` | ❌ không thấy | — |
| browser-use-pi (11 §1g.2) | PostHog EU bật | `telemetry: false` | ✅ | Agent chạy JS có quyền FS + mạng |
| claude-code-templates (20 §3s.1) | Gửi aitmpl.com | `CCT_NO_TRACKING=true` / `CCT_NO_ANALYTICS=true` (tự tắt khi `CI=true`) | ❌ **không đọc** | — |
| Stagehand CLI `browse` (11 §1h.1) | PostHog bật (SDK thì không) | `BROWSERBASE_TELEMETRY_DISABLED=1` (tự tắt khi `CI`) | ✅ | MCP hosted/cloud đi qua Browserbase |
| impeccable (20 §3n.1) | Ghi lượt chọn hướng thiết kế | `npx impeccable telemetry off`, `.impeccable/config.json` | ✅ | Request catalog impeccable.style **luôn chạy** kể cả khi tắt telemetry |
| superpowers (20 §3o.1) | Logo tải từ web kèm phiên bản | `SUPERPOWERS_DISABLE_TELEMETRY=1` | ❌ không thấy | Chỉ khi dùng visual companion |
| ponytail (20 §3p.2) | Không gửi | — | — | Webhook tùy chọn mặc định **gửi kèm tên** |
| gsd-core (20 §3r.3) | — | — | — | Hook kiểm cập nhật gọi mạng mỗi phiên |
| **Claude Code** (03 §8e) | — | `DISABLE_TELEMETRY` | — | Đặt biến này **tắt luôn Advisor Tool** (feature flag không tải được) |

Không thấy gửi về (grep mã 30–31/10): Graphify, Playwright MCP, playwright-cli, agent-browser, Obscura, addyosmani/agent-skills, compound-engineering, VoltAgent subagents.

## 3. Tổng hợp chéo: cổng chất lượng thật của các pack/công cụ (đọc workflow 2026-10-31)

| Repo (hồ sơ) | ★ | CI chạy test | Action ghim SHA | Điểm đáng học cho X-Templates |
|---|---|---|---|---|
| affaan-m/ECC (20 §3l) | 293k | ✅ 483 file test | ✅ | Sidecar fingerprint cho hook (X-Templates đã có tương đương) |
| obra/superpowers (20 §3o.1) | 310k | ❌ **không có CI** | — | Sao cao nhất ≠ có cổng; eval ở repo riêng không license |
| addyosmani/agent-skills (20 §3o.2) | 112k | ✅ lint + **eval routing ≥ 95 % hạng 1** (TF-IDF, tất định) | tag | Eval kích hoạt skill rẻ, chạy mọi PR; sổ thay đổi bị từ chối vì eval |
| open-gsd/gsd-core (20 §3r.3) | 11k | ✅ 34 workflow, **mutation (Stryker)** | ✅ | Workflow quản trị PR (require-issue-link, changeset-required, dismiss-unauthorized-approvals) |
| pbakaus/impeccable (20 §3n.1) | 97k | ✅ | ✅ | Engine tải về kiểm **manifest checksum commit trong repo**; CI chặn phát hành khi mã engine đi quá tag |
| Graphify (16 §2e) | 140k | ✅ 484 file test | tag | Nhãn `EXTRACTED`/`INFERRED` cho cạnh suy luận |
| codegraph (16 §2f) | 76k | ❌ (1.006 test chạy tay) | — | npm trusted publishing + provenance; `install.sh` **không** kiểm checksum |
| chrome-devtools-mcp (11 §1e) | 55k | ✅ + test rò bộ nhớ | một phần | — |
| agent-browser (11 §1h.2) | 45k | ✅ mỏng (20 file Rust) | tag | Hàng rào opt-in: `--allowed-domains`, `--action-policy` fail-closed, `--content-boundaries` có nonce, vault credential |
| wshobson/agents (20 §3q.2) | 42k | ✅ snapshot điểm skill theo sha256 | ✅ | Bắt buộc bump version khi plugin đổi |
| claude-plugins-official (20 §3q.1) | 46k | ✅ Claude policy scan mỗi SHA | một phần | Bot **bump SHA plugin ngoài hằng đêm** → "chính thức" ≠ đứng yên |
| mattpocock/skills (20 §3c, §3p.1) | 308k | ❌ chỉ quản trị issue | — | `SCOPE.md` + `.out-of-scope/` (X-Templates đã lấy) |
| unclebob/ub-mode (20 §3m) | 5,4k | ❌ (6 KB văn bản) | — | Công cụ kèm crapper/dryer/mutator (0BSD) cho 6 ngôn ngữ |

## 4. Bàn giao đợt `fa02a75..e3fdcb0` (15 commit nội dung, 30–31/10/2026) → ID X-Templates

Phạm vi: mục 01 §3b.5 · 03 §8e, §8f · 06 §7n · 10 §4e · 11 §1c (cập nhật), §1e–§1i · 16 §2e, §2f · 19 §1.6 · 20 §3g.6, §3k–§3s. ID X-Templates đối chiếu bằng grep
`framework/` ở commit `0b90230` (31/10/2026).

| # | Bài học (stored) | ID X-Templates | Cột | Đề xuất |
|---|---|---|---|---|
| XT-H-001 | Agent Teams: bật `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` thì mọi subagent có `name` thành teammate **không hỏi**; teammate **kế thừa chế độ quyền của lead (kể cả skip-permissions)**, plan teammate tự duyệt, nhắn nhau trực tiếp (03 §8f) | `LOOP-ORCH-001`, `LOOP-ORCH-003`, `LOOP-ORCH-009` | **missing** | SHOULD (`orchestration-and-subagents.md`): vòng autopilot giữ biến này tắt trừ khi có ADR; `xt.py doctor` báo khi biến = `1` ở settings/env |
| XT-H-002 | `DO_NOT_TRACK` không phủ mọi công cụ; nhiều công cụ chỉ tắt bằng biến/cờ riêng (§2 trên; 11 §1e, 11 §1c, 20 §3s.1, 03 §8e) | `SEC-INFRA-018` | **shallower** | Bổ sung Kiểm: bảng "công cụ đã cài → công tắc telemetry riêng" trong `docs/` + egress allowlist; bẫy: `DISABLE_TELEMETRY` của Claude Code tắt luôn Advisor |
| XT-H-003 | Skill không chứa nội dung mà bảo agent **WebFetch chỉ dẫn từ nhánh `main`** của repo khác mỗi lần chạy (vercel `web-design-guidelines`, `writing-guidelines` — 20 §3n.2) | `AI-PROTO-008`, `SEC-SUPPLY-016`, `SEC-AI-018` | **shallower** | Thêm luật quét tài sản prompt: URL tới `raw.githubusercontent.com/*/main` hoặc lệnh "fetch latest guidelines" trong `SKILL.md` = chưa vendor → ghim commit hoặc chép nội dung |
| XT-H-004 | Marketplace "official" bump SHA plugin ngoài **hằng đêm** sau scan tự động (20 §3q.1) | `SEC-SUPPLY-016` ("cài từ nguồn kiểm duyệt"), `LOOP-HARNESS-031` | **shallower** | Bẫy: nguồn kiểm duyệt ≠ phiên bản đứng yên; repo cần hành vi ổn định ghim phiên bản plugin hoặc vendor |
| XT-H-005 | Công cụ trình duyệt cho agent: profile bền mặc định (Playwright MCP, chrome-devtools-mcp), `--autoConnect`/extension thấy **mọi tab đã đăng nhập**; playwright-cli mặc định profile trong bộ nhớ (11 §1e, 11 §1f, 11 §1g.1) | `QA-E2E-027`, `AI-AGENT-007` | **missing** | SHOULD (`14-testing-quality/e2e-and-accessibility.md`): agent kiểm UI dùng profile cô lập (`--isolated` / mặc định playwright-cli), không gắn vào profile cá nhân; trang ngoài bật ranh giới nội dung + allowlist domain |
| XT-H-006 | Coding agent nên ưu tiên **CLI + skill** thay MCP khi có cả hai (Microsoft tự khuyên với playwright-cli; Google có `chrome-devtools-cli`) vì không nạp schema tool + cây trang vào mọi lượt (11 §1f, 11 §1g.1) | `XC-DOCAI-022`, `context-and-token-budget.md` | **shallower** | SHOULD: chọn biến thể CLI+skill trước MCP cho tool dev; MCP khi cần phiên bền hoặc client chỉ nói MCP |
| XT-H-007 | Định nghĩa agent bên thứ ba **ghim `model: opus`** (54/202 agent wshobson) → subagent luôn chạy Opus dù phiên rẻ (20 §3q.2); VoltAgent không ghim (20 §3s.2) | `LOOP-ORCH-019`, `XC-DOCAI-022` | **shallower** | Bẫy/Kiểm: agent cài từ ngoài phải có `model:` ∈ {`inherit`, tầng của khung}; `harness-check` báo model cứng |
| XT-H-008 | Eval **kích hoạt skill** tất định trong CI (prompt mẫu → skill đúng ở hạng 1 ≥ 95 %, TF-IDF, không tốn token) + sổ thay đổi bị từ chối vì eval (20 §3o.2) | `AI-EVAL-021`, `XC-DOCAI-021`, `LOOP-DESIGN-025` | **shallower** | SHOULD khi repo có ≥ 5 skill (X-Templates có 10): test routing tất định cho `description`; sổ "rejected on eval" cạnh `.out-of-scope/` |
| XT-H-009 | Advisor Tool: executor tự hỏi model mạnh hơn; advisor **không có tool**, đọc toàn transcript, lời khuyên đời mới mã hóa (03 §8e) | `LOOP-ORCH-005`, `LOOP-ORCH-018` | **missing** (MAY) | MAY: bật advisor cho phiên autopilot ở bước duyệt PLAN và trước `/complete`; ghi rõ **không thay** `reviewer` (không tool, không độc lập dữ kiện) |
| XT-H-010 | License **theo từng skill** trong một repo: anthropics/skills có 4 skill tài liệu "© All rights reserved", 1 skill không license (20 §3s.4) | `CMP-LIC-004` | **shallower** | Bẫy `licensing-and-ip.md`: kiểm LICENSE từng thư mục skill khi vendor, không chỉ LICENSE gốc |
| XT-H-011 | Repo MCP chính chủ **archive**, chuyển sang bản hosted (Browserbase, 11 §1i.1) | `AI-PROTO-001` | deeper | Đã có (trạng thái archive là điều kiện cài) |
| XT-H-012 | Installer `curl \| sh` không kiểm checksum (codegraph, oh-my-hermes) vs manifest checksum + bundle ký (impeccable) (16 §2f, 20 §3s.3, 20 §3n.1) | `SEC-SUPPLY-019`, `LOOP-HARNESS-025`, `BASE-SEC-017` | deeper | Đã có |
| XT-H-013 | Hook plugin bên thứ ba **chạy cả khi lệnh model bị từ chối**, lần sửa đầu có thể tải binary (impeccable README, 20 §3n.1) | `SEC-SUPPLY-016`, `LOOP-STOP-023` | deeper | Đã có (vendor + quét trước khi bật) |
| XT-H-014 | Mutation test và CRAP (crapper/dryer/mutator — 20 §3m; Stryker trong gsd-core — 20 §3r.3) | `QA-COV-005`, `QA-COV-006`, `QA-STATIC-009` | deeper | Đã có; crapper có thể ghi làm công cụ tham khảo cho ngôn ngữ ngoài JS |
| XT-H-015 | Badge "Repo of the Day" là SVG tự lưu; sao tăng không kèm commit (OpenMontage 19 §1.6, Understand-Anything 01 §3b.5) | `SEC-SUPPLY-026` | deeper | Đã có |
| XT-H-016 | Daemon/server cục bộ chặn Host header lạ (OpenMontage Backlot 19 §1.6) | `SEC-INFRA-011` | deeper | Đã có (app X-Templates làm đúng) |
| XT-H-017 | Engine trình duyệt "anti-detect" cho scraping (Obscura, 11 §1i.2) | — | not_adding | Ngoài phạm vi khung; nếu thêm hồ sơ data/scraping thì chỉ ghi bẫy ToS/pháp lý |
| XT-H-018 | Browser agent viết và chạy JavaScript tùy ý có quyền FS + mạng (browser-use-pi, 11 §1g.2) | `AI-AGENT-007`, sandbox mục 11 | deeper | Đã có (công cụ có quyền thực thi chạy trong sandbox) |

## 5. Gợi ý tích hợp và nâng cấp X-Templates (theo thứ tự lợi ích / công sức)

1. **Chặn Agent Teams ngoài ý muốn (XT-H-001)** — rủi ro cao nhất, sửa rẻ: thêm kiểm vào `xt.py doctor`/`harness-check` (biến `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` ≠ `1` trừ khi có ADR), vì teammate kế thừa quyền lead và phá giả định `LOOP-ORCH-001` "chỉ phiên chính điều phối". Nếu sau này muốn dùng: hook `TaskCompleted` của khung (đã có) là cổng đúng chỗ.
2. **Nâng `SEC-INFRA-018` thành bảng công tắc theo công cụ (XT-H-002)** — chép bảng §2 vào `docs/` dự án đích; CI mẫu đặt cả `DO_NOT_TRACK=1` lẫn biến riêng (`ANONYMIZED_TELEMETRY=false`, `CCT_NO_TRACKING=true`…); ghi bẫy `DISABLE_TELEMETRY` ↔ Advisor.
3. **Luật quét "chỉ dẫn tải từ xa" trong tài sản prompt (XT-H-003)** — thêm vào bộ quét `SEC-AI-018` hiện có (một regex), chặn skill tự đổi hành vi theo nhánh `main` của bên khác.
4. **Test kích hoạt skill tất định cho 10 skill của khung (XT-H-008)** — X-Templates có `adr audit autopilot blueprint complete gate handover optimize research review`; một bộ prompt mẫu → skill mong đợi, chạy trong `gate-fast`, không tốn token (mẫu: `run-evals.js --min-rank1 95` của addyosmani).
5. **Mục "công cụ trình duyệt cho agent" (XT-H-005, XT-H-006)** — vì autopilot kiểm UI qua `ui-gates/`: mặc định playwright-cli (rẻ token, profile tạm), chrome-devtools-mcp `--isolated --no-usage-statistics` khi đo hiệu năng; bảng chọn có sẵn ở `stored` 11 §1g.3.
6. **Kiểm `model:` của agent bên thứ ba (XT-H-007)** và **license từng skill (XT-H-010)** — hai dòng thêm vào `harness-check`/bẫy, rẻ.
7. **Advisor Tool (XT-H-009)** — tùy chọn, chỉ sau khi có eval bật/tắt theo `LOOP-DESIGN-025`; không thay `reviewer`.

## 6. Cách duy trì

- Mỗi đợt cập nhật `stored` có nội dung đáng bàn giao: thêm dòng vào `data/xt-handoff.json` (và bảng §4 nếu đợt lớn), ghi `date` và `stored_ref`.
- Đợt trích tiếp theo của X-Templates bắt đầu từ commit **`e3fdcb0`** (merge PR #90, 31/10/2026).
- Khi X-Templates đã xử lý một dòng, ghi lại trong research note phía X-Templates; `stored` không sửa trạng thái thay X-Templates (theo phạm vi kho ở `WORKFLOW.md`).
