# 32. Platform & Delivery Engineering: từ môi trường phát triển đến triển khai có thể quay lui

> Nghiên cứu 4/11/2026 phục vụ xưởng phát triển phần mềm. Mục 13 giữ bản đồ stack/DevOps; mục này đào sâu **hợp đồng môi trường, thay đổi hạ tầng, promotion artifact và khôi phục**. Đây là hồ sơ/đánh giá, không chứa implementation triển khai. Đọc LICENSE, spec, implementation/callsite và CI theo phạm vi bên dưới; không cài/build/chạy upstream, không tạo tài nguyên cloud.

## 1. Trần chất lượng và phạm vi

Một pipeline xanh chỉ chứng minh các job được chọn đã thành công. Xưởng cần trả lời: dev và CI có cùng dependency không; ai được apply plan nào; image digest nào chạy ở staging/production; khi lỗi có phục hồi dữ liệu và dịch vụ được không. Các lớp artifact/signing ở [mục 31](../31-software-supply-chain-security/README.md), test ở [mục 30](../30-software-testing-quality/README.md) và SLO/incident ở [mục 33](../33-reliability-observability-operations/README.md) là cổng liên quan, không được thay bằng trạng thái sync của công cụ triển khai.

| Lớp | Artifact làm hợp đồng | Cổng nghiệm thu ở dự án tích hợp |
|---|---|---|
| Môi trường phát triển/CI | Runtime pin, dependency lock, image/Feature ref, cấu hình và lệnh readiness | Tạo môi trường mới rồi build/test một luồng thật; kiểm cả khởi động lại, không chỉ cache nóng |
| Hạ tầng | Source commit, provider lock, plan gắn workspace/state, người duyệt | Plan được review là plan được apply; xử lý drift, concurrency và secret trong state |
| Phát hành ứng dụng | Image/package digest + config/migration version, bằng chứng test/provenance | Promote cùng artifact; kiểm health và hành vi đại diện sau deploy, có điều kiện rollback |
| Môi trường tạm | Owner, TTL, dữ liệu mẫu và đường teardown | Test xong xóa được tài nguyên/secret; môi trường PR không cầm credential production |
| Khôi phục | Revision cũ, khả năng tương thích schema/dữ liệu, backup đã thử | Revert/sync/restore được diễn tập; mục tiêu phục hồi theo sản phẩm và chi phí chấp nhận được |

<a id="factory-devcontainers-2026-11-04"></a>

## 2. Development Container Specification: hợp đồng setup có lifecycle và quyền host

| Thuộc tính | Kết quả đọc |
|---|---|
| Repo / nguồn | `devcontainers/spec`, đặc tả do Microsoft và cộng đồng phát triển; README trỏ `containers.dev`, CLI tham chiếu và `devcontainers/ci` |
| Phiên bản / mức kiểm | HEAD `c95ffeed1d059abfe9ffbe79762dc2fa4e7c2421`; **docs-read**: đọc đặc tả, schema và license. Repo spec không là binary runtime; không gán code-read hay kết quả CI của CLI cho nó |
| License | Nội dung spec: **CC-BY-4.0** trong `LICENSE`/README; mã có `LICENSE-CODE` MIT. Không gán MIT cho toàn bộ nội dung đặc tả |
| Cơ chế | `devcontainer.json`/JSONC mô tả image/build, Features, mounts, user, environment và lifecycle; host thực thi phải hỗ trợ các trường tương ứng |
| Ranh giới | `initializeCommand` chạy trên **host**; `onCreateCommand`/`postCreateCommand` chạy trong container. Container không tự thành sandbox bảo vệ host khi mount socket/thư mục nhạy cảm hoặc bật privileged |
| Tích hợp | Dùng cho local/CI nếu cần cùng hợp đồng setup; startup/readiness phải là lệnh được kiểm trong tool thực tế, không chỉ file JSON schema pass |

Đặc tả phân biệt `remoteUser` (user cho tool/subprocess) với `containerUser` (user cho các operation trong container); mặc định có thể kế thừa root từ image. `waitFor` mặc định `updateContentCommand`, nên một tool attach thành công chưa chứng minh `postCreateCommand` đã hoàn tất. Lifecycle thất bại sẽ bỏ các script tiếp theo; cần lưu log và kiểm kết quả tác vụ. [Tham chiếu lifecycle/user/mount]( https://github.com/devcontainers/spec/blob/c95ffeed1d059abfe9ffbe79762dc2fa4e7c2421/docs/specs/devcontainerjson-reference.md ) · [schema]( https://github.com/devcontainers/spec/blob/c95ffeed1d059abfe9ffbe79762dc2fa4e7c2421/schemas/devContainer.base.schema.json ) · [spec license]( https://github.com/devcontainers/spec/blob/c95ffeed1d059abfe9ffbe79762dc2fa4e7c2421/LICENSE ) · [code license]( https://github.com/devcontainers/spec/blob/c95ffeed1d059abfe9ffbe79762dc2fa4e7c2421/LICENSE-CODE ).

**Chọn thay thế:** runtime pin + package manager lock khi repo nhỏ; Nix/devenv (mục 13) khi cần mô hình package/environment khác; Dev Containers khi nhóm đã dùng container/IDE hỗ trợ. Mỗi cách vẫn phải kiểm dependency nền, architecture, proxy/CA và secret injection theo môi trường thực; không bảo đảm mọi host tương đương bit-for-bit.

<a id="factory-opentofu-2026-11-04"></a>

## 3. OpenTofu: review thay đổi và apply đúng artifact

Hồ sơ gốc đã có ở [mục 13](../13-dev-stack-devops/README.md); đây là phạm vi đọc sâu mới. `opentofu/opentofu`, MPL-2.0, HEAD `c570669d0fed5787f18d2f017f56b2658e2e6cce`. Đã đọc LICENSE, CLI `PlanCommand`, backend local, docs plan/state và workflow Quick Checks. Không chạy plan/apply hay kiểm provider thật.

**Exit code có ba trạng thái.** Với `-detailed-exitcode`, docs và `internal/command/plan.go` khớp: 0 = thành công không thay đổi, 1 = lỗi, 2 = thành công có thay đổi. Wrapper `set -e` coi exit 2 là lỗi nếu không xử lý, còn `|| true` có thể nuốt cả lỗi thật. CI nên phân loại từng mã rồi chạy policy/diff review trên plan; “có thay đổi” chưa phải “được phép apply”. [CLI implementation]( https://github.com/opentofu/opentofu/blob/c570669d0fed5787f18d2f017f56b2658e2e6cce/internal/command/plan.go ) · [contract mã thoát]( https://github.com/opentofu/opentofu/blob/c570669d0fed5787f18d2f017f56b2658e2e6cce/website/docs/cli/commands/plan.mdx ).

**Gắn plan với state.** Backend local có kiểm lineage/serial của saved plan với metadata state; lệch lineage hoặc state thay đổi sẽ báo không khớp/stale khi có metadata tương ứng. Đây là một lớp concurrency/correctness, không thay phân quyền review/apply của tổ chức và không chứng minh mọi provider action quay lui được. [Kiểm saved plan]( https://github.com/opentofu/opentofu/blob/c570669d0fed5787f18d2f017f56b2658e2e6cce/internal/backend/local/backend_local.go ).

**Secret và lưu trữ.** Docs ghi state có thể chứa password/private key, và plan có thể giữ dữ liệu nhạy cảm dù terminal đã che; cần bảo vệ artifact/state, hạn chế đọc, retention và cấu hình encryption nếu dùng. Không đưa plan JSON vào comment PR public theo mặc định. [Sensitive state]( https://github.com/opentofu/opentofu/blob/c570669d0fed5787f18d2f017f56b2658e2e6cce/website/docs/language/state/sensitive-data.mdx ) · [plan file]( https://github.com/opentofu/opentofu/blob/c570669d0fed5787f18d2f017f56b2658e2e6cce/website/docs/cli/commands/plan.mdx ) · [CI Quick Checks]( https://github.com/opentofu/opentofu/blob/c570669d0fed5787f18d2f017f56b2658e2e6cce/.github/workflows/checks.yml ) · [license]( https://github.com/opentofu/opentofu/blob/c570669d0fed5787f18d2f017f56b2658e2e6cce/LICENSE ).

**Chọn thay thế:** OpenTofu cho HCL/provider ecosystem với điều kiện kiểm provider/backend; Terraform cần đọc lại license phiên bản định dùng, không suy từ OpenTofu; Pulumi (mục 13) khi nhóm muốn ngôn ngữ lập trình và quản dependency tương ứng; cấu hình cloud nhỏ vẫn có thể dùng công cụ native nếu giữ diff/review/audit. Không chọn chỉ dựa trên cú pháp quen.

<a id="factory-argocd-2026-11-04"></a>

## 4. Argo CD: desired state không đồng nghĩa phục hồi sản phẩm

`argoproj/argo-cd`, Apache-2.0, HEAD `211c2b4fdc82f2ebd0b94c3fbf48779c06d83bad`; hồ sơ gốc mục 13. Đọc `Server.Rollback`, docs automated sync, LICENSE và CI unit/race/integration. Không dựng cluster, không chạy sync/e2e.

`Server.Rollback` kiểm quyền và từ chối khi application đang có automated sync bật: lỗi `rollback cannot be initiated when auto-sync is enabled`. Tài liệu automated sync cũng ghi điều kiện này. Trong hệ GitOps, cần chọn đường phục hồi phù hợp: **revert desired state trong Git và sync lại**, hoặc thao tác rollback có kiểm soát sau khi xử lý chính sách auto-sync. Không ghi runbook “bấm rollback” mà bỏ qua trạng thái controller. [Đường rollback]( https://github.com/argoproj/argo-cd/blob/211c2b4fdc82f2ebd0b94c3fbf48779c06d83bad/server/application/application.go ) · [contract automated sync]( https://github.com/argoproj/argo-cd/blob/211c2b4fdc82f2ebd0b94c3fbf48779c06d83bad/docs/user-guide/auto_sync.md ).

Các tùy chọn prune/self-heal/allow-empty và ApplicationSet làm hành vi khác nhau; phải review manifest thực của ứng dụng. Synced cho biết live state phù hợp desired state theo cách so sánh của Argo CD; Healthy là health assessment được cấu hình, không thay phép thử login/đặt hàng hay bằng chứng restore dữ liệu. Có thể quay image về bản cũ mà schema migration không tương thích; điều kiện này thuộc ứng dụng và backend ở mục 34. [CI]( https://github.com/argoproj/argo-cd/blob/211c2b4fdc82f2ebd0b94c3fbf48779c06d83bad/.github/workflows/ci-build.yaml ) · [license]( https://github.com/argoproj/argo-cd/blob/211c2b4fdc82f2ebd0b94c3fbf48779c06d83bad/LICENSE ).

**Chọn thay thế:** Argo CD khi cần GitOps Kubernetes và mô hình Application; Flux khi nhóm muốn controller/toolkit cùng GitOps (đối chiếu hồ sơ nếu có, chưa đọc mã Flux trong đợt này); CI deploy trực tiếp có audit/rollback cho hệ nhỏ; dịch vụ platform managed khi chấp nhận ràng buộc nhà cung cấp. Không thêm Kubernetes chỉ để dùng một công cụ GitOps.

## 5. Pipeline tham chiếu cho một xưởng nhiều sản phẩm

1. **Golden path tối thiểu:** template repo liên kết owner, runtime/lock, test, docs, release, health/readiness và runbook. Nơi triển khai giữ implementation; kho này giữ tiêu chí so sánh và nguồn.
2. **Dev/CI có cùng đầu vào:** tạo lại môi trường từ nguồn pin; chạy build/test thật và báo số test. Phân biệt retained dependency/cache với process/service phải restart; thay architecture hoặc image phải kiểm lại.
3. **Plan hạ tầng có quyền hẹp:** tạo plan cho đúng môi trường, xử lý 0/1/2 đúng, review policy/cost/resource diff; bảo vệ plan/state và chỉ apply artifact đã duyệt, không sinh plan mới sau approval rồi mặc định tương đương.
4. **Build một lần, promote theo digest:** release bundle gồm source, test/security evidence, artifact digest và config/migration version. Staging/prod nhận cùng artifact; secret/environment là binding riêng có audit, không nhúng vào image.
5. **Deploy và quan sát hành vi:** controller sync/rollout xong phải qua health + functional smoke/SLO tại mục 30/33. Đặt giới hạn blast radius/canary theo rủi ro; ngưỡng do sản phẩm quyết định, không dùng một tỷ lệ chung cho mọi hệ.
6. **Revert/restore và teardown:** diễn tập quay lui app tương thích schema, phục hồi dữ liệu và xóa preview environment theo owner/TTL. Giữ audit artifact trước/sau; secret/volume/tài nguyên dùng chung cần policy riêng để teardown không xóa nhầm.

## 6. Ma trận nghiệm thu và giới hạn

| Cổng | Bằng chứng tối thiểu | Không được coi là pass |
|---|---|---|
| Onboarding | Môi trường mới chạy được build/test/luồng đại diện với dependency pin | Chỉ có container PID, shell attach, port mở hay cache từ máy cũ |
| Plan/apply | Exit đúng nghĩa, plan hash/workspace/state/reviewer, apply log | Chỉ có comment diff hoặc bỏ qua mọi mã lỗi để làm xanh job |
| Deploy | Artifact/config đúng revision, health và functional smoke, provenance theo policy | Chỉ image tag trùng tên, status Synced hoặc một HTTP 200 không kiểm body |
| Recovery | Diễn tập có outcome, RTO/RPO thực đo theo mục tiêu sản phẩm, migration compatibility | Chỉ giữ một image cũ hoặc backup chưa từng restore |
| Chi phí/quyền | Owner, TTL, quota/budget và audit quyền môi trường | Preview chạy vô hạn hoặc dùng production credentials để tiện test |

Ba hồ sơ trên có vai trò khác nhau: spec môi trường, công cụ IaC và controller deployment. Ghép cả ba chỉ khi sản phẩm cần; monolith nhỏ có thể đạt cùng hợp đồng bằng ít công cụ hơn. Chưa có dữ liệu vận hành của xưởng để khẳng định giảm thời gian, chi phí hay lỗi bao nhiêu; các cổng là đề xuất tích hợp cần đo ở repo đích.

## 7. Nguồn

- Development Container Specification: [README]( https://github.com/devcontainers/spec/blob/c95ffeed1d059abfe9ffbe79762dc2fa4e7c2421/README.md ), [devcontainer.json reference]( https://github.com/devcontainers/spec/blob/c95ffeed1d059abfe9ffbe79762dc2fa4e7c2421/docs/specs/devcontainerjson-reference.md ), [schema]( https://github.com/devcontainers/spec/blob/c95ffeed1d059abfe9ffbe79762dc2fa4e7c2421/schemas/devContainer.base.schema.json ), `LICENSE` và `LICENSE-CODE` tại SHA §2.
- OpenTofu: LICENSE, `internal/command/plan.go`, `internal/backend/local/backend_local.go`, docs plan/sensitive-state và `.github/workflows/checks.yml` tại SHA §3.
- Argo CD: LICENSE, `server/application/application.go`, `docs/user-guide/auto_sync.md` và `.github/workflows/ci-build.yaml` tại SHA §4.
- Các permalink trong từng hồ sơ là nguồn gốc đọc 4/11/2026. Số sao không được thu thập; trạng thái release/maintenance không suy chỉ từ HEAD. Không có phép đo hay chạy upstream được nhận là của kho.
