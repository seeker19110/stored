# Đóng góp và đính chính

Đề xuất một repo, một chuẩn hoặc sửa một nhận định bằng link nguồn gốc, vấn đề nó giải quyết, khác biệt với hồ sơ đã có và lý do đáng khảo sát. Tìm trong `data/projects.json` trước; cùng upstream có thể có nhiều thực thể nhưng không nhân bản cùng hồ sơ chỉ để xuất hiện ở nhiều mục.

Đọc [WORKFLOW.md](WORKFLOW.md), [METHOD.md](METHOD.md) và [TEMPLATE.md](TEMPLATE.md). Khi thêm/sửa hồ sơ:

- Đọc LICENSE thật, file triển khai/callsite và CI tại commit được ghi; phân biệt tuyên bố của tác giả với điều tự xác minh.
- Nêu ít nhất 2–4 lựa chọn cùng loại hoặc dẫn bảng so sánh đã có. Ghi giới hạn, điều kiện license, dữ liệu rời máy và điểm chưa chạy khi liên quan.
- Giữ ID/neo cũ ổn định; thêm mục con hoặc đính chính tại chỗ. Hồ sơ cũ thiếu metadata không được tự gán mức code-read.
- Cập nhật Markdown, JSON, CSV, nguồn và mục lục cùng một PR. Với thay đổi lớn, thêm tuyến đọc chéo; bàn giao bài học X-Templates theo hợp đồng hiện có.
- Tóm tắt bằng lời của người đóng góp, không chép nguyên bài viết hoặc nội dung prompt có quyền không rõ. License upstream không tự cấp quyền cho asset/dataset/model của bên khác.
- Nêu quan hệ với dự án được giới thiệu hoặc lợi ích liên quan nếu có; đính chính claim sai cần nguồn cho phiên bản cụ thể.

Kiểm trước PR:

```bash
python3 -I scripts/check_catalog.py
python3 -I scripts/test_check_catalog.py
npx --yes markdownlint-cli2 '**/*.md'
```

Các kiểm trên chạy trên chính kho; không cần cài/chạy code của dự án được khảo sát. Không đặt app, skill, plugin hoặc demo thực thi trong kho. Các vấn đề của repo ngoài được mô tả như dữ kiện nghiên cứu; việc sửa thuộc repo đó.

Kho hiện chưa có giấy phép chung cho nội dung tự biên soạn và script. Không suy giấy phép của dự án được dẫn sang nội dung của kho; việc cấp phép chung cần chủ sở hữu lựa chọn riêng.
