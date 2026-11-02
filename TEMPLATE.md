# Mẫu thêm dự án vào kho

Sao chép khối dưới vào README của chuyên mục phù hợp (hoặc tạo chuyên mục mới `NN-ten-chuyen-muc/README.md`), rồi thêm một dòng vào `data/projects.json` (và chạy lại script sinh CSV).

```markdown
### <Tên dự án>
| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/<owner>/<repo> |
| Mô tả 1 dòng | … |
| Loại | coding-agent / agent-framework / protocol / ui-library / design-tool / checklist / … |
| License | … |
| Phiên bản đã đọc | Full commit SHA/tag; model/checkpoint/dataset revision nếu liên quan |
| Kiểm chứng | Ngày ISO; docs-read / code-read / checks-run / reproduced; phạm vi và phần chưa chạy |
| ★ (ngày) | ~N ★ (YYYY-MM-DD, nguồn: …) |
| Vì sao đáng tham khảo | 2–4 gạch đầu dòng: điểm khác biệt, bài học kiến trúc, cách áp dụng |
| Hạn chế / rủi ro | … |
| Tích hợp | Cách dùng từ dự án khác: gói/lệnh cài, API hoặc giao thức, điều kiện license khi nhúng, cấu hình an toàn tối thiểu |
| Liên quan | mục NN, dự án X, Y |
| Nguồn | URL đã đọc |
```

## Sinh lại CSV từ JSON

```bash
python3 -I - <<'PY'
import json,csv
d=json.load(open('data/projects.json',encoding='utf-8'))
with open('data/projects.csv','w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['name','repo','url','category','license','stars_est','open_source','section','notes'])
    for p in d['projects']:
        w.writerow([p['name'],p.get('repo') or '',p.get('url') or '',p['category'],p.get('license') or '',p['stars'] if p['stars'] is not None else '',p['open_source'],p['section'],p['notes']])
PY
```

## Quy ước

- Số sao luôn kèm ngày và nguồn; dùng `null` nếu không có số tin cậy.
- Cột `url` của CSV chỉ điền khi JSON có `url` riêng; dự án chỉ có `repo` để trống (đừng suy ra URL GitHub, sẽ làm đổi mọi dòng cũ).
- Nhận định chưa kiểm chứng độc lập ghi rõ **(chưa xác minh)**.
- Ưu tiên nguồn chính thức (repo, docs, paper) hơn blog so sánh.

## Metadata và bằng chứng cho hồ sơ mới hoặc đọc lại

Catalog theo [data/projects.schema.json](data/projects.schema.json), phương pháp theo [METHOD.md](METHOD.md). Giữ `id` ổn định cho mỗi thực thể; cùng `repo` có thể có sản phẩm/plugin/skill khác nhau. `profile_path` trỏ hồ sơ gốc, `profile_anchor` trỏ đúng heading hoặc HTML id của phạm vi đã kiểm; phần đọc lại có thể nằm ở chuyên mục khác với hồ sơ gốc.

Khi đã kiểm hồ sơ, thêm `last_verified_at` (ISO), `verified_ref` (full SHA với GitHub repo), `verification_level`, `sources` (permalink triển khai/LICENSE/CI) và `profile_anchor`. Không backfill các trường kiểm chứng cho hồ sơ cũ chỉ từ metadata API. Mức `code-read` không nói rằng đã chạy test upstream.

JSON có metadata đầy đủ; CSV giữ chín cột cũ để consumer không bị đổi contract. Cổng kiểm so từng ô theo đúng thứ tự JSON và kiểm ngày/nguồn/neo của hồ sơ đã chuẩn hóa.
