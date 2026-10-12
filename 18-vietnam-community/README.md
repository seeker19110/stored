# 18 · Hệ sinh thái AI & lập trình Việt Nam

> Model tiếng Việt mã mở, toolkit NLP, dữ liệu, cộng đồng và sự kiện. Nhiều mục chỉ có 1 nguồn, cần bổ sung khi có link cụ thể (theo WORKFLOW.md).

## 1. Model ngôn ngữ tiếng Việt mã mở
| Model | Tổ chức | Ghi chú |
|---|---|---|
| **PhoGPT** (PhoGPT-4B, 4B-Chat, 7B5) | VinAI Research | Chuỗi LLM tiếng Việt mở 2023; vẫn được dùng làm baseline nghiên cứu 2026 (VietBinoculars, VietAIDetector) |
| **Vistral / Vistral-V** | Viet-Mistral · Vi-VLM | Mistral-7B tinh chỉnh tiếng Việt; Vistral-V là VLM tiếng Việt (cập nhật giữa 2024) |
| **ViGPT** | DopikAI-Labs | LLM đơn ngữ, instruction-tuned, mã + trọng số công khai |
| **URA-LLaMA / GemSUra / MixSUra** | URA, ĐH Bách Khoa TP.HCM | Tinh chỉnh từ LLaMA-2, Gemma, Mixtral; benchmark tiếng Việt |
| **Ghost-7b** | cộng đồng | zephyr-7b-beta tinh chỉnh 50% EN / 50% VI |
| **14B-R1** | GreenNode (VNG) | "LLM suy luận mở tiếng Việt đầu tiên" (9/2025) **(chưa xác minh)** |
| PhoBERT, ViT5, BARTpho, XPhoneBERT | VinAI, VietAI | Encoder/seq2seq nền tảng |
| Qwen/Gemma/Llama bản đa ngôn ngữ | – | Thường tốt hơn model VN chuyên biệt ở quy mô lớn |

## 2. Toolkit NLP tiếng Việt
| Toolkit | Repo | Ghi chú |
|---|---|---|
| **underthesea** | undertheseanlp/underthesea | v9.5.0 (5/2026); từ v9.3 định vị là "Agentic AI Toolkit" có NLP tiếng Việt: tách từ, POS, NER, phân loại, sentiment |
| **VnCoreNLP** | vncorenlp/VnCoreNLP | Java, 1 jar, GPL-3; tách từ, POS, NER, dependency parsing (NAACL 2018) |
| pyvi, PhoNLP, VnCoreNLP-python | – | |
| **awsome-vietnamese-nlp** | vndee/awsome-vietnamese-nlp | Danh sách tổng hợp tài nguyên NLP tiếng Việt – điểm khởi đầu |

## 3. Dữ liệu & benchmark
- **ViGen** (10/2025): bộ dữ liệu tiếng Việt mã mở "đầu tiên" gắn với Chiến lược AI quốc gia đến 2030, lộ trình 2026–2027; SotaTek và nhiều doanh nghiệp đóng góp.
- Stanford CRFM *Crossing Linguistic Horizons*: đánh giá toàn diện LLM tiếng Việt.
- VietBinoculars / VietAIDetector (2025–2026): phát hiện văn bản AI tiếng Việt.

## 4. Tổ chức, cộng đồng, sự kiện
| Tên | Loại | Ghi chú |
|---|---|---|
| VinAI Research (Hùng Bùi) | Lab | NeurIPS/ICML, mở PhoGPT, PhoBERT |
| VietAI | Cộng đồng/giáo dục | ViT5, khóa học |
| Zalo AI, FPT AI, Viettel AI, GreenNode (VNG) | Doanh nghiệp | Zalo AI Challenge, FPT AI Factory (NVIDIA), Viettel–NVIDIA Vietnam AI Open Hackathon 2026 (GenAI, Agentic, Physical AI) |
| VFOSSA | Hiệp hội mã nguồn mở | Software Freedom Day 2026: AI mở, blockchain, PQC, phần cứng mở |
| Codex Community Hackathon Hanoi (27/6/2026) | Sự kiện | 271 đơn, 150 builder; Lotus Hacks >1.000 dev, >200 dự án |
| Viblo, TopDev, ITviec, Dạy Nhau Học, Tôi đi code dạo | Cộng đồng/nội dung | Chia sẻ kỹ thuật, tuyển dụng |
| Xu hướng 2026 | – | Dev VN chuyển từ outsourcing sang "AI building"; dự án hướng ngành: sản xuất, logistics, TMĐT, nông nghiệp |

## 5. Gợi ý bổ sung tiếp
- Thêm link GitHub cụ thể của từng model/toolkit (số sao, ngày cập nhật) khi có.
- Theo dõi: Hugging Face `vinai`, `VietAI`, `Vi-VLM`, `GreenNode`; GitHub topic `vietnamese-nlp`.

## 6. Nguồn
- https://www.emergentmind.com/topics/phogpt · https://arxiv.org/html/2509.26189v2 · https://arxiv.org/html/2608.25478 · https://ai.stanford.edu/blog/crossing-linguistic-horizon/ · https://aisean.org/resources/ · https://huggingface.co/Vi-VLM/Vistral-V-7B · https://github.com/vndee/awsome-vietnamese-nlp
- https://pypi.org/project/underthesea/ · https://github.com/undertheseanlp/underthesea · https://aclanthology.org/N18-5012/
- https://www.sotatek.com/newsroom/sotatek-contributes-to-vigen-vietnams-first-open-source-vietnamese-language-dataset-for-ai/ · https://technode.global/2026/06/18/vietnams-developers-are-moving-from-outsourcing-to-ai-building/ · https://morsoftware.com/news/codex-community-hackathon-hanoi-2026 · https://www.vietnam.vn/en/khoi-dong-cuoc-thi-vietnam-ai-open-hackathon-2026 · https://www.vietnam.vn/en/lam-chu-ai-va-phat-trien-phan-mem-nguon-mo-an-toan · https://www.openhackathons.org/s/siteevent/a0CUP00004VRMiz2AH/se000492
