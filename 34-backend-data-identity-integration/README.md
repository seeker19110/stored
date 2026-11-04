# 34 · Backend, dữ liệu giao dịch, định danh và tích hợp

> Đọc ngày **2026-11-04**, phạm vi `code-read` cho ba hồ sơ có SHA dưới đây; chưa cài, chạy database, migration, IdP hoặc test upstream. Repo này giữ nghiên cứu và điều kiện nghiệm thu; code triển khai thuộc dự án của xưởng.

## 1. Vì sao cần mục riêng

[Mục 13](../13-dev-stack-devops/README.md) chọn stack/framework; [15](../15-ai-for-data/README.md)/[24](../24-ai-data-engineering/README.md) quản lý dữ liệu phân tích/AI; [12](../12-ai-security-guardrails/README.md) có ReBAC và guardrail; [21](../21-autonomous-workflows/README.md) có durable execution. Mục này nối các lớp đó vào **hợp đồng nghiệp vụ của backend**: ai được làm gì trên bản ghi nào, transaction nào được commit, schema nào tương thích với phiên bản app đang chạy, và retry có tạo tác dụng phụ trùng không.

| Năng lực | Artifact phải có | Cổng nhận của xưởng | Sai lầm cần tránh |
|---|---|---|---|
| Mô hình dữ liệu | ERD/schema, invariants, ownership và retention | FK/unique/check, nullability, timezone/currency và concurrency fixture | Chỉ kiểm CRUD happy path |
| Migration | File versioned + manifest release + kế hoạch expand/contract | Fresh DB, upgrade từ bản được hỗ trợ, rolling compatibility, lock/timeout | Có `down` nghĩa là rollback giữ được dữ liệu |
| Truy cập dữ liệu | Query/schema cùng revision, codegen/config | Compile/vet/diff và integration trên DB đúng version | Codegen type-safe chứng minh phân quyền/hiệu năng |
| Định danh | Issuer/client/flow, redirect, scopes, session/recovery policy | OIDC flow dương/âm, key rotation, expiry/logout | Đăng nhập thành công nghĩa là mọi API đã có quyền đúng |
| Phân quyền/đa tenant | Subject/resource/action/tenant, policy/model revision | Ma trận allow/deny, tenant A không đọc/ghi tenant B | Lấy tenant ID trong body hoặc tin mỗi role trong UI |
| Event/webhook/job | Event schema/version, outbox/inbox, idempotency key | Retry/replay, duplicate/out-of-order, crash-before/after-commit | Gọi "exactly-once" khi chỉ có retry hoặc ACK |

Các cổng trong bảng là đề xuất kỹ thuật, phải được dự án chọn ngưỡng, fixture và chủ sở hữu; chúng chưa được chạy tại `stored`.

## 2. Chọn lớp công cụ, tránh xây cả nền tảng khi chưa cần

| Nhu cầu | Điểm bắt đầu | Hai hướng so sánh | Điều quyết định |
|---|---|---|---|
| Schema SQL có lịch sử triển khai | goose | Migration của framework đang dùng; thay đổi SQL được điều phối bởi pipeline | Engine, khóa/DDL, transaction, backward compatibility và quyền DB |
| Query SQL tường minh, code gọi typed | sqlc | ORM của framework; query SQL viết tay có test | Dialect và generator thực sự hỗ trợ, codegen diff, query plan |
| SSO/federation và lifecycle tài khoản | Keycloak | Auth có sẵn của [Supabase](../13-dev-stack-devops/README.md); nhà cung cấp OIDC managed | Mức vận hành, federation/HA, data residency, recovery và chi phí |
| Quyền theo quan hệ tài nguyên | [OpenFGA](../12-ai-security-guardrails/README.md#openfga) | [SpiceDB](../12-ai-security-guardrails/README.md#spicedb); policy/RBAC trong app nhỏ | Mô hình quyền, consistency/revocation, latency và negative tests |
| Event từ transaction đã commit | Transactional outbox + worker | [Debezium](../15-ai-for-data/README.md); job/workflow [Temporal](../21-autonomous-workflows/README.md) | Boundary commit, replay/idempotence, retention/schema và vận hành |

OpenFGA, SpiceDB, Debezium và Temporal giữ hồ sơ gốc ở mục đã dẫn; không nhân bản catalog hay gán ngày kiểm mới cho chúng. Các lựa chọn ở mỗi hàng giải những lớp khác nhau, không thay thế nhau hoàn toàn.

## 3. Hồ sơ đọc mã

<a id="goose-migrations"></a>

### 3.1. goose của pressly: migration không tự điều phối mọi replica

| Thuộc tính | Giá trị |
|---|---|
| Repo / phân biệt tên | [pressly/goose](https://github.com/pressly/goose), migration SQL/Go; khác coding agent `block/goose` ở mục 01 |
| Phiên bản / license | `2d285d2249855c959765409c68b17a6634f0acb4`; MIT |
| Đã đọc | README/LICENSE, `migration_sql.go`, `provider_options.go`, `provider_run.go`, workflow unit và integration; chưa chạy |
| Cơ chế | Đường SQL dùng transaction thì mở transaction, chạy câu lệnh và cập nhật bảng version rồi commit; nhánh không transaction chạy/cập nhật version ngoài transaction. Khả năng DDL transactional còn phụ thuộc DB. |
| Khóa | API `Provider` chỉ dùng lock khi `useLocker` và `cfg.lockEnabled`; `WithSessionLocker`/`WithLocker` bật khóa tường minh. Không suy default của API này thành default của mọi CLI/integration. Một `Provider` mutex trong process không thay khóa giữa các replica. |
| CI | `ci.yaml` có build/vet/unit; `integration.yaml` gọi `make test-integration`. Có workflow không chứng minh engine/version triển khai đã được phủ. |
| Tích hợp | Chọn một migration runner cho release hoặc locker phù hợp DB, quyền DDL riêng và deadline; migration immutable sau phát hành. Kiểm fresh/upgrade/partial failure và ứng dụng N/N−1 cùng schema mới. |
| Giới hạn | `NO TRANSACTION`, DDL lock/backfill và lệnh ngoài DB có thể gây thay đổi dở dang. Down migration có thể mất dữ liệu; rollback phần mềm thường cần schema expand/contract chứ không tự gọi `down`. |

**Nguồn hồ sơ:** [README.md](https://github.com/pressly/goose/blob/2d285d2249855c959765409c68b17a6634f0acb4/README.md) · [LICENSE](https://github.com/pressly/goose/blob/2d285d2249855c959765409c68b17a6634f0acb4/LICENSE) · [migration_sql.go](https://github.com/pressly/goose/blob/2d285d2249855c959765409c68b17a6634f0acb4/migration_sql.go) · [provider_options.go](https://github.com/pressly/goose/blob/2d285d2249855c959765409c68b17a6634f0acb4/provider_options.go) · [provider_run.go](https://github.com/pressly/goose/blob/2d285d2249855c959765409c68b17a6634f0acb4/provider_run.go) · [.github/workflows/ci.yaml](https://github.com/pressly/goose/blob/2d285d2249855c959765409c68b17a6634f0acb4/.github/workflows/ci.yaml) · [.github/workflows/integration.yaml](https://github.com/pressly/goose/blob/2d285d2249855c959765409c68b17a6634f0acb4/.github/workflows/integration.yaml).

<a id="sqlc"></a>

### 3.2. sqlc: ba cổng khác nhau cho SQL và generated code

| Thuộc tính | Giá trị |
|---|---|
| Repo / SHA / license | [sqlc-dev/sqlc](https://github.com/sqlc-dev/sqlc), `3ad8b20fb02b5bea81591b673da0758b8685d951`, MIT cho repo; generator/plugin/dịch vụ kiểm riêng |
| Đã đọc | README/LICENSE, `diff.go`, `vet.go`, `verify.go`, hướng dẫn vet/CLI và CI; chưa generate hoặc kết nối DB |
| Cơ chế | `diff` gọi Generate, so các file đầu ra với file hiện có và trả lỗi khi thiếu/khác; không kiểm mọi file thừa trong thư mục output. `vet` dùng rule CEL; một số rule EXPLAIN cần kết nối DB. |
| Điểm dễ hiểu nhầm | `verify` khởi tạo client theo cấu hình cloud và lấy query sets trước đó; không quảng bá như cổng offline drop-in. `compile`, `diff`, `vet` và compatibility với schema cũ là các phép kiểm riêng. |
| CI | `ci.yml` có build đa OS/arch, unit/end-to-end cùng PostgreSQL/MySQL và các examples; không suy mọi plugin/ngôn ngữ/dialect có cùng độ phủ. |
| Tích hợp | Ghim compiler/generator/config/schema, chạy compile + vet rule thực sự cấu hình + diff, build code và integration với DB cùng version. Review SQL và giới hạn rows/timeout; không log giá trị nhạy cảm. |
| Giới hạn | Typed query không chứng minh row-level authorization, đúng tenant, lock/deadlock hoặc query plan đủ tốt. Rule lint là heuristic; test cardinality/permission/concurrency độc lập. |

**Nguồn hồ sơ:** [README.md](https://github.com/sqlc-dev/sqlc/blob/3ad8b20fb02b5bea81591b673da0758b8685d951/README.md) · [LICENSE](https://github.com/sqlc-dev/sqlc/blob/3ad8b20fb02b5bea81591b673da0758b8685d951/LICENSE) · [internal/cmd/diff.go](https://github.com/sqlc-dev/sqlc/blob/3ad8b20fb02b5bea81591b673da0758b8685d951/internal/cmd/diff.go) · [internal/cmd/vet.go](https://github.com/sqlc-dev/sqlc/blob/3ad8b20fb02b5bea81591b673da0758b8685d951/internal/cmd/vet.go) · [internal/cmd/verify.go](https://github.com/sqlc-dev/sqlc/blob/3ad8b20fb02b5bea81591b673da0758b8685d951/internal/cmd/verify.go) · [docs/howto/vet.md](https://github.com/sqlc-dev/sqlc/blob/3ad8b20fb02b5bea81591b673da0758b8685d951/docs/howto/vet.md) · [docs/reference/cli.md](https://github.com/sqlc-dev/sqlc/blob/3ad8b20fb02b5bea81591b673da0758b8685d951/docs/reference/cli.md) · [.github/workflows/ci.yml](https://github.com/sqlc-dev/sqlc/blob/3ad8b20fb02b5bea81591b673da0758b8685d951/.github/workflows/ci.yml).

<a id="keycloak"></a>

### 3.3. Keycloak: tách xác thực người dùng khỏi quyền trên tài nguyên

| Thuộc tính | Giá trị |
|---|---|
| Repo / SHA / license | [keycloak/keycloak](https://github.com/keycloak/keycloak), `2174fdf38731f7191a00240f66fb599e9779005d`, Apache-2.0; theme/provider/dependency xem riêng |
| Đã đọc | README/LICENSE, authorization endpoint/checker, authorization-code grant, PKCE utility, production guide và CI; chưa triển khai OIDC/cluster |
| Cơ chế | Authorization endpoint gọi kiểm redirect và PKCE; checker phân biệt client có/không ép phương thức PKCE. Authorization-code grant gọi nhánh kiểm verifier tương ứng. Có hỗ trợ PKCE không đồng nghĩa mọi client đã ép S256. |
| Production | Guide yêu cầu TLS, hostname/proxy đúng, database production và cấu hình vận hành; `start-dev` trong quickstart không là cấu hình phát hành. Readiness phải phân biệt liveness khi bootstrap/migration đang chạy. |
| CI | CI có các nhánh điều kiện; `conformance.yml` là workflow dispatch cho các suite nêu trong file. Không coi tên conformance là bằng chứng mọi flow/provider đạt chứng nhận hoặc đã pass tại SHA này. |
| Tích hợp | Dùng thư viện OIDC chuẩn, ghim issuer/client/redirect/scopes; public client chọn Authorization Code + PKCE S256, kiểm state/nonce theo flow. API xác minh signature, issuer, audience, expiry và scope; quyền từng resource/tenant vẫn do app/policy kiểm. |
| Giới hạn | Session revocation, refresh-token rotation, key rotation, account recovery và admin access cần policy/test riêng; realm/client setup không tự tạo isolation ở database ứng dụng. IdP HA/backup/upgrade tạo một trách nhiệm vận hành mới. |

**Nguồn hồ sơ:** [README.md](https://github.com/keycloak/keycloak/blob/2174fdf38731f7191a00240f66fb599e9779005d/README.md) · [LICENSE.txt](https://github.com/keycloak/keycloak/blob/2174fdf38731f7191a00240f66fb599e9779005d/LICENSE.txt) · [services/src/main/java/org/keycloak/protocol/oidc/endpoints/AuthorizationEndpoint.java](https://github.com/keycloak/keycloak/blob/2174fdf38731f7191a00240f66fb599e9779005d/services/src/main/java/org/keycloak/protocol/oidc/endpoints/AuthorizationEndpoint.java) · [services/src/main/java/org/keycloak/protocol/oidc/endpoints/AuthorizationEndpointChecker.java](https://github.com/keycloak/keycloak/blob/2174fdf38731f7191a00240f66fb599e9779005d/services/src/main/java/org/keycloak/protocol/oidc/endpoints/AuthorizationEndpointChecker.java) · [services/src/main/java/org/keycloak/protocol/oidc/grants/AuthorizationCodeGrantType.java](https://github.com/keycloak/keycloak/blob/2174fdf38731f7191a00240f66fb599e9779005d/services/src/main/java/org/keycloak/protocol/oidc/grants/AuthorizationCodeGrantType.java) · [services/src/main/java/org/keycloak/protocol/oidc/utils/PkceUtils.java](https://github.com/keycloak/keycloak/blob/2174fdf38731f7191a00240f66fb599e9779005d/services/src/main/java/org/keycloak/protocol/oidc/utils/PkceUtils.java) · [docs/guides/server/configuration-production.adoc](https://github.com/keycloak/keycloak/blob/2174fdf38731f7191a00240f66fb599e9779005d/docs/guides/server/configuration-production.adoc) · [.github/workflows/ci.yml](https://github.com/keycloak/keycloak/blob/2174fdf38731f7191a00240f66fb599e9779005d/.github/workflows/ci.yml) · [.github/workflows/conformance.yml](https://github.com/keycloak/keycloak/blob/2174fdf38731f7191a00240f66fb599e9779005d/.github/workflows/conformance.yml).

## 4. Tuyến tích hợp cho một sản phẩm nhiều khách hàng

1. **Domain trước framework:** mô tả entity, invariant, boundary transaction, loại dữ liệu nhạy cảm, RPO/RTO và tenant model. Chọn shared tables/schema-per-tenant/database-per-tenant theo mức cô lập; tenant context lấy từ principal/quyền đã xác minh, không tin tùy ý header/body.
2. **Một thay đổi schema có hai thế hệ app:** thêm cột/index tương thích, deploy code đọc/ghi chuyển tiếp, backfill có checkpoint/throttle, kiểm xong rồi mới bỏ trường cũ. Bảng migration lưu version/checksum/runner; test nâng từ version đang hỗ trợ và khóa/timeout trên dữ liệu có kích thước đại diện.
3. **SQL/query cùng revision:** compiler + configured rules + generated diff, build và integration. Fixture âm phải có tenant khác, ID đoán được, NULL, boundary date/decimal, concurrent update, race/unique constraint. Với DB row-level policy, test bằng role thật của app, tránh tài khoản owner/admin che lỗ hổng.
4. **Identity khác authorization:** test login chuẩn/thiếu PKCE/sai redirect/sai issuer/audience/expired token; kiểm ma trận subject × action × resource × tenant và revoke. Quyền đọc, ghi, export, background jobs và search index đều phải cùng boundary.
5. **Giao dịch khác giao nhận event:** ghi business row và outbox trong cùng transaction; dispatcher retry, consumer dùng inbox/idempotency key hoặc unique business key. Tiêm crash sau external side effect nhưng trước ACK, replay và out-of-order; giữ event version, trace/correlation và dead-letter có người xử lý. Webhook cần kiểm chữ ký trên raw body theo provider, timestamp/replay window và secret rotation.
6. **Vận hành và xóa:** backup rồi restore kiểm số liệu/quyền thực tế, quyền DB tối thiểu, pool/backpressure, timeout/cancellation và load test; diễn tập xóa tenant qua primary/replica/search/cache/queue/backup theo retention đã cam kết. Nối [30](../30-software-testing-quality/README.md), [31](../31-software-supply-chain-security/README.md), [32](../32-platform-delivery-engineering/README.md), [33](../33-reliability-observability-operations/README.md).

## 5. Bộ bằng chứng bàn giao

| Artifact | Điều cần đối chiếu | Vì sao một badge chưa đủ |
|---|---|---|
| Schema/migration manifest | App revision, DB engine/version, compatible range, lock/backfill result | Migration pass trên DB rỗng chưa chứng minh upgrade production |
| Query/codegen report | Query+schema+generator hash, configured vet rules, generated diff, DB tests | Zero rule hoặc zero query không là phép kiểm hữu ích |
| Identity/policy report | Issuer/client/model ID, allow/deny/revoke/tenant fixture, key-rotation result | Token hợp lệ chưa chứng minh có quyền với resource |
| Event delivery report | Key/version, crash points, duplicate/reorder/replay và side-effect count | Retry thành công chưa chứng minh không ghi tiền/email hai lần |
| Recovery report | Backup revision, restore timestamp, data/permission checks, RPO/RTO đạt | Có file backup chưa chứng minh dữ liệu phục hồi dùng được |

Ngưỡng chấp nhận phải gắn nghiệp vụ và dữ liệu đại diện; chưa có số benchmark, kết quả chạy hoặc SLA được chứng minh trong đợt đọc mã này.

## Nguồn và giới hạn kiểm chứng

Nguồn ở §3 cố định full SHA cho đường mã, LICENSE và CI đã đọc. Không ghi sao vì GitHub search API bị trả Forbidden trong phiên, không dùng số cũ làm số hiện tại và không suy archive từ clone thành công. Các tiêu chí §1/§4/§5 là thiết kế tổng hợp của kho; công cụ phải được thử trên project, DB và threat model thực tế trước tích hợp.
