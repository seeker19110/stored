# 09 · Engineering Practices, Deployment & Security Checklists

> Các checklist/kiến thức vận hành dùng được cho cả người và AI agent. Mục này mở ra từ link người dùng gửi (repo `PinoyFreeCoder/deployment-checklist`), được nghiên cứu thêm từ trang repo, lịch sử commit, hồ sơ tác giả, và các dự án tương tự.

---

## 1. PinoyFreeCoder/deployment-checklist ⭐ (link từ người dùng, 2026-10-12)

### 1.1 Hồ sơ nhanh

| Thuộc tính | Giá trị (đã xác minh 2026-10-12) |
|---|---|
| Repo | https://github.com/PinoyFreeCoder/deployment-checklist |
| Mô tả | "Language-agnostic pre-deployment checklist for web & mobile apps — security-heavy, with human and AI-agent versions." |
| Định dạng | Markdown thuần, không phụ thuộc ngôn ngữ/framework; không có code chạy |
| ★ / forks / watchers | 48 ★ · 8 forks · 1 watcher |
| Lịch sử | Tạo **26/9/2026**; 8 commit đến 6/10/2026 (toàn bộ do tác giả); PR #1 chỉ là tự sửa README |
| License | **Không có file LICENSE**. README mục "License / reuse": được copy/fork/adapt; `checklists/base.md` là "source of truth" |
| Trạng thái | Rất mới, đang phát triển tích cực (thêm 1 stack mỗi ~3–7 ngày) |

### 1.2 Cấu trúc thật (đã kiểm tra cây thư mục)

```
README.md              # tổng quan, cách dùng, severity
agent.md               # luật + prompt cho AI agent
CONTRIBUTING.md        # cách thêm checklist theo stack
checklist.md, banner.png
checklists/
  base.md              # checklist nền, chạy trước (~130–135 mục)
  _template.md         # khung cho stack mới
  laravel.md           # 28/9/2026
  nextjs.md            # 30/9/2026 (~28 mục, 6 phần)
  django.md            # 6/10/2026
```

> ⚠️ README nhắc `go.md`, `java.md` làm ví dụ nhưng **các file này không tồn tại** (404). Stack thực tế có: Laravel, Next.js, Django.

### 1.3 `base.md` – 6 phần, 3 mức độ

| Phần | ≈ mục | Ví dụ tiêu biểu |
|---|---|---|
| 1. Shared/Universal | 35 | `[BLOCKER]` build tái lập từ clean checkout; không secret trong repo **kể cả git history**; logout vô hiệu session phía server; backup có test restore · `[SHOULD]` changelog cập nhật |
| 2. Web-Specific | 25 | `[BLOCKER]` CSP chặt (không `unsafe-inline` cho script); HSTS; CORS không wildcard trên endpoint có auth; SSRF guard · `[SHOULD]` bot protection/CAPTCHA |
| 3. Mobile-Specific | 22 | `[BLOCKER]` ký bằng release key; chỉ xin permission dùng thật; token trong Keychain/Keystore; cấm cleartext · `[SHOULD]` force-update |
| 4. Security audit-grade | 52 | 4.1 Threat model (STRIDE) · 4.2 OWASP Web Top 10 (A01, A03, A10…) · 4.3 OWASP Mobile Top 10 (M1, M9…) · 4.4 AuthN/AuthZ server-side + IDOR, MFA · 4.5 Vault & rotation · 4.6 SCA / secret scan toàn history / SAST / DAST · 4.7 Compliance (privacy, breach, PCI) · 4.8 Incident response (on-call, rollback, revoke key) |
| 5. Sign-off | – | Bảng ký duyệt, yêu cầu **0 blocker** |
| 6. References | – | OWASP, MASVS, ASVS, SSL Labs… |

Mức độ: `[BLOCKER]` không deploy cho tới khi sửa · `[SHOULD]` deploy nếu có ticket + owner · `[NICE]` làm khi rảnh.

### 1.4 Ví dụ stack: `nextjs.md` (~28 mục)

Phần: Dependencies & build · Environment & secrets · Rendering/caching/data · API routes, Server Actions & middleware · Security headers & client · Runtime/deploy/observability.

- `[BLOCKER]` build production không lỗi type/ESLint và **không** dùng `ignoreBuildErrors`/`ignoreDuringBuilds` để giấu lỗi.
- `[BLOCKER]` chỉ giá trị công khai mới dùng tiền tố `NEXT_PUBLIC_` (bị inline vào bundle client).
- `[BLOCKER]` route động theo user không bị cache tĩnh (tránh lộ dữ liệu chéo user).
- `[BLOCKER]` mọi Route Handler/Server Action kiểm tra auth phía server (Server Action = public POST endpoint).
- `[SHOULD]` validate env khi khởi động (ví dụ module env parse bằng `zod`); `<Image>` dùng `remotePatterns` cụ thể.

### 1.5 `agent.md` – phiên bản cho AI agent (điểm đáng học nhất)

- Tách rõ **what** (checklist) và **how** (agent.md): *"The checklists provide the items; this file provides the rules."*
- Prompt copy-paste yêu cầu agent: fetch base + stack khớp ngôn ngữ chính (hoặc dùng bản local); bỏ phần Mobile nếu repo web-only và ngược lại.
- Mỗi mục: PASS / FAIL / N/A, **phải trích bằng chứng** (file:dòng, giá trị config, output lệnh); N/A phải có lý do 1 dòng.
- *"Evidence or it's a FAIL"*: "looks fine" / "framework handles this" không được tính.
- Kiểm tra **artifact thật** (quét secret toàn bộ git history, không chỉ working tree).
- **Report-only**: không deploy, không chạy lệnh phá hủy; liệt kê fix rồi chờ duyệt.
- Output cố định: (1) đếm PASS/FAIL/N/A → (2) bảng FAIL (mục, phần, mức, bằng chứng, cách sửa) → (3) **GO / NO-GO**; NO-GO nếu bất kỳ `[BLOCKER]` FAIL. Con người ký quyết định cuối.

### 1.6 `CONTRIBUTING.md` – quy tắc đóng góp (có thể tái dùng cho kho này)

- Một stack = một file lowercase `checklists/<stack>.md`, H1: `Pre-Deployment Checklist — <Stack> (extends base)`; 5–20 mục; không lặp mục của base.
- Chỉ dùng 3 nhãn có sẵn; mỗi mục phải **kiểm chứng được trên code/config thật**, tránh ý kiến; trung lập về tool (chỉ nêu tool làm ví dụ).
- PR phải nêu nguồn chính thức; mọi claim bảo mật phải có link trong References.

### 1.7 Tác giả

- **PinoyFreeCoder** – "A coder and a teacher", Philippines; YouTube/Facebook dạy web dev bằng tiếng Tagalog; site pinoyfreecoder.com, X @pinoyfreecoder; 262 followers, 58 repo (chủ yếu tutorial: ReactApp, fetchapi…).
- Dự án liên quan: **mcp-project-planner** (1★) – MCP server remote tại `https://pinoyfreecoder.com/api/mcp` (Streamable HTTP, không cần key, không gọi LLM phía server) với 3 tool `plan_project`, `search_github_finds`, `search_public_apis`; gợi ý repo mở, API công khai và tech stack giá rẻ cho một ý tưởng dự án. Kết nối: `claude mcp add --transport http --scope user pinoyfreecoder https://pinoyfreecoder.com/api/mcp`.

### 1.8 So sánh với dự án tương tự

| Dự án | Quy mô | Cách tiếp cận | Khác biệt so với deployment-checklist |
|---|---|---|---|
| **MarinJursic/production-readiness-checklist** (MIT, ~40★, 142 commit) | **10.042 control** (8.621 lifecycle `USEQ-*` + 1.421 production `PRC-*`); 686 deterministic | Có **scanner CLI `prc`** (npm/Go, read-only; `quick` 18 check, mặc định 40, `verify` thêm secret-detection trong container, `full` thêm AI advice); mỗi control có ID, owner, evidence; CLAUDE.md + prompt cho AI review; AI chỉ "advisory", không tạo Pass/Fail | Nặng, hướng web-app & doanh nghiệp; deployment-checklist nhẹ, đọc trong 10 phút, có mobile |
| **OWASP ASVS / MASVS (+ MASTG)** | Tiêu chuẩn chính thức | Yêu cầu xác minh theo level; checklist cộng đồng: `shenril/owasp-asvs-checklist` (ASVS 5.0, xlsx), `D1X7R4/owasp-asvs-checklist` (generator), `jeremychoi/owasp-asvs-wstg-checklist` (map sang WSTG), OWASP DevGuide MAS checklist | Chuẩn gốc mà deployment-checklist phần 4 tham chiếu; không có dạng markdown "pre-launch" gộp web+mobile |
| **thedaviddias/Front-End-Checklist** | Rất nổi tiếng | Checklist frontend trước khi ship (HTML, SEO, a11y, perf) | Chỉ frontend, không có bản cho agent |
| Checklist "AI agent go-live" (futureagi, dev.to/techsavant_lab, akto.io, aona.ai) | Bài viết | GO/NO-GO cho **việc triển khai agent AI** (authorization, drift, rollback, guardrails log-only trước) | Khác đối tượng: deployment-checklist dùng agent để audit app thường |

### 1.9 Nhận xét & cách tận dụng

- **Giá trị cốt lõi:** không phải danh sách mục (OWASP đã có) mà là **giao thức cho agent**: evidence-first, report-only, verdict nhị phân, con người ký. Đây là ví dụ gọn của **evaluator pattern** (mục 03) áp vào DevSecOps.
- **Ghép vào kho này:** có thể đóng gói `agent.md` + `base.md` thành **SKILL.md** (mục 04) `pre-deploy-audit`; hoặc dùng làm điều kiện dừng trong Ralph loop (NO-GO → tiếp tục sửa, GO → dừng).
- **Hạn chế / rủi ro:** 48★ & 2 tuần tuổi → chưa qua kiểm chứng cộng đồng; **không có LICENSE** (rủi ro pháp lý khi tái dùng trong tổ chức – nên xin tác giả thêm MIT/CC); README chưa đồng bộ với file thật (go/java vs laravel/nextjs/django); chưa có stack Node/Express, Python/FastAPI, Flutter, React Native; không có cơ chế machine-check như `prc`.
- **Gợi ý hành động:** fork + thêm stack của mình theo `_template.md`; kết hợp `prc quick` (MarinJursic) cho phần deterministic + deployment-checklist cho phần cần phán đoán.

---

## 2. Các checklist / kho kiến thức nổi tiếng liên quan

| Repo | Chủ đề | Ghi chú |
|---|---|---|
| `MarinJursic/production-readiness-checklist` | Production readiness, 10k control + scanner `prc` | MIT; xem 1.8 |
| `OWASP/CheatSheetSeries` | Cheat sheet bảo mật ứng dụng | Nguồn tham chiếu cho phần 4 |
| `OWASP/ASVS` · `OWASP/wstg` · OWASP MASVS/MASTG | Tiêu chuẩn xác minh & kiểm thử | |
| `shenril/owasp-asvs-checklist` · `jeremychoi/owasp-asvs-wstg-checklist` | Checklist ASVS cộng đồng | |
| `thedaviddias/Front-End-Checklist` | Checklist frontend trước khi ship | |
| `trimstray/the-book-of-secret-knowledge` | Tool/kiến thức sysadmin, security | |
| `donnemartin/system-design-primer` | Thiết kế hệ thống | Mục 08 |
| `bregman-arie/devops-exercises` | Bài tập DevOps | |
| `sdras/awesome-actions` | GitHub Actions | CI/CD |

## 2b. greenarmor/GESF — compliance-as-code tự chấm GDPR/OWASP/CIS (ảnh "4 repos worth bookmarking", 2026-10-18)

> Một trong 4 repo của slide Chris Porter (nhưng của tác giả khác, `greenarmor`). Đã clone đầy đủ (HEAD `e9ffd74`, 19/9/2026). Đây là **công cụ thật**, khác hẳn các repo phễu ở mục 08 §2d.

| Thuộc tính | Giá trị (18/10/2026) |
|---|---|
| Repo / URL | https://github.com/greenarmor/GESF (Green Engineering Standard Framework) · slide: 41★/6 fork |
| Mô tả 1 dòng | CLI `ges` "compliance-as-code" quét repo rồi tự chấm điểm tuân thủ GDPR, OWASP, CIS (README cũng nhắc NIST) và sinh báo cáo/badge |
| Loại | checklist / compliance-as-code (công cụ CLI) |
| License | **MIT** (file LICENSE, © 2025–2026 greenarmor) |
| Cài đặt | `brew tap greenarmor/gesf && brew install ges` · `npm i -g @greenarmor/ges` · `pnpm add -g` · `npx @greenarmor/ges init` (Node ≥ 22) |
| Cấu trúc thật | `controls/gdpr/controls.json` (22 control), `controls/owasp/controls.json` (6), CIS (5) — control định nghĩa dạng JSON; `compliance/` có mẫu tài liệu (data-inventory, risk-register, DPIA, retention-policy…); có CI (`.github/workflows`), `.gitleaks.toml`, `.semgrepignore`, SECURITY.md, CODE_OF_CONDUCT, CONTRIBUTING, docs đầy đủ, brew formula `.brew/ges.rb` |
| Vì sao đáng tham khảo | • **Control là dữ liệu (JSON), không hard-code** → thêm/sửa chuẩn mà không đụng engine; hợp để nhúng vào CI như một cổng.<br>• Đi kèm **mẫu tài liệu tuân thủ** (DPIA, risk register, processing records) — phần nhiều đội thiếu.<br>• Hạ tầng repo chỉn chu: gitleaks + semgrep ignore, badge tự sinh, nhiều cách cài. |
| Hạn chế / rủi ro | • **Điểm "100% (A)" trong README là tự chấm trên chính repo GESF** (`Last evaluated: 2026-07-01`), không phải chứng nhận độc lập — đừng đọc như bảo chứng tuân thủ pháp lý.<br>• Quét tĩnh theo heuristic/pattern: "pass" nghĩa là khớp luật đã viết, không bảo đảm đúng GDPR thực tế; GDPR/CIS cần đánh giá con người.<br>• Một tác giả; chưa thấy đánh giá độc lập (web 18/10 ít kết quả) **(chưa xác minh)**.<br>• Số control khiêm tốn (22/6/5) so với bộ chuẩn đầy đủ. |
| Tích hợp | Dùng làm **cổng CI tư vấn** (chạy `ges` rồi đọc báo cáo), không làm bằng chứng tuân thủ đối ngoại. Control JSON có thể tách ra tái dùng; giữ con người duyệt với GDPR/CIS. |
| Liên quan | mục 09 §1 (deployment-checklist), mục 12 (OWASP, security scanner, SAST), mục 13 §4 (CI/CD) |
| Nguồn | clone 18/10/2026 (README, LICENSE, controls/{gdpr,owasp}/controls.json, compliance/, .github/workflows, .brew/ges.rb); slide "4 GitHub repos worth bookmarking" |

## 3. Case study: agent QA/Test Engineer 7 tầng + 4 verdict (ảnh và bài đăng người dùng gửi, 2026-10-17)

> Bốn ảnh chụp màn hình và một bản nháp bài đăng. Ảnh 1-2 là trang giải thích lệnh `.claude/commands/qa-test-engineer.md` ("QA / Test Engineer: bước Test của vòng lặp"): sơ đồ Plan → Design → Build → **Test** → Deploy → Maintain, kim tự tháp 4 tầng, 3 mặt cắt ngang, 4 verdict cho test đỏ. Ảnh 3 là một danh mục có 256 mục (tìm "test": agent QA, `/unit-tests`, `e2e-testing`, Penetration Testing…). Ảnh 4 là `qa-testing/SKILL.md` mở trong dự án `trello-clone`. **Nguồn gốc không xác minh được:** danh mục "Bộ Master" là private, không có repo hay URL công khai để đối chiếu; mọi nhận xét dưới đây dựa trên ảnh và bài nháp, không dựa trên mã.

### 3.1 Cơ chế trong ảnh

| Thành phần | Nội dung |
|---|---|
| Vị trí | Bước Test của vòng đời; đầu vào là code kèm danh sách hành vi cần assert, đầu ra là verdict **SHIP / BLOCK** có bằng chứng cho Deploy |
| Phối hợp | Software Engineer (nhận lại bug thật), Project Manager (acceptance criteria → test case), DevOps (CI gate chặn merge), SRE (chaos, môi trường giống prod) |
| Kim tự tháp (tầng 1-4) | Source (review, lint, type, unit, secret scan) → Integration (BE↔DB/Redis/queue, API, contract) → Business (auth, order, payment, RBAC) → E2E/MCP (Playwright, chỉ luồng chính) |
| Ba mặt cắt ngang (tầng 5-7) | Performance (load, stress, spike, soak, volume) · Security (authn/authz, IDOR/BOLA, SQLi, XSS, CSRF, SSRF, rate-limit, prompt-injection) · Reliability (logging, tracing, retry, idempotency, chaos, backup/restore, rollback) |
| Luật chọn tầng | "Đặt mỗi kiểm tra ở tầng rẻ nhất chứng minh được nó" |
| 4 verdict cho test đỏ | Real bug (báo branch + input cụ thể, giữ nguyên test) · Wrong expectation (sửa assertion) · Over-coupled (assert theo cài đặt, viết lại theo hành vi) · Missing branch (lộ nhánh chưa phủ, thêm case) |
| Mô hình chạy | Agent QA ở session riêng; code xong "tự ném sang" QA; fail thì tự trả về cho bên code |

### 3.2 Kiểm từng ý

| Ý | Kiểm | Ghi chú |
|---|---|---|
| "Test là một bản spec chạy được. Suite chưa chạy là lời tuyên bố, không phải kết quả" | ✅ | Khớp nguyên tắc "bằng chứng, không lời khai"; xem mục 21 §10c (Anthropic: "every stage commits an artifact the next stage can read") |
| Kim tự tháp: đáy rộng, đỉnh hẹp; đẩy test xuống tầng thấp nhất | ✅ | Đúng ý Cohn/Fowler: "push your tests as far down the test pyramid as you can"; E2E "notoriously flaky" nên giữ ít luồng giá trị cao |
| Tầng 3 Business nằm giữa tháp | ⚠️ | Ba tầng còn lại chia theo **phạm vi** (đơn vị, ghép nối, toàn hệ). Business chia theo **nội dung**; test nghiệp vụ thường viết ở tầng unit hoặc integration. Nên đọc là "nội dung cần kiểm", không phải một bậc đắt rẻ riêng |
| Tầng 5-7 "áp cho mọi tầng" | ⚠️ | Đúng ý (đây là mặt cắt, không phải tầng), nhưng gọi chung là "tầng" gây nhầm với tháp. Gọi là "mặt cắt ngang" cho nhất quán |
| "Đừng đẩy lên E2E cho đắt token" (bài đăng) | ⚠️ | E2E đắt chủ yếu vì **chậm và flaky**; token chỉ là một phần |
| Verdict 1-3 | ✅ | Ba nguyên nhân thật của test đỏ: code sai, kỳ vọng sai, test bó vào cài đặt. Quy tắc "code sai thì báo bug, không sửa test cho khớp output sai" là điểm mạnh nhất |
| Verdict 4 "Missing branch" | ⚠️ | Không phải nguyên nhân khiến test **đỏ**; thiếu nhánh là lỗ hổng coverage, test không chạy thì không đỏ. Bộ phân loại thường gặp thay bằng **flaky / môi trường** (đỏ không do code lẫn test). Nếu giữ "missing branch", nên đặt ở bước đọc báo cáo coverage/mutation, không ở bước phân loại test đỏ |
| "Không ngồi giữa, đỡ tốn token hẳn" (bài đăng) | ❌ | Hai session thì tổng token **tăng** (thêm một ngữ cảnh). Cái giảm là công sức điều phối của người. Chưa có số đo nào trong ảnh |
| "Fail là tự trả về cho thằng code sửa" | ⚠️ | Thiếu trần vòng lặp và điều kiện dừng; ảnh không nói. Vòng tự động không giới hạn dễ lặp mãi cùng một lỗi |
| Chạy "đủ 7 tầng" cho mọi thay đổi | ⚠️ | Mâu thuẫn với luật rẻ nhất ở chính bài. Nên chọn tầng theo **rủi ro của thay đổi** |

**Tổng:** 3✅ / 6⚠️ / 1❌. Ảnh đúng ở khung và luật; sai ở hai tuyên bố về chi phí và ở verdict thứ 4.

### 3.3 Nền khoa học: vì sao tách người viết test khỏi người viết code

- Bài "Design choices made by LLM-based test generators prevent them from finding bugs" (arXiv 2412.14137, đọc qua tóm tắt tìm kiếm 2026-10-17, chưa đọc toàn văn) nói công cụ sinh test bằng LLM thường **quan sát cài đặt hiện có rồi lọc hoặc "sửa" test đỏ**, nên khó phát hiện bug; đây là bài toán **test oracle** cũ. Chính tuyên bố của ảnh ("code sai thì báo bug, không sửa test") đánh vào đúng điểm này.
- arXiv 2601.05542 (2026, tóm tắt): oracle do LLM sinh chính xác hơn khi được cho thêm ngữ cảnh lớp, nhưng ngữ cảnh đó **chứa cả code lỗi**. Chưa kiểm số liệu gốc **(chưa xác minh)**.
- AugmenTest (arXiv 2501.17461): suy hành vi đúng từ tài liệu và comment thay vì từ code, để oracle không bắt chước lỗi của code.
- Kết luận dùng được: để test bắt được lỗi, **oracle nên đến từ spec, không từ code**, và người viết test nên khác ngữ cảnh với người viết code. Đây là lý do thiết kế "QA ở session riêng" có cơ sở, dù tuyên bố về token thì không.

### 3.4 Đối chiếu với kho (ba cột)

| Cơ chế | Kho đã có, sâu hơn | Kho đã có, nông hơn | Kho chưa có |
|---|---|---|---|
| Kim tự tháp, đẩy test xuống thấp | Mục 13 §4b (quality gate stack), mục 11 §1b (e2e có agent: tester-army/e2e) | | |
| Verdict SHIP/BLOCK kèm bằng chứng | Mục 09 §1.5 (`agent.md`: GO/NO-GO nhị phân, evidence-first) | | |
| Hook chặn agent sửa test khi sửa lỗi | Mục 21 §10c.5, mục 23 | | |
| Giới hạn vòng sửa (tối đa 3 repair cùng lỗi) | Mục 23 (AI Delivery Loop, xboss) | | |
| Mutation test kiểm test có bắt lỗi không | Mục 07 | | |
| **Phân loại test đỏ thành 4 nguyên nhân, mỗi nguyên nhân một hành động được phép** | | Mục 21 §9 chỉ có quy tắc "không skip/disable test để xanh" | ✅ Bảng đầy đủ kèm bằng chứng bắt buộc cho từng verdict |
| **Vai QA riêng, viết test từ spec, không sửa code sản phẩm** | | Mục 01 §3g (pipeline PM→Coder→QA, nhưng QA dùng lệnh do LLM sinh) | ✅ Vai có quyền ghi giới hạn trong thư mục test |
| **Chọn tầng theo rủi ro thay đổi** | | | ✅ |

### 3.5 Dùng thế nào

- **Lấy:** luật "tầng rẻ nhất", bảng verdict (đổi verdict 4 thành flaky/môi trường), và ý tách người viết test khỏi người viết code ở vùng rủi ro cao.
- **Sửa trước khi dùng:** bỏ tuyên bố "đỡ tốn token", thêm trần vòng lặp, chọn tầng theo rủi ro thay đổi, oracle lấy từ spec.
- **Không lấy:** mô hình QA "tự nhận việc" từ bên code. Điều phối nên đi qua một phiên chính duy nhất để giữ ngân sách và điểm dừng (đúng nguyên tắc ở mục 23 §4.4).
- Các điểm nên lấy được đưa vào khung X-Templates ở PR riêng (repo `seeker19110/X-Templates`, mảng 14 và harness `.claude/`).

**Nguồn §3:** ảnh và bài nháp người dùng gửi (2026-10-17) · https://martinfowler.com/articles/practical-test-pyramid.html (đọc 2026-10-17) · https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html (đọc một phần, 2026-10-17) · https://arxiv.org/html/2412.14137v1 · https://arxiv.org/html/2601.05542v1 · https://arxiv.org/html/2501.17461v1 (cả ba chỉ đọc qua kết quả tìm kiếm)

---

## 3b. Nâng cấp 31/10/2026: rà repo lớn

> Hai việc. (1) Đọc lại sao, license, ngày push của **8 repo** mục 09 trong catalog (GitHub search API, 31/10/2026). (2) Tìm repo lớn còn thiếu: truy vấn GitHub "checklist", "best practices", "security checklist", `topic:best-practices`, "engineering handbook", "production readiness", lọc theo `data/projects.json`. Chọn **5 repo**, clone `--filter=blob:none`, đọc LICENSE, cấu trúc, file chính, CI, lịch sử commit. Đã xét nhưng **không thêm**: `google/eng-practices` (23,3k★, **đã archive**, push cuối 19/9/2024) và `thedaviddias/Front-End-Performance-Checklist` (17,4k★; nhánh `main` đứng yên từ 23/3/2025, 164/224 commit là năm 2018, không nhắc tới INP). **Không chạy script nào của các repo.**

### 3b.1 Repo cũ: điều đã đổi

| Repo | Thay đổi (→ 31/10/2026) | Hệ quả |
|---|---|---|
| `thedaviddias/Front-End-Checklist` | Catalog ghi `null`; nay **74,6k★** MIT, push 31/10. Mô tả GitHub đổi thành "for humans and AI agents" | Bổ sung số; checklist đã nhắm tới agent như `agent.md` ở §1.5 |
| `OWASP/CheatSheetSeries` | Catalog `null`; nay **33,8k★** CC-BY-SA-4.0, push 30/10 | Bổ sung số |
| `shenril/owasp-asvs-checklist` | Catalog `null`; nay 220★, push 2/9/2026 | Nên đối chiếu với ASVS 5.0 gốc (dưới) trước khi dùng |
| `jeremychoi/owasp-asvs-wstg-checklist` | 22★, **push cuối 11/8/2020** | Đứng yên 6 năm, theo ASVS 4.0; thay bằng CSV chính thức của ASVS 5.0 |
| `trimstray/the-book-of-secret-knowledge` (bảng §2, chưa có trong catalog) | 254,8k★, push cuối 19/11/2024 | Đứng yên gần 2 năm (khớp mục 08 §2i) |
| `MarinJursic/production-readiness-checklist`, `PinoyFreeCoder/deployment-checklist`, `greenarmor/GESF` | 41 / 49 / 45★, đều còn push trong tháng 10 | Không đổi |

### 3b.2 Bảng nhanh 5 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `goldbergyoni/nodebestpractices` | Best practice Node.js | 105,7k · CC BY-SA 4.0 | 15/6/2026 | 108 mục ✔ trong 8 nhóm (kiến trúc, lỗi, test, bảo mật…), 10 bản dịch | **"2026 edition" chỉ là đổi chữ** |
| `shanraisshan/claude-code-best-practice` | Best practice Claude Code | 68,4k · MIT | 31/10/2026 | Ghi chú, 83 mẹo, workflow, `.claude/` mẫu đầy đủ hook/agent/skill | `settings.json` mở rộng quyền; 67% commit do Claude viết |
| `shieldfy/API-Security-Checklist` | Checklist bảo mật API | 23,3k · MIT | 21/7/2026 | 66 mục ngắn, 30 bản dịch (có `README-vi.md`) | Thiếu BOLA, SSRF, PKCE |
| `OWASP/ASVS` | Chuẩn xác minh bảo mật | 3,7k · CC BY-SA 4.0 | 26/10/2026 | ASVS 5.0.0 (30/5/2025): 17 chương, 345 yêu cầu, xuất CSV/JSON/CycloneDX | Sao thấp nhưng là chuẩn gốc |
| `OWASP/wstg` | Hướng dẫn kiểm thử web | 10,2k · CC BY-SA 4.0 | 30/10/2026 | 134 bài kiểm thử (không tính README), checklist JSON 13 nhóm / 115 mục, mục mới "Human-AI Collaborative Testing" | Bản ổn định v4.2 từ 12/2020 |

### 3b.3 Hồ sơ ngắn

- **nodebestpractices (Yoni Goldberg).** 3.917 commit, 275 tác giả (505 commit là bot all-contributors). Nội dung vẫn tốt cho backend Node: cấu trúc theo thành phần, phân biệt lỗi vận hành và lỗi lập trình, bảo mật, Docker. Kiểm lời quảng cáo: ❌ README ghi **"2026 edition is here! Modernized to 2026"**, nhưng commit duy nhất của 2026 (15/6) chỉ sửa 2 dòng, đổi "2024" thành "2026"; thư mục `sections/` không đổi từ 16/4/2025. Badge ghi "102 Best Practices", README đếm được 108 tiêu đề ✔ (⚠️ lệch nhẹ). License CC BY-SA 4.0: khi chia sẻ bản phái sinh cần tuân attribution/share-alike; không suy ra mọi tài liệu chỉ liên kết hoặc trích dẫn đều phải đổi license. Đọc tại https://github.com/goldbergyoni/nodebestpractices.
- **claude-code-best-practice (Shayan Rais).** Tạo 31/10/2025, 2.633 commit, trong đó **1.375 commit tác giả "Claude" và 401 "Claude Routine"** (67%), chỉ 5 tác giả. Không có CI. Giá trị nằm ở tài liệu `best-practice/*.md` (settings, skills, subagents, memory, MCP) và thư mục `.claude/` làm mẫu chạy được (77 file hook, agent, command, skill). **Nhưng `.claude/settings.json` của chính repo** cho phép `Bash(*)`, `Edit(*)`, `Write(*)`, `WebFetch(domain:*)`, `deny: []`, `enableAllProjectMcpServers: true` (tự bật 3 MCP chạy bằng `npx -y`, đã ghim phiên bản) và đổi spinner thành câu khen tác giả. Danh sách `ask` có `rm`, `wget` nhưng không có `curl`. ⚠️ Mâu thuẫn: `best-practice/claude-settings.md` tự ghi `Write(path)` và `NotebookEdit` trong `allow` "never consulted", nhưng settings mẫu vẫn dùng. Không mở repo này bằng Claude Code rồi chấp nhận trust nếu chưa đọc `settings.json`; chép từng phần thay vì cả `.claude/`.
- **API-Security-Checklist (Shieldfy).** Checklist cổ điển (2017), 374 commit, 104 tác giả, gần như chỉ còn nhận bản dịch (commit nội dung cuối 2/2026: "You don't need JWT", khuyên dùng API key ngẫu nhiên). Phần "Advanced" (rate limit, GraphQL, secrets, zero trust) thêm 1/2026. ⚠️ Không nhắc BOLA/IDOR theo đối tượng, SSRF, PKCE hay OWASP API Top 10: dùng làm danh sách nhắc nhanh, kiểm sâu thì theo ASVS V4/V8/V10.
- **OWASP ASVS.** 3.292 commit, 153 tác giả, đầu bảng Josh Grossman và Elar Lang. Bản 5.0.0 (tag `v5.0.0_release`, 30/5/2025) có chương mới cho token tự chứa (V9), OAuth/OIDC (V10), WebRTC (V17). Điểm hợp với agent: **file máy đọc được** `5.0/docs_en/*.csv|json|xml|cdx.json` (cột `req_id`, `req_description`, `L`), đủ để sinh checklist theo cấp L1–L3 hay đối chiếu tự động. Commit gần nhất cập nhật tham chiếu RFC mới và bản dịch tiếng Ba Tư. Có 11 ngôn ngữ, chưa có tiếng Việt.
- **OWASP WSTG.** 1.397 commit, 199 tác giả, 156 commit từ 1/7/2026. CI kiểm link (`md-link-check`), lint markdown, textlint, tự build checklist (`wstgbot` đăng checklist mới 30/10/2026). Bài mới **"Human-AI Collaborative Testing"** (23/10/2026) nói rõ AI đổi tốc độ và độ lặp lại, không đổi trách nhiệm và phạm vi kiểm thử. Bản ổn định vẫn là v4.2 (3/12/2020); bản "latest" là nhánh chính.

### 3b.4 Mẫu chung rút ra

1. **Chuẩn gốc thắng checklist cộng đồng**: ASVS 5.0 có CSV/JSON chính thức; các checklist ASVS cộng đồng ở §2 (shenril, jeremychoi) theo bản cũ. Agent nên đọc nguồn máy đọc được của chuẩn, không đọc bản chép lại.
2. **Nhãn năm không phải bằng chứng cập nhật**: nodebestpractices "2026 edition" chỉ đổi chữ; Front-End-Performance-Checklist không biết INP. Kiểm `git log -- <thư mục nội dung>`, đừng tin tiêu đề.
3. **Repo "best practice" cho agent cũng cần kiểm như code**: claude-code-best-practice mang settings mở quyền và tự bật MCP. Tài liệu đúng nhưng cấu hình mẫu thì không.
4. **License chia sẻ tương tự (CC BY-SA)** phổ biến ở checklist lớn (nodebestpractices, ASVS, WSTG, CheatSheetSeries): khi nhúng và phân phối nội dung phải giữ attribution/license và xét share-alike theo phạm vi bản phái sinh; chỉ liên kết không đồng nghĩa đổi license cho template.

**Nguồn §3b:** GitHub search API 31/10/2026 (`repo:` cho 8 repo cũ, 5 repo mới, `google/eng-practices`, `trimstray/the-book-of-secret-knowledge`; 6 truy vấn chủ đề) · `meta_all.json`/`status_all.json` đợt rà 31/10 · clone `--filter=blob:none`, đọc: goldbergyoni/nodebestpractices (LICENSE, README.md, `git show` commit 15/6/2026, lịch sử `sections/`), shanraisshan/claude-code-best-practice (LICENSE, README.md, .claude/settings.json, .mcp.json, .claude/hooks/scripts/hooks.py, best-practice/claude-settings.md, tác giả commit), shieldfy/API-Security-Checklist (LICENSE, README.md, lịch sử commit), OWASP/ASVS (LICENSE.md, 5.0/en/*.md, 5.0/docs_en/*.csv, 5.0/languages.txt, tag), OWASP/wstg (LICENSE, checklists/checklist.json, document/3-The_OWASP_Testing_Framework/2-Human-AI_Collaborative_Testing.md, .github/workflows/), thedaviddias/Front-End-Performance-Checklist (README.md, nhánh) · https://owasp.org/www-project-application-security-verification-standard/ · https://owasp.org/www-project-web-security-testing-guide/

## 3c. Nâng trần 2/11/2026: chuẩn cấp dự án dạng máy đọc được, SLO và ADR (yêu cầu người dùng)

> Tìm chuẩn và cổng máy còn thiếu cho phần dự án/phát hành/vận hành. Số sao, license và ngày push lấy từ GitHub search API ngày 2/11/2026; clone `--filter=blob:none`, đọc LICENSE, README, file chuẩn (YAML, Markdown), workflow. **Không chạy mã nào của các repo.** Đã xét nhưng **không thêm**: `mercari/production-readiness-checklist` (947★, MIT, HEAD 17/5/2021, đứng yên 5 năm) và `npryce/adr-tools` (5,8k★, push cuối 4/2024).

**Trần hiện tại**

- Mục có checklist cộng đồng (§1, §2), chuẩn bảo mật **ứng dụng** dạng máy đọc được (ASVS 5.0 CSV/JSON, WSTG checklist JSON ở §3b), compliance-as-code tự chấm (GESF §2b) và scanner `prc` (§1.8).
- Thiếu chuẩn cho **dự án và repo** (quản trị, phát hành, chuỗi cung ứng) có ID ổn định và mức độ, để agent đối chiếu bằng máy.
- Thiếu lớp **vận hành đo được**: SLO và error budget. GO/NO-GO của `agent.md` (§1.5) vẫn dựa vào checklist, không dựa vào số đo sau khi chạy thật.
- Thiếu mẫu **ghi quyết định** (ADR). `google/eng-practices` đã archive (§3b).

**Bảng repo mới**

| Repo | Lớp | ★ · license (2/11/2026) | Commit cuối | Vì sao nâng trần | Rủi ro |
|---|---|---|---|---|---|
| `ossf/security-baseline` (OSPS Baseline) | Chuẩn máy đọc được | 171 · Apache-2.0 | 29/10/2026 | 8 nhóm, 41 control, **67 yêu cầu có ID** `OSPS-XX-NN.NN` (2 mục đã retired), chia 3 mức: 24 / 19 / 22 yêu cầu còn hiệu lực bắt đầu ở L1 / L2 / L3. YAML theo schema Gemara; **14 file mapping** sang SSDF, SLSA, Scorecard, SAMM, CRA, NIST CSF, PCI DSS, ISO 18974, OpenCRE… Workflow của chính repo chạy `osps-baseline-action` hằng tuần và xuất SARIF | Sao thấp. Chuẩn đổi theo phiên bản ngày (workflow dùng catalog `osps-baseline-2026-02`, trang web 2026-08-28). Action quét là của bên thứ ba (`revanite-io`) |
| `ossf/best-practices-badge` | Cổng máy (badge) | 1,4k · MIT | 2/11/2026 | App bestpractices.dev, hai chuỗi tiêu chí: **Baseline 1–3** (64 control, sinh tự động từ OSPS bản 2026-08-28, `criteria/baseline_criteria.yml`) và **Metal** passing/silver/gold. Có API (`best_practices.openapi.yaml`), có `AGENTS.md` | Phần lớn tiêu chí do dự án tự khai. Repo đã chuyển từ `coreinfrastructure/` (search API trả 422 với tên cũ). Bản trong app (64) chậm hơn repo chuẩn (67) |
| `slsa-framework/slsa` | Chuẩn | 2,0k · Community Specification License 1.0 (GitHub báo `NOASSERTION`) | 28/10/2026 | Đặc tả SLSA. Tag **`v1.2` (24/11/2025)** thêm **Source Track** (yêu cầu với hệ quản lý mã) bên cạnh Build Track; định nghĩa provenance, threat model, cách xác minh | Chỉ là đặc tả: muốn có provenance phải dùng `slsa-github-generator` hoặc `actions/attest-build-provenance` (mục 12/13). Nhánh `main` là bản nháp kế tiếp |
| `OpenSLO/OpenSLO` | Chuẩn máy đọc được | 1,5k · Apache-2.0 | 27/10/2026 (HEAD 25/9) | Đặc tả YAML `apiVersion: openslo/v1` cho SLO, SLI, AlertPolicy, không phụ thuộc nhà cung cấp. SLO thành file trong repo, CI kiểm được | Chỉ là đặc tả. CLI kiểm hợp lệ `oslo` nằm ở repo riêng (chưa đọc). Mức hỗ trợ của các nền tảng giám sát **(chưa xác minh)** |
| `adr/madr` | Chuẩn (mẫu) | 2,6k · MIT hoặc CC0-1.0 (GitHub báo `NOASSERTION`) | 28/8/2026 | Mẫu Markdown ADR v4.0.0 (17/9/2024), 4 biến thể (đầy đủ, tối giản, bare, bare-minimal). Các mục Context, Considered Options, Decision Outcome và **Confirmation** (cách kiểm quyết định đã được thực hiện) | Chỉ là mẫu. Có bản dịch `de`, chưa có `vi` |
| `twelve-factor/twelve-factor` | Chuẩn nền | 2,8k · CC BY 4.0 | 21/8/2025 (HEAD 9/7/2025) | Nội dung 12factor.net đã mở mã nguồn, có `VISION.md`, `GOVERNANCE.md`. Kế hoạch thêm "Guidelines" thành yêu cầu cụ thể, kiểm được | Cập nhật chậm. Nội dung 12 factor chưa đổi lớn **(chưa xác minh)** |
| Google *SRE Workbook* (sre.google/workbook, web) | Chuẩn | Không có repo · CC BY-NC-ND 4.0 | 2018 | Chương 2–5 về SLO và cảnh báo theo SLO, **Phụ lục A mẫu tài liệu SLO**, **Phụ lục B chính sách error budget mẫu**, chương canary và postmortem | Phi thương mại, không cho phái sinh: chỉ trích dẫn và link, không chép vào template |

**Stack nâng trần**

1. **Lấy OSPS Baseline L1 làm sàn cho mọi repo.** Gắn mục của `base.md` (§1.3) và control GESF (§2b) với ID OSPS. Chạy `osps-baseline-action` (SARIF) cạnh OpenSSF Scorecard (mục 12/13); file `osps-to-scorecard.yaml` cho biết check nào trùng.
2. **Repo công khai đăng ký badge Baseline-1** trên bestpractices.dev, để người ngoài và agent đọc được trạng thái.
3. **Dùng SLSA v1.2 làm thang cho phần "Build & Release"** của deployment-checklist. Công cụ sinh provenance lấy từ mục 12.
4. **SLO thành file**: viết SLO bằng OpenSLO, thêm chính sách error budget theo Phụ lục B của SRE Workbook. Verdict GO/NO-GO của `agent.md` (§1.5) đọc trạng thái error budget, không phán đoán cảm tính.
5. **ADR theo MADR**, mục *Confirmation* trỏ tới cổng CI kiểm quyết định, để ADR không chỉ là văn xuôi.
6. **Giữ hai trục riêng**: ASVS/WSTG (§3b) cho **ứng dụng**, OSPS/SLSA cho **dự án và phát hành**. Đừng gộp vào một checklist.

**Nguồn §3c:** GitHub search API 2/11/2026 (`repo:` cho 8 repo; `best-practices-badge in:name`) · clone `--filter=blob:none`: ossf/security-baseline (HEAD `c62696c` 29/10/2026: LICENSE, README.md, `baseline/OSPS-*.yaml`, `baseline/mappings/`, `.github/workflows/baseline-scanner.yaml`), coreinfrastructure→ossf/best-practices-badge (`dfb72c1` 1/11/2026: LICENSE, README.md, `criteria/baseline_criteria.yml`), slsa-framework/slsa (`4d3f9d4` 28/10/2026: LICENSE.md, `docs/spec/draft/whats-new.md`, tag `v1.2`), OpenSLO/OpenSLO (`e025975` 25/9/2026: LICENSE, README.md, examples/), adr/madr (`ba75bb1` 28/8/2026: LICENSE*, CHANGELOG.md, template/), twelve-factor/twelve-factor (`3ad5a5f` 9/7/2025: LICENSE, VISION.md, content/), mercari/production-readiness-checklist (`5834a23` 17/5/2021) · https://sre.google/workbook/table-of-contents/ · https://baseline.openssf.org · https://www.bestpractices.dev · https://slsa.dev/spec/v1.2/ · https://openslo.com · https://adr.github.io/madr/ · https://12factor.net

---

<a id="operations-recovery-cost-evidence"></a>

## 3d. Nâng trần 2/11/2026: bằng chứng phục hồi, vận hành sự cố và phân bổ chi phí (rà soát toàn diện)

> Mở sâu phần vận hành sau §3c trong cùng ngày. Đã đọc metadata GitHub, clone nông, LICENSE, CI và mã/cấu hình chính của ba repo dưới đây; không cài, chạy backup/restore hay triển khai cluster. Số sao đọc 2/11/2026; ngày commit là HEAD nhánh mặc định. Đây là hồ sơ tham khảo cho dự án tích hợp, không phải kết quả diễn tập đã chạy.

### 3d.1 Khoảng trống sau SLO và checklist phát hành

§3c đã có SLO/error budget và chuẩn cấp repo. Phần còn thiếu là bằng chứng **phục hồi được** khi dữ liệu/hạ tầng hỏng, cách tách kiểm tra backup khỏi phục hồi dịch vụ, và chi phí đầy đủ khi tự host inference. Ba công cụ dưới đây giải quyết các lớp khác nhau; không công cụ nào tự cấp một verdict GO cho toàn ứng dụng.

| Repo | Lớp | ★ · license (2/11/2026) | HEAD · ngày commit | Vì sao đáng tham khảo | Giới hạn quan trọng |
|---|---|---|---|---|---|
| `restic/restic` | Backup/restore file, cổng integrity | 36.948 · BSD-2-Clause | `dd09b6bd01af220b1d5d95c0d4d7d472e05e05c4` · 18/10/2026 | Snapshot, mã hóa, dedupe; backend local/SFTP/S3 và nhiều object store; CLI `check`, `restore`, JSON output | `check` mặc định không đọc toàn bộ payload; backup file DB đang ghi chưa chứng minh nhất quán ứng dụng |
| `velero-io/velero` (trước `vmware-tanzu/velero`) | Backup/restore Kubernetes | 10.365 · Apache-2.0 | `10d28735d33aee36eb2bf15c6d93f2aa4baf248c` · 30/10/2026 | CRD/controller quản backup, restore, schedule; plugin object storage/volume snapshot; file-system backup qua **Kopia** | FSB đọc file đang chạy, không cùng một thời điểm; docs nhánh `main` gọi FSB là beta. Node agent cần root, có môi trường cần privileged |
| `opencost/opencost` | Phân bổ cost và cổng đo FinOps | 6.799 · Apache-2.0 | `24b94ef6acb4f4db39140d2380488e3c5bf45265` · 29/10/2026 | Cost theo namespace/model, CPU/GPU/RAM/volume và hạ tầng dùng chung; có API/Prometheus, inference cost cho vLLM | Giá đầu vào và metric/label phải đúng; cost tính theo usage không gồm idle/shared, không thể lấy làm toàn bộ hóa đơn |

### 3d.2 Hồ sơ và cổng thực sự đã đọc

- **restic** là chương trình Go cộng đồng, có `GOVERNANCE.md`, CI đa hệ điều hành, race test và một số backend integration. `cmd/restic/cmd_check.go` nói rõ muốn đọc dữ liệu phải chọn `--read-data` hoặc `--read-data-subset`; kiểm một phần không bao phủ toàn repo trong một lần. `restore` có đích riêng và chế độ dry-run. Giá trị tích hợp: dùng cho file, export DB nhất quán, artifact và dữ liệu ứng dụng; mật khẩu/credential phục hồi phải tồn tại ngoài chính máy cần cứu. `restore` ghi đè đích mặc định, nên diễn tập vào môi trường trống tách biệt. [Mã check](https://github.com/restic/restic/blob/dd09b6bd01af220b1d5d95c0d4d7d472e05e05c4/cmd/restic/cmd_check.go), [restore](https://github.com/restic/restic/blob/dd09b6bd01af220b1d5d95c0d4d7d472e05e05c4/doc/050_restore.rst), [license](https://github.com/restic/restic/blob/dd09b6bd01af220b1d5d95c0d4d7d472e05e05c4/LICENSE).
- **Velero** được phát triển từ Heptio Ark; canonical hiện là `velero-io/velero`, không coi việc redirect là bằng chứng repo cũ đã archive. `ARCHITECTURE.md` nối CRD với controller và provider plugin; `backup_controller.go` theo dõi lần backup thành công, nhưng metric đó chưa chứng minh ứng dụng đọc được dữ liệu sau restore. Tài liệu tách snapshot/CSI khỏi FSB và có pre/post hook để thực hiện bước nhất quán theo ứng dụng. CI có E2E trên kind và nhánh test CSI; chưa chạy lại trong đợt này. Phù hợp dịch vụ đã dùng Kubernetes; một VPS đơn giản không cần thêm cluster chỉ để dùng Velero. [Kiến trúc](https://github.com/velero-io/velero/blob/10d28735d33aee36eb2bf15c6d93f2aa4baf248c/ARCHITECTURE.md), [FSB và giới hạn](https://github.com/velero-io/velero/blob/10d28735d33aee36eb2bf15c6d93f2aa4baf248c/site/content/docs/main/file-system-backup.md), [backup hook](https://github.com/velero-io/velero/blob/10d28735d33aee36eb2bf15c6d93f2aa4baf248c/site/content/docs/main/backup-hooks.md).
- **OpenCost**, bắt đầu từ Kubecost, kết hợp specification và implementation Go. `pkg/inferencecost/collector.go` ghép allocation với metric token từ Prometheus theo model/namespace; calculator có fallback khi thiếu timing. `INFERENCE_COST_ENABLED` mặc định **false** trong mã. Tài liệu phân biệt `allocation` (gồm idle/shared để đối soát hạ tầng) với `usage` (tiêu thụ thực, không đối soát hóa đơn). Chỉ tiêu $/triệu token chưa phản ánh số task đạt eval; cần nối mục 07 để tính chi phí mỗi task thành công. CI có unit/integration nhưng chưa tái lập trên cluster. [Cổng opt-in](https://github.com/opencost/opencost/blob/24b94ef6acb4f4db39140d2380488e3c5bf45265/pkg/env/costmodel.go), [collector](https://github.com/opencost/opencost/blob/24b94ef6acb4f4db39140d2380488e3c5bf45265/pkg/inferencecost/collector.go), [hai cost basis](https://github.com/opencost/opencost/blob/24b94ef6acb4f4db39140d2380488e3c5bf45265/docs/inference-cost-tracking.md).

### 3d.3 Ma trận chọn theo hệ thống và bằng chứng

| Tình huống | Phương án tham khảo | Bằng chứng cần từ dự án đích | Chỉ số / giới hạn |
|---|---|---|---|
| Một máy/VPS, file và DB | Export DB nhất quán bằng công cụ DB + restic; so với snapshot/PITR của dịch vụ DB | Restore vào máy trống; mở ứng dụng, đọc bản ghi mẫu và kiểm quyền/schema; xác minh lấy được key | **RPO thực đo** = tuổi dữ liệu mới nhất còn khôi phục; **RTO thực đo** = thời gian tới khi dịch vụ đạt tiêu chí nghiệm thu; không suy ra từ lịch backup |
| Kubernetes có persistent volume | Velero resource backup + CSI hoặc FSB phù hợp volume; đối chiếu provider-native backup | Restore namespace/cluster tách biệt, kiểm CRD/RBAC/volume và đường đọc/ghi của ứng dụng | FSB cần application hook hoặc DB-native backup để đạt consistency mong muốn; migration còn phụ thuộc API/storage tương thích |
| Tự host model trên K8s | OpenCost + Prometheus + vLLM; chi phí API cloud giữ ở gateway/billing riêng | Model label khớp metric; báo cáo allocation/usage riêng và đối soát giá/khung giờ | Theo dõi $/task **đạt eval**, GPU idle, latency p95, quality cùng nhau; OpenCost không thay bảng phí API bên ngoài |
| Chưa dùng K8s hay không tự host model | Backup/PITR và billing export sẵn có của nền tảng | Bài restore thực và báo cáo hóa đơn | Không thêm Velero/OpenCost chỉ để đủ danh sách công cụ |

### 3d.4 Kiến trúc ghép vào vòng đời vận hành

1. **Định nghĩa khả năng phục hồi trước khi chọn công cụ:** phân loại dữ liệu, điểm nhất quán, RPO/RTO mục tiêu và điều kiện dịch vụ dùng lại được. Tách source code, cấu hình, DB, object store và key; không mặc định tất cả đã nằm trong volume backup.
2. **Ba tầng bằng chứng backup:** job đã thành công → integrity check có phạm vi rõ → restore và nghiệm thu ứng dụng. Với restic ghi tỷ lệ dữ liệu được đọc; với Velero ghi volume nào dùng CSI/FSB và hook nào thực sự chạy. Chỉ tầng cuối mới cho số RPO/RTO thực đo.
3. **Sự cố nối về SLO §3c:** runbook ghi triệu chứng/impact, người chỉ huy và người liên lạc, hành động giảm thiệt hại, rollback/restore, cách xác nhận phục hồi; postmortem giữ timeline và yếu tố hệ thống. Đây là mẫu phân tích vận hành của kho, không phải tính năng ba repo tự sinh. Dùng chương incident/postmortem của SRE Workbook đã có §3c để đối chiếu.
4. **Đo cost cùng chất lượng:** trace/eval mục 07 + token/caching mục 03/10 + allocation OpenCost. Giữ nguyên workload, phiên bản model và cửa sổ giá khi so; báo cả chi phí chạy lại sau lỗi và tài nguyên nhàn rỗi.
5. **Diễn tập trong môi trường thử có phạm vi:** chọn mất volume, dependency timeout hoặc mất credential giả; giới hạn dữ liệu/tài khoản, ghi điều kiện dừng. Kết quả là báo cáo thật của dự án đích; đợt nghiên cứu này **chưa chứng minh** các mục tiêu RPO/RTO hay độ đúng số cost trên hệ thống cụ thể.

**Đã đổi sau §3c:** checklist vận hành nay phân biệt “backup tồn tại” với “dịch vụ khôi phục được”, và cost hiệu suất với cost phân bổ đầy đủ. Không thay SLO, OSPS hay ADR đã có; thêm cách thu bằng chứng cho những nhận định đó.

**Nguồn §3d:** metadata GitHub API 2/11/2026; các permalink §3d.2; đọc `restic` LICENSE/README, `doc/{045_working_with_repos,050_restore}.rst`, `cmd/restic/cmd_{check,restore}.go`, `.github/workflows/tests.yml`; `velero` LICENSE/README, ARCHITECTURE, `pkg/controller/backup_controller.go`, docs backup/FSB/disaster recovery, `.github/workflows/e2e-test-kind.yaml`; `opencost` LICENSE/README, spec, `pkg/env/costmodel.go`, `pkg/inferencecost/{collector,calculator}.go` và unit/integration workflow. Nguồn chính thức ngoài repo: [restic check và repo health](https://restic.readthedocs.io/en/stable/045_working_with_repos.html), [Velero FSB](https://velero.io/docs/main/file-system-backup/), [OpenCost specification](https://opencost.io/docs/specification/), [OpenCost API](https://opencost.io/docs/integrations/api/), [SRE Workbook mục lục](https://sre.google/workbook/table-of-contents/). Docs `main` là bản phát triển; khi triển khai phải đọc đúng release của dự án đích.

## 3e. Nâng trần 4/11/2026: checklist thành hồ sơ bằng chứng theo từng bản phát hành

<a id="checklist-factory-2026-11-04"></a>

**Khoảng trống:** OSPS/SLSA/ASVS đã có ID chuẩn, SLO/backup/cost đã có thước đo. Xưởng vẫn cần biết **ai chứng minh, bằng artifact nào, tại bản nào, còn hiệu lực đến đâu**. Một checklist được agent đánh dấu đầy không đủ để chấp nhận release; báo cáo scanner cũ hoặc sai target cũng không đủ.

### 3e.1 Thêm lớp trưởng thành tổ chức: OWASP SAMM

<a id="owasp-samm-factory"></a>

**OWASP SAMM Core**, owaspsamm/core, SHA **bc2b5474ab248effbc357c389bec372b0f5e200f**, HEAD 2026-07-06; đọc 2026-11-04. License trong license.txt là **CC BY-SA 4.0**. Repo lưu model gốc dạng YAML cho **5 business functions, 15 security practices**, các hoạt động, câu hỏi và quality criteria; không phải scanner ứng dụng. Ví dụ V-ST-1-A hỏi tổ chức có dùng kiểm thử bảo mật tự động phù hợp stack không; V-ST-3-A đi tới tích hợp build/deploy, theo dõi kết quả và nối defect management. Workflow yaml-process.yml lint YAML rồi sinh Markdown; **không kiểm chứng tổ chức đã thực hiện control**.

Giá trị cho xưởng: nối chính sách và năng lực đội với bằng chứng thực hiện. Có thể dùng ID câu hỏi/hoạt động để tạo bản đồ trạng thái theo sản phẩm, chủ sở hữu và phạm vi. Khi trích/chuyển thể model cần giữ attribution và nghĩa vụ ShareAlike phù hợp; không suy license của SAMM sang tài liệu sản phẩm tự viết độc lập.

| Lớp đánh giá | Nguồn đã có/bổ sung | Đơn vị đánh giá | Artifact cần có |
|---|---|---|---|
| Chất lượng hoạt động của tổ chức | SAMM | Nhóm, hoạt động và mục tiêu trưởng thành | Phỏng vấn/quan sát + policy + mẫu artifact thực tế; tự khai phải ghi là tự khai |
| Mức tối thiểu của repo và release | OSPS/SLSA §3c | Repo/build identity/artifact | Quyền nhánh, CI, provenance và kết quả verify artifact đúng bản |
| Yêu cầu bảo mật ứng dụng | ASVS/WSTG §3b | Control áp dụng cho ứng dụng cụ thể | Test/evidence theo control, target/environment và phần chưa phủ |
| Khả năng vận hành/phục hồi | OpenSLO/restic/Velero §3c–§3d | Dịch vụ và dữ liệu | SLI và bài restore có kiểm tính đúng đắn sau phục hồi |

Các lớp bổ sung nhau; không lấy “SAMM level cao” thay test ứng dụng hoặc badge tự khai thay bằng chứng một release.

### 3e.2 Hợp đồng bằng chứng và ngoại lệ

Một dòng kiểm phát hành nên có: **requirement/control ID · owner · target/revision · command/method · artifact URI + checksum · observed result · thời điểm/hạn hiệu lực · reviewer · exception**. Tách pass/fail/skipped/not-applicable/inconclusive; not-applicable phải có lý do theo threat model hoặc phạm vi hợp đồng, không tự chuyển lỗi thành miễn trừ.

| Cổng đề xuất | Điều kiện chấp nhận | Ca phải từ chối |
|---|---|---|
| Đúng target và đúng lần chạy | Artifact gắn commit/build/image digest cần phát hành, có kết quả hiện tại | Dùng lại báo cáo của nhánh khác hoặc bộ test rỗng |
| Kiểm thực sự có hiệu lực | Một fixture lỗi đã biết bị policy/test/scanner từ chối | Có file cấu hình nhưng job không gọi, bị allow-failure hoặc lọc hết target |
| Ngoại lệ có giới hạn | Người chịu trách nhiệm, phạm vi, lý do, biện pháp bù và ngày hết hạn | Ignore wildcard hoặc miễn trừ vĩnh viễn không người sở hữu |
| Bằng chứng dữ liệu/vận hành | Migration/restore và rollback chạy trên dữ liệu thử đại diện | Backup job xanh nhưng chưa từng kiểm ứng dụng đọc dữ liệu phục hồi |
| Nghiệm thu độc lập | Reviewer đối chiếu yêu cầu critical và artifact | Chỉ nhận lời tự báo “xong” từ agent sinh code |

### 3e.3 Ghép vào xưởng

Bắt đầu bằng ASVS/OSPS control áp dụng và mức SAMM mục tiêu theo rủi ro; không bắt mọi sản phẩm đạt mức cao nhất ngay. Ánh xạ ID tới cổng mục 30–34, giữ manifest bằng chứng trong repo sản phẩm, chặn release khi thiếu bằng chứng critical hoặc ngoại lệ hết hạn. Sau incident, cập nhật một ca regression và control liên quan; giữ lịch sử quyết định để người mới hiểu lý do. Đây là thiết kế quản trị bằng chứng, **chưa có công cụ nào trong đợt này tự chứng minh toàn bộ quy trình**.

**Nguồn §3e:** [license.txt](https://github.com/owaspsamm/core/blob/bc2b5474ab248effbc357c389bec372b0f5e200f/license.txt) · [README.md](https://github.com/owaspsamm/core/blob/bc2b5474ab248effbc357c389bec372b0f5e200f/README.md) · [model/security_practices/V-Security-Testing.yml](https://github.com/owaspsamm/core/blob/bc2b5474ab248effbc357c389bec372b0f5e200f/model/security_practices/V-Security-Testing.yml) · [model/questions/V-ST-1-A.yml](https://github.com/owaspsamm/core/blob/bc2b5474ab248effbc357c389bec372b0f5e200f/model/questions/V-ST-1-A.yml) · [model/questions/V-ST-3-A.yml](https://github.com/owaspsamm/core/blob/bc2b5474ab248effbc357c389bec372b0f5e200f/model/questions/V-ST-3-A.yml) · [.github/workflows/yaml-process.yml](https://github.com/owaspsamm/core/blob/bc2b5474ab248effbc357c389bec372b0f5e200f/.github/workflows/yaml-process.yml)

## 4. Nguồn

- https://github.com/PinoyFreeCoder/deployment-checklist (README, `agent.md`, `CONTRIBUTING.md`, `checklists/base.md`, `checklists/nextjs.md`, cây `checklists/`, lịch sử commit – đọc 2026-10-12)
- https://github.com/PinoyFreeCoder · https://github.com/PinoyFreeCoder/mcp-project-planner · https://www.youtube.com/channel/UCFpZDxOMGzsx05epqfvmzbQ · https://www.facebook.com/PHfreecoder/
- https://github.com/MarinJursic/production-readiness-checklist
- https://github.com/shenril/owasp-asvs-checklist · https://github.com/D1X7R4/owasp-asvs-checklist · https://github.com/jeremychoi/owasp-asvs-wstg-checklist · https://github.com/nicoSWD/asvs-checklist · https://github.com/OWASP/DevGuide/blob/main/docs/en/04-design/03-mas-checklist.md · https://owasp.org/www-project-application-security-verification-standard
- https://futureagi.com/blog/self-improving-ai-agents-pre-deployment-checklist-2026/ · https://dev.to/techsavant_lab/should-this-ai-agent-go-live-a-10-question-gono-go-check-ckg · https://www.akto.io/blog/ai-agent-guardrails-checklist · https://aona.ai/resources/templates/ai-agent-deployment-checklist/ · https://www.alliancetek.com/blog/post/2026/08/31/secure-ai-agents-enterprise-deployment.aspx
- arXiv 2603.20953 (pre-action authorization) · 2606.04037 (pre-deployment assurance) · 2608.16411 (risk-free agent deployment)
