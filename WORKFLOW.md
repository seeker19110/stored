# Quy trình vận hành kho (WORKFLOW)

## Khi người dùng gửi một link (repo, bài viết, sản phẩm)

Quy ước do người dùng đặt ra (2026-10-12): **mọi link gửi lên đều phải được nghiên cứu kỹ từ nhiều nguồn khác, rồi cập nhật vào kho `stored`.**

### Các bước bắt buộc

1. **Đọc nguồn gốc**: README, cấu trúc thư mục thật (không tin README mô tả), file chính (docs, agent/prompt, CONTRIBUTING, LICENSE), lịch sử commit, issues/PR, releases.
2. **Hồ sơ tác giả/tổ chức**: profile, dự án liên quan, kênh (blog/YouTube/X), độ uy tín.
3. **Nguồn bên ngoài**: tìm web về dự án (bài viết, thảo luận, review, HN/Reddit/dev.to, paper); ghi rõ nguồn nào là chính thức, nguồn nào là blog.
4. **Dự án tương tự / thay thế**: ít nhất 2–4 lựa chọn cùng loại, so sánh quy mô, cách tiếp cận, license, điểm khác biệt.
5. **Phân tích**: giá trị cốt lõi, bài học kiến trúc, cách ghép vào các mục khác của kho, hạn chế/rủi ro (license, tuổi đời, bảo trì, mâu thuẫn trong tài liệu), gợi ý hành động.
6. **Cập nhật kho**:
   - README của chuyên mục phù hợp (hoặc tạo chuyên mục mới `NN-…/README.md`) theo [TEMPLATE.md](TEMPLATE.md);
   - `data/projects.json` (+ sinh lại `data/projects.csv`);
   - `SOURCES.md`; mục lục & phần tóm tắt trong `README.md` gốc nếu có nhận định mới;
   - ghi ngày khảo sát và đánh dấu **(chưa xác minh)** cho điều chưa kiểm chứng.
7. **Commit & push** lên nhánh làm việc với message mô tả rõ dự án được thêm.
8. **PR & auto-merge** (quy ước từ 2026-10-12): nhánh mặc định là `main`. Mỗi đợt cập nhật đi qua PR; **luôn bật auto-merge** cho PR ngay khi tạo. Nếu PR đã ở trạng thái "clean" (không có check chờ) thì GitHub không cho bật auto-merge → merge trực tiếp (merge commit). Sau khi merge, tạo lại nhánh làm việc từ `main` cho đợt kế tiếp.

### Tiêu chuẩn chất lượng

- Mọi con số (sao, fork, commit, ngày) phải kèm ngày đọc.
- Ưu tiên bằng chứng trực tiếp (file trong repo, trang chính thức) hơn bài tổng hợp.
- Ghi lại các mâu thuẫn phát hiện được (ví dụ README nói A nhưng file thật là B).
- Không sao chép nguyên văn nội dung dài của dự án; tóm tắt + trích dẫn ngắn + link.
- **Grep cổng đang chạy, đừng đọc văn xuôi** (từ `projects-template/docs/framework/adopt-from-outside.md`, 2026-10-12): với repo có harness, đọc `settings.json`, hook, CI, script trước; README chỉ là tuyên bố.
- **Ba cột khi học repo ngoài**: với mỗi cơ chế ghi *kho đã có & sâu hơn / đã có nhưng nông hơn / chưa có*; chỉ cột 2–3 mới sinh việc.
- **Cảnh báo nguồn dựng**: số sao/tên dự án lấy từ bài tổng hợp hoặc docs nội bộ của repo khác phải ghi "(theo docs nội bộ, chưa xác minh)"; mục 19 từng ghi sai ~100× vì tin aggregator.
- **Mirror/fork**: nếu repo là clone không sửa (ví dụ `reveser` = `morluto/rea`), cite upstream, không ghi là của chủ kho.

## Cập nhật định kỳ

- Mỗi quý: rà lại số sao, trạng thái bảo trì (archive, đổi tên, mua lại), license của các dự án đầu bảng.
- Khi một chuẩn/giao thức ra phiên bản mới (MCP, A2A, AG-UI, Agent Skills): cập nhật mục 04.
