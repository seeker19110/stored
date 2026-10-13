# 13 · Dev Stack: Frontend · Backend · Mobile · DevOps · Spec-driven · AI Code Review

> Nền tảng kỹ thuật "cổ điển" mà agent/AI tooling đứng trên. Số sao ước lượng 2026 (nguồn lệch).

## 1. Frontend

| Framework | Repo | ★ | Ghi chú |
|---|---|---|---|
| React | facebook/react | ~251k (11/10/2026) | React 19; nền của Next.js, shadcn/ui |
| Vue | vuejs/core | ~208k | Vue 3.5; Nuxt |
| Next.js | vercel/next.js | ~125–138k | App Router, Server Actions; 59% dev dùng (State of JS 2025) |
| Angular | angular/angular | ~95k | Angular 18+ |
| Svelte | sveltejs/svelte | ~78k | Svelte 5 runes; SvelteKit |
| Nuxt | nuxt/nuxt | ~54k | |
| Astro | withastro/astro | ~45.5k | Islands, content-first |
| SolidJS | solidjs/solid | ~32k | |
| Vite | vitejs/vite | – | Build tool mặc định của hệ sinh thái; Rolldown |
| TanStack (Query/Router/Start) | TanStack/* | – | Full-stack TS mới nổi |

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

## 6. AI code review

| Công cụ | Giá | Thế mạnh | Hạn chế |
|---|---|---|---|
| **CodeRabbit** | $24 / $48 dev/tháng; free public repo | All-rounder ít nhiễu; hỗ trợ 4 Git host | |
| **Greptile** | – | Bắt lỗi cross-file tốt (82% một benchmark) | Nhiều false positive; GitHub-first; benchmark Macroscope cho thấp hơn |
| **Qodo** (CodiumAI) | Qodo Merge mở, self-host | F1 cao nhất trong 8 tool (2/2026); sinh test | |
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

## 7. Nguồn

- Mục 23 (19 repo của chủ kho, đọc 2026-10-12) · https://github.com/alibaba/open-code-review · https://github.com/googleapis/release-please · https://github.com/oxc-project/oxc · https://github.com/webpro-nl/knip · https://github.com/kucherenko/jscpd · https://github.com/astral-sh/uv · https://github.com/astral-sh/ruff
- https://www.solutelabs.com/blog/top-frontend-web-frameworks · https://www.intuz.com/best-frontend-frameworks/ · https://findarepo.com/categories/web-frameworks/ · https://wasp.sh/resources/2026/02/24/best-frameworks-web-dev-2026 · https://github.com/vanodevium/node-framework-stars · https://encore.dev/articles/best-typescript-backend-frameworks · https://www.hirenodejs.com/blog/nodejs-frameworks-compared-2026 · https://rankingdevs.com/best-backend-tools
- https://www.javacodegeeks.com/2026/02/kotlin-multiplatform-vs-flutter-vs-react-native-the-2026-cross-platform-reality.html · https://www.drizz.dev/post/cross-platform-mobile-development · https://mobisoftinfotech.com/resources/blog/cross-platform-app-development-flutter-vs-react-native-vs-native-apps
- https://spacelift.io/blog/gitops-tools · https://www.pulumi.com/blog/best-kubernetes-iac-tools-2026/ · https://www.qovery.com/blog/best-devops-automation-tools · https://oghabi.it/en-us/blog/devops-2026-trends-overview/ · https://medium.com/@h.stoychev87/devops-cloud-platform-tools-by-category-for-2026-68ed92103c17
- https://www.augmentcode.com/tools/best-spec-driven-development-tools · https://reenbit.com/bmad-vs-spec-kit-vs-openspec-choosing-your-spec-driven-ai-framework/ · https://www.fundesk.io/spec-driven-development-github-spec-kit-guide · https://github.com/Anioko/spec-driven-development · https://www.braingrid.ai/blog/spec-driven-development-tools
- https://dupple.com/learn/best-ai-code-review-tools · https://www.morphllm.com/github-ai-code-review · https://www.stork.ai/blog/best-ai-code-review-tools-2026 · https://screencli.sh/blog/best-ai-pr-review-tools-2026 · https://wetheflywheel.com/en/guides/best-ai-code-review-tools-2026/ · https://blog.codercops.com/blog/ai-code-review-tools-compared-2026
- §4c (12/10/2026): https://github.com/astral-sh/uv · https://pydevtools.com/blog/openai-acquires-astral/ · https://github.com/astral-sh/ruff · https://github.com/microsoft/pyright · https://github.com/biomejs/biome · https://github.com/oxc-project/oxc · https://github.com/webpro-nl/knip · https://github.com/kucherenko/jscpd · https://github.com/renovatebot/renovate · https://github.com/pre-commit/pre-commit · https://github.com/googleapis/release-please · https://github.com/reviewdog/reviewdog · https://github.com/stryker-mutator/stryker-js · https://github.com/GoogleChrome/lighthouse-ci · https://github.com/alibaba/open-code-review
