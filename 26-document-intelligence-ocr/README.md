# 26 · Document Intelligence, OCR & Structured Extraction

Từ ảnh/PDF đến dữ liệu có cấu trúc kèm bằng chứng. Ngày đọc **2026-11-02**: đã đọc LICENSE, README, CI và các file triển khai được dẫn; **không cài, chạy model hoặc tái lập benchmark**. Điểm số và giá do tác giả công bố không phải kết quả của kho.

## 1. Chọn đúng lớp xử lý

| Đầu vào / nhu cầu | Hướng ưu tiên | Phải kiểm trước khi chọn |
|---|---|---|
| PDF có lớp text tốt, cần trích văn bản | Parser native/Docling (đã có mục 10) | Thứ tự đọc, text ẩn/sai encoding, bảng và tọa độ |
| Scan sạch, CPU, cần searchable PDF | Tesseract + OCRmyPDF | Language pack `vie`, DPI, xoay/nghiêng; searchable không có nghĩa hiểu bảng |
| Bảng, công thức, layout phức tạp | PP-StructureV3; so Docling/Marker/MinerU | Chất lượng từng thành phần, model revision, quyền weights |
| Corpus PDF cho LLM | olmOCR, có đánh dấu fallback và lỗi trang | Ngôn ngữ/domain, trang bị loại, tốc độ/chi phí trên corpus riêng |
| Hóa đơn/hợp đồng ra JSON | Parser + schema extractor + đối chiếu trường | Citation trang/bbox, tổng tiền/đơn vị, trường thiếu phải null |
| So sánh parser | OmniDocBench + tập tài liệu đích | Version dữ liệu/metric, contamination, không suy điểm công khai sang tiếng Việt |

**Ranh giới:** mục 16 là tài liệu phần mềm/docs-for-AI; mục 10 là retrieval/memory; mục này giữ độ trung thực khi biến tài liệu gốc thành dữ liệu. Docling có hồ sơ gốc ở [10 §6b](../10-local-llm-rag-memory/README.md#6b-nâng-cấp-31102026-rà-repo-lớn), không thêm bản ghi trùng.

## 2. Hồ sơ và bằng chứng

### PaddleOCR

| Thuộc tính | Giá trị |
|---|---|
| Repo | [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) |
| Snapshot | 92,120★, chưa archive (GitHub API, 2026-11-02); HEAD `dab3fe353790` ngày 2026-09-16 |
| License | Apache-2.0 (code); weights kiểm riêng; [file thật](https://github.com/PaddlePaddle/PaddleOCR/blob/dab3fe35379033fdcb2d0e9572fac0b36c9a9ebf/LICENSE) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/PaddlePaddle/PaddleOCR/blob/dab3fe35379033fdcb2d0e9572fac0b36c9a9ebf/paddleocr/_pipelines/pp_structurev3.py); [CI tại cùng commit](https://github.com/PaddlePaddle/PaddleOCR/tree/dab3fe35379033fdcb2d0e9572fac0b36c9a9ebf/.github/workflows); đọc mã/đặc tả, chưa chạy |

PP-StructureV3 tách layout/OCR/table và có phép ghép Markdown nhiều trang; wrapper kiểm tổ hợp language/OCR version. Nên so pipeline có tọa độ với VLM theo loại tài liệu, không lấy một điểm SOTA của README đại diện mọi tác vụ.

**Tích hợp và giới hạn:** API Python/pipeline qua PaddleX; ghim backend và model revision. Quyền từng checkpoint và độ đúng biểu mẫu tiếng Việt chưa xác minh; chưa chạy CPU/GPU.

### olmOCR

| Thuộc tính | Giá trị |
|---|---|
| Repo | [allenai/olmocr](https://github.com/allenai/olmocr) |
| Snapshot | 19,814★, chưa archive (GitHub API, 2026-11-02); HEAD `f7cfe4c22098` ngày 2026-03-25 |
| License | Apache-2.0 (code); weights kiểm riêng; [file thật](https://github.com/allenai/olmocr/blob/f7cfe4c22098b154c76b6ec950d1c0a464eecf8d/LICENSE) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/allenai/olmocr/blob/f7cfe4c22098b154c76b6ec950d1c0a464eecf8d/olmocr/pipeline.py); [CI tại cùng commit](https://github.com/allenai/olmocr/tree/f7cfe4c22098b154c76b6ec950d1c0a464eecf8d/.github/workflows); đọc mã/đặc tả, chưa chạy |

Pipeline có retry, kiểm xoay và cờ is_fallback; mức fallback quá ngưỡng có thể loại cả tài liệu. --apply_filter là opt-in và filter trong mã giữ English/unknown, nên không bật như một bước làm sạch chung cho corpus tiếng Việt.

**Tích hợp và giới hạn:** Local GPU hoặc endpoint tương thích OpenAI; ghi lại trang fallback/bị bỏ. README có giá và benchmark do nhóm công bố, kho chưa tái lập; không suy giá đó sang hạ tầng khác.

### OCRmyPDF

| Thuộc tính | Giá trị |
|---|---|
| Repo | [ocrmypdf/OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) |
| Snapshot | 35,208★, chưa archive (GitHub API, 2026-11-02); HEAD `b457e9efa68c` ngày 2026-10-25 |
| License | MPL-2.0 (code); dependency licenses riêng; [file thật](https://github.com/ocrmypdf/OCRmyPDF/blob/b457e9efa68c3a46be2470ffb222ed1bccc4dcbc/LICENSE) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/ocrmypdf/OCRmyPDF/blob/b457e9efa68c3a46be2470ffb222ed1bccc4dcbc/src/ocrmypdf/_validation.py); [CI tại cùng commit](https://github.com/ocrmypdf/OCRmyPDF/tree/b457e9efa68c3a46be2470ffb222ed1bccc4dcbc/.github/workflows); đọc mã/đặc tả, chưa chạy |

Thêm lớp text để tìm kiếm trong PDF scan, có kiểm language pack tồn tại trước xử lý. Vai trò khác parser hiểu layout/schema; phù hợp bảo toàn PDF với OCR cơ bản.

**Tích hợp và giới hạn:** CLI/Python API nối Tesseract; kiểm version Ghostscript, language vie, sandbox và trần tài nguyên. PDF/A/searchable không chứng minh bảng/trường trích đúng.

### Tesseract

| Thuộc tính | Giá trị |
|---|---|
| Repo | [tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract) |
| Snapshot | 77,298★, chưa archive (GitHub API, 2026-11-02); HEAD `d1ebd2a789f8` ngày 2026-11-02 |
| License | Apache-2.0; [file thật](https://github.com/tesseract-ocr/tesseract/blob/d1ebd2a789f8220209d675c1d4bc18d7a25c8e26/LICENSE) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/tesseract-ocr/tesseract/blob/d1ebd2a789f8220209d675c1d4bc18d7a25c8e26/src/api/baseapi.cpp); [CI tại cùng commit](https://github.com/tesseract-ocr/tesseract/tree/d1ebd2a789f8220209d675c1d4bc18d7a25c8e26/.github/workflows); đọc mã/đặc tả, chưa chạy |

Engine OCR cổ điển có API Init/Recognize và xuất hOCR/TSV; làm baseline CPU để đo lợi ích thật của model lớn. Language pack là artifact phải ghim riêng.

**Tích hợp và giới hạn:** Thư viện C++/CLI, hoặc qua OCRmyPDF. Độ đúng phụ thuộc preprocessing/segmentation; không tự hiểu quan hệ bảng, ngữ nghĩa hóa đơn hay citation RAG.

### MinerU

| Thuộc tính | Giá trị |
|---|---|
| Repo | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) |
| Snapshot | 82,987★, chưa archive (GitHub API, 2026-11-02); HEAD `0ef2c20c4a56` ngày 2026-10-30 |
| License | Apache-2.0 + điều khoản bổ sung; [file thật](https://github.com/opendatalab/MinerU/blob/0ef2c20c4a56e68f81a66647f819d924ef2d89ce/LICENSE.md) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/opendatalab/MinerU/blob/0ef2c20c4a56e68f81a66647f819d924ef2d89ce/mineru/cli/commands/parse.py); [CI tại cùng commit](https://github.com/opendatalab/MinerU/tree/0ef2c20c4a56e68f81a66647f819d924ef2d89ce/.github/workflows); đọc mã/đặc tả, chưa chạy |

Reader cho agent có parse/read theo trang/block và locator ổn định. CLI thư viện tài liệu mặc định chỉ đọc nhóm trang đầu theo README, nên consumer phải đi tiếp theo continuation và kiểm tổng trang.

**Tích hợp và giới hạn:** License thật yêu cầu giấy phép riêng khi bạn và Affiliates tính gộp có MAU vượt 100 triệu hoặc doanh thu tháng vượt 20 triệu USD; dịch vụ online phải attribution. Không gắn nhãn Apache thuần/OSI. Ghim cache/config/model; quyền weights và độ bền locator sau thay tài liệu cần kiểm riêng.

### Marker

| Thuộc tính | Giá trị |
|---|---|
| Repo | [datalab-to/marker](https://github.com/datalab-to/marker) |
| Snapshot | 40,748★, chưa archive (GitHub API, 2026-11-02); HEAD `71dd5fd7e51a` ngày 2026-10-29 |
| License | Apache-2.0 (code); modified OpenRAIL-M (weights); [file thật](https://github.com/datalab-to/marker/blob/71dd5fd7e51ab24f8624b6ba2fcb6014b4e40ed4/LICENSE) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/datalab-to/marker/blob/71dd5fd7e51ab24f8624b6ba2fcb6014b4e40ed4/marker/converters/pdf.py); [CI tại cùng commit](https://github.com/datalab-to/marker/tree/71dd5fd7e51ab24f8624b6ba2fcb6014b4e40ed4/.github/workflows); đọc mã/đặc tả, chưa chạy |

PdfConverter dựng Document qua provider/builder/processor rồi renderer, cho phép output Markdown/JSON và xử lý riêng block. Cần đo lỗi từng tầng, nhất là khi thêm LLM sửa kết quả OCR.

**Tích hợp và giới hạn:** README tách code Apache khỏi model weights: sử dụng weights thương mại vượt điều kiện miễn phí cần license riêng. Không coi license code bao trùm weights; tắt/kiểm endpoint LLM tùy chọn trước tài liệu nhạy cảm.

### OmniDocBench

| Thuộc tính | Giá trị |
|---|---|
| Repo | [opendatalab/OmniDocBench](https://github.com/opendatalab/OmniDocBench) |
| Snapshot | 2,140★, chưa archive (GitHub API, 2026-11-02); HEAD `ea2d138c7d2e` ngày 2026-10-29 |
| License | Apache-2.0 (eval code); dataset kiểm riêng; [file thật](https://github.com/opendatalab/OmniDocBench/blob/ea2d138c7d2e185feb71ef8014e97d7206820b34/LICENSE) |
| Bằng chứng | [Triển khai/đặc tả](https://github.com/opendatalab/OmniDocBench/blob/ea2d138c7d2e185feb71ef8014e97d7206820b34/configs/end2end.yaml); [CI tại cùng commit](https://github.com/opendatalab/OmniDocBench/tree/ea2d138c7d2e185feb71ef8014e97d7206820b34/.github/workflows); đọc mã/đặc tả, chưa chạy |

Config end-to-end chấm text/reading order bằng edit distance, table bằng TEDS, formula bằng CDM/edit distance. Match có timeout/fallback; phải giữ config và lỗi evaluator cùng kết quả.

**Tích hợp và giới hạn:** Ghim version corpus lẫn code; v1.5 và v1.6 không mặc nhiên so cùng bảng. README/giấy phép eval không xác nhận quyền mọi trang dữ liệu, và corpus công khai chưa đại diện biểu mẫu tiếng Việt.

## 3. Cổng kiểm cho pipeline tài liệu

1. **Đầu vào bất biến:** hash file, số trang, nguồn/quyền sử dụng, loại native/scan, ngôn ngữ; giữ bản gốc. PDF không tin cậy xử lý trong sandbox, có trần trang/pixel/thời gian; không tự chạy nội dung nhúng.
2. **Chuẩn hóa có kiểm:** xoay/deskew/dewarp kèm ảnh trước/sau; chuẩn hóa NFC để chấm tiếng Việt nhưng giữ nguyên bản gốc phục vụ truy vết.
3. **Kết quả trung gian:** mỗi block có `document_hash`, `page`, `bbox` nếu parser cung cấp, `parser_ref`, `model_revision`, trạng thái OCR/fallback. Nếu parser chỉ ra Markdown, ghi rõ chưa có bbox; không bịa tọa độ.
4. **Trích schema:** kiểu dữ liệu, đơn vị, định dạng tiền/ngày và quy tắc cross-field; trường thiếu/không đọc được trả null + lý do. Citation phải trỏ đúng trang/vùng chứa giá trị; không chỉ kiểm JSON hợp lệ.
5. **Chấm tập đích:** CER/text edit distance, table TEDS hoặc độ đúng ô, reading order, precision/recall từng trường, tỷ lệ bỏ trang, p95 latency và chi phí/trang đạt yêu cầu. Ngưỡng lấy từ tác vụ; không dùng một điểm tổng để che lỗi trường quan trọng.
6. **Review có trọng tâm:** số tiền, mã số thuế, điều khoản và kích thước bản vẽ cần đối chiếu với ảnh gốc; độ tự tin model tự khai chưa đủ để bỏ bước này. Liên kết [07](../07-eval-observability/README.md), [12](../12-ai-security-guardrails/README.md), [18](../18-vietnam-community/README.md), [24](../24-ai-data-engineering/README.md).

## 4. Bài học kiến trúc

Một pipeline tốt giữ riêng **trang xử lý thành công, fallback, bị bỏ và chưa kiểm**. Cache phải khóa theo hash tài liệu + parser/model/config; thay model hoặc trang gốc phải làm mất hiệu lực bằng chứng cũ. Chunk cho RAG ở bước sau không được làm mất trang/bbox và provenance.

Paper gốc [OmniDocBench (CVPR 2025)](https://openaccess.thecvf.com/content/CVPR2025/html/Ouyang_OmniDocBench_Benchmarking_Diverse_PDF_Document_Parsing_with_Comprehensive_Annotations_CVPR_2025_paper.html) hỗ trợ đánh giá nhiều thành phần tài liệu; benchmark miền đích vẫn cần corpus riêng, nhất là biểu mẫu tiếng Việt và ảnh chụp điện thoại.

## Nguồn

Các permalink trong từng hồ sơ cố định đúng phiên bản đã đọc; số sao/trạng thái archive là snapshot GitHub API ngày 2026-11-02. Không chạy mã, huấn luyện model hoặc tái lập kết quả của upstream.
