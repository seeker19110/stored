# 29. Kiến trúc phần mềm, yêu cầu & hợp đồng API

> Bổ sung cho xưởng phát triển phần mềm, khảo sát 2026-11-04. Phạm vi: từ yêu cầu có định danh, quyết định kiến trúc đến kiểm cấu trúc mã và tương thích API. Đây là hồ sơ nghiên cứu; không đặt bộ triển khai hay demo thực thi vào `stored`. Bốn upstream dưới được clone chỉ đọc, đọc LICENSE, implementation, callsite và CI tại full SHA; **code-read**, không cài/chạy/build upstream. Sao để `null`, không dùng mức quan tâm làm thước chất lượng.

## 1. Trần cần đạt và ranh giới với các mục khác

Một xưởng không chỉ sinh code nhanh: phải truy được vì sao có thay đổi, nó thuộc ranh giới nào và khách hàng nào có thể bị hỏng. Tuyến [28](../28-product-discovery-experimentation/README.md) chứng minh nhu cầu/giả thuyết; mục này biến quyết định thành hợp đồng; [30](../30-software-testing-quality/README.md) chứng minh hành vi; [32](../32-platform-delivery-engineering/README.md) và [33](../33-reliability-observability-operations/README.md) giữ bản phát hành vận hành được.

| Lớp | Artifact giữ trong repo tích hợp | Cổng nên có | Giới hạn |
|---|---|---|---|
| Yêu cầu | ID ổn định, tiêu chí nhận, owner, nguồn và trạng thái | Trace không đứt, thay đổi chưa review bị phát hiện | Trace đầy đủ không chứng minh yêu cầu đúng nhu cầu |
| Quyết định kiến trúc | ADR: bối cảnh, lựa chọn, trade-off, điều kiện xem lại | Review quyết định khi constraint đổi | Một mẫu ADR không là oracle tự động |
| Mô hình hệ thống | Context/container, boundary, dependency và deployment view có cùng ID | DSL hợp lệ và review chênh lệch mô hình | Sơ đồ đẹp không chứng minh mã tuân theo |
| Kiến trúc mã | Rule dependency theo module/layer | Import trái ranh giới/cycle làm CI fail | Phân tích tĩnh không phủ dynamic/runtime dependency |
| Hợp đồng API | OpenAPI versioned + compatibility policy + spec của bản đã phát hành | Breaking diff + runtime contract/consumer test | Hai spec khớp không chứng minh server thực thi spec |

Không chọn cả bốn công cụ cho mọi dự án. Một service nhỏ có thể dùng requirements/ADR Markdown, một OpenAPI và vài rule; hệ nhiều đội, khách hàng SDK hoặc chứng cứ truy vết mới cần lớp công cụ dày hơn.

<a id="doorstop-requirements-traceability"></a>

## 2. Doorstop: yêu cầu trong git, link có dấu vết thay đổi

| Thuộc tính | Giá trị |
|---|---|
| Repo/tổ chức | `doorstop-dev/doorstop` — cộng đồng Doorstop |
| License | LGPL-3.0-only; đọc LICENSE.md và SPDX của implementation |
| Phiên bản/phạm vi | `f5f2bef01a99c92210cad2713079f09cc4aed876`, 2026-11-04; `code-read` |
| Vai trò | Yêu cầu/test case dạng YAML, cây document và liên kết có stamp |
| Tích hợp | CLI `doorstop` ở repo đích; review requirements và trace diff cùng thay đổi code |

[README](https://github.com/doorstop-dev/doorstop/blob/f5f2bef01a99c92210cad2713079f09cc4aed876/README.md) mô tả item YAML có ID, link, validate và publish. [`Item.cleared`/`reviewed`](https://github.com/doorstop-dev/doorstop/blob/f5f2bef01a99c92210cad2713079f09cc4aed876/doorstop/core/item.py) so stamp của parent/link và nội dung để biết review không còn trùng bản hiện tại. Cơ chế này hữu ích khi yêu cầu gốc đổi: downstream phải xem lại, thay vì mặc định test case cũ vẫn hợp.

**Giới hạn quyết định:** [`ItemValidator`](https://github.com/doorstop-dev/doorstop/blob/f5f2bef01a99c92210cad2713079f09cc4aed876/doorstop/core/validators/item_validator.py) bỏ qua item inactive; một số tình huống `needs initial review` là info, `unreviewed changes`/suspect là warning. Mặc định `validate=True` không đồng nghĩa không còn warning. [CLI options](https://github.com/doorstop-dev/doorstop/blob/f5f2bef01a99c92210cad2713079f09cc4aed876/doorstop/cli/main.py) có `--warn-all`, `--error-all`, `--no-reformat`; nếu tổ chức muốn review/trace là điều kiện bắt buộc cần định nghĩa severity và dùng profile kiểm tương ứng, không tắt review/suspect cho qua. Stamp là dấu toàn vẹn nội dung, không là chữ ký người đã duyệt hay chứng cứ test đã chạy.

**Ghép vào xưởng:** định danh requirement → acceptance case → test/artifact thực thi; reviewer chịu trách nhiệm tính đúng của link; bật cổng được kiểm bằng fixture đứt link/thay parent/chưa review; lưu log và trạng thái inactive có giải thích. So với Markdown+ADR, Doorstop thêm trace/stamp; so với hệ ALM thương mại, cần tự đánh giá SSO, audit, phân quyền và workflow phê duyệt — **(chưa xác minh)** những khả năng ALM đó trong đợt này.

**Bằng chứng:** [LICENSE](https://github.com/doorstop-dev/doorstop/blob/f5f2bef01a99c92210cad2713079f09cc4aed876/LICENSE.md) · [Call validate](https://github.com/doorstop-dev/doorstop/blob/f5f2bef01a99c92210cad2713079f09cc4aed876/doorstop/cli/commands.py) · [CI đa OS/Python](https://github.com/doorstop-dev/doorstop/blob/f5f2bef01a99c92210cad2713079f09cc4aed876/.github/workflows/_common.yml). LGPL của công cụ không tự quyết định license tài liệu yêu cầu do người dùng viết; phân phối/nhúng thư viện cần xem nghĩa vụ tương ứng.

<a id="structurizr-model-code-boundary"></a>

## 3. Structurizr: một mô hình tạo nhiều view, vẫn cần kiểm mã riêng

| Thuộc tính | Giá trị |
|---|---|
| Repo/tác giả | `structurizr/structurizr` — Simon Brown, tác giả C4 |
| License | Apache-2.0 cho cây đã đọc; không suy sang dịch vụ thương mại |
| Phiên bản/phạm vi | `e3a736a90194d3ac692ad7b5c1c7a48287355347`, 2026-11-04; `code-read` |
| Vai trò | DSL/model cho context/container và nhiều view từ cùng mô hình |
| Tích hợp | Workspace DSL/JSON trong repo thiết kế, validate bằng toolchain ghim phiên bản |

[README monorepo](https://github.com/structurizr/structurizr/blob/e3a736a90194d3ac692ad7b5c1c7a48287355347/README.md) giới thiệu reference implementation C4 và đường `local`/playground. Không dùng đường dẫn `structurizr/dsl` như repo hiện hành: thao tác Git tới đường đó trả `Repository not found` trong phiên; mã DSL đọc được nằm trong monorepo này. Kết quả truy cập không tự xác định nguyên nhân archive/xoá/đổi quyền của repo cũ.

[`ValidateCommand`](https://github.com/structurizr/structurizr/blob/e3a736a90194d3ac692ad7b5c1c7a48287355347/structurizr-application/src/main/java/com/structurizr/command/ValidateCommand.java) load workspace, round-trip JSON để kích hoạt validation và tải themes để kiểm truy cập. Vì vậy `validate` không chỉ là parser offline nếu workspace dùng tài nguyên mạng; cũng **không kiểm rằng import/dependency trong code ứng với sơ đồ**. [DSL parser](https://github.com/structurizr/structurizr/blob/e3a736a90194d3ac692ad7b5c1c7a48287355347/structurizr-dsl/src/main/java/com/structurizr/dsl/StructurizrDslParser.java) có `setRestricted` tắt nhóm tính năng như plugin/script/filesystem. Không mặc định coi DSL từ nguồn lạ là dữ liệu thụ động; host/CLI có bật chế độ nào cần kiểm riêng, chưa thử runtime trong đợt này.

**Ghép vào xưởng:** lưu mô hình + ADR gắn ID boundary; review diff views theo thay đổi hệ thống; dùng parser/validator đúng phiên bản và giới hạn tài nguyên tham chiếu; ghép dependency-cruiser/ArchUnit hoặc kiểm phù hợp ngôn ngữ để chặn drift mã. So với Mermaid/PlantUML, giá trị ở shared semantic model nhiều view; so với bản đồ lấy từ source, đây là kiến trúc khai báo cần người giữ đúng.

**Bằng chứng:** [LICENSE](https://github.com/structurizr/structurizr/blob/e3a736a90194d3ac692ad7b5c1c7a48287355347/LICENSE) · [CI JDK21/Maven](https://github.com/structurizr/structurizr/blob/e3a736a90194d3ac692ad7b5c1c7a48287355347/.github/workflows/maven.yml). CI hiện loại nhóm `IntegrationTest`; không gọi “mọi integration đã được test” từ việc job build tồn tại.

<a id="dependency-cruiser-architecture-gates"></a>

## 4. dependency-cruiser: biến luật dependency JS/TS thành cổng

| Thuộc tính | Giá trị |
|---|---|
| Repo/tác giả | `sverweij/dependency-cruiser` — Sander Verweij |
| License | MIT |
| Phiên bản/phạm vi | `e6517db02e169f3db5c838bb1565ebd0fefeb452`, 2026-11-04; `code-read` |
| Vai trò | Graph dependency + rule forbidden/required theo cấu trúc JS/TS |
| Tích hợp | Dev dependency ghim lockfile, config rule được review cùng kiến trúc |

[README](https://github.com/sverweij/dependency-cruiser/blob/e6517db02e169f3db5c838bb1565ebd0fefeb452/README.md) minh hoạ chặn import từ production sang test và phát hiện dependency/cycle. Dùng quy tắc thể hiện boundary thật — ví dụ domain không import UI/DB adapter, package không vượt public entry point — thay vì chỉ xuất một đồ thị rồi gọi là kiểm kiến trúc.

**Bẫy cổng:** [CLI callsite](https://github.com/sverweij/dependency-cruiser/blob/e6517db02e169f3db5c838bb1565ebd0fefeb452/src/cli/index.mjs) trả exit code từ reporter. [JSON reporter](https://github.com/sverweij/dependency-cruiser/blob/e6517db02e169f3db5c838bb1565ebd0fefeb452/src/report/json.mjs) đặt `exitCode: 0`, trong khi [Error reporter](https://github.com/sverweij/dependency-cruiser/blob/e6517db02e169f3db5c838bb1565ebd0fefeb452/src/report/error.mjs) dùng `summary.advisedExitCode` (fallback `summary.error`). Vì vậy chạy `--output-type json` rồi thấy lệnh thành công chưa chứng minh không vi phạm. Dùng reporter `err` làm gate, giữ JSON/graph làm artifact riêng hoặc có consumer kiểm summary rõ. Không áp kết luận này sang mọi reporter.

**Ghép vào xưởng:** bắt đầu vài rule error quan trọng; fixture cố tình import trái lớp/cycle phải làm gate fail, fixture hợp lệ phải pass; kiểm alias/tsconfig và phạm vi include/exclude; baseline nợ cũ phải có owner và không được tăng âm thầm. Static graph không thể bao phủ mọi dependency được tạo động, network call hay cấu hình runtime; nối mô hình Structurizr và test tích hợp. ArchUnit phù hợp Java, kiểm kiến trúc riêng từng ngôn ngữ hoặc rule monorepo có sẵn là lựa chọn thay thế; không thêm dependency-cruiser chỉ để có graph nếu pipeline hiện tại đã chặn đủ boundary.

**Bằng chứng:** [LICENSE](https://github.com/sverweij/dependency-cruiser/blob/e6517db02e169f3db5c838bb1565ebd0fefeb452/LICENSE) · [Rule defaults](https://github.com/sverweij/dependency-cruiser/blob/e6517db02e169f3db5c838bb1565ebd0fefeb452/src/cli/init-config/config-template.mjs) · [CI tự kiểm dependency/test](https://github.com/sverweij/dependency-cruiser/blob/e6517db02e169f3db5c838bb1565ebd0fefeb452/.github/workflows/ci.yml). Nhiều rule khởi tạo là warning; severity phải phù hợp hợp đồng của đội.

<a id="oasdiff-compatibility-gates"></a>

## 5. oasdiff: tương thích API là quyết định release, không chỉ là báo cáo diff

| Thuộc tính | Giá trị |
|---|---|
| Repo/nhóm | `oasdiff/oasdiff` — nhóm oasdiff |
| License | Apache-2.0 |
| Phiên bản/phạm vi | `aa8a46f666d73479c542cd089037cc4989b6e42d`, 2026-11-04; `code-read` |
| Vai trò | So OpenAPI base/revision, phân loại thay đổi và breaking changes |
| Tích hợp | CLI/binary hoặc container đã ghim digest tại pipeline API |

[Tài liệu compatibility](https://github.com/oasdiff/oasdiff/blob/aa8a46f666d73479c542cd089037cc4989b6e42d/docs/BREAKING-CHANGES.md) phân biệt contract với server có thể chấp nhận dữ liệu rộng hơn. Thêm field request bắt buộc có thể phá client ngay khi server tự bù default; spec dùng cho SDK/gateway/validator cũng là khách hàng của thay đổi. Cần chọn policy theo API công bố, không suy từ vài request nội bộ vẫn trả 200.

[Command breaking](https://github.com/oasdiff/oasdiff/blob/aa8a46f666d73479c542cd089037cc4989b6e42d/internal/breaking_changes.go) mặc định `--fail-on` rỗng; [Callsite severity/exit](https://github.com/oasdiff/oasdiff/blob/aa8a46f666d73479c542cd089037cc4989b6e42d/internal/changelog.go) chỉ bật điều kiện fail khi được cấu hình. Cổng mẫu ở repo đích là `oasdiff breaking --fail-on ERR base.yaml revision.yaml`; nếu policy chặn cả warning, chọn `WARN` có chủ ý. Một lệnh chỉ in breaking changes có thể thoát 0. Base phải là spec **của bản đã phát hành/consumer đang dùng**, không tự so với một file đã bị ghi đè trong cùng PR.

**Giới hạn:** spec diff không gọi server, không biết authorization thực, logic idempotency hay dữ liệu production. Ghép Spectral (mục 05) để lint quy ước, Schemathesis và consumer/integration tests (mục 30) cho runtime; AsyncAPI/Protobuf/GraphQL cần bộ compatibility đúng định dạng, không ép vào OpenAPI. Ignore/severity override là thay đổi policy cần review, không là cách làm check xanh.

**Bằng chứng:** [LICENSE](https://github.com/oasdiff/oasdiff/blob/aa8a46f666d73479c542cd089037cc4989b6e42d/LICENSE) · [Fixture exit-code](https://github.com/oasdiff/oasdiff/blob/aa8a46f666d73479c542cd089037cc4989b6e42d/internal/breaking_files_test.go) · [CI Go đa OS](https://github.com/oasdiff/oasdiff/blob/aa8a46f666d73479c542cd089037cc4989b6e42d/.github/workflows/go.yml). Test nguồn củng cố ngữ nghĩa intended nhưng chưa được chạy lại trong phiên này.

## 6. Chuỗi áp dụng cho xưởng và cổng nghiệm thu

1. **Chọn phạm vi tối thiểu:** requirement ID + acceptance examples; ghi constraint bảo mật, dữ liệu, latency, chi phí và owner. Dùng Markdown trước; thêm Doorstop khi trace/version ảnh hưởng đáng kể.
2. **Chốt quyết định:** ADR nêu 2–4 phương án và vì sao chọn; vẽ context/container/boundary trong mô hình có ID. Thiết kế API/data ownership trước khi chia task cho nhiều coding agent.
3. **Biến boundary thành rule:** dependency-cruiser hoặc công cụ đúng ngôn ngữ chặn import trái lớp. Giữ fixture tốt/xấu chứng minh cổng có tác dụng, không chỉ kiểm file config tồn tại.
4. **Chốt compatibility:** spec phát hành có version/hash; lint + breaking diff + test runtime/consumer trước release. Thử thêm required field, xoá operation, đổi auth requirement để kiểm cổng bắt điều dự án coi là breaking.
5. **Truy vết artifact:** requirement → ADR/boundary → change/PR → test run → artifact digest → release/rollback. Link ID không được tự gán trạng thái “đã kiểm” nếu chỉ có file test mà chưa có run.
6. **Đánh giá drift:** khi requirement/API/dependency thay đổi, review lại downstream và giữ exception có owner/hạn xem lại. Đo defect lọt qua boundary, compatibility incident và thời gian tìm nguyên nhân; không đo bằng số sơ đồ hay số dòng requirement.

**Đầu ra đủ dùng:** một thay đổi mẫu đi qua toàn chuỗi, một ca cố tình vi phạm từng cổng bị bắt, một ca hợp lệ được nhận, và hồ sơ rõ phần chưa được kiểm. Đây là mục tiêu áp dụng ở dự án của xưởng, không phải tuyên bố `stored` đã dựng hay benchmark các công cụ đó.

## 7. Nguồn chuẩn và tuyến đọc chéo

- Nguồn gốc từng claim nằm ở permalink full SHA ngay trong hồ sơ; tham khảo mô hình gốc [C4](https://c4model.com/) và đặc tả [OpenAPI](https://spec.openapis.org/oas/latest.html) để chọn đúng phiên bản trước tích hợp. Hai trang chuẩn là đường tra cứu bổ sung, không được dùng để nâng mức kiểm vượt các file đã đọc ở đây.
- [Mục 04](../04-protocols-standards/README.md): phiên bản wire/conformance cho MCP/A2A; khác compatibility của API nghiệp vụ.
- [Mục 09](../09-engineering-checklists/README.md): checklist quyết định; [mục 13](../13-dev-stack-devops/README.md): toolchain; [mục 23](../23-own-repos-lessons/README.md): bài học repo chủ kho.
- [Mục 28](../28-product-discovery-experimentation/README.md): nhu cầu và phép đo sản phẩm; mục 30/34 bổ sung nghiệm thu runtime và data/identity.
