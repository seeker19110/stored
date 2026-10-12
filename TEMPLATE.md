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
| ★ (ngày) | ~N ★ (YYYY-MM-DD, nguồn: …) |
| Vì sao đáng tham khảo | 2–4 gạch đầu dòng: điểm khác biệt, bài học kiến trúc, cách áp dụng |
| Hạn chế / rủi ro | … |
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
        w.writerow([p['name'],p.get('repo') or '',p.get('url') or (f"https://github.com/{p['repo']}" if p.get('repo') else ''),p['category'],p.get('license') or '',p['stars'] if p['stars'] is not None else '',p['open_source'],p['section'],p['notes']])
PY
```

## Quy ước
- Số sao luôn kèm ngày và nguồn; dùng `null` nếu không có số tin cậy.
- Nhận định chưa kiểm chứng độc lập ghi rõ **(chưa xác minh)**.
- Ưu tiên nguồn chính thức (repo, docs, paper) hơn blog so sánh.
