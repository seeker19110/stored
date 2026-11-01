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

## Nâng cấp 31/10/2026: rà repo lớn

> Cách làm: đọc lại sao, license, trạng thái của 19 repo GitHub đã có trong mục 15 (GitHub API, 31/10/2026); clone và đọc lại mã của Vanna và PandasAI vì hai repo này đã dừng. Tìm repo còn thiếu bằng 18 truy vấn GitHub search (`text-to-sql`, `nl2sql`, `chatbi`, `semantic layer`, `data analysis agent`, `data science agent`, `mcp database sql`, `duckdb`, `dataframe`, topic `data-analysis`/`data-engineering`, và `created:>2025-10-01`). Chọn **5 repo**, clone `--filter=blob:none`, đọc LICENSE, README, manifest, CI, file telemetry và đường thực thi SQL/code. **Không cài, không chạy script của repo.** Số liệu đọc 31/10/2026.

### Trạng thái repo cũ

| Repo | Thay đổi | Hệ quả |
|---|---|---|
| `vanna-ai/vanna` | **Đã archive** (GitHub API 31/10/2026); commit cuối **2/2/2026** (v2.0.2). Trang tổng hợp ghi ngày archive 29/3/2026 **(chưa xác minh)**. README không có thông báo ngừng | Không chọn cho dự án mới. Fork vẫn chạy được nhưng không có bản vá bảo mật |
| `sinaptik-ai/pandas-ai` | Commit cuối **28/10/2025** (v3.0.0 ngày 7/10/2025), tròn 1 năm đứng yên; 23,9k★ | Coi như ngừng phát triển; bảng đầu mục ghi "Cập nhật cuối 10/2025" vẫn đúng |
| `duckdb/duckdb` · `pola-rs/polars` | 42,7k · 40,2k | Polars nay ngang DuckDB; catalog bổ sung sao Polars |
| `marimo-team/marimo` · `microsoft/data-formulator` · `jupyterlab/jupyter-ai` | 23,4k · 17,6k · 4,4k | Catalog bổ sung sao còn thiếu |
| `Canner/WrenAI` · `OtterMind/Chat2DB` · `dataease/SQLBot` · `metabase/metabase` | GitHub báo `NOASSERTION` | Không đổi license: đều là license nhiều phần hoặc tuỳ chỉnh đã ghi ở bảng "Bổ sung" |
| `mindsdb/mindsdb` · `openinterpreter/open-interpreter` | Không có trong kết quả API đợt này | Chưa kiểm lại được; giữ nguyên |

**Vanna 2.0 khi đọc mã (thông tin cho ai còn dùng bản fork):**

- ⚠️ README quảng cáo "row-level security", nhưng `ToolRegistry.transform_args` trong `src/vanna/core/registry.py` mặc định **không làm gì** (NoOp); RLS là chỗ để người dùng tự viết.
- ❌ `src/vanna/tools/run_sql.py` chạy cả câu không phải `SELECT` (INSERT/UPDATE/DELETE) và chỉ báo số dòng bị ảnh hưởng. An toàn phụ thuộc hoàn toàn vào quyền của connection.
- Web component mặc định tải `https://img.vanna.ai/vanna-components.js`; mã legacy 0.x gọi `ask.vanna.ai`. Khi dịch vụ của công ty ngừng, cả hai sẽ hỏng; nên tự host file JS.

**PandasAI 3.0 khi đọc mã:**

- ⚠️ Telemetry chạy **ngay khi import**: `pandasai/helpers/logger.py` gọi `scarf_analytics()` gửi `GET https://package.pandabi.ai/pandasai-telemetry?version=…&platform=…`. Chỉ tắt khi `SCARF_NO_ANALYTICS` hoặc `DO_NOT_TRACK` **bằng đúng chuỗi `"true"`**; giá trị `DO_NOT_TRACK=1` (quy ước phổ biến) **không** tắt được.
- ⚠️ Code Python do LLM sinh chạy **ngay trong tiến trình** (`CodeExecutor.execute_and_return_result`) trừ khi truyền `sandbox=`. Thư mục `ee/` theo license Enterprise, cần ký điều khoản trước khi dùng production.

### Bảng nhanh 5 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `cube-js/cube` | Semantic layer | 21,1k · Apache-2.0 (+ MIT một số gói) | 31/10/2026 | Định nghĩa metric/dimension một lần, xuất SQL/REST/GraphQL cho BI và agent | **Telemetry bật mặc định**; MCP chỉ ở Cube Cloud |
| `K-Dense-AI/scientific-agent-skills` | Skill phân tích dữ liệu khoa học | 55,5k · MIT | 26/10/2026 | 177 skill theo chuẩn Agent Skills (polars, statsmodels, EDA, tra cứu 100+ CSDL khoa học) | Nạp nhiều skill vào ngữ cảnh |
| `bytebase/dbhub` | MCP cho CSDL | 3,8k · MIT | 26/10/2026 | MCP gọn (2 tool), phân loại câu SQL + giao dịch READ ONLY làm lớp chặn | **Read-only không bật mặc định** |
| `t8y2/dbx` | Client CSDL có AI | 28,4k · Apache-2.0 | 1/11/2026 | Client 25 MB cho 100+ CSDL, trợ lý AI, MCP 3 mức quyền | 6 tháng tuổi, nhịp commit cực cao |
| `ruc-datalab/DeepAnalyze` | Model + agent data science | 4,8k · MIT (code) | 13/10/2026 | Model 8B tự làm pipeline phân tích dữ liệu, có WebUI | Không CI; sandbox Docker tuỳ chọn |

### Hồ sơ ngắn

- **Cube Core.** 11.796 commit từ 2018, 419 tác giả, 12% commit có trailer Claude, có workflow `claude-code-review.yml`. LICENSE gốc: mặc định Apache-2.0, một số gói MIT. ⚠️ `packages/cubejs-backend-shared/src/env.ts`: `CUBEJS_TELEMETRY` mặc định `true`; `track.ts` gửi sự kiện kèm `machineIdSync()` tới `https://track.cube.dev/track` (chỉ bỏ qua khi biến `CI` được đặt). Tắt bằng `CUBEJS_TELEMETRY=false`. Tài liệu MCP và "analytics chat" là dịch vụ hosted của Cube Cloud (MCP connectors chỉ ở gói Premium/Enterprise). Giá trị cho kho: semantic layer giữa LLM và kho dữ liệu, cùng ý với MDL của WrenAI. Cài: `docker run -p 4000:4000 -p 15432:15432 -v ${PWD}:/cube/conf -e CUBEJS_DEV_MODE=true -e CUBEJS_TELEMETRY=false cubejs/cube`.
- **Scientific Agent Skills (K-Dense).** 762 commit, đổi tên từ "Claude Scientific Skills"; 177 thư mục skill. Đã **gỡ 4 skill docx/pdf/pptx/xlsx chép từ `anthropics/skills`** vì license của Anthropic không cho phân phối lại, một ví dụ dọn license đúng. `scan_skills.py` quét bảo mật từng skill bằng LLM, có cache theo hash nội dung; CI chạy `security-scan`, `skill-spec-validation`, `skill-tests` ✅. Rủi ro: cài cả bộ đưa 177 mô tả skill vào ngữ cảnh; README kêu gọi star. Cài: `npx skills add K-Dense-AI/scientific-agent-skills` (chọn skill cần thay vì cài hết).
- **DBHub (Bytebase).** TypeScript, 655 commit, **68% commit có trailer Claude**. Điểm đáng học là `src/utils/sql-access-policy.ts`: phân loại từng câu thành read/dml/ddl/admin/unknown (bắt cả `xp_cmdshell`, `pg_read_file`, `LOAD_FILE`), câu không phân loại được bị coi nguy hiểm như mức cao nhất; thêm **giao dịch READ ONLY ở tầng engine** làm lớp chặn thứ hai (`readonly-transaction.ts` tự ghi rõ DDL vẫn thoát được qua implicit commit). ⚠️ Cờ `--readonly` đã bị bỏ; muốn read-only phải khai báo `readonly = true` trong `dbhub.toml`, mặc định `execute_sql` được ghi. "Ít token hơn 13–14×" là so sánh tự đo. Cài: `npx @bytebase/dbhub@latest --transport stdio --dsn "<dsn>"` kèm file `dbhub.toml` bật read-only.
- **DBX.** Rust + TS, repo tạo 29/4/2026, 9.292 commit (6.524 từ 1/7/2026), 446 tác giả, 28,4k★. Client CSDL đa nền tảng, plugin ký số, trợ lý AI tích hợp, MCP server phát hành riêng (`@dbx-app/mcp-server`) với 3 mức `read_only`/`safe_write`/`high_risk_write` và allowlist kết nối chỉnh trong Settings. Mức mặc định của MCP **chưa xác minh**. README có quảng cáo nhà tài trợ. Cài MCP: `npx -y @dbx-app/mcp-server`.
- **DeepAnalyze (RUC DataLab).** Paper arXiv 2510.16872, model DeepAnalyze-8B và dữ liệu huấn luyện trên Hugging Face, 309 commit, không có workflow CI. Model sinh và chạy code phân tích; từ 3/2026 WebUI v2 có **thực thi trong Docker sandbox** nhưng là tuỳ chọn. Hợp để nghiên cứu "data agent" chạy local bằng vLLM; license weights trên Hugging Face **chưa xác minh**. Cài: tải model rồi `vllm serve DeepAnalyze-8B`.

Đã cân nhắc nhưng chưa thêm: `tencentmusic/supersonic` (5,2k, ChatBI; Apache-2.0 **kèm điều kiện** cấm phân phối bản phái sinh khi chưa mua license, tag cuối 3/3/2025, chỉ 15 commit từ 7/2026), `sqlchat/sqlchat` (5,9k), `clidey/whodb` (5,0k), `streamlit/streamlit` (46,2k, đã nhắc ở bảng đầu), `apache/datafusion` (9,6k), `Eventual-Inc/Daft` (5,8k), `evidence-dev/evidence` (7,1k), `rilldata/rill` (3,0k).

### Mẫu chung rút ra

1. **Text-to-SQL "an toàn" phải đo bằng mã, không bằng README.** Vanna quảng cáo RLS nhưng mặc định NoOp và vẫn chạy DML; DBHub có bộ phân loại + giao dịch READ ONLY nhưng không bật mặc định. Mẫu đúng: read-only bật mặc định, hai lớp (parser như sqlglot/DBHub + quyền DB), và test các câu thoát như `SELECT 1--1;DROP TABLE t`.
2. **Opt-out telemetry phải chấp nhận nhiều dạng giá trị.** PandasAI chỉ nhận `"true"`, nên `DO_NOT_TRACK=1` không có tác dụng; Cube bật mặc định với machine id. Template nên đặt cả `DO_NOT_TRACK=1`, `DO_NOT_TRACK=true` và biến riêng của từng công cụ.
3. **Code do LLM sinh chạy trong tiến trình là mặc định nguy hiểm** (PandasAI, DeepAnalyze trước 3/2026). Ghép với sandbox ở mục 11.
4. **Dự án text-to-SQL độc lập đang tàn**: Vanna archive, PandasAI dừng 1 năm; phần AI dồn về semantic layer (Cube, WrenAI), BI lớn (Superset MCP, Metabase Metabot) và MCP cho CSDL (DBHub, DBX).
5. **Dọn license khi gom skill**: K-Dense gỡ skill chép từ Anthropic. Kho skill nào vendored nội dung bên thứ ba cần ghi nguồn và license từng skill.

**Nguồn (31/10/2026):** GitHub search API (18 truy vấn + `repo:` cho 19 repo cũ và 5 repo mới) · clone `--filter=blob:none`, đọc: vanna (LICENSE, README.md, pyproject.toml, src/vanna/core/registry.py, src/vanna/tools/run_sql.py, src/vanna/servers/base/templates.py, src/vanna/legacy/), pandas-ai (LICENSE, ee/LICENSE, pyproject.toml, pandasai/helpers/telemetry.py, pandasai/helpers/logger.py, pandasai/agent/base.py), cube (LICENSE, README.md, packages/cubejs-backend-shared/src/{env.ts, track.ts}, docs-mintlify/docs/integrations/mcp-server.mdx, docs-mintlify/admin/ai/mcp-connectors.mdx), scientific-agent-skills (LICENSE.md, README.md, scan_skills.py, .github/workflows/), dbhub (LICENSE, README.md, dbhub.toml.example, src/utils/{sql-access-policy.ts, readonly-transaction.ts}, src/config/env.ts), dbx (LICENSE, NOTICE, README.md), DeepAnalyze (LICENSE, README.md), supersonic (LICENSE) · https://github.com/vanna-ai/vanna · https://landscape.jimmysong.io/projects/vanna/ · https://github.com/sinaptik-ai/pandas-ai · https://github.com/cube-js/cube · https://github.com/K-Dense-AI/scientific-agent-skills · https://github.com/bytebase/dbhub · https://github.com/t8y2/dbx · https://github.com/ruc-datalab/DeepAnalyze · https://arxiv.org/abs/2510.16872 · https://github.com/tencentmusic/supersonic

## Nguồn

- https://duckdb.org/2026/08/05/github-40k-stars · https://en.wikipedia.org/wiki/Polars_(software) · https://github.com/sinaptik-ai/pandas-ai · https://github.com/topics/sql?l=python · https://aitools.flocci.in/alternatives/pandasai · https://jupysql.readthedocs.io/en/latest/tutorials/duckdb-github.html
- Bổ sung (12/10/2026): https://github.com/Canner/WrenAI · https://github.com/eosphoros-ai/DB-GPT · https://github.com/OtterMind/Chat2DB · https://github.com/dataease/SQLBot · https://github.com/apache/superset · https://github.com/apache/superset/tree/master/superset/mcp_service · https://github.com/metabase/metabase · https://www.metabase.com/docs/latest/ai/settings · https://github.com/tobymao/sqlglot · https://github.com/datahub-project/datahub · https://github.com/Kanaries/pygwalker · https://github.com/evidence-dev/evidence · https://github.com/getredash/redash · https://github.com/dataease/dataease · https://github.com/airbytehq/airbyte · https://github.com/great-expectations/great_expectations
