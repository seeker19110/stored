# 15 · AI for Data: Query Engines, Dataframes, Text-to-SQL, Notebooks, Data Agents

| Dự án | Repo | License | ★ | Vai trò | Ghi chú |
|---|---|---|---|---|---|
| **DuckDB** | duckdb/duckdb | MIT | **40k+** (5/8/2026) | OLAP in-process, SQL trên Parquet/CSV; 1.4 LTS, 1.5 | Nền cho nhiều tool AI-data |
| **Polars** | pola-rs/polars | MIT | – | Dataframe Rust, >24M tải/tháng | Thay pandas cho dữ liệu lớn |
| **PandasAI** | sinaptik-ai/pandas-ai | MIT (trừ `ee/`) | ~24k | Hỏi dữ liệu bằng ngôn ngữ tự nhiên (SQL, CSV, pandas, polars) | Cập nhật cuối 10/2025 |
| **Vanna** | vanna-ai/vanna | MIT | ~23.7k | Text-to-SQL với RAG trên schema | |
| **marimo** | marimo-team/marimo | Apache-2.0 | ~22–23k | Notebook Python reactive, lưu dạng .py thuần, AI-native | Thay Jupyter cho reproducibility |
| **Jupyter AI** | jupyterlab/jupyter-ai | BSD-3 | – | Nối agent (Claude, Gemini) vào JupyterLab qua Agent Client Protocol | |
| **Ibis** | ibis-project/ibis | Apache-2.0 | ~6.6k | Dataframe portable, backend DuckDB/Polars/BigQuery | |
| **Data Formulator** (Microsoft) | microsoft/data-formulator | MIT | – | Tạo biểu đồ/transform bằng AI | |
| **MindsDB** | mindsdb/mindsdb | Elastic 2.0 | – | "AI trong database", federated query | |
| **Open Interpreter** | openinterpreter/open-interpreter | AGPL-3.0 | – | LLM chạy code local để phân tích | |
| Evidence, Streamlit, Gradio | – | – | – | Dashboard/app dữ liệu | |

**Mẫu kiến trúc phổ biến:** DuckDB/Polars làm engine → LLM sinh SQL/Python (Vanna/PandasAI) → chạy trong sandbox (mục 11) → trực quan hóa (Data Formulator/marimo). Bảo mật: text-to-SQL cần read-only connection + allowlist bảng.

## Bổ sung: text-to-SQL, BI có AI & lớp metadata (đã xác minh 2026-10-12)

| Repo | ★ (12/10) | License | Hoạt động gần nhất | Vì sao chất lượng | Lưu ý |
|---|---|---|---|---|---|
| **Canner/WrenAI** | 17,9k | Apache-2.0 (code), CC-BY-4.0 (docs) | wren v0.15.0 (21/9/2026) | Text-to-SQL/GenBI có quản trị qua semantic layer (MDL); engine Rust kiểm SQL sinh ra trước khi chạy; MCP server; hơn 20 nguồn dữ liệu | Vừa tái cấu trúc lớn; dành sẵn AGPL-3.0 cho module tương lai; tên và logo là thương hiệu |
| **eosphoros-ai/DB-GPT** | 20,1k | MIT | commit 11/10/2026 (v0.8.2, 8/2026) | Trợ lý dữ liệu agentic: Text2SQL, RAG, workflow AWEL; fine-tune Text2SQL qua DB-GPT-Hub; có paper multi-agent | Phát hành thưa |
| **OtterMind/Chat2DB** (chuyển từ chat2db/Chat2DB) | 28,3k | Apache-2.0 sửa đổi, source-available từ v5.3.0 (không OSI) | v5.3.8 (9/10/2026) | Client SQL có AI, tự mang LLM để sinh, giải thích, tối ưu SQL; hơn 40 CSDL; chạy local | Cấm host hoặc cung cấp cho bên thứ ba khi chưa có văn bản cho phép |
| **dataease/SQLBot** | 6,9k | FIT2CLOUD Open Source License (GPLv3 + hạn chế) | v1.10.2 (23/9/2026) | Hỏi dữ liệu bằng LLM + RAG, tách workspace, phân quyền dữ liệu chi tiết; MCP; nhúng vào Dify, n8n, MaxKB | Không được đổi logo/bản quyền; bản phái sinh theo GPLv3 |
| **apache/superset** | 75,1k | Apache-2.0 | 12/10/2026 | BI doanh nghiệp quản trị kiểu ASF; MCP server ngay trong repo (`superset/mcp_service`) cho agent đọc chart, dashboard, SQL Lab | Phần AI chỉ qua MCP, README không có trợ lý AI dựng sẵn |
| **metabase/metabase** | 49,6k | AGPL-3.0 + license thương mại | v64.1 (7/10/2026) | BI dễ dùng, embedded analytics; trợ lý **Metabot** chạy tự host bằng API key riêng, không cần gói trả phí | AGPL; nội dung "verified" và audit AI chỉ có ở Pro/Enterprise |
| **tobymao/sqlglot** | 9,7k | MIT | 12/10/2026 | Parser/transpiler/optimizer SQL không phụ thuộc, hơn 30 dialect; SQLMesh dùng | Chỉ là thư viện; commit breaking ("!") thường xuyên → ghim phiên bản |
| **datahub-project/datahub** | 12,8k | Apache-2.0 | v1.8.0rc5 (8/10/2026) | Nền tảng metadata/ngữ cảnh dữ liệu cho agent, khởi đầu ở LinkedIn; hơn 150 tích hợp, MCP server chính thức | Tích hợp agent native nằm ở DataHub Cloud trả phí; chạy thử local cần 8 GB RAM |

**Nhận xét:**

- Lớp an toàn cho text-to-SQL (bổ sung cho "read-only + allowlist bảng" ở trên): parse câu SQL do LLM sinh bằng **sqlglot**, chặn mọi lệnh không phải `SELECT` và mọi bảng ngoài allowlist **trước khi** gửi tới DB; WrenAI làm việc tương tự trong engine Rust của nó.
- License là điểm khác biệt lớn nhất của nhóm này: Chat2DB bỏ Apache-2.0 từ v5.3.0 và cấm cả việc host miễn phí cho người khác; SQLBot (và DataEase) dùng license FIT2CLOUD; Metabase là AGPL. Superset, WrenAI (phần hiện có), DB-GPT, sqlglot, DataHub dùng license OSI thoáng.
- Commit của sqlglot nay gắn nhãn `[CLAUDE]` và có Claude là đồng tác giả — ví dụ một dự án hạ tầng lớn dùng coding agent công khai.
- Đã cân nhắc nhưng không thêm: pygwalker (16,0k★, commit cuối 5/9/2026), evidence (7,0k★), redash (28,8k★), dataease (24,6k★, FIT2CLOUD), airbyte (22,2k★, MIT + ELv2), great_expectations (11,9k★).

## Nguồn

- https://duckdb.org/2026/08/05/github-40k-stars · https://en.wikipedia.org/wiki/Polars_(software) · https://github.com/sinaptik-ai/pandas-ai · https://github.com/topics/sql?l=python · https://aitools.flocci.in/alternatives/pandasai · https://jupysql.readthedocs.io/en/latest/tutorials/duckdb-github.html
- Bổ sung (12/10/2026): https://github.com/Canner/WrenAI · https://github.com/eosphoros-ai/DB-GPT · https://github.com/OtterMind/Chat2DB · https://github.com/dataease/SQLBot · https://github.com/apache/superset · https://github.com/apache/superset/tree/master/superset/mcp_service · https://github.com/metabase/metabase · https://www.metabase.com/docs/latest/ai/settings · https://github.com/tobymao/sqlglot · https://github.com/datahub-project/datahub · https://github.com/Kanaries/pygwalker · https://github.com/evidence-dev/evidence · https://github.com/getredash/redash · https://github.com/dataease/dataease · https://github.com/airbytehq/airbyte · https://github.com/great-expectations/great_expectations
