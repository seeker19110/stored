# 13 · Dev Stack: Frontend · Backend · Mobile · DevOps · Spec-driven · AI Code Review

> Nền tảng kỹ thuật "cổ điển" mà agent/AI tooling đứng trên. Số sao ước lượng 2026 (nguồn lệch).

## 1. Frontend

| Framework | Repo | ★ | Ghi chú |
|---|---|---|---|
| React | facebook/react | ~251k (11/10/2026) | React 19; nền của Next.js, shadcn/ui |
| Vue | vuejs/core | ~54,9k (31/10/2026; số ~208k cũ là lỗi dữ liệu, §6g.1) | Vue 3.5; Nuxt |
| Next.js | vercel/next.js | ~125–138k | App Router, Server Actions; 59% dev dùng (State of JS 2025) |
| Angular | angular/angular | ~95k | Angular 18+ |
| Svelte | sveltejs/svelte | ~78k | Svelte 5 runes; SvelteKit |
| Nuxt | nuxt/nuxt | ~54k | |
| Astro | withastro/astro | ~63,6k (31/10/2026) | Islands, content-first |
| SolidJS | solidjs/solid | ~32k | |
| Vite | vitejs/vite | ~83k (13/10/2026) | Build tool mặc định của hệ sinh thái; Rolldown; v8.3 |
| TanStack (Query/Router/Start) | TanStack/* | Query ~50k (13/10/2026) | Full-stack TS mới nổi; Query có adapter React/Vue/Solid/Svelte/Angular/Preact |
| Tailwind CSS | tailwindlabs/tailwindcss | ~98k (13/10/2026) | Utility-first CSS, v4.3 (cấu hình CSS-first); kiểm ảnh ở §6c |

## 2. Backend

| Framework | Repo | ★ | Ghi chú |
|---|---|---|---|
| FastAPI | fastapi/fastapi | ~100k | Mặc định cho API AI/Python |
| NestJS | nestjs/nest | ~76.8k (10/2026) | TS enterprise |
| Django | django/django | – | Python full-stack; Django 5 |
| Spring Boot | spring-projects/spring-boot | – | Spring Boot 4, Java enterprise |
| Hono | honojs/hono | ~32.5k | Edge-first, 1.5M tải/tuần, tăng nhanh nhất Node |
| Express / Fastify | expressjs/express · fastify/fastify | – | Express 5; Fastify hiệu năng |
| Bun / Deno | oven-sh/bun · denoland/deno | – | Runtime thay Node |
| Go (Gin, Fiber), Rust (Axum, Actix) | – | – | Hiệu năng cao |

## 3. Mobile / cross-platform

| Framework | Chia sẻ | Phù hợp |
|---|---|---|
| **Flutter** | UI + logic (Dart) | UI tùy biến, mobile + web + desktop |
| **React Native + Expo** | UI + logic (TS) | Team có sẵn React; New Architecture bỏ bridge |
| **Kotlin Multiplatform (+ Compose MP)** | Logic (UI native hoặc Compose) | Enterprise/fintech có kỹ năng Kotlin |
| .NET MAUI | UI + logic (C#) | Hệ sinh thái Microsoft |
| Capacitor/Ionic, Tauri Mobile | Web → native | Web team |

## 4. DevOps / Platform

| Lĩnh vực | Công cụ | Ghi chú |
|---|---|---|
| Container | Docker, Podman | |
| Orchestration | **Kubernetes** (CNCF graduated) | Baseline |
| IaC | **Terraform** (BSL) vs **OpenTofu** (MPL, fork cộng đồng), Pulumi, Crossplane | OpenTofu tăng do lo lock-in |
| GitOps / CD | **Argo CD** (CNCF graduated, phổ biến nhất), Flux | |
| CI | **GitHub Actions**, GitLab CI, Dagger (pipeline as code), Buildkite | |
| Observability | Prometheus, Grafana, OpenTelemetry, Loki | |
| Dev env | Dev Containers, Nix, mise | Quan trọng cho agent chạy test/lint |
| Danh sách | `bregman-arie/devops-exercises`, CNCF Landscape | |

### 4b. "Quality gate stack" quan sát trong 19 repo của chủ kho (mục 23, 2026-10-12)

| Lớp | Công cụ / mẫu | Repo |
|---|---|---|
| Bảo vệ nhánh | **GitHub rulesets** dưới dạng code (`.github/rulesets/main.json`), job `quality`/`quality-gate` gom mọi cổng làm required check duy nhất | case-study-ft41, Dhcb-Tools, Sales-Hunter |
| Dependency | Dependabot **gom nhóm đa hệ sinh thái** + **WIP cap** (giới hạn PR bot mở cùng lúc); `scheduled-audit.yml` pip-audit hằng tuần; `dotnet list package --vulnerable` | case-study-ft41, Sales-Hunter, Dhcb-Tools |
| Policy | OPA/conftest, `pr-policy.yml` (PR `feat` phải link spec "Approved for implementation"; tự xin Copilot review qua `pulls.requestReviewers`) | qlkh, xboss |
| Web | Playwright CI 4 worker + cache browser; **Lighthouse CI** chặn merge 4 category; `@axe-core/playwright` | Xgold, xboss |
| Release | release-please (conventional commits → changelog + tag), Keep a Changelog + commitlint/husky/lint-staged, nhãn `no-changelog` cho PR bot | REA, xboss, Sales-Hunter |
| Chất lượng mã | **oxlint** (lint Rust nhanh), **knip** (code/dep chết), **jscpd** (trùng lặp), fast-check (property test), TypeDoc; Python: **uv**, **ruff**, **pyright**, pip-audit, hatchling, pre-commit, import-linter | REA, Sales-Hunter, qlkh |
| Cổng tĩnh tự viết | 17+ `check:*` (route-perms, db-params, lib-layers, migrations, coverage ratchet, hex-hardcode, contrast, progress-freshness); fitness function AST; mutation test ~150 dòng | xboss, qlkh |
| Tài liệu tươi | `check-progress-freshness.ts` / `check_status_freshness.py` (SHA ghi trong PROGRESS/STATUS phải là tổ tiên HEAD; PROGRESS đổi cùng code); `validate_repo.py` hợp đồng repo (file bắt buộc, link md, config theo schema) | xboss, Sales-Hunter |
| Supply chain | hash-locked tool (`ci/tool-checksums.txt`), Action pin SHA, syft SBOM, gitleaks, CodeQL, concurrency group theo SHA | qlkh, X-Scanner, Dhcb-Tools |

**Stack frontend ghi nhận (10/2026):** Next.js 16 App Router + React 19 + TypeScript 6 (strict) + Tailwind 4; Postgres raw SQL hoặc Supabase; node:test thay vitest (xboss ADR-0002) — chọn theo nguyên tắc "ít phụ thuộc, agent chạy test được ngay".

### 4c. Thông số các repo trong quality gate stack (đã xác minh 2026-10-12)

| Repo | ★ (12/10) | License | Phát hành / hoạt động gần nhất | Vì sao chất lượng | Lưu ý |
|---|---|---|---|---|---|
| **astral-sh/uv** | 90,6k | Apache-2.0 + MIT | 0.13.0 (9/10/2026) | Quản lý gói/dự án Python viết bằng Rust; README đo nhanh hơn pip 10–100 lần | Vẫn 0.x; OpenAI công bố mua Astral (19/3/2026) |
| **astral-sh/ruff** | 50,0k | MIT | 0.17.0 (9/10/2026) | Linter + formatter Python, hơn 900 rule; FastAPI, pandas, SciPy, transformers, Airflow dùng | Không kiểm kiểu; rule có thể đổi giữa các bản 0.x |
| **microsoft/pyright** | 15,7k | MIT | 1.1.414 (9/9/2026), commit 9/10 | Type checker Python theo chuẩn, Microsoft bảo trì, CLI + VS Code | Cần Node; một số tính năng IDE chỉ có trong Pylance |
| **biomejs/biome** | 25,9k | MIT / Apache-2.0 | CLI v2.5.15 (30/9/2026), commit 12/10 | Formatter + linter JS/TS/JSON/CSS/GraphQL, hơn 500 rule, tương thích Prettier 97%, không cần Node | Chưa ngang hoàn toàn ESLint/Prettier, chuyển config cần cẩn thận |
| **oxc-project/oxc** (oxlint) | 23,0k | MIT | oxlint v1.87.0 (5/10/2026) | Bộ công cụ JS nhanh (parser, oxlint, oxfmt); Preact, Shopify, ByteDance dùng oxlint | Phát hành rất dày |
| **webpro-nl/knip** | 12,4k | ISC | 6.41.0 (9/10/2026) | Tìm file, dependency, export không dùng trong JS/TS; có `@knip/mcp` và language server; chỉ 11 issue mở | Framework cần cấu hình plugin (vd. chạy typegen của react-router trước) |
| **kucherenko/jscpd** | 6,4k | MIT | v5.4.1 (9/10/2026) | Phát hiện code trùng lặp cho 224 định dạng; reporter SARIF/AI, GitHub Action, MCP server; engine Rust | Phát hiện trùng lặp ngữ nghĩa (Type-4) còn thử nghiệm |
| **renovatebot/renovate** | 22,7k | AGPL-3.0 | 44.151.5 (12/10/2026) | Tự động cập nhật dependency cho hơn 90 trình quản lý gói trên GitHub, GitLab, Bitbucket, Azure DevOps, Gitea, Forgejo | AGPL; khoảng 1k issue mở |
| **pre-commit/pre-commit** | 15,6k | MIT | v4.6.2 (10/8/2026), commit 9/10 | Framework hook git đa ngôn ngữ, ghim phiên bản hook theo repo; có pre-commit.ci; chỉ 18 issue mở | Hook local bỏ qua được bằng `--no-verify` → luôn chạy lại trong CI |
| **googleapis/release-please** | 7,6k | Apache-2.0 | v17.11.2 (24/8/2026) | Conventional commits → changelog + tag (REA, xboss dùng) | — |
| **reviewdog/reviewdog** | 9,7k | MIT | commit 11/10/2026 | Biến kết quả linter bất kỳ thành comment review trên PR | Bản phát hành cuối v0.21.2 (18/9, nhiều khả năng năm 2025) |
| **stryker-mutator/stryker-js** | 3,2k | Apache-2.0 | v10.0.0 (14/8/2026) | Mutation testing chuẩn cho JS/TS; thay script tự viết ở §4b khi repo lớn | — |
| **GoogleChrome/lighthouse-ci** | 7,1k | Apache-2.0 | **commit cuối 26/6/2025** | Chặn merge theo điểm Lighthouse (Xgold, xboss dùng) | **Đứng yên hơn 15 tháng** — vẫn chạy được nhưng cần theo dõi phương án thay |

**Nhận xét:**

- Phần lớn stack trong §4b được bảo trì rất tích cực (có bản phát hành trong 10/2026). Ngoại lệ đáng chú ý: **Lighthouse CI không commit từ 6/2025**, trong khi hai repo của chủ kho đang dùng nó làm cổng chặn merge.
- uv và ruff giờ thuộc OpenAI (thương vụ Astral công bố 19/3/2026); license vẫn MIT/Apache nên rủi ro thấp, nhưng nên theo dõi.
- Repo JS/TS mới: biome (format + lint) hoặc oxlint, cộng knip và jscpd. Python: uv + ruff + pyright. Cả hai: pre-commit ở máy **và** chạy lại trong CI; Renovate hoặc Dependabot gom nhóm.
- `alibaba/open-code-review` (§6) nay có 46,4k★, v1.12.13 (8/10/2026); mới mở mã giữa 2026, chỉ có benchmark tự công bố, và theo chính số liệu đó recall thấp hơn Claude Code.

## 5. Spec-driven development (SDD) cho AI coding

| Công cụ | Repo / nhà cung cấp | License | Cách tiếp cận | Nhận xét |
|---|---|---|---|---|
| **GitHub Spec Kit** | github/spec-kit | MIT | CLI + template: `specify → plan → tasks → implement`, chạy trên agent có sẵn (Copilot, Claude Code, Cursor, Gemini CLI) | Trung lập nhất; còn breaking changes |
| **AWS Kiro** | kiro.dev | Proprietary | IDE fork VS Code, spec-first từ đầu, hooks | Lock-in AWS |
| **BMAD-METHOD** | bmad-code-org/BMAD-METHOD | MIT | Agent theo vai trò (analyst, PM, architect, dev) mô phỏng team | Opinionated về quy trình |
| **OpenSpec** | Fission-AI/OpenSpec | MIT | Spec thay đổi (change proposals) nhẹ | |
| Tessl, intentdocs, codemyspec | – | – | Thương mại | |

**Liên hệ mục 03:** spec là "hợp đồng" để chạy nhiều agent song song và là tiêu chí dừng cho loop.

### 5a. Hồ sơ github/spec-kit: từ bộ template SDD thành khung quy trình có extension, preset, workflow và bundle (ảnh trang repo người dùng gửi, đọc mã 3/11/2026)

> Ảnh ghép hai phần: trang repo (`github/spec-kit`, 102 issue, 125 PR, 13k fork, 145k★, commit cuối `7370e59` của Quratulain-bilal "3 days ago", About "Toolkit to help you get started with SDD or any other process!", topic ai/copilot/development/engineering/prd/spec/spec-driven, MIT) và đầu README ("Build with a spec, fix a bug, or assess an idea — with your coding agent", badge release **v1.2.5**, 145k★, MIT, docs GitHub Pages). Đã clone `--filter=blob:none` đủ lịch sử, HEAD `ba8363f8ab56b2da456a81299cfdbfee1ef7b871` (2/11/2026). **Không cài, không chạy.** Dòng bảng §5 ở trên là ghi chép từ 10/2026; hồ sơ này thay cho nó.

**Kiểm ảnh**

| Ô trong ảnh | Kết quả | Đối chiếu (3/11/2026) |
|---|---|---|
| 145k★, 13k fork | ✅ | 145.528★, 13.055 fork (GitHub search API) |
| 102 issue + 125 PR | ✅ gần đúng | API trả 214 issue+PR mở; ảnh cộng lại là 227, khác nhau do thời điểm chụp |
| "release v1.2.5" | ⚠️ cũ | v1.2.5 ra 28/10/2026; **v1.2.6** ra 2/11/2026 (PyPI cũng 1.2.6). `pyproject.toml` ở HEAD đã là `1.2.7.dev0` |
| "MIT" | ✅ | `LICENSE` MIT, "Copyright GitHub, Inc." |
| Câu "SDD or any other process" | ✅ | README nay chia **ba quy trình**: SDD nằm trong lõi, còn bug fixing và idea assessment là extension đi kèm (bundle `bugfix`, `assess`), cộng cơ chế để tự làm quy trình riêng |

**Đã đổi so với dòng §5 (ghi 10/2026)**

- Không còn chỉ là `specify → plan → tasks → implement` với 4 agent. `integrations/catalog.json` có **43 integration**. Có thêm 5 lớp mở rộng: extension (5 chính thức, **186 cộng đồng**), preset (42 cộng đồng), workflow (có overlay và step package), bundle theo vai trò, và catalog riêng của tổ chức, hỗ trợ cả air-gapped. README tự nói: "Catalog listings are not audits or endorsements, so review community source code before installing".
- Cài bằng `uv tool install specify-cli` từ PyPI (Python ≥ 3.11). Trước đây README hướng dẫn cài `--from git+https://github.com/github/spec-kit.git`; lệnh này bị bỏ trong đợt tinh gọn README 5/2026 (`707e929`) rồi 9/2026 (`3affdb2`).
- Dự án lớn nhanh: 2.329 commit từ 21/8/2025. Manfred Riem 424, bot 249, Den Delimarsky khoảng 286 (2 tên); **869 dòng trailer Co-Authored-By Claude**.

**Cổng và chuỗi phát hành (đọc mã)**

- `publish-pypi.yml` build bằng `uv build`, rồi `uv publish` trong environment `pypi` với `id-token: write` (trusted publishing OIDC). Action ghim theo **SHA**. Tuy vậy PyPI **không có provenance** cho `specify_cli-1.2.6-py3-none-any.whl` (API integrity của PyPI trả "No provenance available"). Muốn kiểm nguồn gốc thì phải đối chiếu với release trên GitHub.
- CI có `test.yml` (Python 3.11 và 3.12 từ #5220), `lint.yml`, `codeql.yml`, `security.yml`, `extension-version-guard.yml`. Repo cũng tự dùng **GitHub Agentic Workflows** (cặp `*.md` + `*.lock.yml`) để agent đánh giá bug, PR và feature, và để duyệt đề xuất thêm extension, preset, bundle cộng đồng, có danh sách `trusted-users` (xem gh-aw ở mục 21).
- Grep `telemetry|posthog|analytics` trong `src/` chỉ thấy comment về handler sự kiện; **không thấy mã gửi telemetry**.

**Rủi ro và cách dùng**

- Extension, preset và workflow cộng đồng có thể chạy lệnh shell và hook theo vòng đời agent. Hãy đọc mã trước khi cài, hoặc dựng catalog riêng chỉ gồm thành phần đã duyệt (tính năng có sẵn).
- Ghim phiên bản (`uv tool install specify-cli==1.2.6`). Nhịp phát hành vài ngày một bản; CHANGELOG và `docs/upgrade` là nơi xem thay đổi phá vỡ tương thích.
- Spec Kit "sở hữu quy trình" giống BMAD hay GSD. Nếu chỉ cần skill nhỏ, xem phản đề ở mục 20 §3c (mattpocock/skills). OpenSpec gọn hơn cho thay đổi nhỏ; Kiro khoá vào IDE của AWS.

**Nguồn §5a:** ảnh người dùng gửi 3/11/2026 · clone https://github.com/github/spec-kit HEAD `ba8363f8ab56b2da456a81299cfdbfee1ef7b871` (README.md, LICENSE, pyproject.toml, `integrations/catalog.json`, `extensions/catalog{,.community}.json`, `presets/catalog.community.json`, `workflows/`, `bundles/`, `.github/workflows/{publish-pypi,test}.yml` và các `*.lock.yml`; `git tag`, `git shortlog`, `git log -S git+https`) · https://pypi.org/pypi/specify-cli/json (1.2.6, 78 bản) · PyPI integrity API (không có provenance cho 1.2.6) · GitHub search API `repo:github/spec-kit` 3/11/2026.

## 6. AI code review

| Công cụ | Giá | Thế mạnh | Hạn chế |
|---|---|---|---|
| **CodeRabbit** | $24 / $48 dev/tháng; free public repo | All-rounder ít nhiễu; hỗ trợ 4 Git host | |
| **Greptile** | – | Bắt lỗi cross-file tốt (82% một benchmark) | Nhiều false positive; GitHub-first; benchmark Macroscope cho thấp hơn |
| **Qodo** (CodiumAI) | Qodo Merge mở, self-host (bản mã mở nay là `The-PR-Agent/pr-agent`, MIT, cộng đồng giữ, §6g.1) | F1 cao nhất trong 8 tool (2/2026); sinh test | |
| **GitHub Copilot Code Review** | Theo Copilot; usage-based private repo từ 6/2026 | Ít ma sát | Nông hơn |
| **Claude Code Review / `/code-review`** | Theo gói Claude | Chạy trong CLI/CI, GitHub Action | |
| Bito, Macroscope | – | | |
| **alibaba/open-code-review** (`ocr`) | Mở, Apache-2.0, Go; `ocr delegate` không cần API key | **Luật review theo glob đường dẫn** (`rule.json`, first-match-wins); xboss sinh rule từ mảnh markdown + test khớp file→rule; dhcb dùng | CI chỉ góp ý, không chặn |
| Santa Method / Council (skill ECC) | Theo gói model | 2 reviewer độc lập cùng rubric, cả hai phải pass | Xem mục 07 |

## 6b. Kiểm ảnh "CRM System Architecture" (#codepathindia, ảnh người dùng gửi, 2026-10-13)

Ảnh vẽ một CRM theo kiểu microservices. Client (web, mobile, nhân viên sales, cổng tự phục vụ của khách) đi qua CDN và load balancer, rồi API Gateway (Kong/NGINX/AWS) có IAM (Keycloak/Auth0). Phía sau là 6 service viết bằng Go/Echo: User, Contact, Opportunity, Task, Communication, Report & Analytics. Tầng dữ liệu gồm PostgreSQL, Redis, S3 và ClickHouse. Tích hợp ngoài: SendGrid/SES, Twilio, Stripe/Razorpay, Google Calendar. Hạ tầng chạy Docker và Kubernetes (HPA, EBS/EFS); quan sát bằng Prometheus, Grafana, ELK/OpenSearch, Jaeger. CI/CD dùng GitHub Actions/Jenkins, IaC dùng Terraform.

| Ô trong ảnh | Đánh giá | Ghi chú |
|---|---|---|
| CDN + LB, API Gateway (routing, rate limit, auth), IAM có RBAC/SSO | ✅ | Đúng vai trò từng lớp. Rate limit đặt ở gateway là hợp lý |
| 6 service tách theo miền (contact, opportunity, task…) | ⚠️ | Cách chia hợp lý về mặt miền. Nhưng với một CRM của một công ty, 6 service + Kubernetes là chi phí vận hành lớn; modular monolith tách đúng theo các miền này rồi mới tách dần thường rẻ hơn nhiều |
| Mỗi service ghi "PostgreSQL", tầng dữ liệu chỉ có một "PostgreSQL (Primary DB)" | ⚠️ | Ảnh không nói rõ database riêng cho từng service hay dùng chung. Dùng chung một schema thì các service dính nhau qua bảng, mất lợi ích chính của microservices |
| Không có message broker | ❌ | Các mũi tên đều là gọi trực tiếp. CRM cần sự kiện bất đồng bộ (lead mới → gửi email, đổi stage → cập nhật báo cáo, webhook ra ngoài). Thiếu Kafka/RabbitMQ/NATS hoặc ít nhất outbox pattern, và Communication Service dựa vào Redis thì dễ mất tin khi Redis không bật persistence |
| ClickHouse cho báo cáo | ⚠️ | Hợp lý cho analytics. Nhưng ảnh thiếu đường đưa dữ liệu từ PostgreSQL sang (CDC như Debezium, hoặc ETL); không có nó thì báo cáo sai hoặc chậm |
| "Load Balancer (Service Mesh)" có circuit breaker | ⚠️ | Gộp hai khái niệm khác nhau. Service mesh (Istio/Linkerd) lo mTLS, retry, circuit breaker giữa các service; LB ở rìa là chuyện khác |
| Persistent Volumes EBS/EFS | ⚠️ | Service Go nên stateless; volume chỉ cần nếu tự chạy DB trong cluster, mà khi đó nên dùng dịch vụ quản lý (RDS…) và có backup/PITR |
| Prometheus + Grafana + ELK/OpenSearch + Jaeger | ✅ | Bộ quan sát chuẩn. Ngày nay nên thu traces/metrics/logs qua OpenTelemetry rồi đẩy vào các backend này |
| CI/CD: Code Push → Build → Test → Build Image → Deploy | ⚠️ | Thiếu quét bảo mật (SAST, quét image, quét bí mật), migration DB, và môi trường staging trước production |
| Không có trong ảnh | ❌ | Tìm kiếm khách hàng/full-text (OpenSearch chỉ được vẽ cho log), audit log, backup và khôi phục, quản lý bí mật (Vault/Secrets Manager), multi-tenant nếu bán SaaS, đồng ý/xoá dữ liệu cá nhân (GDPR, Nghị định 13/2023 ở Việt Nam) |

**Tổng:** 2 ✅, 6 ⚠️, 2 ❌. Ảnh dùng được làm **bản đồ thuật ngữ** cho người mới (các lớp trong một hệ thống SaaS điển hình), không dùng được làm bản thiết kế: không có gì riêng của CRM ngoài tên service, và thiếu đúng phần khó nhất là luồng sự kiện giữa các service.

**Nếu cần CRM thật, xem mã nguồn mở trước khi tự dựng** (★ qua shields.io, 13/10/2026):

| Repo | ★ | Giấy phép | Stack | Ghi chú |
|---|---|---|---|---|
| twentyhq/twenty | ~58k | Phần lớn AGPL-3.0; một số file `@license Enterprise` là thương mại; SDK/CLI/UI là MIT | TypeScript, NestJS, PostgreSQL, Redis | CRM hiện đại, tự host được; dự án sôi động (commit hôm qua) |
| krayin/laravel-crm | ~24k | MIT | PHP Laravel | Giấy phép thoáng nhất trong nhóm |
| odoo/odoo | ~55k | LGPL-3.0 (bản Community) | Python | ERP đầy đủ, CRM là một module; Enterprise là bản trả phí |
| salesagility/SuiteCRM | ~5,8k | AGPL-3.0 | PHP | Kế thừa SugarCRM; lâu đời |
| frappe/crm | ~3,8k | AGPL-3.0 | Python (Frappe), Vue | Gọn, đi cùng hệ Frappe/ERPNext |
| espocrm/espocrm | ~3,5k | AGPL-3.0 | PHP | Nhẹ, dễ tuỳ biến |

Đọc kỹ các repo này cho thấy chúng đều là **monolith** (một ứng dụng + PostgreSQL/MySQL + job queue), không phải 6 microservice như ảnh.

## 6c. Kiểm ảnh "5 GitHub Repositories Every Frontend Developer Should Know" (codingwithparvez, ảnh người dùng gửi, 2026-10-13)

Ảnh giới thiệu 5 repo, mỗi repo kèm thẻ, "Why it's useful", một đoạn mã và ảnh minh họa. Số liệu kiểm bằng shields.io và `npm view` ngày 13/10/2026.

| Ô trong ảnh | Kết luận |
|---|---|
| ① **shadcn-ui/ui**: "Customizable UI components", thẻ React/TypeScript, "Add accessible components and own the code in your project", `import { Button } from "@/components/ui/button"` | ✅ Đúng mô hình copy mã vào dự án; đường dẫn import đúng mặc định CLI. ~125k★, MIT, CLI `shadcn` 4.21.4. Tính "accessible" đến từ primitive bên dưới (Base UI mặc định từ 7/2026, trước là Radix, xem mục 06) |
| ② **TanStack/query**: thẻ React, `const { data, isLoading } = useQuery({ queryKey, queryFn })` | ⚠️ Thẻ chỉ ghi React, trong khi thư viện có adapter Vue, Solid, Svelte, Angular, Preact (`@tanstack/*-query` đều có trên npm). `isLoading` vẫn chạy ở v5 nhưng tài liệu hiện chỉ dạy `isPending` rồi `isError`. ~50k★, MIT, `@tanstack/react-query` 5.104.2 |
| ③ **storybookjs/storybook**: thẻ React, `import type { Meta, StoryObj } from "@storybook/react"` + `satisfies Meta<typeof Button>` | ⚠️ Tài liệu Storybook 10.6 bảo import từ gói **framework** (`@storybook/react-vite`, `@storybook/nextjs`…), không phải gói renderer `@storybook/react`. Thẻ React thiếu Vue/Angular/Svelte/Web Components. `satisfies` đúng. ~91k★, MIT, v10.6.2 |
| ④ **vitejs/vite**: `npm create vite@latest my-app` → `npm install` → `npm run dev`; màn hình "VITE v5.x ready in 320 ms", "Network: http://192.168.1.5:5173" | ⚠️ Lệnh đúng (create-vite 9.2.1 còn có cờ `--immediate` cài và chạy luôn). Màn hình cũ: bản hiện tại là **8.3.4**, và mặc định Vite in "Network: use `--host` to expose"; dòng địa chỉ LAN chỉ có khi chạy với `--host` (đọc mã `vite` 8.3.4). ~83k★, MIT |
| ⑤ **tailwindlabs/tailwindcss**: "Utility-first CSS", JSX `className="min-h-screen bg-gray-950 text-white flex items-center justify-center"` | ✅ Mọi class có trong Tailwind 4.3.3. ~98k★, MIT |

**Tổng: 2✅ / 3⚠️ / 0❌.**

**Dùng ảnh thế nào:** danh sách đúng là 5 công cụ phổ biến, cả 5 đều MIT và còn hoạt động (commit trong ngày). Ba lỗi đều là lỗi "chụp lúc cũ hoặc chỉ nhìn React": sửa nhãn thành đa framework, đổi `isLoading` → `isPending`, import Storybook từ gói framework, cập nhật màn hình Vite. Tiêu đề "every frontend developer" thực ra là "dev React + Vite"; không có công cụ test (Vitest, Playwright) hay lint (ESLint, Biome) nào, xem §1 và §4b. Không tìm được bài gốc của codingwithparvez.

**Nguồn của mục:** shields.io 13/10/2026 (5 repo: sao, license, commit cuối, release) · `npm view` 13/10/2026 (shadcn, @tanstack/{react,vue,svelte,solid,angular-query-experimental,preact}-query, storybook, @storybook/{react,react-vite,vue3-vite,angular,sveltekit,web-components-vite}, vite, create-vite, tailwindcss) · https://storybook.js.org/docs/writing-stories · https://tanstack.com/query/latest/docs/framework/react/guides/queries · mã `vite` 8.3.4 (`dist/node/chunks/node.js`, chuỗi "--host … to expose") và README `create-vite` 9.2.1.

## 6d. Homebrew/BrewUI: GUI chính thức của Homebrew cho macOS (link người dùng gửi, 2026-10-14)

> Đã clone toàn bộ repo (1.201 commit, HEAD `7bc5efa` 13/10/2026, tag v0.6.0) và đọc README, `ARCHITECTURE.md`, `AGENTS.md` (`CLAUDE.md` là symlink tới nó), `Package.swift`, `.github/workflows/`, PR template, `Sources/`. Đối chiếu bài BleepingComputer, dev.to và trang GitHub.

### 6d.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 14/10/2026) |
|---|---|
| Repo | `Homebrew/BrewUI` · ~2,5k★, 80 fork, 2 issue + 2 PR mở · **AGPL-3.0** · About: "Homebrew's official macOS GUI" |
| Tuổi và nhịp | Commit đầu 2/3/2026; đỉnh 334 commit tháng 5, 235 commit tháng 9; 15 tag, v0.4.2 (15/9) → v0.6.0 (13/10/2026) |
| Tác giả | Graeme Arthur 875/1.201 commit; Mike McQuaid (trưởng dự án Homebrew) 67; BrewTestBot 102, dependabot 51; Ruoyu Zhong, Patrick Linnane là maintainer Homebrew |
| Ra mắt | "Phát hành đầy đủ" cùng **Homebrew 7.0.0 (13/9/2026)**, bản kèm lệnh `brew vulns` quét lỗ hổng qua OSV.dev (BleepingComputer 14/9/2026) |
| Cài | `brew install --cask homebrew-app`; app ký và notarize trong `release.yml` |
| Yêu cầu | **macOS 26 Tahoe trở lên** (`Package.swift`: `.macOS("26.0")`), Swift 6.2; Homebrew phải cài sẵn ở prefix mặc định (`/opt/homebrew` hoặc `/usr/local`) |
| Quy mô | 222 file Swift / ~20k dòng nguồn, 181 file test / ~24k dòng test (test nhiều hơn mã) |

### 6d.2 Kiến trúc và cổng chất lượng (đọc mã)

- **Không giấu Homebrew.** Mọi thao tác hiện lệnh `brew` copy được và giữ toàn bộ output trong console. Dữ liệu lấy từ `brew` CLI và JSON API formulae.brew.sh. App không sửa nội bộ Homebrew và chưa hỗ trợ prefix hay tap tuỳ chỉnh.
- **Clean Architecture + MVVM** chia 21 module SwiftPM: `BrewCore`, `BrewCLI` (chạy tiến trình), `BrewNetworking`, `BrewRepositories`, các `BrewFeature*` (Discover, Installed, Services, Doctor, Config, Console, SelfUpgrade). Feature không import feature khác.
- **Một hàng đợi lệnh.** Actor `SerialBrewCommandCenter` chạy tuần tự mọi lệnh làm thay đổi hệ thống và gộp lệnh trùng. Huỷ lệnh sẽ dừng cả process group.
- **Môi trường shell cô lập.** Luôn chạy `/bin/zsh --no-rcs --no-global-rcs` với PATH tối thiểu. Tham số đi qua argv nguyên văn, không nội suy chuỗi shell. Hệ quả: alias và biến export trong shell **không có tác dụng**, cấu hình phải đặt trong `brew.env`.
- **Tự nâng cấp** qua helper riêng: đợi app thoát, chạy upgrade, ghi kết quả, mở lại app. App từ chối nâng cấp khi đang có lệnh chạy.
- **Cổng máy:** pre-commit chạy SwiftFormat, SwiftLint strict và `BrewUILint` (luật lint riêng của dự án). CI có `pr_build_test` (`scripts/test`, `scripts/test-ui` trên runner `macos-26`), `swift_quality`, `licenses`, `actionlint`, `e2e`. Test UI tất định, không gọi Homebrew thật. Test e2e cài rồi gỡ gói `hello` thật.

### 6d.3 Điều đáng chú ý

- **Repo của một tổ chức lớn viết chủ yếu cùng AI, và nói rõ.** 455 trailer `Co-Authored-By` là model Claude (Opus 5, Opus 4.7/4.8, Sonnet 4.6) trên 1.201 commit. PR template có mục bắt buộc "AI assistance" và yêu cầu tách phần người tự kiểm với phần AI kiểm.
- **`AGENTS.md` (50 KB) là mẫu đáng học.** Có thứ tự ưu tiên chỉ dẫn (người dùng > `AGENTS.md` gần nhất > gốc) và quy định "web-search giá trị có phiên bản (runner, SDK, action) thay vì đoán theo dữ liệu huấn luyện". Agent phải chạy `scripts/test` trước mỗi commit. Bug sửa theo red-green TDD. Cấm dùng `scripts/test-e2e` trừ khi được yêu cầu. Cấm tắt test để qua CI. Cấm file nhớ phiên hay rule riêng cho từng tool. Khớp với khung drop-in của chủ kho (mục 23) và quy ước AGENTS.md (mục 04).
- **Không telemetry riêng của app** (grep `Sources/` không thấy SDK analytics). "Analytics" trong mã là số lượt cài công khai từ API Homebrew để xếp hạng trong Discover. Báo crash không tự gửi đi: app đọc báo cáo macOS ghi trong `~/Library/Logs/DiagnosticReports` rồi mở trang `issues/new` điền sẵn cho người dùng tự nộp. Lưu ý: chính `brew` vẫn gửi analytics theo mặc định của Homebrew. Muốn tắt thì đặt `HOMEBREW_NO_ANALYTICS=1` trong `~/.homebrew/brew.env`, vì app bỏ qua biến export của shell.
- **Tên dễ nhầm:** `mckaymic/Brewui` là app khác không liên quan. Bài Medium tả BrewUI như một phần của Homebrew, nhưng thực ra BrewUI là cask riêng (`homebrew-app`).
- **Thông tin cũ:** bài dev.to viết lúc dự án mới bắt đầu, nói "chưa tải về được". Nay đã có cask và bản v0.6.0.

### 6d.4 So sánh và dùng thế nào

| GUI Homebrew | ★ (14/10/2026, shields) | License | Ghi chú |
|---|---|---|---|
| **Homebrew/BrewUI** | ~2,5k | AGPL-3.0 | Chính chủ, cần macOS 26, hiện lệnh thật, dịch vụ chỉ đọc |
| `milanvarady/Applite` | ~7,1k | MIT | Tập trung cask/app, commit cuối 9/2026 |
| `buresdv/Cork` | ~4,7k | **"provisional license", không phải OSI** | Bản build sẵn bán trả phí (chưa xác minh giá) |
| `brunophilipe/Cakebrew` | ~5k | GPL-3.0 | **Đứng yên từ 3/2021** |

- **Cho người không quen Terminal** (đội văn phòng, thiết kế) trên macOS 26: BrewUI là lựa chọn an toàn nhất vì chính chủ, không giấu lệnh và không có telemetry riêng. Máy chạy macOS cũ hơn chỉ còn Applite.
- **Tái dùng mã:** AGPL-3.0 kèm điều khoản dùng qua mạng. Nhúng hay sửa để phát hành thì phải công bố mã. Học kiến trúc (hàng đợi lệnh tuần tự, shell cô lập, helper tự nâng cấp) thì không vướng.
- **Cho agent của chủ kho:** đáng mượn ba quy ước từ `AGENTS.md`: thứ tự ưu tiên chỉ dẫn, "tra web cho mọi giá trị có phiên bản" và mục AI assistance trong PR template.

**Nguồn §6d:** https://github.com/Homebrew/BrewUI (clone đầy đủ, HEAD 7bc5efa 13/10/2026; README.md, ARCHITECTURE.md, AGENTS.md, Package.swift, .github/workflows/{pr_build_test,release,build}.yml, .github/PULL_REQUEST_TEMPLATE.md, Sources/BrewCrashReporting/, Sources/BrewNetworking/, Tools/BrewUILint/; git log/tag) · trang GitHub và shields 14/10/2026 · https://github.com/Homebrew/BrewUI/releases · https://www.bleepingcomputer.com/news/security/homebrew-700-gets-built-in-gui-better-security-controls/ · https://dev.to/arshtechpro/brewui-a-first-look-at-homebrews-official-macos-gui-3fk2 · https://medium.com/@kanishks772/homebrew-just-got-a-gui-after-10-years-the-terminal-finally-has-a-window-64e73307752b · https://runany.dev/blog/brewui/ · https://www.opensourcealternatives.to/item/brewui · https://github.com/mckaymic/Brewui · https://github.com/milanvarady/Applite · https://github.com/buresdv/Cork · https://github.com/brunophilipe/Cakebrew · https://docs.brew.sh/Analytics

## 6e. Better-Linux/CleanMyLinux — app dọn dẹp Linux desktop (Tauri/Rust), có lỗ leo thang quyền đáng lưu ý (ảnh "4 repos worth bookmarking", 2026-10-18)

> Một trong 4 repo của slide Chris Porter (tác giả `Better-Linux` / PRAS Samin). Đã clone đầy đủ (HEAD `02de64d`, 25/5/2026, v1.0.0-beta.2), đọc README, `app.toml`, policy PolicyKit và mã Rust gọi helper.

| Thuộc tính | Giá trị (18/10/2026) |
|---|---|
| Repo / URL | https://github.com/Better-Linux/CleanMyLinux · slide: 8★/1 fork |
| Mô tả 1 dòng | App desktop "CleanMyMac cho Linux": gỡ ứng dụng an toàn, cập nhật đa trình quản lý gói (APT/Pacman/DNF/Flatpak/Snap), dọn rác, theo dõi app lâu không dùng |
| Loại | devops / desktop tool (GUI) |
| License | **MIT** (© 2026 Better Linux) |
| Stack | **Tauri v2 + Rust + React 19 + Bun**; GUI chạy quyền user thường, tác vụ admin qua **PolicyKit (pkexec)**; có thư mục `ml/` (app_classifier, progress_model) để lọc "app người dùng" khỏi thư viện hệ thống |
| Vì sao đáng tham khảo | • Hiếm có app dọn dẹp Linux desktop có GUI thống nhất nhiều trình quản lý gói; kiến trúc Tauri (Rust core + web UI) gọn.<br>• Có `docs/architecture.md`, CHANGELOG, SECURITY.md, CI, bảng distro/GLIBC hỗ trợ rõ ràng. |
| Hạn chế / rủi ro | • **⚠️ Lỗ leo thang quyền (đọc mã):** policy `config/com.betterlinux.cleanmylinux.policy` đăng ký đích pkexec là `/usr/bin/cleanmylinux-helper`, mà helper (`scripts/cleanmylinux-helper.sh`) chỉ là `exec "$@"`. Mã Rust gọi `pkexec /usr/bin/cleanmylinux-helper sh -c <lệnh>` (`src-tauri/src/system_info/ops.rs`). Đây là **primitive chạy lệnh tùy ý với quyền root**: với `allow_active = auth_self_keep`, sau một lần xác thực mật khẩu được cache, bất kỳ tiến trình nào của user active (kể cả mã độc) đều có thể gọi helper để chạy lệnh root. Một helper "exec mọi thứ" làm mất ý nghĩa của việc giới hạn action PolicyKit.<br>• Mới (beta), một tác giả, 8★; tên "premium" nhưng mã mở MIT.<br>• Binary dựng sẵn cần GLIBC ≥ 2.39. |
| Tích hợp | Nếu dùng/đóng gói: nên thu hẹp helper thành **danh sách lệnh cho phép** (không `exec "$@"`), hoặc tách từng action PolicyKit theo tác vụ, thay vì một đích exec vạn năng. Trước khi cài bản binary, cân nhắc build từ nguồn và đọc lại helper. |
| Liên quan | mục 13 §6d (BrewUI, GUI cho package manager), mục 12 §4 (nguyên tắc: allowlist tham số, review cho hành động quyền cao), mục 11 (sandbox) |
| Nguồn | clone 18/10/2026 (README, app.toml, config/*.policy, scripts/cleanmylinux-helper.sh, src-tauri/src/system_info/{ops,sudo}.rs); slide "4 GitHub repos worth bookmarking" |

## 6f. Case study: thsangyk-oss/sremote — terminal + remote desktop tự host qua Tailscale, không có lớp auth ứng dụng (link người dùng gửi, clone 2026-10-19)

**Kết luận:** một công cụ "mở lại phiên terminal/desktop của máy trạm từ trình duyệt hay điện thoại", gọn và trung thực về phạm vi, hợp để tiếp tục một phiên coding agent đang chạy. Nhưng toàn bộ an toàn **chỉ dựa vào ranh giới mạng Tailscale**: không có mật khẩu, token hay bất kỳ xác thực ứng dụng nào. Ai ở trên cùng tailnet (hoặc localhost) đều có shell toàn quyền, điều khiển chuột/bàn phím và đọc/ghi toàn bộ ổ đĩa của máy host. Cài bằng `irm … | iex` và tự nâng quyền admin. Repo mới, 2★, một phần code do agent Devin viết, chưa có file LICENSE.

### 6f.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 19/10/2026) |
|---|---|
| Repo | `thsangyk-oss/sremote` · **~2★, 2 fork** · 53 commit, 25/9 → 19/10/2026 · tag mới nhất **v1.14.1** (README nói APK kèm v1.11.3) · **không có file LICENSE**; `package.json` ghi `"license":"ISC"`, trường `author` để trống |
| Tác giả | `thsangyk-oss` (16 repo công khai). README có QR **VietQR·MB** "Ủng hộ tác giả cốc cafe mua token" → tác giả Việt Nam **(chưa xác minh danh tính)**. Commit: `thsangyk-oss` 44, **`Devin` (agent AI) 6**, `thsangyk` 3 |
| Là gì | Máy chủ Node (`server.js` 1.091 dòng, cổng 2209; deps `node-pty`, `ws`, `@xterm/*`) + `agent/` (session broker giữ PTY sống trong tiến trình riêng; `screen-pro/ScreenPro.cs` 673 dòng chụp màn hình DXGI trên Windows; tray C#) + `public/` (web UI xterm.js, `app.js` 2.612 dòng) + `android/` (client Java thuần, không AndroidX) |
| Chức năng | Phiên terminal **sống xuyên thiết bị** (PTY sống trong broker, sống sót đóng tab/mất wifi/restart app); remote desktop (chuột, bàn phím, clipboard, đa màn hình, "trackpad mode" cho điện thoại); file explorer toàn máy (upload tới 4 GB, tự zip thư mục, giải nén, xem trước code/ảnh/video); git diff |
| Nền tảng | Host Windows/Linux/macOS; client trình duyệt + app Android |

### 6f.2 Mô hình bảo mật: chỉ có một lớp, là mạng

- **Lớp duy nhất:** `isAllowedRemote()` (server.js) chỉ cho `127.0.0.1`/`::1`, dải Tailscale `100.64.0.0/10` và ULA tailnet `fd7a:115c:a1e0:`; mọi địa chỉ khác bị **403** trước khi vào app, cho cả HTTP và WebSocket. README ghi đúng điều này ("Private by design").
- **Không có lớp thứ hai:** không mật khẩu, không token, không phiên đăng nhập. Khi đã qua được lớp IP, mọi route đều mở. Nghĩa là **bất kỳ thiết bị nào trên cùng tailnet** (hoặc bất kỳ tiến trình nào trên chính máy host, qua localhost) đều: mở shell mới, gõ lệnh vào phiên đang chạy, điều khiển desktop, và duyệt/tải/ghi file bất kỳ đâu trên máy.
- **"Jail" chỉ cho API file, không cho terminal:** các route `/api/files|file|fileop` có kiểm `jail()` chặn ra ngoài thư mục gốc (403 "outside jail"), nhưng terminal là shell đầy đủ nên giới hạn này không áng gì với người đã vào được.
- **Máy chủ `listen(PORT, "0.0.0.0")`:** lắng nghe trên mọi interface rồi lọc bằng IP ở tầng ứng dụng. An toàn chỉ còn đúng khi (a) Tailscale ACL thực sự giới hạn ai vào được tailnet, và (b) không có ai/cái gì không tin cậy chạy trên chính máy host. README có hướng dẫn thêm firewall giới hạn cổng 2209 vào riêng interface Tailscale — nên làm, vì nó là lớp phòng thủ thứ hai mà mặc định không có.

Đây **không phải lỗ hổng giấu kín** — mô hình "tin toàn bộ tailnet" là lựa chọn thiết kế, và README nói rõ chỉ tailnet vào được. Điều cần người đọc kho nắm: tailnet của bạn thường gồm nhiều thiết bị, và Tailscale cho phép chia sẻ node cho người khác; trên sremote, mọi nút được chia sẻ đều ngang bằng chủ máy. Không có "chế độ chỉ xem" hay phân quyền.

### 6f.3 Cài đặt và quyền

- **`irm … | iex`:** cách cài khuyến nghị là tải `install.ps1` từ `raw.githubusercontent.com` rồi chạy thẳng (`fix-state.ps1`, `elevate.ps1` cũng vậy). Đây là mẫu "chạy script từ xa không kiểm" — rủi ro chuỗi cung ứng như mọi `curl|sh`/`irm|iex`: tin tưởng repo + CDN tại thời điểm chạy. Nên tải script về đọc rồi mới chạy.
- **Tự nâng quyền admin:** cài từ shell elevated thì tác vụ autostart tự elevate, và **mọi phiên terminal kế thừa token admin** của chuỗi task → tray → server → PTY (README mục elevate). Đặt `$env:SREMOTE_LIMITED=1` để không elevate. Hệ quả: nếu đã bật, một phiên mở từ điện thoại là shell admin.
- Cài sẵn rule firewall qua `install.bat`/installer elevated.

### 6f.4 So với lựa chọn cùng loại

| | sremote | ttyd | sshx | wetty |
|---|---|---|---|---|
| Bản chất | Terminal + remote desktop + file, phiên bền, app phone | Chia sẻ 1 terminal qua web, 1 binary C | Terminal cộng tác, hạ tầng tác giả | SSH client trong trình duyệt |
| License | **chưa có file** (package.json ghi ISC) | MIT | — | MIT |
| Auth ứng dụng | **Không** (chỉ lọc IP tailnet) | Basic Auth tùy chọn (`-c user:pass`), ghi mặc định tắt | Link bí mật/khóa | Tùy chọn, + proxy |
| Phiên sống sau mất kết nối | Có (PTY trong broker) | Không | Có | Không (là SSH) |
| Điểm mạnh riêng | Remote desktop + file + app Android trong một | Nhẹ, chín, có auth | Cộng tác nhiều người | Dựa trên SSH sẵn có |

sremote thêm nhiều thứ ttyd không có (phiên bền, desktop, file, app phone), nhưng **bỏ hẳn lớp auth ứng dụng** mà ttyd có tùy chọn. Với ai chỉ cần terminal web có mật khẩu, ttyd + Tailscale vẫn an toàn hơn theo lớp.

### 6f.5 Dùng thế nào

- **Hợp khi:** một người, một tailnet riêng chỉ gồm thiết bị của chính mình, muốn tiếp tục phiên build/dev/coding-agent từ điện thoại. Đúng ca dùng README mô tả.
- **Không nên:** đặt trên tailnet chia sẻ nhiều người; dựa vào sremote như lớp an toàn khi host chạy cả tiến trình không tin cậy (localhost luôn vào được); để chế độ elevate nếu không cần shell admin.
- **Nếu dùng, tối thiểu:** thêm firewall giới hạn cổng 2209 vào riêng interface Tailscale (README có lệnh); siết Tailscale ACL để chỉ thiết bị của bạn thấy được node; đọc `install.ps1` trước khi `iex`; cân nhắc `SREMOTE_LIMITED=1`.
- **Trưởng thành:** repo 2★, 3 tuần tuổi, một phần do agent viết, chưa có LICENSE (dùng lại/nhúng chưa có cơ sở pháp lý rõ). Xem là công cụ cá nhân đang phát triển, không phải sản phẩm đã kiểm.

**Nguồn §6f:** https://github.com/thsangyk-oss/sremote (clone đầy đủ, 53 commit, HEAD `ce9e17c` 19/10/2026, tag v1.14.1; đọc README.md, AGENTS.md, package.json, server.js (`isAllowedRemote`, các route `/api/*`, `listen`), install.ps1, elevate.ps1, agent/screen-pro/ScreenPro.cs, public/app.js; không có file LICENSE) · https://github.com/thsangyk-oss (16 repo) · ttyd: github.com/tsl0922/ttyd (MIT) · besthub.dev/articles/three-open-source-web-terminal-tools · selfhostyourself.com/tags/ssh-client-web

## 6g. Nâng cấp 31/10/2026: rà repo lớn

> Cách làm: 7 truy vấn GitHub search (repo >40k★ theo TypeScript/Go/Rust push sau 1/9/2026, `code review ai`, `spec-driven development`, `devops agent kubernetes`, topic `developer-tools` tạo sau 1/10/2025), lọc bỏ repo đã có trong `data/projects.json`, chọn 7 repo. Repo lớn (Bun, Supabase, Tauri, act, PocketBase) clone `--filter=tree:0` và chỉ đọc file đích; repo nhỏ clone `--filter=blob:none`. **Không cài, không chạy gì.** Số sao từ GitHub search API ngày 31/10/2026.

### 6g.1 Trạng thái repo cũ của mục

| Repo | Thay đổi | Hệ quả |
|---|---|---|
| `vuejs/core` | Catalog từng ghi **~208k★ là lỗi dữ liệu**; số thật **54,9k** (GitHub API 31/10/2026) | Đã sửa bảng §1. Vue vẫn là framework lớn, nhưng không lớn hơn React |
| `withastro/astro` | 45,5k → **63,6k★**; GitHub báo license NOASSERTION (file vẫn MIT theo lần đọc trước, chưa đọc lại) | Sửa bảng §1 |
| `qodo-ai/pr-agent` | Repo nay ở **`The-PR-Agent/pr-agent`** (13,8k★, commit 31/10/2026). README: Qodo đã **tặng dự án cho cộng đồng**, "not the Qodo offering"; file LICENSE hiện là **MIT** (©2026 The PR Agent), catalog đang ghi AGPL-3.0 | Sửa link; catalog cần đổi license thành MIT. Qodo Merge thương mại nay là "Qodo 2.0" |
| `vercel/next.js`, `angular/angular`, `sveltejs/svelte`, `nuxt/nuxt` | Bảng §1 ghi số cũ; nay 143k · 101k · 88,5k · 61k★ | Thứ tự không đổi |
| `hashicorp/terraform`, `bmad-code-org/BMAD-METHOD`, `JetBrains/kotlin` | GitHub báo NOASSERTION/không nhận license | Giữ license đã đọc trong file (Terraform BUSL-1.1) |

### 6g.2 Bảng nhanh 7 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `supabase/supabase` | Backend (BaaS) | 114,4k · Apache-2.0 | 31/10/2026 | Postgres + Auth + Storage + Realtime + Studio, tự host bằng Docker | `.env.example` chứa secret mẫu |
| `tauri-apps/tauri` | Desktop/mobile | 112,4k · MIT/Apache-2.0 | 31/10/2026 | App desktop/mobile nhỏ nhẹ với frontend web + lõi Rust | v3 đang alpha |
| `oven-sh/bun` | Runtime JS | 96,5k · MIT + LGPL tĩnh (GitHub: NOASSERTION) | 31/10/2026 | Runtime, bundler, test runner, package manager | **Đã viết lại bằng Rust (5/2026)**, thuộc Anthropic |
| `nektos/act` | DevOps/CI | 72,5k · MIT | 31/10/2026 | Chạy GitHub Actions cục bộ trong Docker | **5 lỗ Critical thoát container**, vá trong v0.2.94 |
| `pocketbase/pocketbase` | Backend 1 file | 61,6k · MIT | 26/10/2026 | Backend Go: SQLite, auth, file, realtime, admin UI | **Archive, rời GitHub** |
| `tirth8205/code-review-graph` | AI code review | 32,5k · MIT | 15/10/2026 | Đồ thị mã Tree-sitter trong SQLite, cấp "blast radius" qua MCP | Cài ghi cấu hình vào ~20 công cụ |
| `buildermethods/agent-os` | Spec-driven | 5,6k · MIT | 7/10/2026 | Lệnh/prompt để rút chuẩn mã từ codebase và viết spec | 22 file, docs ở web riêng |

### 6g.3 Hồ sơ từng repo

- **Bun.** Anthropic mua Bun 2/12/2025 (theo tin báo chí). Git log có commit **"Rewrite Bun in Rust (#30412)" của Jarred Sumner ngày 14/5/2026**; báo chí nói phần lớn do Claude viết trong ~11 ngày, nhà sáng lập Zig chê là "unreviewed" (các con số dòng mã, chi phí **chưa xác minh**). Tag `bun-v1.4.0` ngày 19/8/2026, mới nhất `bun-v1.4.4` (22/10). `CLAUDE.md` nay ghi "written primarily in Rust with C++"; 729 commit (3,9%) có trailer Claude, bot `robobun` 3.091 commit. `LICENSE.md`: Bun là MIT nhưng **link tĩnh JavaScriptCore/WebKit (LGPL-2)** và tinycc (LGPL-2.1), nên GitHub báo NOASSERTION; phân phối binary Bun phải tôn trọng điều khoản relink của LGPL. Crate `src/analytics` tôn trọng `DO_NOT_TRACK`. Cài: `npm install -g bun` hoặc `curl -fsSL https://bun.com/install | bash`. Với dự án dùng Bun làm runtime production: theo dõi độ ổn định sau đợt viết lại.
- **act.** `SECURITY_AUDIT.md` (10/2026) công khai kết quả audit: **5 lỗi Critical** (GHSA-7x4h, -v5hg, -hf9j, -3m58, -45wq) cho phép workflow qua `container.options`/`volumes:` bỏ CapDrop/seccomp, mount thư mục host, đọc file host, dùng PID/IPC host; thêm path traversal ở `uses:` và `.actrc` của project ghi đè hardening. Bản vá thêm chính sách `--container-options-policy` và allowlist `.actrc` (cờ có trong `cmd/root.go` ở HEAD = tag v0.2.94, 31/10/2026). Hệ quả: **chạy `act` trên repo lạ trước v0.2.94 tương đương chạy mã không tin cậy trên host**. Đáng chú ý: 61 commit từ 8/2026 có tác giả "Cursor Agent". Cài: `brew install act`; checksum ở `checksums.txt` của release.
- **PocketBase.** Commit cuối 26/10/2026 thêm dòng "The repo has moved to https://ganigeorgiev.com/pocketbase/pocketbase", repo đã archive. CHANGELOG v0.40.6: lệnh `update` từ nay tải bản mới từ `ganigeorgiev.com` "(there is nothing there yet)". 2.514/2.570 commit của một người. ⚠️ Kênh cập nhật chuyển từ GitHub Releases sang domain cá nhân: ghim phiên bản, kiểm checksum, đừng bật tự cập nhật. `go.mod` vẫn là `github.com/pocketbase/pocketbase`, đường import tương lai **chưa xác minh**.
- **Supabase.** 39.562 commit, 2.156 tác giả. Self-host qua `docker/` với tag riêng `self-hosted/v*` (mới nhất v0.8.3, 16/10/2026) và nhiều biến thể compose (Kong, Envoy, Caddy, Nginx, PG15/17). ✅ `docker/setup.sh` **tự sinh secret và khoá API bất đối xứng**. ⚠️ `docker/.env.example` vẫn chứa `JWT_SECRET`, `DASHBOARD_PASSWORD=this_password_is_insecure…`, `SECRET_KEY_BASE` mẫu: nếu copy thẳng file này thì instance dùng secret công khai. `.mcp.json` ở gốc trỏ tới MCP hosted `mcp.supabase.com`. Có `AGENTS.md`/`CLAUDE.md`, zizmor cho workflow.
- **Tauri.** 6.391 commit, 634 tác giả, dual license MIT/Apache-2.0 (có `LICENSE.spdx`). Bản ổn định v2.12.5 (21/10/2026); **v3 đang alpha** (alpha đầu 12/9, alpha.5 ngày 14/10). `SECURITY.md` yêu cầu báo lỗi qua private advisory. Gần như không có commit AI (2 trailer). Là lựa chọn nhẹ hơn Electron khi agent cần dựng app desktop (BrewUI §6d, CleanMyLinux §6e đã dùng).
- **code-review-graph.** Python, 1.270 commit từ 26/2/2026, 885 của một người, **35% có trailer Claude**. Tree-sitter → đồ thị node/edge trong SQLite, trả "blast radius" và tập file tối thiểu cần review qua MCP; có GitHub Action và extension VS Code. ⚠️ "65× ít token hơn" so token của cả codebase với token của một câu trả lời đồ thị, không đo chất lượng review. ⚠️ `code-review-graph install` tự dò và **ghi MCP entry, hook, skill vào file rules của tới ~20 công cụ** (Claude Code, Cursor, Codex…); có `uninstall --dry-run`. Cài: `pipx install code-review-graph`, rồi `install --platform claude-code` để chỉ đụng một công cụ.
- **Agent OS.** Chỉ 22 file: lệnh trong `commands/agent-os`, `profiles/`, 3 script bash cài vào project. Bốn bước: rút chuẩn từ codebase, tiêm chuẩn theo việc, shape spec, đánh chỉ mục. Tài liệu và cách cài nằm ở buildermethods.com (kèm gói Pro trả phí). 110/132 commit của một người, v3.0.0 (20/1/2026). Nhẹ hơn spec-kit/OpenSpec (§5), hợp khi chỉ cần "standards file" cho agent.

### 6g.4 Mẫu chung rút ra

1. **Hạ tầng dev cốt lõi đang được viết bởi agent**: Bun viết lại bằng Rust phần lớn nhờ Claude, act nhận vá bảo mật từ "Cursor Agent", code-review-graph 35% commit có trailer Claude. Khi chọn dependency, xem thêm tỉ lệ commit agent và mức review.
2. **Audit công khai trong repo** (act `SECURITY_AUDIT.md`: công cụ quét, GHSA, commit vá, mặc định an toàn và cách tắt) là mẫu đáng chép cho template.
3. **Kênh phân phối có thể đổi chủ**: PocketBase rời GitHub sang domain cá nhân, PR-Agent đổi org và license, Daytona (mục 11 §3c.1) đóng mã. Ghim phiên bản và nguồn tải.
4. **File mẫu chứa secret** (Supabase `.env.example`) vẫn phổ biến; script sinh secret phải là đường mặc định.
5. **Số catalog phải đọc từ API, không chép bài tổng hợp**: lỗi Vue ~208k đã nằm cả trong README §1 lẫn catalog.

**Nguồn §6g:** GitHub search API 31/10/2026 (7 truy vấn; `pr-agent in:name`) · `../meta_all.json`, `status_all.json` (GitHub API 31/10) · clone `--filter=tree:0`: bun (LICENSE.md, README.md, CLAUDE.md, src/analytics/lib.rs, git log #30412, tag bun-v1.4.0), act (README.md, SECURITY_AUDIT.md, VERIFICATION, cmd/root.go, tag v0.2.94), pocketbase (README.md, CHANGELOG.md, go.mod, LICENSE.md, commit 7f2773e), supabase (LICENSE, .mcp.json, docker/{.env.example, setup.sh}), tauri (SECURITY.md, LICENSE.spdx, tag tauri-v2.12.5/v3.0.0-alpha.5) · clone `--filter=blob:none`: code-review-graph (LICENSE, README.md, docs/, code_review_graph/), agent-os (LICENSE, README.md, scripts/, commands/), The-PR-Agent/pr-agent (LICENSE, README.md) · Web: simonwillison.net/2026/jul/8/rewriting-bun-in-rust, devclass.com/devops/2026/07/15/zig-creator-calls-buns-claude-rust-rewrite-unreviewed-slop, i-programmer.info (Bun 1.4) — báo chí/blog · https://github.com/oven-sh/bun · https://github.com/nektos/act · https://github.com/pocketbase/pocketbase · https://github.com/supabase/supabase · https://github.com/tauri-apps/tauri · https://github.com/tirth8205/code-review-graph · https://github.com/buildermethods/agent-os · https://github.com/The-PR-Agent/pr-agent

## 6h. Nâng trần 2/11/2026: chuẩn SLSA, lint bảo mật GitHub Actions, quét lỗ hổng theo SBOM và giám sát runner (yêu cầu người dùng)

> Cách làm: grep `data/projects.json` theo `repo` (Renovate, pre-commit, Dagger ở mục này; syft, gitleaks, trufflehog, osv-scanner, Trivy, cosign, Scorecard ở mục 12 nên không thêm); GitHub search API 2/11/2026; clone `--depth 1 --filter=blob:none`, đọc LICENSE, README, docs, danh sách audit, `action.yml`. **Không cài, không chạy.**

**Trần hiện tại:**

- §4b/§4c có quality gate cho **mã** (lint, type, mutation, Lighthouse) và vài mẩu supply chain (pin SHA, hash-locked tool, syft, gitleaks); thiếu **chuẩn đích** để biết "đủ" là mức nào.
- **Chính file workflow CI không được lint bảo mật**: chưa có công cụ bắt template injection, `pull_request_target` nguy hiểm, quyền `GITHUB_TOKEN` thừa, Action không pin. Vụ Trivy (mục 12 §3d) và act (§6g) cho thấy CI là bề mặt tấn công chính.
- Có SBOM (syft) nhưng chưa có bước **quét SBOM đó** và chưa có **giám sát lúc runner chạy** (egress, file bị sửa).

| Repo / chuẩn | Lớp | ★ · license (2/11/2026) | Commit cuối | Vì sao nâng trần | Rủi ro |
|---|---|---|---|---|---|
| `slsa-framework/slsa` | Chuẩn | 2,0k · Community Specification License 1.0 (GitHub: NOASSERTION) | 28/10/2026 | Đặc tả SLSA của OpenSSF. **v1.2 được duyệt 24/11/2025** (`www/_data/versions.yml`: `current: v1.2`, blog announce-slsa-v1.2), gồm Build track và **Source track** mới; bản nháp đang làm thêm Dependency track, Build Environment track, "Verified Properties". Cho đích đo được: Build L1 (có provenance) → L2 (nền tảng ký) → L3 (build cách ly) | Là đặc tả, cần công cụ khác để đạt (GitHub artifact attestations, slsa-github-generator, cosign). Các track mới ngoài Build/Source còn ở bản nháp |
| `zizmorcore/zizmor` | Cổng máy | 6,9k · MIT | 2/11/2026 | Phân tích tĩnh bảo mật GitHub Actions, viết bằng Rust; 41 audit (`template-injection`, `dangerous-triggers`, `excessive-permissions`, `unpinned-uses`, `impostor-commit`, `cache-poisoning`, `known-vulnerable-actions`, `dependabot-cooldown`…); chế độ offline/online, xuất SARIF để hiện trên Code Scanning. Giskard và Supabase đã dùng (mục 07, §6g) | Bản 1.31.1, nhánh chính đang 1.32.0-rc; audit online cần `GH_TOKEN`. Chỉ cho GitHub Actions |
| `rhysd/actionlint` | Cổng máy | 4,4k · MIT | 19/4/2026 (push 16/7) | Lint **đúng cú pháp/kiểu** cho workflow: kiểm kiểu biểu thức `${{ }}`, gọi shellcheck và pyflakes cho `run:`, cảnh báo input không tin cậy dùng thẳng trong script. Bổ sung cho zizmor (zizmor thiên về bảo mật) | Nhịp chậm lại (commit cuối 4/2026); một người bảo trì chính |
| `anchore/grype` | Cổng máy | 13,2k · Apache-2.0 | 30/10/2026 | Quét lỗ hổng cho image, filesystem và **SBOM của syft** (`grype sbom:./sbom.json`); xếp ưu tiên theo **EPSS, KEV**, lọc bằng OpenVEX. Ghép thẳng với syft đã có ở §4b | Trùng phần lớn với osv-scanner/Trivy (mục 12); chọn một làm cổng chính để tránh nhiễu |
| `step-security/harden-runner` | Cổng máy (runtime) | 1,3k · Apache-2.0 | 27/10/2026 | Agent giám sát runner GitHub Actions: ghi egress, file bị sửa, process; chế độ `egress-policy: block` với allowlist domain. README liệt kê vụ đã bắt được: tj-actions/changed-files (CVE-2025-30066), Trivy v0.69.4, axios npm, nx. Mã action kiểm checksum agent (`src/checksum.ts`) | **Bản free chỉ cho repo public trên runner GitHub-hosted**; repo private hay self-hosted phải trả phí. Gửi telemetry về API StepSecurity, chỉ tắt được (`disable-telemetry`) khi đã ở chế độ block |

**Stack nâng trần** (lợi ích/công sức giảm dần):

1. **Lint workflow ở mọi PR:** `actionlint` (đúng) + `zizmor --format=sarif` (an toàn) làm required check trong job `quality-gate` của §4b; sửa theo audit `unpinned-uses` khớp luôn quy tắc "Action pin SHA" đã có.
2. **Quyền tối thiểu cho CI:** `permissions: {}` ở đầu workflow, mở theo job; bỏ `pull_request_target` có checkout mã PR. zizmor `excessive-permissions`/`dangerous-triggers` giữ quy tắc này khỏi trôi.
3. **SBOM → quét → chặn:** syft sinh SBOM (§4b) → `grype sbom:` với ngưỡng mức nghiêm trọng, ưu tiên mục có KEV/EPSS cao; Renovate (§4c) mở PR vá, đặt độ trễ để tránh bản độc vừa phát hành (zizmor có audit `dependabot-cooldown` cho Dependabot).
4. **Đặt đích SLSA:** tối thiểu Build L2 (provenance do nền tảng ký, vd. GitHub artifact attestations hoặc cosign mục 12 §3d), đích L3 cho artifact phát hành; theo Source track v1.2 thì rulesets-as-code (§4b) là bằng chứng phía mã nguồn.
5. **Giám sát runner:** repo public dùng harden-runner `egress-policy: audit` vài tuần rồi chuyển `block`; repo private cân nhắc chi phí hoặc tự giới hạn egress ở runner self-hosted. Chấm lại tổng thể bằng OpenSSF Scorecard (mục 12 §3d).

**Nguồn §6h:** GitHub search API 2/11/2026 (`repo:` gộp) · `data/projects.json` (grep `repo`) · clone `--depth 1 --filter=blob:none`: slsa-framework/slsa (HEAD 4d3f9d4, 28/10/2026; LICENSE.md, `spec/whats-new.md`, `spec/` danh sách track, `www/_data/versions.yml`, `www/_posts/`), zizmorcore/zizmor (HEAD fbf8d0c, 2/11/2026; LICENSE, Cargo.toml, `docs/{usage,release-notes}.md`, `crates/zizmor/src/audit/`), rhysd/actionlint (HEAD 011a6d1, 19/4/2026; LICENSE.txt, README.md), anchore/grype (HEAD cb4a51d, 30/10/2026; LICENSE, README.md), step-security/harden-runner (HEAD 46b06ce, 27/10/2026; LICENSE, README.md, action.yml, `src/checksum.ts`, `src/bravo-config.ts`) · https://github.com/slsa-framework/slsa · https://slsa.dev/spec/v1.2/ · https://github.com/zizmorcore/zizmor · https://github.com/rhysd/actionlint · https://github.com/anchore/grype · https://github.com/step-security/harden-runner

## 6i. Nâng trần toàn diện 2/11/2026: môi trường dev, build và release tái lập

> Metadata GitHub đọc 2/11/2026, ba repo chưa archive; clone nông và đọc LICENSE, CI, lock/config và implementation. **Chỉ đọc mã, không cài Nix/devenv, không build, không phát hành.** Phân biệt môi trường khai báo, artifact tái lập và provenance có chữ ký: ba loại bằng chứng bổ sung nhau.

**Trần hiện tại:** §4c có quality gates/toolchain, §6g có Dagger, §6h có SLSA/scan/runner hardening. Chưa có hồ sơ đủ sâu về môi trường dev ghim đầu vào và pipeline đưa *đúng artifact đã kiểm* tới người dùng. [Định nghĩa Reproducible Builds](https://reproducible-builds.org/docs/definition/) yêu cầu tạo lại artifact giống từng bit dưới điều kiện đã công bố; có lockfile hoặc provenance chưa tự chứng minh điều đó.

| Dự án | ★ · license (đọc 2/11/2026) | HEAD / ngày commit | Lớp và điều kiện dùng |
|---|---|---|---|
| [Nix](https://github.com/NixOS/nix) | 17,960 · LGPL-2.1 | `b64c28c2134f` · 2026-11-02 | Package/build manager Unix; pin inputs và sandbox, vẫn cần build lại so hash để chứng minh tái lập |
| [devenv](https://github.com/cachix/devenv) | 7,794 · Apache-2.0 | `0d6c556e5f86` · 2026-10-28 | Môi trường dev khai báo trên Nix với lock/packages/services/tests; không tự cách ly tác dụng phụ service |
| [GoReleaser](https://github.com/goreleaser/goreleaser) | 16,131 · MIT | `3d5c3a2efe15` · 2026-11-01 | Release pipeline đa nền tảng; phân biệt bản OSS và Pro trong chính cấu hình upstream |

### Nix

Package/build manager của cộng đồng Nix, LGPL v2.1 theo [COPYING](https://github.com/NixOS/nix/blob/b64c28c2134f5b6e4900e423ec281a2985e57086/COPYING). Inputs/derivation và store giúp ghim toolchain, chia sẻ cache và build trong môi trường kiểm soát. [Build command](https://github.com/NixOS/nix/blob/b64c28c2134f5b6e4900e423ec281a2985e57086/src/nix/build.cc) có `--rebuild` đi qua `bmCheck`; [Build goal](https://github.com/NixOS/nix/blob/b64c28c2134f5b6e4900e423ec281a2985e57086/src/libstore/build/derivation-building-goal.cc) có đường kiểm output đã tồn tại. Khi cần chứng minh tái lập, buộc build lại và đối chiếu output, không chỉ tải lại cùng binary cache. Cần ghim Nix/nixpkgs/input lock, platform, flags và trạng thái sandbox. Timestamp, đường dẫn, mạng, CPU/tool nondeterminism vẫn có thể làm output khác; Nix không bảo đảm mọi package tái lập. Không cần chuyển cả hệ điều hành sang NixOS để dùng Nix; Linux/macOS có khác biệt sandbox, Windows thường qua WSL.

### devenv

Lớp khai báo môi trường dev trên Nix của Cachix: package/ngôn ngữ, service, task và hook trong cấu hình, dependency pin ở lock. [Test module](https://github.com/cachix/devenv/blob/0d6c556e5f862c14a75a543e2ee4fdb7acc005ad/src/modules/tests.nix) nối `enterTest` với lifecycle/readiness của process; [CI test](https://github.com/cachix/devenv/blob/0d6c556e5f862c14a75a543e2ee4fdb7acc005ad/.github/workflows/test.yml) thực sự gọi `devenv test`. Giá trị là dùng cùng định nghĩa dev/CI, so với Dagger thiên pipeline container. Shell hook và service vẫn chạy mã, DB state/secret vẫn phải quản lý riêng; lock không làm database fixture bất biến. Với nhiều agent/worktree, tách cổng/service data và định danh môi trường trước khi chạy song song. Các tính năng giao diện/cloud không phải điều kiện để dùng bản Apache-2.0 này.

### GoReleaser

Release engineering đa nền tảng, mã trong repo MIT; có bản Pro thương mại. [Cấu hình tự phát hành](https://github.com/goreleaser/goreleaser/blob/3d5c3a2efe1544b8f7d24a8c2ed10dab45b89a61/.goreleaser.yaml) mở bằng `pro: true`, nên sao chép toàn bộ file không bảo đảm chạy với bản OSS. Trong cấu hình có `-trimpath`, timestamp theo commit, checksum/SBOM/signing; [Checksum pipe](https://github.com/goreleaser/goreleaser/blob/3d5c3a2efe1544b8f7d24a8c2ed10dab45b89a61/internal/pipe/checksums/checksums.go) triển khai băm và sắp thứ tự danh sách. [Release verification](https://github.com/goreleaser/goreleaser/blob/3d5c3a2efe1544b8f7d24a8c2ed10dab45b89a61/.github/workflows/release.yml) tải artifact, kiểm checksum, cosign identity/issuer và GitHub attestation: đây là mẫu kiểm ở phía người nhận đáng học. Dùng GoReleaser đóng gói binary đã qua kiểm, ghim edition/version và tách quyền build với publish. Phải tự kiểm artifact đa kiến trúc/installer; chữ ký đúng không chứng minh ứng dụng đúng hay build tái lập.

**Kiến trúc tham khảo:** source commit + input lock → môi trường Nix/devenv hoặc Dagger hiện có → lint/test/eval → build candidate → rebuild độc lập → so artifact → SBOM/provenance/signature → publish chính candidate ấy. Khi signing/notarization tạo byte biến động, công bố rõ artifact được so và lớp ký ngoài thay vì tuyên bố cả gói giống bit. Devcontainer/container có thể là lựa chọn đủ dùng nếu team chỉ cần môi trường đồng nhất; Nix phù hợp khi cần biểu diễn/ghim dependency sâu hơn.

| Cổng tại dự án tích hợp | Đạt khi | Không thay được bởi |
|---|---|---|
| Môi trường dev/CI | Checkout mới vào môi trường đã ghim, cùng lệnh kiểm chạy được | README ghi “works on my machine” |
| Input closure | Toolchain, dependency, image và nguồn tải đều có phiên bản/hash; thay lock được review | Chỉ ghim package manager |
| Tái lập artifact | Hai build sạch có cùng điều kiện công bố cho cùng hash; khác thì giữ diff/báo cáo | Hai lần tải cùng cache |
| Nguồn gốc artifact | Verify chữ ký/issuer/identity/source commit ở phía nhận | Chỉ sinh provenance rồi không kiểm |
| Phát hành | Hash artifact kiểm thử khớp artifact phát hành; rollback/version có kiểm | Rebuild lại lúc publish mà không đối chiếu |

**Đối chiếu ba cột:** đã có và sâu hơn: gate mã/supply chain (§4c/§6h); đã có nhưng mỏng hơn: môi trường dev nhất quán và liên kết build–release; mới: hồ sơ Nix/devenv/GoReleaser với cổng tái lập và xác minh phía nhận. Không khuyến nghị dùng cùng lúc mọi build system; chọn một đường có bằng chứng và chi phí vận hành phù hợp.

**Nguồn §6i:** [CI Nix](https://github.com/NixOS/nix/blob/b64c28c2134f5b6e4900e423ec281a2985e57086/.github/workflows/ci.yml); [devenv LICENSE](https://github.com/cachix/devenv/blob/0d6c556e5f862c14a75a543e2ee4fdb7acc005ad/LICENSE), [devenv lock](https://github.com/cachix/devenv/blob/0d6c556e5f862c14a75a543e2ee4fdb7acc005ad/devenv.lock); [GoReleaser LICENSE](https://github.com/goreleaser/goreleaser/blob/3d5c3a2efe1544b8f7d24a8c2ed10dab45b89a61/LICENSE.md), [GoReleaser build CI](https://github.com/goreleaser/goreleaser/blob/3d5c3a2efe1544b8f7d24a8c2ed10dab45b89a61/.github/workflows/build.yml); [Nix how it works](https://nixos.org/guides/how-nix-works/), [devenv basics](https://devenv.sh/basics/), [GoReleaser Go build](https://goreleaser.com/customization/builds/builders/go/), [định nghĩa tái lập](https://reproducible-builds.org/docs/definition/).

## 6j. Nâng sâu 4/11/2026: hợp đồng toolchain và lệnh chuẩn của xưởng

**Trần hiện tại:** mục này đã có môi trường tái lập, IaC, release và lint. Lớp còn thiếu là cách cùng một repository chỉ ra toolchain và lệnh chuẩn cho người, IDE, coding agent và CI; cập nhật môi trường phải đi qua diff review được. Triển khai nền tảng/rollback xem [mục 32](../32-platform-delivery-engineering/README.md), còn chứng thực build xem [mục 31](../31-software-supply-chain-security/README.md).

<a id="factory-2026-11-04-mise"></a>

### mise: khóa toolchain, không thay lockfile dependency của ứng dụng

| Thuộc tính | Kết quả đọc |
|---|---|
| Repo · license · SHA | `jdx/mise` · MIT · `02d59ef93faf219319cccac23249501e8763e2da` |
| Cơ chế đã đọc | `mise.toml` khai báo tools/tasks/env; `mise lock` ghi version cùng URL/checksum khi backend cung cấp; `mise install --locked` yêu cầu dùng dữ liệu lock theo phạm vi cấu hình |
| Đường gọi | `src/cli/install.rs` truyền `ResolveOptions.use_locked_version` và trạng thái `Settings.locked`; `src/cli/lock.rs` có trust check và từ chối khóa phiên bản không xác minh được khi truy vấn version thất bại |
| Ranh giới | Lock tool không khóa package của app: vẫn giữ npm/uv/Cargo lock. Download checksum còn phụ thuộc backend/platform; lock có version nhưng thiếu digest không đồng nghĩa byte-for-byte reproducible |
| Cấu hình thực thi | Template `exec`, hook, env directives và postinstall có thể chạy mã. Trust là quyết định cho phép config, không phải sandbox hay kiểm duyệt tool upstream; phải review trước khi trust |
| CI | `test.yml` tách luồng trusted/untrusted rồi gọi `test-impl.yml`; không suy việc này thành mọi task của người dùng được cách ly |

**Phạm vi kiểm (2026-11-04):** đọc tài liệu, LICENSE, mã đường gọi và workflow tại SHA dưới đây; không cài/chạy upstream. Các cổng nghiệm thu là đề xuất cho repo tích hợp, chưa phải kết quả chạy của kho. Số sao không thu thập trong đợt này.

| Lựa chọn | Giá trị chính | Chọn khi |
|---|---|---|
| mise | Tool versions + task/env ở nhiều hệ sinh thái | Đội cần điểm vào gọn cho runtime/linter/codegen; kiểm đủ platform và backend |
| Nix | Mô tả build/dev shell và store theo đầu vào | Cần khóa cả dependency hệ thống và chấp nhận học mô hình Nix; đánh giá impurity/network riêng |
| devenv | Trải nghiệm môi trường dev dựa trên Nix | Cần dịch vụ dev và shell tiện dụng trên nền Nix |
| Dev Containers | Cấu hình môi trường IDE/container | Cần host/IDE thống nhất; image/features vẫn phải pin và kiểm provenance |

**Stack cho xưởng:** khóa bootstrap của tool manager → review `mise.toml` và task graph → tạo lock cho từng platform dùng thật → install locked → cài dependency app bằng frozen lock → chạy cùng task lint/test/build ở local và CI. Tách task cần secret khỏi PR không tin cậy; ghi tool versions, lock digest và target vào báo cáo.

**Cổng nghiệm thu:** máy sạch và runner mới chạy cùng entrypoint cho kết quả chức năng tương đương; lock không đủ platform/backend phải làm fail rõ thay vì âm thầm chọn latest. Thử thay cấu hình, artifact digest và quyền mạng để chứng minh cổng phát hiện sai lệch. Build thành công chỉ là một lớp; kiểm test count, artifact checksum, SBOM và deployment smoke ở các mục 30–32. Cache hit không được bỏ qua xác minh input.

**Nguồn §6j:** [LICENSE](https://github.com/jdx/mise/blob/02d59ef93faf219319cccac23249501e8763e2da/LICENSE) · [lock contract](https://github.com/jdx/mise/blob/02d59ef93faf219319cccac23249501e8763e2da/docs/dev-tools/mise-lock.md) · [trust/security](https://github.com/jdx/mise/blob/02d59ef93faf219319cccac23249501e8763e2da/docs/security.md) · [install callsite](https://github.com/jdx/mise/blob/02d59ef93faf219319cccac23249501e8763e2da/src/cli/install.rs) · [lock implementation](https://github.com/jdx/mise/blob/02d59ef93faf219319cccac23249501e8763e2da/src/cli/lock.rs) · [CI](https://github.com/jdx/mise/blob/02d59ef93faf219319cccac23249501e8763e2da/.github/workflows/test.yml).

## 7. Nguồn

- Mục 23 (19 repo của chủ kho, đọc 2026-10-12) · https://github.com/alibaba/open-code-review · https://github.com/googleapis/release-please · https://github.com/oxc-project/oxc · https://github.com/webpro-nl/knip · https://github.com/kucherenko/jscpd · https://github.com/astral-sh/uv · https://github.com/astral-sh/ruff
- https://www.solutelabs.com/blog/top-frontend-web-frameworks · https://www.intuz.com/best-frontend-frameworks/ · https://findarepo.com/categories/web-frameworks/ · https://wasp.sh/resources/2026/02/24/best-frameworks-web-dev-2026 · https://github.com/vanodevium/node-framework-stars · https://encore.dev/articles/best-typescript-backend-frameworks · https://www.hirenodejs.com/blog/nodejs-frameworks-compared-2026 · https://rankingdevs.com/best-backend-tools
- https://www.javacodegeeks.com/2026/02/kotlin-multiplatform-vs-flutter-vs-react-native-the-2026-cross-platform-reality.html · https://www.drizz.dev/post/cross-platform-mobile-development · https://mobisoftinfotech.com/resources/blog/cross-platform-app-development-flutter-vs-react-native-vs-native-apps
- https://spacelift.io/blog/gitops-tools · https://www.pulumi.com/blog/best-kubernetes-iac-tools-2026/ · https://www.qovery.com/blog/best-devops-automation-tools · https://oghabi.it/en-us/blog/devops-2026-trends-overview/ · https://medium.com/@h.stoychev87/devops-cloud-platform-tools-by-category-for-2026-68ed92103c17
- https://www.augmentcode.com/tools/best-spec-driven-development-tools · https://reenbit.com/bmad-vs-spec-kit-vs-openspec-choosing-your-spec-driven-ai-framework/ · https://www.fundesk.io/spec-driven-development-github-spec-kit-guide · https://github.com/Anioko/spec-driven-development · https://www.braingrid.ai/blog/spec-driven-development-tools
- https://dupple.com/learn/best-ai-code-review-tools · https://www.morphllm.com/github-ai-code-review · https://www.stork.ai/blog/best-ai-code-review-tools-2026 · https://screencli.sh/blog/best-ai-pr-review-tools-2026 · https://wetheflywheel.com/en/guides/best-ai-code-review-tools-2026/ · https://blog.codercops.com/blog/ai-code-review-tools-compared-2026
- §4c (12/10/2026): https://github.com/astral-sh/uv · https://pydevtools.com/blog/openai-acquires-astral/ · https://github.com/astral-sh/ruff · https://github.com/microsoft/pyright · https://github.com/biomejs/biome · https://github.com/oxc-project/oxc · https://github.com/webpro-nl/knip · https://github.com/kucherenko/jscpd · https://github.com/renovatebot/renovate · https://github.com/pre-commit/pre-commit · https://github.com/googleapis/release-please · https://github.com/reviewdog/reviewdog · https://github.com/stryker-mutator/stryker-js · https://github.com/GoogleChrome/lighthouse-ci · https://github.com/alibaba/open-code-review
