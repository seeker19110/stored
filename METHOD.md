# Phương pháp nghiên cứu và đọc bằng chứng

Kho lưu hồ sơ và đánh giá để dự án khác chọn và tích hợp công cụ. Mỗi kết luận có phạm vi phiên bản và thời điểm; số sao, tên tác giả hoặc việc có CI không thay bằng chứng công cụ đáp ứng tác vụ.

## 1. Đơn vị đánh giá và tiêu chí chọn

Một hồ sơ là một **thực thể**: sản phẩm, thư viện, chuẩn, plugin hoặc skill. Một upstream có thể chứa nhiều thực thể với license và cơ chế khác nhau. `id` nhận diện hồ sơ ổn định; `repo` không phải khóa duy nhất. `section` là nơi giữ hồ sơ gốc; chuyên mục khác dẫn về đó thay vì nhân bản nhận định.

Chọn dự án khi nó đem lại một cơ chế khác, một baseline hữu ích, chuẩn gốc, cổng kiểm hoặc bài học thất bại có bằng chứng. So 2–4 lựa chọn cùng nhiệm vụ; nêu cả điều kiện khiến lựa chọn nhỏ, tất định hoặc không dùng agent phù hợp hơn. Không cộng các tiêu chí tùy ý thành một điểm chất lượng chung.

## 2. Các mức kiểm chứng

| `verification_level` | Đã làm | Chưa tự chứng minh |
|---|---|---|
| `unassessed` hoặc không có trường | Hồ sơ cũ chưa chuẩn hóa mức kiểm trong catalog | Không có nghĩa hồ sơ Markdown chưa từng được nghiên cứu |
| `docs-read` | Đọc tài liệu/đặc tả tại nguồn được dẫn | Tuyên bố của tác giả đúng với triển khai |
| `code-read` | Đọc LICENSE, file triển khai và CI liên quan tại commit cụ thể | Mã chạy được, default có hiệu lực trong mọi cấu hình, benchmark tái lập |
| `checks-run` | Chạy kiểm với log, môi trường, lệnh và kết quả được dẫn | Đúng ở môi trường khác hoặc toàn bộ tính năng |
| `reproduced` | Tái lập phép đo được mô tả, đối chiếu baseline và artifact | Kết quả tổng quát cho domain/phần cứng khác |

Các mức mô tả việc đã làm trong **phạm vi hồ sơ**, không phải chứng chỉ an toàn. Đợt mở rộng 2026-11-02 chỉ đọc mã/đặc tả upstream; các phép kiểm chạy trong phiên là kiểm dữ liệu và tài liệu của chính kho. Ghi riêng điều **(chưa xác minh)** và phần chưa chạy.

## 3. Một kết luận có thể kiểm lại

- Ghi claim cụ thể, `last_verified_at`, `verified_ref` full SHA, nguồn permalink và file/hàm liên quan. Với chuẩn, ghi phiên bản đặc tả/corpus; với model ghi checkpoint revision riêng.
- Đọc đường gọi và điều kiện kích hoạt: có hàm chặn chưa đủ nếu callsite không gọi; default trong constructor có thể bị CLI/config ghi đè. Thiếu kết quả trong tìm kiếm không chứng minh toàn repo không có cơ chế.
- Phân biệt HEAD nhánh mặc định, ngày commit và `pushed_at`; push có thể thuộc nhánh/tag khác. Archive=false không chứng minh dự án được bảo trì tích cực.
- License tách code, weights, dữ liệu, assets và enterprise subdirectory. `NOASSERTION`, `null`, không có LICENSE và license hạn chế là các trạng thái khác nhau; `open_source` không thay việc đọc điều kiện ở hồ sơ.
- Nguồn ngoài dùng để kiểm chéo: đặc tả, paper, changelog và tài liệu chính thức. Claim marketing, benchmark do nhà bán tự công bố hoặc docs nội bộ của repo khác phải được nhận diện đúng nguồn.
- Kết luận quan trọng được người/agent khác cố bác bỏ bằng nguồn gốc. Khi sai một phần, sửa cả README lẫn catalog; giữ giới hạn thay vì làm câu văn mạnh hơn bằng suy đoán.

## 4. Mẫu báo cáo phép đo

| Trường | Nội dung cần ghi |
|---|---|
| Quyết định | Cần chọn gì; metric chính và điều kiện chấp nhận |
| Phiên bản | Repo SHA/tag, model/checkpoint, dataset/config revision |
| Môi trường | OS, CPU/GPU/RAM, driver/runtime, cấu hình provider |
| Corpus | Domain/ngôn ngữ, số mẫu, cách lấy mẫu/split, contamination và quyền sử dụng |
| Baseline | Cùng input, ngân sách, phần cứng hoặc lý do khác nhau |
| Cách chạy | Lệnh/cấu hình, seed, số lần lặp, warm/cold cache, concurrency |
| Kết quả | Chất lượng từng nhóm, latency/phân vị, chi phí, tỷ lệ lỗi/bỏ mẫu, khoảng bất định |
| Artifact | Log/kết quả/checksum và nơi lưu có quyền truy cập phù hợp |
| Giới hạn | Không chạy, lỗi môi trường, cấu hình chưa phủ; không đổi inconclusive thành pass |

Kho giữ mô tả, kết quả và link artifact; implementation benchmark/demo thuộc repo thực hiện. Không nâng một kết quả của upstream thành kết quả tự chạy của `stored`.

## 5. Tuổi dữ liệu và bảo trì

`meta.snapshot_date` là ngày tập hợp catalog, **không phải** ngày xác minh mọi hồ sơ. Trường `last_verified_at` chỉ có khi đã kiểm hồ sơ đó; không tự backfill bằng ngày hôm nay cho hồ sơ cũ. `stars` cần ngày/nguồn và chỉ giúp nhận diện quy mô quan tâm.

Trước tích hợp, kiểm lại claim biến động cao: license, ownership, endpoint/telemetry, security advisory, model/provider dependency và trạng thái hỗ trợ. Có thể lọc JSON theo thiếu metadata hoặc ngày cũ để lập lượt rà; không coi việc thêm một lịch tự động là đã hoàn thành xác minh.

Catalog có [JSON Schema](data/projects.schema.json); [cổng kiểm](scripts/check_catalog.py) kiểm dữ liệu cơ bản, CSV từng ô và sự tồn tại của neo nội bộ. Cổng offline không xác minh nội dung trang nguồn hoặc chứng minh ngữ nghĩa claim đúng.
