# Quy trình vận hành kho (WORKFLOW)

## Phạm vi kho

Quy ước do người dùng đặt ra (2026-10-12): **kho `stored` chỉ lưu hồ sơ repo và đánh giá, để các dự án khác tham khảo và tích hợp.**

- **Có trong kho:** hồ sơ và đánh giá từng repo (README chuyên mục), catalog máy-đọc-được (`data/projects.json`, `data/projects.csv`), nguồn (`SOURCES.md`), cùng quy trình và mẫu giữ những thứ đó nhất quán.
- **Không đặt trong kho:** code, skill, plugin hay công cụ để dùng (chúng thuộc dự án tích hợp); danh sách việc cần làm cho repo khác; nhật ký sửa kho (đã có lịch sử git). Phát hiện về một repo được ghi thành dữ kiện đánh giá kèm ngày đọc; việc sửa làm ở chính repo đó.
- **Hạ tầng của kho** chỉ gồm phần giữ dữ liệu đúng: CI `markdownlint` và `scripts/check_catalog.py`.
- **X-Templates dùng kho:** đọc [X-TEMPLATES.md](X-TEMPLATES.md) (hợp đồng, tổng hợp chéo, bàn giao) và `data/xt-handoff.json`; trích phần mới theo khoảng commit ghi ở §6 của file đó.
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
   - nếu bài học có thể thành yêu cầu cho khung **X-Templates**: grep ID trong `framework/` của X-Templates, phân cột *deeper/shallower/missing/not_adding*, thêm dòng `XT-H-NNN` vào `data/xt-handoff.json` (và bảng §4 của [X-TEMPLATES.md](X-TEMPLATES.md) với đợt lớn). Chỉ đề xuất, không sửa repo X-Templates.
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

## Nâng trần định kỳ (2 tuần/lần)

Quy ước do người dùng đặt ra (2026-11-02): **cứ 2 tuần nâng trần toàn bộ 23 mục một lần, tìm bằng mọi cách trên internet và GitHub.** Một tác vụ định kỳ mở phiên mới (model Opus, chế độ ultracode, effort high) vào ngày 1 và 15 hằng tháng và chạy đúng prompt dưới đây. Muốn đổi cách chạy thì sửa prompt ở đây, rồi cập nhật cả tác vụ định kỳ.

"Nâng trần" nghĩa là nâng mức chất lượng cao nhất mà dự án đạt được khi dùng một mục. Ba lớp hay thiếu nhất là: **chuẩn/đặc tả gốc**, **cổng kiểm bằng máy** (benchmark, conformance, eval, lint, scanner, CI) và **công cụ đầu bảng** chưa có trong catalog. Đợt đầu là 2/11/2026 (PR #102).

### Prompt chạy tự động

```text
Bạn đang chạy đợt "nâng trần" định kỳ 2 tuần/lần cho kho seeker19110/stored (kho tri thức tiếng Việt, chỉ lưu hồ sơ + đánh giá repo). Chạy ở chế độ ultracode trên model Opus: dùng workflow nhiều agent cho mọi bước nặng; mọi agent() trong workflow đặt `effort: "high"` (bước kiểm đối kháng có thể dùng cao hơn). Tìm bằng mọi cách trên internet và GitHub.

0. Chuẩn bị
- Nếu phiên chưa có checkout của kho: gọi add_repo (owner `seeker19110`, repo `stored`, access `push`), clone theo hướng dẫn trả về và làm việc trong thư mục đó. Nếu công cụ GitHub MCP (tạo PR, bật auto-merge) không có trong phiên thì vẫn làm hết, push nhánh, và ở báo cáo cuối đưa link tạo PR để người dùng bấm.
- Đọc WORKFLOW.md (phạm vi kho, quy trình, tiêu chuẩn chất lượng, mục này), TEMPLATE.md và X-TEMPLATES.md.
- Tìm đợt nâng trần gần nhất: `git log --oneline --grep "nâng trần" -i | head` và các heading "Nâng trần <ngày>" trong `NN-*/README.md`. Mốc thời gian của đợt này = từ ngày đợt trước đến hôm nay.
- Làm trên nhánh phiên được chỉ định; nếu PR cũ của nhánh đã merge thì tạo lại nhánh từ `main`.

1. Quét (song song, chia 23 mục cho ~6 agent, mỗi agent 3–4 mục)
Mỗi mục tìm repo/chuẩn/công cụ MỚI hoặc VỪA ĐỔI trong mốc thời gian, ưu tiên ba lớp: chuẩn gốc, cổng kiểm bằng máy, công cụ đầu bảng. Dùng mọi kênh:
- GitHub search API (`gh api -X GET search/repositories -f q="<từ khoá> stars:>300 pushed:>=<ngày đợt trước>" -f sort=stars`, thêm `created:>=` để bắt repo mới; `search/issues`, `search/commits` khi cần). `gh api repos/...` có thể bị chặn với repo ngoài phạm vi, nên dùng search.
- WebSearch (mode "extended" cho tin mới/ngách) và WebFetch: blog chính thức, changelog/release notes, Hacker News, Reddit, dev.to, arXiv/paper, trang chuẩn (W3C, IETF, OWASP, NIST, OpenSSF, CNCF, OpenTelemetry, MCP/A2A spec), awesome-list, GitHub Trending.
- Rà lại các repo đã ghi ở các phần "Nâng trần" đợt trước: archive, đổi tên/chủ, đổi license, telemetry mới, bản phát hành lớn, số sao.
Không thêm trùng: grep `repo` trong `data/projects.json` trước. Mỗi mục mới phải được đọc mã: clone `--depth 1 --filter=blob:none` vào scratchpad, đọc LICENSE (license thật, không tin nhãn GitHub), README, CI, file chính. Không chạy, cài hay build mã repo ngoài. Xoá clone khi xong.

2. Viết
- Mỗi mục có phát hiện: thêm phần `## <số kế tiếp>. Nâng trần <d/m/yyyy>: <tóm tắt> (định kỳ)` trước phần Nguồn cuối của README mục. Nội dung: Trần hiện tại · bảng repo mới (Repo | Lớp | ★ · license (ngày) | Commit cuối | Vì sao nâng trần | Rủi ro) · "Đã đổi từ đợt trước" · Stack nâng trần (3–6 bước, tham chiếu § có sẵn) · dòng `**Nguồn §…:**`.
- Mục không có gì đáng thêm thì không viết phần rỗng, chỉ ghi vào báo cáo cuối.
- Agent chỉ sửa README mục mình. Agent không sửa `data/*`, `SOURCES.md`, `README.md` gốc hay `X-TEMPLATES.md`. Mỗi agent trả JSON gồm: sections, projects (schema giống data/projects.json, category thuộc meta.categories), sources, xt_lessons.

3. Kiểm (bắt buộc trước khi commit)
- Tra lại tất định bằng GitHub search API cho mọi repo mới: tên, số sao (lệch ≤ 5%), archived.
- Kiểm đối kháng: mỗi mục chọn tối đa 4 nhận định quan trọng nhất (license thật, telemetry, đổi tên/archive, trạng thái spec, con số dẫn tới khuyến nghị). Mỗi nhận định do một agent độc lập cố bác bỏ bằng nguồn gốc. Áp mọi bản sửa "sai một phần/bị bác bỏ" vào README và catalog.
- Điều chưa kiểm được ghi **(chưa xác minh)**.

4. Gộp
- Gộp projects vào `data/projects.json` (khử trùng theo repo), sinh lại `data/projects.csv` theo TEMPLATE.md. Thêm mục "Bổ sung <ngày> (nâng trần định kỳ)" vào `SOURCES.md`. Thêm một mục tóm tắt mới vào "Bức tranh tổng thể" của `README.md` gốc.
- X-Templates: clone công khai `https://github.com/seeker19110/x-templates`. Mỗi bài học được một agent grep `framework/` để tìm 1–3 ID thật và xếp cột deeper/shallower/missing/not_adding; dòng trùng XT-H cũ ghi duplicate. Thêm XT-H-NNN vào `data/xt-handoff.json` và một bảng §4x mới trong `X-TEMPLATES.md`, ghi commit X-Templates đã đối chiếu.
- Chạy `python3 scripts/check_catalog.py` và `npx --yes markdownlint-cli2` trên mọi file đã sửa, sửa đến khi sạch.

5. Phát hành
- Commit theo từng nhóm mục rồi push. Mở PR vào `main` và bật auto-merge NGAY sau khi tạo (theo bước 8 của quy trình). Nếu PR đã "clean" thì merge trực tiếp.
- Bàn giao X-Templates: add_repo push `seeker19110/X-Templates`, thêm `research/<ngày>-stored-delta-ceiling.md` theo mẫu các note `stored-delta` trước. Note chỉ là đề xuất: không sửa `framework/`, không nêu tên model/phiên AI trong nội dung. Mở PR theo template của repo đó, không bật auto-merge. Sau đó ghi "Đã gửi đề xuất" kèm link PR vào §6 `X-TEMPLATES.md` của stored (PR nhỏ, có auto-merge).

6. Báo cáo cuối (ngắn, tiếng Việt)
Số mục có phần mới, số dự án thêm (catalog trước → sau), phát hiện quan trọng nhất (license, telemetry, archive, chuẩn mới), kết quả kiểm đối kháng, link các PR, và những gì chưa làm được kèm lý do. Nếu một bước bị chặn quyền thì dừng bước đó, ghi rõ và làm tiếp phần còn lại; không lách quyền.
```
