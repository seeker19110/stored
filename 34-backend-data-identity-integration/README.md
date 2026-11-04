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

## 6. Kiểm bài viết “218 developers vắt kiệt server 12 đô” (twelve-dollar-server-challenge): kỹ thuật đúng, bảng xếp hạng trong bài đã cũ (bài người dùng gửi, đối chiếu repo 4/11/2026)

> Bài người dùng gửi tóm tắt cuộc thi của Arjay McCandless: dựng một Social Media API trên SQLite, chạy trên server 12 đô (1 vCPU, 2 GB). Bài kể "Top 10" đạt 240.000–280.000 người dùng ảo đồng thời (khoảng 23.000–26.800 req/s), và rút ra điểm chung: `io_uring` với direct descriptors, batching từ I/O tới transaction, tái dùng buffer, tách WAL checkpoint khỏi event loop. Đối chiếu với repo https://github.com/arjaythedev/twelve-dollar-server-challenge (MIT, 660★, 318 fork, tạo 3/10/2026), clone nông tại `b7b7b651fe243b0417ae82b3bfc1fc4beb53c456` (4/11/2026 13:34 UTC): `README.md` (luật), `SPEC.md`, `LEADERBOARD.md`, `benchmarks/batch-1.md`, `batch-2.md`. **Không chạy bài dự thi nào.**

### 6.1 Luật chơi: khớp bài viết

| Bài viết nói | Repo | Kết quả |
|---|---|---|
| SQLite, cấm cache feed và cấm nhớ kết quả xác thực token | README luật 2 và 5: chỉ SQLite in-process; "no response caches, query-result caches, in-memory copies of tables, or remembered JWT verifications (verify every token's signature)". Page cache và `mmap` của SQLite được phép; prepared statement được phép | ✅ |
| Ghi phải commit trước khi trả lời | Luật 6: WAL với `synchronous=NORMAL` trở lên; cấm `synchronous=OFF` và DB trong RAM; **được gom ghi của nhiều request vào một transaction** (group commit) nếu mỗi response chờ commit | ✅ (đây chính là nền của kỹ thuật batching) |
| 500.000 posts, 2 triệu likes | `seed/make-seed.sh`: 50k users, 500k posts, 2M likes, token ký sẵn cho 20.000 user (HS256) | ✅ |
| Giữ 5 phút, P95 < 500 ms, P99 < 1 s, lỗi < 1% | Đúng; điểm là số user cao nhất giữ qua một lần 5 phút | ✅ |
| "Concurrent virtual users" | Mỗi user ảo chạy `bench/load.js`: feed → nghỉ → post → nghỉ, 15% like, 2% đăng bài. **Có thời gian nghỉ**, nên 280.000 user tương ứng khoảng 26.700 req/s chứ không phải 280.000 request cùng lúc | ⚠️ cần hiểu đúng |
| "Hệ điều hành giới hạn mỗi process 65.000 file descriptor" | Không phải giới hạn của Linux: ban tổ chức chạy mọi bài qua systemd với **`LimitNOFILE=65535`** (`LEADERBOARD.md`). Direct descriptor của `io_uring` (file đăng ký trong ring) không chiếm bảng fd của process nên vượt được giới hạn đó | ⚠️ sai nguyên nhân, đúng kỹ thuật |
| Server "12 đô" | Batch 1 (10–11/10) chạy trên droplet DigitalOcean 12 đô; từ batch 2 (20–21/10) chuyển sang **VPS Synteq** 1 vCPU / 2 GB (Xeon Platinum 8260, AVX-512), nhanh hơn khoảng 2 lần với bài nặng CPU. Mọi con số 240k–310k là trên máy Synteq | ⚠️ |

### 6.2 Từng bài trong "Top 10" của bài viết, đối chiếu `LEADERBOARD.md` (4/11/2026)

| Bài viết | Dòng tương ứng trên leaderboard | Kết quả |
|---|---|---|
| Assembly, 240.000 user, RAM thấp nhất 545 MB | `asm-epoll-umitaltintas` #152: 240.000, 545 MB, **hạng 23** | ✅ số đúng, nhưng không còn trong top 10 |
| F# bẻ Kestrel, 247.000, P99 72 ms | `fsharp-kestrel-delneg` #201: 247.000, P99 72 ms, **hạng 21** | ✅ |
| C và Assembly cùng tác giả, 250.000 | `asm-iouring-unorig-username` #206: 250.000, P99 397 ms, 1.486 MB ✅. Bản C cùng tác giả (`c-iouring-unorig-username` #290) nay **280.000** (P99 713 ms) | ⚠️ số của bản C đã cũ |
| Rust, 264.000, range scan cho feed | `rust-epoll-scooter1337` #82: 264.000. Chú thích ˣ: lần đầu **hết cổng nguồn của máy tạo tải** ở khoảng 240.000 kết nối (1 IP × 4 máy), phải chấm lại với thêm 3 IPv4 và 5 máy tạo tải; 360k/480k thì app bị OOM-kill | ✅, kèm lưu ý về giới hạn của chính bộ đo |
| Ada, 270.000, P99 177 ms | `ada-native-visseranalytics` hiện được chấm ở #237: **250.000**. Các lần #211 và #216 giữ được 270.000; cùng mã của #216 chạy lại thì 260k/280k trượt P99. Lịch sử 226k → 270k khớp bài viết | ⚠️ điểm dao động giữa các lần chạy |
| Crystal tắt GC, 270.000 | `crystal-epoll-faustinoaq` #193: 270.000, P99 879 ms | ✅ |
| Lean sinh mã C, 280.000, P99 316 ms | `lean-derive-hargup` #153: 280.000, P99 316 ms, 836 MB | ✅ |
| Tự viết engine đọc/ghi file SQLite, 280.000, P99 23 ms | `c-rawsqlite-larvance` #210 từng chấm 280.000 khi chưa link libsqlite3. **Arjay ra phán quyết ngày 31/10: không được phép** ("an own engine for SQLite's file format", luật 2), nên bài bị gỡ khỏi bảng. Bản sửa dùng SQLite 3.54.1 gốc và đọc qua B-tree cursor API được chấm lại **260.000** | ⚠️ bài viết nói "đi quá giới hạn", thực tế là bị loại rồi chấm lại |
| C dùng SIMD xác thực theo lô và đọc thẳng B-tree, 266.000 | Không tìm được dòng 266.000 khớp; có thể là lần chạy cũ của một bài C io_uring | (chưa xác minh) |
| "Hai nhà đồng vô địch ở 280.000" | Bảng hiện tại: hạng 1 **`rust-iouring-kensac` 310.000** (P99 190 ms), Mojo 304.000, C 295.000, Rust 290.000; 280.000 là **hạng 5**, đồng hạng giữa hai bài Lean 4, Objective-C và C | ❌ đã cũ |
| "218 developers" | Leaderboard ghi tổng số bài dự thi, không ghi số người; bản 25/10 có 167 bài | (chưa xác minh) |

Phán quyết ngày 31/10 cũng làm rõ: đọc `/feed` và `/posts/:id` qua **B-tree/cursor API của chính SQLite là hợp lệ**; được dùng page cache tùy chỉnh (`SQLITE_CONFIG_PCACHE2`) và VFS riêng; **không** được sửa mã nguồn SQLite (hai bài đã bỏ bản vá và chấm lại). Ngoài ra còn các câu hỏi đang chờ: PGO profile huấn luyện trên chính bài tải (go-lowlevel #91), bài tối ưu theo thứ tự lặp của bộ tạo tải (cpp-eastl #32), bài trả cả lô request bằng một SELECT qua virtual table (sql-oneselect #243).

### 6.3 Bài học cho dự án thật (đã lọc)

1. **Group commit là kỹ thuật dùng được ngay.** Gom ghi của nhiều request vào một transaction, mỗi request vẫn chờ commit xong mới trả lời. Giữ an toàn dữ liệu và chia đều chi phí fsync. Cần giới hạn kích thước lô hoặc thời gian chờ (bài viết nhắc 128 request / 6 ms) để không phá P99.
2. **Tách WAL checkpoint khỏi đường phục vụ** và theo dõi kích thước WAL: áp dụng cho mọi app SQLite có nhiều ghi.
3. **Đếm việc trên mỗi request**: query plan (`EXPLAIN QUERY PLAN`), số lần cấp phát, serialize thẳng vào buffer. Top 10 có µs CPU/request khoảng 25–34; framework thông thường ở cuối bảng cao hơn nhiều lần.
4. **Đừng mang về production**: đọc thẳng B-tree cursor (gắn vào phiên bản SQLite), tự viết engine theo định dạng file (bị cấm ngay trong cuộc thi), tắt GC toàn cục, fast path dựa vào bất biến của dữ liệu seed (ID liên tiếp, timestamp tăng dần) mà không có fallback và test.
5. **Benchmark có giới hạn của chính nó**: hết cổng nguồn của máy tạo tải ở khoảng 240k kết nối/IP, đổi máy chấm giữa các đợt, điểm dao động giữa các lần chạy cùng mã. So sánh chỉ có nghĩa trong cùng một đợt và cùng một máy.

**Nguồn §6:** bài người dùng gửi 4/11/2026 · clone `--depth 1` https://github.com/arjaythedev/twelve-dollar-server-challenge HEAD `b7b7b651fe243b0417ae82b3bfc1fc4beb53c456`: https://github.com/arjaythedev/twelve-dollar-server-challenge/blob/b7b7b651fe243b0417ae82b3bfc1fc4beb53c456/README.md (luật 2, 5, 6, 9) · https://github.com/arjaythedev/twelve-dollar-server-challenge/blob/b7b7b651fe243b0417ae82b3bfc1fc4beb53c456/SPEC.md · https://github.com/arjaythedev/twelve-dollar-server-challenge/blob/b7b7b651fe243b0417ae82b3bfc1fc4beb53c456/LEADERBOARD.md (bảng, chú thích ˣ, "Arjay's rulings on SQLite (2026-10-31)") · https://github.com/arjaythedev/twelve-dollar-server-challenge/blob/b7b7b651fe243b0417ae82b3bfc1fc4beb53c456/benchmarks/batch-1.md · https://github.com/arjaythedev/twelve-dollar-server-challenge/blob/b7b7b651fe243b0417ae82b3bfc1fc4beb53c456/benchmarks/batch-2.md · https://benchmarks.arjaythedev.com/12-dollar-server/leaderboard (bản 25/10/2026, 167 bài) · GitHub search API `repo:arjaythedev/twelve-dollar-server-challenge` 4/11/2026.

## Nguồn và giới hạn kiểm chứng

Nguồn ở §3 cố định full SHA cho đường mã, LICENSE và CI đã đọc. Không ghi sao vì GitHub search API bị trả Forbidden trong phiên, không dùng số cũ làm số hiện tại và không suy archive từ clone thành công. Các tiêu chí §1/§4/§5 là thiết kế tổng hợp của kho; công cụ phải được thử trên project, DB và threat model thực tế trước tích hợp.
