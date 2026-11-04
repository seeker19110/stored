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
2. **Opt-out telemetry phải chấp nhận nhiều dạng giá trị.** PandasAI chỉ nhận `"true"`, nên `DO_NOT_TRACK=1` không có tác dụng; Cube bật mặc định với machine id. Khi kiểm thử cần kiểm cả hai dạng `1`/`true`; khi cấu hình chọn giá trị đúng từng công cụ và dùng biến opt-out riêng. Không thể đặt đồng thời hai giá trị cho cùng một biến.
3. **Code do LLM sinh chạy trong tiến trình là mặc định nguy hiểm** (PandasAI, DeepAnalyze trước 3/2026). Ghép với sandbox ở mục 11.
4. **Dự án text-to-SQL độc lập đang tàn**: Vanna archive, PandasAI dừng 1 năm; phần AI dồn về semantic layer (Cube, WrenAI), BI lớn (Superset MCP, Metabase Metabot) và MCP cho CSDL (DBHub, DBX).
5. **Dọn license khi gom skill**: K-Dense gỡ skill chép từ Anthropic. Kho skill nào vendored nội dung bên thứ ba cần ghi nguồn và license từng skill.

**Nguồn (31/10/2026):** GitHub search API (18 truy vấn + `repo:` cho 19 repo cũ và 5 repo mới) · clone `--filter=blob:none`, đọc: vanna (LICENSE, README.md, pyproject.toml, src/vanna/core/registry.py, src/vanna/tools/run_sql.py, src/vanna/servers/base/templates.py, src/vanna/legacy/), pandas-ai (LICENSE, ee/LICENSE, pyproject.toml, pandasai/helpers/telemetry.py, pandasai/helpers/logger.py, pandasai/agent/base.py), cube (LICENSE, README.md, packages/cubejs-backend-shared/src/{env.ts, track.ts}, docs-mintlify/docs/integrations/mcp-server.mdx, docs-mintlify/admin/ai/mcp-connectors.mdx), scientific-agent-skills (LICENSE.md, README.md, scan_skills.py, .github/workflows/), dbhub (LICENSE, README.md, dbhub.toml.example, src/utils/{sql-access-policy.ts, readonly-transaction.ts}, src/config/env.ts), dbx (LICENSE, NOTICE, README.md), DeepAnalyze (LICENSE, README.md), supersonic (LICENSE) · https://github.com/vanna-ai/vanna · https://landscape.jimmysong.io/projects/vanna/ · https://github.com/sinaptik-ai/pandas-ai · https://github.com/cube-js/cube · https://github.com/K-Dense-AI/scientific-agent-skills · https://github.com/bytebase/dbhub · https://github.com/t8y2/dbx · https://github.com/ruc-datalab/DeepAnalyze · https://arxiv.org/abs/2510.16872 · https://github.com/tencentmusic/supersonic

## 4. Nâng trần 2/11/2026: đo độ đúng text-to-SQL, data contract và lineage (yêu cầu người dùng)

> Cách làm: grep `data/projects.json` theo `repo` để loại trùng; GitHub search API ngày 2/11/2026 (`repo:` cho từng ứng viên; phát hiện `great-expectations/great_expectations` nay là `fivetran/great_expectations` và `dbt-labs/dbt-core` nay là `dbt-labs/dbt` qua truy vấn tên); clone `--depth 1 --filter=blob:none` 7 repo, đọc LICENSE, README, manifest, file chấm điểm, mã telemetry và CI. **Không cài, không chạy mã của repo.**

**Trần hiện tại:**

- Mục có nhiều công cụ text-to-SQL/BI và một lớp **an toàn** đã đo bằng mã (sqlglot, DBHub, "Mẫu chung rút ra" ý 1), nhưng **không có bộ đo độ đúng** của SQL do LLM sinh: không biết WrenAI, DB-GPT hay bản fork Vanna trả lời đúng bao nhiêu phần trăm.
- Không có lớp **chất lượng dữ liệu**: `great_expectations` bị "cân nhắc nhưng không thêm" (bảng Bổ sung 12/10/2026). Agent trả lời đúng SQL trên dữ liệu sai vẫn là trả lời sai.
- Không có chuẩn **lineage**: DataHub (bảng Bổ sung) là kho metadata, nhưng chưa có giao thức mở để job tự phát sự kiện "bảng này sinh từ đâu". Lớp transform (dbt) cũng chưa có trong catalog.

| Repo | Lớp | ★ · license (2/11/2026) | Commit cuối | Vì sao nâng trần | Rủi ro |
|---|---|---|---|---|---|
| `xlang-ai/Spider2` | Chuẩn | 886 · MIT | 12/8/2026 | Text-to-SQL cấp doanh nghiệp: Spider 2.0-Snow 547 task (Snowflake), -Lite 547 task (BigQuery 214, Snowflake 198, SQLite 135), -DBT 68 task; có baseline Spider-Agent (bản gọi tool không cần Docker) và leaderboard | Bản Snow phụ thuộc tài khoản Snowflake của nhóm, đang bị tạm ngưng theo News 12/8/2026; gold SQL chỉ công bố một phần, nhóm khuyên không dùng để SFT |
| `bird-bench/mini_dev` | Chuẩn | 192 · CC BY-SA 4.0 (badge README; repo **không có file LICENSE**) | 28/10/2026 | BIRD Mini-Dev: 500 câu SELECT chất lượng cao trên SQLite, MySQL, PostgreSQL; ba metric EX (đúng kết quả), R-VES (hiệu năng câu SQL), Soft F1; bản cập nhật 2026 (28/10) sửa nhãn sau góp ý cộng đồng; kèm LiveSQLBench | Dữ liệu share-alike; sao thấp vì leaderboard chính nằm ở bird-bench.github.io; R-VES dao động theo máy, README khuyên tăng timeout và chạy lặp |
| `fivetran/great_expectations` (GX Core) | Cổng máy | 11,9k · Apache-2.0 | 22/10/2026 (1.24.1) | "Unit test cho dữ liệu": Expectation + Checkpoint, Python 3.10–3.14. Bản mới **đóng gói agent skill** và lệnh cài: mỗi thư mục skill có manifest sở hữu (phiên bản + hash), chạy lại là no-op, không ghi đè thư mục người dùng đã sửa, ghi qua thư mục tạm rồi rename | Repo đã chuyển sang tổ chức Fivetran (thời điểm và lý do **chưa xác minh**); analytics điều khiển bằng `GX_ANALYTICS_ENABLED`, giá trị mặc định **chưa xác minh**; đóng góp cần ký CLA |
| `sodadata/soda-core` | Cổng máy | 2,5k · **Elastic License 2.0** (GitHub: NOASSERTION) | 29/10/2026 (4.29.1rc0) | Data contract viết bằng YAML, hơn 50 check, chạy CLI/Python trên Postgres, Snowflake, BigQuery, Databricks, DuckDB…; có workflow `claude-de-review.yml` | ⚠️ README gọi là "open source" nhưng LICENSE là **ELv2**: cấm cung cấp dạng dịch vụ hosted, không phải license OSI. Phát hiện bất thường (anomaly detection) nằm ở Soda Cloud |
| `dbt-labs/dbt` (trước là `dbt-core`) | Đầu bảng | 14,1k · Apache-2.0 | 2/11/2026 (2.0.8) | Nhánh `main` nay là **dbt v2.0 viết lại bằng Rust** (binary đơn, artifact Parquet, kiểm chặt lúc parse); v1 Python ở nhánh `1.latest`. Data test và unit test của dbt là cổng chuẩn cho lớp transform | ⚠️ Telemetry bật mặc định: `crates/dbt-clap-core` đặt `send_anonymous_usage_stats` mặc định `true`, chỉ tắt bằng `--no-send-anonymous-usage-stats`, biến `DBT_SEND_ANONYMOUS_USAGE_STATS` hoặc cờ trong `dbt_project.yml`. `DO_NOT_TRACK` chỉ được đọc ở phần docs (docs server, export) và chỉ khi bằng đúng `"1"` |
| `OpenLineage/OpenLineage` | Chuẩn | 2,7k · Apache-2.0 | 29/10/2026 | Chuẩn mở (dự án Graduate của LF AI & Data): mô hình run/job/dataset mở rộng bằng facet, spec OpenAPI + JSON Schema (`spec/`), client Python/Java/Go, tích hợp Spark, Airflow, dbt, Flink; Marquez là bản cài đặt tham chiếu | Chỉ là chuẩn + client: cần backend (Marquez hoặc DataHub) để lưu và xem |
| `sqlfluff/sqlfluff` | Cổng máy | 10,0k · MIT | 1/11/2026 (4.5.0) | Linter và auto-fix SQL, 28 file `dialect_*.py`, templater Jinja/dbt, lõi Rust `sqlfluffrs` đang tách ra; CI test riêng với dbt và SQLMesh; workflow AgentScan phân loại PR do AI agent tạo, viết theo mẫu `pull_request_target` an toàn (không checkout mã của PR) | Chỉ kiểm cú pháp và phong cách, không kiểm ngữ nghĩa hay quyền: bổ sung chứ không thay sqlglot/DBHub |

**Stack nâng trần** (theo thứ tự lợi ích/công sức):

1. **Cổng độ đúng cho text-to-SQL:** chạy BIRD Mini-Dev (SQLite, metric EX) mỗi lần đổi prompt hoặc model của WrenAI, DB-GPT, DBHub + LLM (bảng Bổ sung, Nâng cấp 31/10); thêm tập con SQLite 135 task của Spider 2.0-Lite cho câu hỏi kiểu doanh nghiệp, và Spider 2.0-DBT nếu agent sửa dự án dbt.
2. **Ghép vào lớp an toàn đã có:** SQL do LLM sinh → sqlglot/DBHub phân loại và chặn (Mẫu chung ý 1) → sqlfluff lint → chạy trên kết nối read-only.
3. **Data contract trước khi cho agent đọc bảng:** Checkpoint của GX (Apache-2.0) hoặc contract của Soda (chỉ khi không cung cấp lại dạng dịch vụ, vì ELv2); contract fail thì agent báo "dữ liệu chưa đạt" thay vì trả lời.
4. **Lớp transform có test:** data test và unit test của dbt chạy trong CI; đặt `DBT_SEND_ANONYMOUS_USAGE_STATS=false` cùng `DO_NOT_TRACK=1`, vì chỉ `DO_NOT_TRACK` không tắt được telemetry của CLI.
5. **Lineage cho câu trả lời có nguồn:** phát sự kiện OpenLineage từ dbt/Airflow vào DataHub (đã có) hoặc Marquez; agent trích tên bảng nguồn và lần chạy job khi trả lời.

**Nguồn §4:** GitHub search API 2/11/2026 (`repo:` cho 7 repo trên; `great_expectations in:name`, `dbt in:name org:dbt-labs`; ứng viên loại: `MarquezProject/marquez` 2,3k★ (nhắc trong bước 5), `awslabs/deequ` 3,7k★ (Scala/Spark), `unionai-oss/pandera` 4,5k★, `AlibabaResearch/DAMO-ConvAI` 1,6k★ (monorepo chứa BIRD gốc)) · clone `--depth 1 --filter=blob:none`, đọc: Spider2 (HEAD cafb8673 12/8/2026; LICENSE, README.md), mini_dev (1c49a37 28/10/2026; README.md, evaluation/), great_expectations (99f4d0c 22/10/2026; LICENSE, README.md, `great_expectations/agent_skills/installer.py`, `great_expectations/__main__.py`, `data_context/data_context/abstract_data_context.py`), soda-core (1b71142 29/10/2026; LICENSE, README.md, soda-core/pyproject.toml, .github/workflows/), dbt (1890fb3 2/11/2026; LICENSE, README.md, Cargo.toml, crates/dbt-clap-core/src/lib.rs, crates/dbt-main/src/dbt_lib.rs, crates/dbt-docs-server/src/state.rs), OpenLineage (bad2d7f 29/10/2026; LICENSE, README.md, spec/, client/, integration/), sqlfluff (4339c07 1/11/2026; LICENSE.md, README.md, pyproject.toml, src/sqlfluff/dialects/, .github/workflows/agent-scan.yml) · https://github.com/xlang-ai/Spider2 · https://spider2-sql.github.io · https://github.com/bird-bench/mini_dev · https://bird-bench.github.io · https://github.com/fivetran/great_expectations · https://github.com/sodadata/soda-core · https://github.com/dbt-labs/dbt · https://github.com/OpenLineage/OpenLineage · https://github.com/MarquezProject/marquez · https://github.com/sqlfluff/sqlfluff

## 5. Data ingestion and asset orchestration

> Mở rộng ngày 2/11/2026. §4 đã có dbt, GX/Soda và OpenLineage; phần còn thiếu là **dữ liệu tới từ đâu, cập nhật thế nào, phục hồi có làm trùng hay bỏ mất không**. Các repo dưới đây đã đọc LICENSE/CI/mã chính tại commit ghim, không cài và không chạy. Mục này khác durable workflow ở mục 21: đơn vị quản lý là asset/partition/cursor và độ tươi dữ liệu.

| Repo | ★ · license (2/11/2026) | Commit đọc | Cơ chế đáng học | Giới hạn / điều kiện |
|---|---|---|---|---|
| [dagster-io/dagster](https://github.com/dagster-io/dagster/tree/ef5c227a91576661f7c4b8619b855cd95e68ccd5) | 16,361 · Apache-2.0 | 2026-10-30 · `ef5c227` | Asset dependencies, partition/backfill, resource và asset check | Cần storage/daemon/deployment; một số quan sát vận hành thuộc Dagster+; telemetry instance thường bật mặc định |
| [dlt-hub/dlt](https://github.com/dlt-hub/dlt/tree/f3b6223c82fbaf8e9119497689022e8c211883fb) | 6,049 · Apache-2.0 | 2026-10-31 · `f3b6223` | Python ingestion, cursor có state, schema inference, destination và merge | Incremental cursor không đồng nghĩa dedup toàn bảng; cần khóa/merge phù hợp; telemetry bật mặc định |
| [debezium/debezium](https://github.com/debezium/debezium/tree/859540ed7983caa6939927c9ed0fc3f83f713e61) | 13,305 · Apache-2.0 | 2026-11-01 · `859540e` | CDC theo log CSDL; snapshot rồi stream thay đổi có offset/schema | Quyền replication và hạ tầng connector; có thể phát lại event sau lỗi; exactly-once phụ thuộc connector và cấu hình toàn tuyến |

### 5.1 Đọc cơ chế trước khi chọn

- **Dagster (Dagster Labs và cộng đồng):** [BackfillPolicy](https://github.com/dagster-io/dagster/blob/ef5c227a91576661f7c4b8619b855cd95e68ccd5/python_modules/dagster/dagster/_core/definitions/backfill_policy.py) tách một run cho nhiều partition với nhiều run có trần partition; [tài liệu backfill chính thức](https://dagster.io/docs/guides/build/partitions-and-backfills/backfilling-data) giải thích khi cần tính lại lịch sử. Asset check phải gắn với điều kiện ngăn downstream phù hợp, không suy ra mọi check tự chặn materialization. [Cấu hình instance](https://github.com/dagster-io/dagster/blob/ef5c227a91576661f7c4b8619b855cd95e68ccd5/python_modules/dagster/dagster/_core/instance/methods/settings_methods.py) đặt telemetry mặc định `True` cho instance thường, `False` cho ephemeral; tắt bằng `telemetry.enabled: false` trong cấu hình instance. Cần kiểm riêng dữ liệu log/metadata và dịch vụ Dagster+ khi tích hợp.
- **dlt (dltHub):** [Incremental](https://github.com/dlt-hub/dlt/blob/f3b6223c82fbaf8e9119497689022e8c211883fb/dlt/extract/incremental/__init__.py) giữ cursor và xử lý trùng vùng biên; [merge loading](https://dlthub.com/docs/general-usage/merge-loading) mới là nơi upsert/dedup staging theo khóa. Khi nguồn có cập nhật đến muộn, cửa sổ lag và merge phải được thiết kế cùng nhau; đừng coi `max(updated_at)` là bảo đảm không mất bản ghi. [RuntimeConfiguration](https://github.com/dlt-hub/dlt/blob/f3b6223c82fbaf8e9119497689022e8c211883fb/dlt/common/configuration/specs/runtime_configuration.py) đặt `dlthub_telemetry=True`; [hướng dẫn telemetry](https://github.com/dlt-hub/dlt/blob/f3b6223c82fbaf8e9119497689022e8c211883fb/docs/website/docs/reference/telemetry.md) có cấu hình `[runtime] dlthub_telemetry=false`.
- **Debezium (cộng đồng Debezium):** đọc `README.md`, `LICENSE.txt`, `debezium-core`, connector PostgreSQL và CI connector. [FAQ chính thức](https://debezium.io/documentation/faq/) nêu lỗi xác nhận/khởi động lại có thể tạo event lặp; [tài liệu exactly-once](https://debezium.io/documentation/reference/3.5/configuration/eos.html) mô tả điều kiện Kafka Connect. Tên sản phẩm hoặc trạng thái một connector không chứng minh exactly-once từ nguồn tới bảng đích. So với polling dlt: CDC nhận delete và thứ tự log rõ hơn, đổi lại thêm quyền và gánh vận hành; với batch file nhỏ, polling có thể đủ.

### 5.2 Ma trận lựa chọn

| Bài toán | Khởi đầu phù hợp | Ràng buộc cần chứng minh |
|---|---|---|
| API/file theo giờ, số nguồn vừa phải | dlt + lịch ở mục 21 | Cursor, khóa đích, delete/tombstone, retry và state restore |
| Nhiều asset phụ thuộc, cần tính lại lịch sử | Dagster + dlt/dbt | Partition mapping, backfill đồng thời, giới hạn tải nguồn, chặn asset lỗi |
| CSDL có thay đổi liên tục, cần delete/latency thấp | Debezium + sink có upsert | Quyền replication, snapshot/offset, replay, schema evolution, khóa nguồn |
| BI/agent đọc dữ liệu | Bất kỳ luồng trên + GX/Soda/dbt + DataHub/OpenLineage (§4) | Freshness theo domain, quyền từng tenant, lineage và khả năng truy ngược câu trả lời |

### 5.3 Cổng chất lượng cho đường dữ liệu

1. **Hợp đồng nguồn:** ghi owner, timezone/cursor, khóa, schema, dữ liệu nhạy cảm, quyền lưu và SLA cập nhật; tách nó khỏi schema suy ra tự động.
2. **Replay nhỏ trước:** tập có insert/update/delete, trùng event, đến muộn, đổi schema; so cả tập khóa và giá trị sau khi chạy lại/khôi phục state, không chỉ số dòng.
3. **Quarantine và publish:** bản không hợp lệ vào vùng cách ly; chỉ xuất partition đạt contract/freshness, không để agent âm thầm đọc lẫn dữ liệu dở dang.
4. **Backfill có ngân sách:** ghim code/schema, snapshot đầu vào, phạm vi partition và concurrency; không để chạy lịch thường xung đột backfill trên cùng khóa.
5. **Đo vận hành:** lag nguồn→đích, tỷ lệ bản ghi bị loại, sai lệch khóa, thời gian phục hồi và chi phí mỗi lần đồng bộ. Ghép OpenLineage/DataHub và eval text-to-SQL (§4) để phân biệt SQL sai với dữ liệu cũ.

**Liên quan:** dữ liệu để huấn luyện/gán nhãn thuộc [mục 24](../24-ai-data-engineering/README.md); đây là pipeline dữ liệu vận hành. Lịch/retry tổng quát ở [mục 21](../21-autonomous-workflows/README.md), kiểm quyền ở mục 12.

**Nguồn §5:** GitHub metadata/HEAD 2/11/2026 và permalink trên; LICENSE, README, CI, `BackfillPolicy`, instance settings, `Incremental`, runtime telemetry, Debezium core/PostgreSQL; tài liệu chính thức Dagster/dlt/Debezium. Các cổng trên là tiêu chí để dự án đích áp dụng, chưa có kết quả chạy trong khảo sát này.

## 6. Nâng sâu 4/11/2026: thay đổi dữ liệu phải có plan, test, audit và đường phục hồi

**Trần hiện tại:** kho đã có text-to-SQL, semantic layer, ingestion và lineage. Xưởng cần thêm vòng đời thay đổi mô hình dữ liệu: AI đề xuất SQL → review thay đổi → test logic → tính dữ liệu ở môi trường riêng → audit kết quả → promote có kiểm soát. Phân quyền DB/tenant và migration giao dịch thuộc [mục 34](../34-backend-data-identity-integration/README.md); mô hình analytical không thay migration OLTP.

<a id="factory-2026-11-04-sqlmesh"></a>

### SQLMesh: version mô hình và audit có đường chặn thật

| Thuộc tính | Kết quả đọc |
|---|---|
| Repo · license · SHA | `TobikoData/sqlmesh` · Apache-2.0 · `c4dbac499c312ccab17cb328ffb6ecfd801ce73d` |
| Cơ chế | Model SQL/Python, snapshot/version, plan tác động và virtual environment; test dùng fixture, audit trả hàng dữ liệu vi phạm |
| Cổng test | `Context._run_plan_tests` raise `PlanError` nếu test không thành công; `skip_tests` và chế độ chỉ test thay đổi là nhánh cấu hình cần kiểm, không mặc nhiên mọi plan đều chạy mọi test |
| Cổng audit | `ModelAudit.blocking=True` mặc định, nhưng `StandaloneAudit` mặc định không blocking và validator từ chối `blocking=True`; không thể chỉ bật cờ để đổi loại audit này thành cổng chặn. Scheduler gom audit có kết quả lỗi: blocking → `NodeAuditsErrors`, nonblocking → cảnh báo |
| Telemetry | `disable_anonymized_analytics=False` trong config; dispatcher đích `analytics.tobikodata.com/v1/`. Có optout `SQLMESH__DISABLE_ANONYMIZED_ANALYTICS=true` hoặc config tương ứng; không khẳng định payload đã được audit toàn bộ |
| CI | `pr.yaml` có docs/tests/lint và ma trận; chưa chạy SQLMesh, engine cloud hay benchmark trong đợt này |

**Phạm vi kiểm (2026-11-04):** đọc tài liệu, LICENSE, mã đường gọi và workflow tại SHA dưới đây; không cài/chạy upstream. Các cổng nghiệm thu là đề xuất cho repo tích hợp, chưa phải kết quả chạy của kho. Số sao không thu thập trong đợt này.

| Lựa chọn | Mặt mạnh | Phạm vi khác nhau |
|---|---|---|
| SQLMesh | Plan/version/environment gắn với backfill và audit | Hợp với vòng thay đổi analytical model; cần đánh giá engine, state store và lịch chạy |
| dbt | Mô hình biến đổi, tests và ecosystem | So feature ở đúng bản/adapter; không gộp dbt Core/fusion/cloud thành một thực thể |
| Great Expectations / Soda | Kiểm data quality theo expectation/check | Bổ sung contract ở nguồn/đầu ra; không tự thay kế hoạch deployment SQL |
| Dagster + OpenLineage | Orchestration tài sản và quan hệ chạy | Bổ sung nguồn gốc, không tự chứng minh ý nghĩa nghiệp vụ của SQL |

**Stack cho xưởng:** chốt schema và ví dụ nghiệp vụ → AI chỉ đề xuất SQL trên dữ liệu đã giảm nhạy cảm → parser/lint + test fixture → đọc plan gồm dữ liệu cần backfill → chạy môi trường dev có hạn mức → audit blocking → promote và theo dõi freshness/volume/business invariant. Ghi plan digest, snapshot/model revision, engine, window thời gian và lineage. Không cho text-to-SQL agent quyền DDL/write production chỉ vì truy vấn đã parse.

**Cổng nghiệm thu:** fixture làm sai join cardinality, duplicate key, timezone, tiền tệ, late-arriving data và PII phải gây lỗi đúng test/audit; test rỗng, audit bị skip/nonblocking và backfill ngoài window phải được phát hiện. So sánh kết quả theo khóa/grain, không chỉ row count. Thử rollback/khôi phục state và dữ liệu trên engine đích trước khi gọi quy trình có thể phục hồi; đổi virtual view không tự đảo ngược side effect bên ngoài hay mọi DDL.

**Nguồn §6:** [LICENSE](https://github.com/TobikoData/sqlmesh/blob/c4dbac499c312ccab17cb328ffb6ecfd801ce73d/LICENSE) · [test callsite](https://github.com/TobikoData/sqlmesh/blob/c4dbac499c312ccab17cb328ffb6ecfd801ce73d/sqlmesh/core/context.py) · [audit types](https://github.com/TobikoData/sqlmesh/blob/c4dbac499c312ccab17cb328ffb6ecfd801ce73d/sqlmesh/core/audit/definition.py) · [scheduler enforcement](https://github.com/TobikoData/sqlmesh/blob/c4dbac499c312ccab17cb328ffb6ecfd801ce73d/sqlmesh/core/scheduler.py) · [analytics config](https://github.com/TobikoData/sqlmesh/blob/c4dbac499c312ccab17cb328ffb6ecfd801ce73d/sqlmesh/core/config/root.py) · [analytics dispatcher](https://github.com/TobikoData/sqlmesh/blob/c4dbac499c312ccab17cb328ffb6ecfd801ce73d/sqlmesh/core/analytics/dispatcher.py) · [CI](https://github.com/TobikoData/sqlmesh/blob/c4dbac499c312ccab17cb328ffb6ecfd801ce73d/.github/workflows/pr.yaml).

## Nguồn

- https://duckdb.org/2026/08/05/github-40k-stars · https://en.wikipedia.org/wiki/Polars_(software) · https://github.com/sinaptik-ai/pandas-ai · https://github.com/topics/sql?l=python · https://aitools.flocci.in/alternatives/pandasai · https://jupysql.readthedocs.io/en/latest/tutorials/duckdb-github.html
- Bổ sung (12/10/2026): https://github.com/Canner/WrenAI · https://github.com/eosphoros-ai/DB-GPT · https://github.com/OtterMind/Chat2DB · https://github.com/dataease/SQLBot · https://github.com/apache/superset · https://github.com/apache/superset/tree/master/superset/mcp_service · https://github.com/metabase/metabase · https://www.metabase.com/docs/latest/ai/settings · https://github.com/tobymao/sqlglot · https://github.com/datahub-project/datahub · https://github.com/Kanaries/pygwalker · https://github.com/evidence-dev/evidence · https://github.com/getredash/redash · https://github.com/dataease/dataease · https://github.com/airbytehq/airbyte · https://github.com/great-expectations/great_expectations
