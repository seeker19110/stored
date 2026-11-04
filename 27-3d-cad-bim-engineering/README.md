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

## 5b. Kiểm bài giới thiệu CanvasAnvil (codingfeng101/canvasanvil): “bản vẽ cải tạo nội thất chuyên nghiệp từ một câu” phần lớn là ảnh do model sinh ảnh vẽ (bài người dùng gửi, đọc mã 3/11/2026)

> Bài người dùng gửi: "CanvasAnvil: The AI Studio For Everything… turns a single sentence into a full set of professional interior renovation drawings, including floor plans, ceiling layouts, and material lists… Open source: github.com/codingfeng101/canvasanvil". Đã clone `--filter=blob:none` đủ lịch sử, HEAD `27f1aea1b8a7e2fcfe01cb2610a3d4e54db4987e` (1/11/2026). **Không cài, không chạy.**

### 5b.1 Hồ sơ nhanh

| Thuộc tính | Giá trị (3/11/2026) |
|---|---|
| Repo | https://github.com/codingfeng101/canvasanvil · **113★, 8 fork**, tạo 24/1/2026 (GitHub search API). README ghi v2.2.0 |
| License | MIT, "Copyright (c) 2026 CodingFeng101" |
| Lịch sử | 157 commit, một tác giả (hai email), **88 commit có trailer Co-Authored-By Claude** |
| Là gì | Web app React + Vite + server Node với 4 workspace: sơ đồ (flowchart, xuất XML), nội thất ("CAD"), slide (PPT xuất PDF hoặc PPT dạng ảnh), chỉnh ảnh. Dùng API tương thích OpenAI do người dùng tự cấu hình (`server/ai/model.ts`: key, base URL, model theo từng request) |

### 5b.2 Kiểm nhận định "bộ bản vẽ kỹ thuật chuyên nghiệp"

Đọc `client/workspaces/cad/lib/tasks.ts` và `resources/prompts/cad/`:

1. LLM sinh **plan JSON + một mặt bằng 2D dạng SVG** (`svg-markup.ts`, `apply-cad-patch.ts`). Đây là phần duy nhất có hình học vector.
2. Agent "Master Renovation Scheme" viết phương án tổng làm nguồn chung.
3. Với mỗi tờ (Renovation Plan Layout, Floor Finish Plan, **Reflected Ceiling Plan**, Wall Setting-Out, **MEP**, Elevations, Detail Drawings, hai bảng phân tích), một agent riêng viết **prompt JSON "directly usable by the downstream image generator"** (`images-agents/reflected-ceiling-plan.md`). Prompt này được gửi tới model sinh ảnh (`server/ai/image.ts`: `/images/generations`, gpt-image hoặc dall-e-3, hoặc cổng chat tương thích).
4. Bảng vật tư (BOM) do LLM viết từ plan JSON + SVG (`bom-prompt.md`).

| Nhận định | Kết quả |
|---|---|
| "single sentence → full set of drawings" | ✅ đúng về luồng: một yêu cầu kéo theo chuỗi agent sinh đủ các tờ |
| "professional interior renovation drawings… floor plans, ceiling layouts" | ⚠️ **phần lớn là ảnh raster do AI vẽ**, không phải bản vẽ CAD: không có lớp (layer), kích thước không đo được, không xuất DXF, DWG hay IFC (grep dxf, dwg, ifc trong `client/` và `server/` không có kết quả). Kích thước, ký hiệu đèn, MEP và chi tiết trên ảnh có thể trông hợp lý nhưng không có cơ chế kiểm tra nào ràng buộc chúng với mặt bằng SVG |
| "material lists" | ⚠️ văn bản do LLM viết, không tính từ hình học; số lượng cần kiểm lại |
| "Open source" | ✅ MIT. Nhưng cần API key trả phí của bên thứ ba cho LLM và model sinh ảnh |

### 5b.3 Dữ liệu và rủi ro

- **Langfuse tùy chọn ghi toàn bộ nội dung**: nếu đặt `LANGFUSE_PUBLIC_KEY` (`server/telemetry/langfuse.ts`), mọi request chat ghi `recordInputs` và `recordOutputs`, và `server/routes/chat.ts` lấy **IP của người dùng (`x-forwarded-for`) làm `userId`**. Không bật thì không gửi. Ai tự host cho người khác dùng cần thông báo việc này và cân nhắc dữ liệu cá nhân (mục 18 §4e).
- Nội dung yêu cầu và ảnh tham chiếu đi tới nhà cung cấp model mà người dùng cấu hình.
- Dự án nhỏ, một tác giả; README ghi "PRs welcome", 0 issue mở.

### 5b.4 Đặt trong bối cảnh mục 27

- Khác với các cổng kiểm theo biểu diễn ở §3 (IFC/IDS, hình học có kiểm), CanvasAnvil cho ra **ảnh minh họa phương án**: dùng được để trao đổi ý tưởng với khách hoặc làm moodboard, **không dùng làm hồ sơ thi công** khi chưa có người có chứng chỉ dựng lại trên CAD/BIM thật.
- Nếu muốn agent ra bản vẽ đo được: sinh hình học (SVG/DXF/IFC) rồi kiểm bằng máy (kích thước phòng, va chạm, IDS), như các stack ở §5, thay vì nhờ model sinh ảnh vẽ tờ hoàn chỉnh.

**Nguồn §5b:** bài người dùng gửi 3/11/2026 · clone https://github.com/codingfeng101/canvasanvil HEAD `27f1aea1b8a7e2fcfe01cb2610a3d4e54db4987e`: https://github.com/codingfeng101/canvasanvil/blob/27f1aea1b8a7e2fcfe01cb2610a3d4e54db4987e/README.md · https://github.com/codingfeng101/canvasanvil/blob/27f1aea1b8a7e2fcfe01cb2610a3d4e54db4987e/LICENSE · https://github.com/codingfeng101/canvasanvil/blob/27f1aea1b8a7e2fcfe01cb2610a3d4e54db4987e/client/workspaces/cad/lib/tasks.ts · https://github.com/codingfeng101/canvasanvil/blob/27f1aea1b8a7e2fcfe01cb2610a3d4e54db4987e/resources/prompts/cad/images-agents/reflected-ceiling-plan.md · https://github.com/codingfeng101/canvasanvil/blob/27f1aea1b8a7e2fcfe01cb2610a3d4e54db4987e/resources/prompts/cad/bom-prompt.md · https://github.com/codingfeng101/canvasanvil/blob/27f1aea1b8a7e2fcfe01cb2610a3d4e54db4987e/server/ai/image.ts · https://github.com/codingfeng101/canvasanvil/blob/27f1aea1b8a7e2fcfe01cb2610a3d4e54db4987e/server/ai/model.ts · https://github.com/codingfeng101/canvasanvil/blob/27f1aea1b8a7e2fcfe01cb2610a3d4e54db4987e/server/telemetry/langfuse.ts · https://github.com/codingfeng101/canvasanvil/blob/27f1aea1b8a7e2fcfe01cb2610a3d4e54db4987e/server/routes/chat.ts · GitHub search API `repo:codingfeng101/canvasanvil` 3/11/2026.

<a id="factory-2026-11-04"></a>

## 6. Nâng trần 4/11/2026: CAD tạo bằng mã phải có hợp đồng đơn vị và vòng xuất–nhập

**Trần hiện tại:** §3 đã tách mesh/B-rep/BIM và §4 có đọc lại host. Xưởng còn cần fixture hồi quy hình học, unit/tolerance qua exporter và quy trình kiểm artifact độc lập với ảnh preview. Các ngưỡng dưới đây do dự án tích hợp chọn theo domain, không phải một chuẩn an toàn chế tạo chung.

| Lựa chọn | Điểm mạnh phù hợp | Bằng chứng nghiệm thu | Giới hạn phải giữ |
|---|---|---|---|
| CadQuery dưới đây | Sinh B-rep tham số bằng Python, hợp backend/CI không GUI | Validity + số solid + bbox/volume + STEP round-trip có đơn vị | Kernel hợp lệ không chứng minh chi tiết sản xuất được |
| FreeCAD ở §2 | Workbench/tài liệu tham số và GUI cho kỹ sư | Recompute, mở/lưu/mở lại file, đọc giá trị sau chỉnh | Phiên bản host/add-in và headless cần kiểm riêng |
| OpenSCAD ở §2 | Mô hình CSG bằng mã dễ review | Render backend đã ghim, solid/dimension sau export | Preview không thay render; STL không tự định nghĩa unit |
| IfcOpenShell/IfcTester ở §2 | BIM và yêu cầu thông tin IDS | Schema IFC + IDS + GUID/property/domain | IDS pass chỉ phủ yêu cầu được mô tả |
| Trimesh ở §2 | Kiểm mesh độc lập sau tessellation | Component, winding, volume, bbox/scale | Không thay kernel B-rep, kiểm độ bền hoặc DFM |

<a id="cadquery"></a>

### CadQuery: exporter và importer đều mang tham số đơn vị

| Thuộc tính | Giá trị |
|---|---|
| Repo / SHA / license | [CadQuery/cadquery](https://github.com/CadQuery/cadquery), `8178185a24a035c9af7f4679033be14267f6a6ef`, Apache-2.0; OCP/OCCT và dependency kiểm quyền riêng |
| Kiểm chứng 2026-11-04 | `code-read`: README/LICENSE, `shapes.py`, export/import STEP và workflow container; chưa tạo shape/build hoặc chạy kernel |
| Cơ chế cụ thể | `Shape.isValid()` gọi `BRepCheck_Analyzer(...).IsValid()`. `export()` nhận `unit="MM"`, `outputUnit`, chuyển tham số cho `exportStep`; import STEP nhận `unit="MM"`, đặt target cascade unit trước khi đọc, để OCCT scale từ unit khai trong file. |
| Cổng đã có trong upstream | Workflow `apptainer_build.yml` build container rồi gọi `pytest tests/`; sự hiện diện workflow không xác nhận run thành công hoặc mọi distro/phiên bản kernel đều tương đương. |
| Tích hợp | Khóa schema tham số, phiên bản CadQuery/OCP/OCCT, đơn vị đầu vào/xuất/nhập và tolerance theo model units. Lưu script + input manifest + checksum STEP/STL + số đo sau reimport. |
| Hạn chế / rủi ro | Một cờ valid không chứng minh đúng kích thước, không self-intersection ở mọi phép biểu diễn, wall thickness, clearance hoặc tuân quy chuẩn. Python script do agent sinh cần sandbox/quota như mã thực thi, không mở quyền ghi host tùy ý. |

**Tuyến nâng sâu:**

1. Mô tả yêu cầu thành schema: đơn vị, hệ tọa độ, miền tham số, dung sai kích thước, số solid và feature quan trọng; có fixture biên/âm (rỗng, chiều âm, giao nhau, lỗ nhỏ hơn ngưỡng). Agent chỉ đề xuất tham số/lệnh trong capability của host.
2. Sinh bằng engine đã ghim, giữ artifact gốc và lịch sử tham số; kiểm exception, recompute, validity, số solid, bbox và volume có ý nghĩa. Sai một cổng không được che bằng ảnh render đẹp.
3. Export STEP theo unit rõ, import vào tiến trình sạch bằng target unit rõ; so dimensions/volume theo tolerance nghiệp vụ. Đối với STL, mang unit trong manifest ngoài file và kiểm lại scale ở consumer.
4. Chạy hồi quy hình học trên nhiều bộ tham số; so invariants/đặc trưng thay vì hash binary đơn độc vì kernel/export có thể đổi byte không đổi hình. Với BIM thêm schema/IDS; với host thật kiểm save/reopen và readback.
5. Kỹ sư có thẩm quyền duyệt DFM/tải trọng/quy chuẩn theo ngữ cảnh; giữ report đo và người duyệt bên cạnh model revision. Nối [mục 30](../30-software-testing-quality/README.md) cho contract/hồi quy, [31](../31-software-supply-chain-security/README.md) cho dependency/asset.

**Đã đổi so với đợt trước:** bổ sung CadQuery như một tuyến B-rep chạy trong pipeline, và kiểm đơn vị ở cả hai phía STEP thay vì chỉ ghi unit trong prompt. Không suy ảnh CanvasAnvil ở §5b thành artifact CAD đo được. **Nguồn §6:** [README.md](https://github.com/CadQuery/cadquery/blob/8178185a24a035c9af7f4679033be14267f6a6ef/README.md) · [LICENSE](https://github.com/CadQuery/cadquery/blob/8178185a24a035c9af7f4679033be14267f6a6ef/LICENSE) · [cadquery/occ_impl/shapes.py](https://github.com/CadQuery/cadquery/blob/8178185a24a035c9af7f4679033be14267f6a6ef/cadquery/occ_impl/shapes.py) · [exporter STEP](https://github.com/CadQuery/cadquery/blob/8178185a24a035c9af7f4679033be14267f6a6ef/cadquery/occ_impl/exporters/__init__.py) · [importer STEP](https://github.com/CadQuery/cadquery/blob/8178185a24a035c9af7f4679033be14267f6a6ef/cadquery/occ_impl/importers/__init__.py) · [.github/workflows/apptainer_build.yml](https://github.com/CadQuery/cadquery/blob/8178185a24a035c9af7f4679033be14267f6a6ef/.github/workflows/apptainer_build.yml).

## Nguồn

Các permalink trong từng hồ sơ cố định đúng phiên bản đã đọc; số sao/trạng thái archive là snapshot GitHub API ngày 2026-11-02. Không chạy mã, huấn luyện model hoặc tái lập kết quả của upstream.
