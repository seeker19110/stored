# 27 · 3D, CAD/BIM & Engineering Agents

Mục dành cho hình học và dữ liệu kỹ thuật có thể kiểm. Ngày đọc **2026-11-02**: đọc LICENSE, README, CI, API/validator được dẫn; **chưa chạy CAD host, geometry engine hoặc corpus conformance**.

## 1. Ba miền có tiêu chí đúng khác nhau

| Miền | Biểu diễn / công cụ | Tiêu chí đầu ra |
|---|---|---|
| Render / game asset | Mesh, material, UV; Blender, glTF | Hình nhìn thấy, topology/triangle budget, UV/material, license asset |
| CAD / chế tạo | Solid B-rep, tham số, STEP; FreeCAD/OpenSCAD | Kích thước, đơn vị, dung sai, solid hợp lệ, lắp ráp/khả năng chế tạo |
| BIM / AEC | IFC entity/property/relationship; IfcOpenShell | Schema, classification, property/unit, IDS, phối hợp vấn đề qua BCF |

Mesh kín không chứng minh dung sai chế tạo; B-rep hợp lệ không chứng minh tải trọng; IFC qua schema không chứng minh đủ thông tin bàn giao. Không suy ảnh render đẹp thành kiểm chứng kỹ thuật.

Case study sẵn có: [Dhcb-Tools: Revit/AutoCAD, dryRun→confirm→snapshot](../23-own-repos-lessons/README.md#44-dhcb-tools--agent-cho-cadbim-desktop-revit--autocad) và [Blender: verify ladder, hash scene/spec](../23-own-repos-lessons/README.md#61-design-os-3d-blender--agent-điều-khiển-blender-ship-được-phần-in-3d). Các nguồn từng ghi theo docs nội bộ vẫn giữ nhãn chưa xác minh; phần dưới đọc trực tiếp upstream.

## 2. Hồ sơ nền tảng và chuẩn

### IfcOpenShell

| Thuộc tính | Giá trị |
|---|---|
| Repo | [IfcOpenShell/IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell) |
| Snapshot | 2,917★, chưa archive (GitHub API, 2026-11-02); HEAD `28bae192780e` ngày 2026-10-30 |
| License | LGPL-3.0-or-later (core); GPL-3.0-or-later (Bonsai); [file thật](https://github.com/IfcOpenShell/IfcOpenShell/blob/28bae192780ebd34936441f1f7bc1ffb9d282be9/README.md) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/IfcOpenShell/IfcOpenShell/blob/28bae192780ebd34936441f1f7bc1ffb9d282be9/src/ifctester/ifctester/ids.py); [CI tại cùng commit](https://github.com/IfcOpenShell/IfcOpenShell/tree/28bae192780ebd34936441f1f7bc1ffb9d282be9/.github/workflows); đọc mã/đặc tả, chưa chạy |

Monorepo có core IFC, IfcTester, IfcDiff, IfcClash và Bonsai. IfcTester open/from_string có validate mặc định false: chỉ bỏ bước validate() tường minh; decode vẫn qua XMLSchema và bắt lỗi, nên không kết luận validation mặc định bị tắt. Kiểm schema IDS, đánh giá requirements và kiểm schema IFC là các cổng riêng.

**Tích hợp và giới hạn:** Chọn đúng package thay vì gán một license cho cả monorepo. IDS pass chỉ bao phủ yêu cầu đã viết; thêm kiểm schema/geometry/domain và fixture âm. API/core version phải khớp exporter.

### FreeCAD

| Thuộc tính | Giá trị |
|---|---|
| Repo | [FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD) |
| Snapshot | 35,047★, chưa archive (GitHub API, 2026-11-02); HEAD `66644dee63d3` ngày 2026-11-01 |
| License | LGPL-2.1-or-later; thành phần riêng kiểm thêm; [file thật](https://github.com/FreeCAD/FreeCAD/blob/66644dee63d3d260f1e0b9a8517d1a13631e903f/LICENSE) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/FreeCAD/FreeCAD/blob/66644dee63d3d260f1e0b9a8517d1a13631e903f/src/Mod/Part/App/TopoShape.cpp); [CI tại cùng commit](https://github.com/FreeCAD/FreeCAD/tree/66644dee63d3d260f1e0b9a8517d1a13631e903f/.github/workflows); đọc mã/đặc tả, chưa chạy |

CAD tham số/B-rep dựa OpenCascade; TopoShape::isValid dùng BRepCheck_Analyzer. Đây là cổng hình học cụ thể, không chỉ ảnh chụp hoặc exit code.

**Tích hợp và giới hạn:** Dùng Python/GUI/CLI theo workbench và build. Kiểm recompute, valid solid, kích thước và export/reimport STEP; API/workbench/plugin khác license và khả năng headless. Chưa chạy model thật.

### OpenSCAD

| Thuộc tính | Giá trị |
|---|---|
| Repo | [openscad/openscad](https://github.com/openscad/openscad) |
| Snapshot | 10,572★, chưa archive (GitHub API, 2026-11-02); HEAD `8e8df3ddae29` ngày 2026-11-01 |
| License | GPL-2.0-or-later + ngoại lệ liên kết CGAL; [file thật](https://github.com/openscad/openscad/blob/8e8df3ddae295e8667cbc9f6c4fbb7c88b0ec45b/COPYING) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/openscad/openscad/blob/8e8df3ddae295e8667cbc9f6c4fbb7c88b0ec45b/src/openscad.cc); [CI tại cùng commit](https://github.com/openscad/openscad/tree/8e8df3ddae295e8667cbc9f6c4fbb7c88b0ec45b/.github/workflows); đọc mã/đặc tả, chưa chạy |

Mô hình CSG viết bằng mã, thuận lợi diff và tái sinh; CLI có export và phân biệt render/preview. Hợp chi tiết tham số hơn thao tác trực tiếp mesh nghệ thuật.

**Tích hợp và giới hạn:** Ghim engine/backend, tham số, font và dependency; kiểm số solid/dimension sau xuất. File STL không tự mang hợp đồng đơn vị hay dung sai; license output/asset kiểm riêng.

### Trimesh

| Thuộc tính | Giá trị |
|---|---|
| Repo | [mikedh/trimesh](https://github.com/mikedh/trimesh) |
| Snapshot | 3,716★, chưa archive (GitHub API, 2026-11-02); HEAD `6c158cce2265` ngày 2026-10-23 |
| License | MIT; [file thật](https://github.com/mikedh/trimesh/blob/6c158cce226500fc64b12acd265af0cf01d1c212/LICENSE.md) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/mikedh/trimesh/blob/6c158cce226500fc64b12acd265af0cf01d1c212/trimesh/base.py); [CI tại cùng commit](https://github.com/mikedh/trimesh/tree/6c158cce226500fc64b12acd265af0cf01d1c212/.github/workflows); đọc mã/đặc tả, chưa chạy |

is_watertight kiểm mỗi cạnh thuộc hai mặt; is_volume còn kiểm winding, center_mass hữu hạn và volume dương. Đây là các predicate khác nhau, không dùng một cờ watertight đại diện mọi kiểm.

**Tích hợp và giới hạn:** API Python cho mesh loading/analysis; giữ scale/unit và hash mesh. is_volume chưa chứng minh self-intersection-free, wall thickness, độ bền hay tính chế tạo; không thay kernel B-rep.

### buildingSMART IDS

| Thuộc tính | Giá trị |
|---|---|
| Repo | [buildingSMART/IDS](https://github.com/buildingSMART/IDS) |
| Snapshot | 329★, chưa archive (GitHub API, 2026-11-02); HEAD `870f9c4e6e8f` ngày 2026-09-25 |
| License | CC-BY-ND-4.0 (đặc tả); [file thật](https://github.com/buildingSMART/IDS/blob/870f9c4e6e8f414e737b4d84ca1aa9b46fc6c8f3/LICENSE) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/buildingSMART/IDS/blob/870f9c4e6e8f414e737b4d84ca1aa9b46fc6c8f3/Schema/ids.xsd); [CI tại cùng commit](https://github.com/buildingSMART/IDS/tree/870f9c4e6e8f414e737b4d84ca1aa9b46fc6c8f3/.github/workflows); đọc mã/đặc tả, chưa chạy |

Chuẩn XML mô tả thông tin IFC cần bàn giao; repo có XSD, testcases và workflow AuditAllIdsFiles. Dùng làm corpus kiểm validator thay vì chỉ tin tuyên bố hỗ trợ IDS.

**Tích hợp và giới hạn:** Ghim release/spec corpus, phân applicability và requirements; đặc tả có ND nên không tự gắn license phần mềm/đổi tên bản sửa. XSD validity và compliance với model là hai phép kiểm.

### buildingSMART BCF-XML

| Thuộc tính | Giá trị |
|---|---|
| Repo | [buildingSMART/BCF-XML](https://github.com/buildingSMART/BCF-XML) |
| Snapshot | 263★, chưa archive (GitHub API, 2026-11-02); HEAD `bc48611d0d7a` ngày 2023-11-28 |
| License | CC-BY-ND-4.0 (đặc tả); [file thật](https://github.com/buildingSMART/BCF-XML/blob/bc48611d0d7a1587f028a2b69677a1aafd5cd0a8/LICENSE) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/buildingSMART/BCF-XML/blob/bc48611d0d7a1587f028a2b69677a1aafd5cd0a8/.github/workflows/check-test-cases.yml); [CI tại cùng commit](https://github.com/buildingSMART/BCF-XML/tree/bc48611d0d7a1587f028a2b69677a1aafd5cd0a8/.github/workflows); đọc mã/đặc tả, chưa chạy |

Chuẩn trao đổi issue/viewpoint, có schema/testcases; default branch release_3_0 tại lần đọc. Không mặc định tương thích BCF2.1 của một host với3.0.

**Tích hợp và giới hạn:** Chọn version theo consumer, kiểm GUID/viewpoint/model revision và round-trip. CI CheckTestCases là bằng chứng repo có kiểm spec, kho chưa chạy corpus; khác BCF API và khác kiểm model IFC.

## 3. Cổng kiểm theo biểu diễn

| Lớp kiểm | Bằng chứng tối thiểu | Giới hạn |
|---|---|---|
| Contract | Đơn vị, trục tọa độ, kích thước, hệ dung sai, phiên bản schema và giới hạn xuất | Prompt có số đo không thay spec máy đọc được |
| Mesh | Số component, bounding box, watertight, winding, volume hữu hạn/dương | Chưa chứng minh wall thickness, khoảng hở hoặc độ bền |
| B-rep | Shape validity, solid count, volume/bbox, round-trip STEP với sai số đã định | Chưa chứng minh thiết kế có thể gia công/lắp ráp |
| BIM | IFC schema, yêu cầu IDS áp dụng đúng tập phần tử, unit/property/classification | IDS chỉ kiểm yêu cầu đã viết; không bao trùm toàn bộ quy chuẩn xây dựng |
| Trao đổi vấn đề | BCF version, GUID/viewpoint liên kết đúng model revision | BCF đóng issue không tự chứng minh model được sửa đúng |
| Host thật | Revit/AutoCAD/Blender version, file mở/save/reopen, ảnh và dữ liệu sau lệnh | Test bridge/CLI trên Linux không chứng minh add-in chạy đúng trong host |

## 4. Kiến trúc agent sửa model

1. Đọc capability và schema của host; tra tên tham số có thật. Agent đề xuất lệnh có phạm vi phần tử cụ thể.
2. Tạo preview/dry-run với **model revision, operation hash, affected IDs** và ước lượng tài nguyên. Query lớn có limit/pagination.
3. Xác nhận gắn với chính preview; model thay đổi thì preview hết hiệu lực. Dùng transaction/snapshot theo khả năng host; không gọi undo là rollback đã kiểm.
4. Thực thi, lấy IDs thay đổi và đọc lại giá trị/hình học. Timeout có thể là đã chạy: đối soát operation ID trước retry.
5. Chạy cổng rẻ trước render đắt; bằng chứng khóa vào hash scene/spec. Ghi `passed`, `failed`, `not-run` theo từng check.
6. Kiểm xuất/nhập lại bằng bộ đọc độc lập khi cần bàn giao; giữ native file cùng STEP/IFC/mesh. Liên kết [04](../04-protocols-standards/README.md), [11](../11-browser-computer-use-sandbox/README.md), [21](../21-autonomous-workflows/README.md), [23](../23-own-repos-lessons/README.md).

## 5. Chọn stack theo nhu cầu

- **BIM kiểm thông tin:** IFC + IDS chính thức → IfcTester → báo cáo phần tử lỗi → BCF. Cần test requirement bị thiếu/sai và trường hợp không áp dụng, không chỉ fixture xanh.
- **Chi tiết tham số:** FreeCAD/OpenSCAD → kiểm hình học → STEP/STL → kiểm kích thước lại; muốn giao dịch trong Revit dùng host bridge của case study, không thay bằng mesh generator.
- **Asset mesh:** Blender → Trimesh → kiểm kỹ thuật + render review; license texture/font/model là lớp riêng với license code.

## Nguồn

Các permalink trong từng hồ sơ cố định đúng phiên bản đã đọc; số sao/trạng thái archive là snapshot GitHub API ngày 2026-11-02. Không chạy mã, huấn luyện model hoặc tái lập kết quả của upstream.
