# Quy trình vận hành kho (WORKFLOW)

## Phạm vi kho

Quy ước do người dùng đặt ra (2026-10-12): **kho `stored` chỉ lưu hồ sơ repo và đánh giá, để các dự án khác tham khảo và tích hợp.**

- **Có trong kho:** hồ sơ và đánh giá từng repo (README chuyên mục), catalog máy-đọc-được (`data/projects.json`, `data/projects.csv`), nguồn (`SOURCES.md`), cùng quy trình và mẫu giữ những thứ đó nhất quán.
- **Không đặt trong kho:** code, skill, plugin hay công cụ để dùng (chúng thuộc dự án tích hợp); danh sách việc cần làm cho repo khác; nhật ký sửa kho (đã có lịch sử git). Phát hiện về một repo được ghi thành dữ kiện đánh giá kèm ngày đọc; việc sửa làm ở chính repo đó.
- **Hạ tầng của kho** chỉ gồm phần giữ dữ liệu đúng: CI `markdownlint` và `scripts/check_catalog.py`.
- **Dự án khác dùng kho:** đọc README chuyên mục để xem đánh giá; lọc `data/projects.json` theo `category`, `license`, `open_source`, số sao để chọn ứng viên. Trước khi tích hợp, kiểm lại ngày đọc và mọi chỗ ghi **(chưa xác minh)**.

## Khi người dùng gửi một link (repo, bài viết, sản phẩm)

Quy ước do người dùng đặt ra (2026-10-12): **mọi link gửi lên đều phải được nghiên cứu kỹ từ nhiều nguồn khác, rồi cập nhật vào kho `stored`.**

### Các bước bắt buộc

1. **Đọc nguồn gốc**: README, cấu trúc thư mục thật (không tin README mô tả), file chính (docs, agent/prompt, CONTRIBUTING, LICENSE), lịch sử commit, issues/PR, releases.
2. **Hồ sơ tác giả/tổ chức**: profile, dự án liên quan, kênh (blog/YouTube/X), độ uy tín.
3. **Nguồn bên ngoài**: tìm web về dự án (bài viết, thảo luận, review, HN/Reddit/dev.to, paper); ghi rõ nguồn nào là chính thức, nguồn nào là blog.
4. **Dự án tương tự / thay thế**: ít nhất 2–4 lựa chọn cùng loại, so sánh quy mô, cách tiếp cận, license, điểm khác biệt.
5. **Phân tích**: giá trị cốt lõi, bài học kiến trúc, cách ghép vào các mục khác của kho, hạn chế/rủi ro (license, tuổi đời, bảo trì, mâu thuẫn trong tài liệu), điều kiện khi tích hợp (license khi nhúng, cấu hình an toàn tối thiểu, phương án thay thế).
6. **Cập nhật kho**:
   - README của chuyên mục phù hợp (hoặc tạo chuyên mục mới `NN-…/README.md`) theo [TEMPLATE.md](TEMPLATE.md);
   - `data/projects.json` (+ sinh lại `data/projects.csv`);
   - `SOURCES.md`; mục lục & phần tóm tắt trong `README.md` gốc nếu có nhận định mới;
   - ghi ngày khảo sát và đánh dấu **(chưa xác minh)** cho điều chưa kiểm chứng.
7. **Commit & push** lên nhánh làm việc với message mô tả rõ dự án được thêm.
8. **PR & auto-merge** (quy ước từ 2026-10-12): nhánh mặc định là `main`. Mỗi đợt cập nhật đi qua PR; **luôn bật auto-merge** cho PR ngay khi tạo. Nếu PR đã ở trạng thái "clean" (không có check chờ) thì GitHub không cho bật auto-merge → merge trực tiếp (merge commit). Sau khi merge, tạo lại nhánh làm việc từ `main` cho đợt kế tiếp. Từ 2026-10-12 `main` có required checks `markdownlint` + `catalog (json + csv)` (bật tay trong Settings → Branches), nên auto-merge là đường đi bình thường; lệnh bật phải gọi **ngay sau khi tạo PR**, trước khi check chạy xong (PR #4, #5 bị "already clean" vì gọi muộn).

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
