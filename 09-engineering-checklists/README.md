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

## 3. Nguồn
- https://github.com/PinoyFreeCoder/deployment-checklist (README, `agent.md`, `CONTRIBUTING.md`, `checklists/base.md`, `checklists/nextjs.md`, cây `checklists/`, lịch sử commit – đọc 2026-10-12)
- https://github.com/PinoyFreeCoder · https://github.com/PinoyFreeCoder/mcp-project-planner · https://www.youtube.com/channel/UCFpZDxOMGzsx05epqfvmzbQ · https://www.facebook.com/PHfreecoder/
- https://github.com/MarinJursic/production-readiness-checklist
- https://github.com/shenril/owasp-asvs-checklist · https://github.com/D1X7R4/owasp-asvs-checklist · https://github.com/jeremychoi/owasp-asvs-wstg-checklist · https://github.com/nicoSWD/asvs-checklist · https://github.com/OWASP/DevGuide/blob/main/docs/en/04-design/03-mas-checklist.md · https://owasp.org/www-project-application-security-verification-standard
- https://futureagi.com/blog/self-improving-ai-agents-pre-deployment-checklist-2026/ · https://dev.to/techsavant_lab/should-this-ai-agent-go-live-a-10-question-gono-go-check-ckg · https://www.akto.io/blog/ai-agent-guardrails-checklist · https://aona.ai/resources/templates/ai-agent-deployment-checklist/ · https://www.alliancetek.com/blog/post/2026/08/31/secure-ai-agents-enterprise-deployment.aspx
- arXiv 2603.20953 (pre-action authorization) · 2606.04037 (pre-deployment assurance) · 2608.16411 (risk-free agent deployment)
