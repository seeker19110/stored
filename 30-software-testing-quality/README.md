# 30. Kiểm thử phần mềm và cổng chất lượng cho xưởng phát triển

<a id="testing-factory-2026-11-04"></a>

> Khảo sát 2026-11-04. Chuyên mục bổ sung lớp kiểm thử **hành vi phần mềm** bên cạnh eval LLM ở mục 07, checklist ở mục 09 và hạ tầng CI ở mục 13/32. Đã đọc LICENSE, code/callsite và CI của sáu upstream ghim dưới đây; không cài, build, chạy test hay phát tải vào dịch vụ. Không có kết quả benchmark do kho này thực hiện. Số sao để null vì không thu thập số liệu tin cậy trong đợt này.

## 1. Bài toán và phạm vi còn thiếu

Agent tạo được nhiều code làm tăng nhu cầu có oracle độc lập: **test phải có khả năng bác bỏ lời giải sai**. Một suite xanh chưa đủ nếu không thu được test, chỉ kiểm mock của chính implementation, cập nhật snapshot tự động hoặc bỏ qua integration. Xưởng cần quản từ ID yêu cầu tới test case, bộ dữ liệu, runner và artifact; không dùng một tỷ lệ coverage thay mọi tiêu chí chất lượng.

Cùng upstream đã có hồ sơ thì dẫn về đó: [Playwright](../11-browser-computer-use-sandbox/README.md), [StrykerJS](../13-dev-stack-devops/README.md), [axe-core/visual regression](../06-ui-ux-design/README.md#ui-factory-2026-11-04). Phần này thêm runner unit/property/integration/schema/load, không nhân bản catalog các thực thể đã có.

## 2. So sánh công cụ theo lớp lỗi

| Công cụ | Lớp và khác biệt | License đã đọc | Khi chọn | Giới hạn phải giữ |
|---|---|---|---|---|
| **Vitest** | Runner JS/TS theo Vite, Node/browser, coverage/reporters | MIT | Frontend/full-stack JS/TS đã dùng Vite; ghép Storybook addon-vitest | Browser Mode không tự là E2E toàn hệ; phải kiểm runtime và dependency theo phiên bản |
| **pytest** | Runner Python, fixture/parametrization/plugin, mã thoát phân loại | MIT | Backend Python, CLI và integration; giữ test nhỏ trước | Plugin/hook có thể thay hành vi; fixture không thay dữ liệu đại diện |
| **Hypothesis** | Sinh input theo strategy, tìm và thu nhỏ phản ví dụ | MPL-2.0 | Invariant, serialization, parser, tính tiền, state machine | Sinh dữ liệu tốt không tự sinh oracle đúng; không thay kiểm yêu cầu |
| **Testcontainers Python** | Dependency thật sống ngắn, lifecycle/wait strategy | Apache-2.0 | Postgres/Redis/queue khi mock hoặc SQLite khác production | Cần Docker/OCI daemon, image và tài nguyên; không phải sandbox chạy code không tin cậy |
| **Schemathesis** | Sinh request từ schema, kiểm response và chuỗi thao tác | MIT | Kiểm OpenAPI/GraphQL/gRPC có schema và môi trường thử | Gửi request thật có thể tạo/sửa/xóa dữ liệu; schema sai hoặc thiếu assertion nghiệp vụ vẫn bỏ sót lỗi |
| **Grafana k6** | Workload JS chạy trên Go runtime, đo metric và threshold | AGPL-3.0 | Load/soak và hồi quy latency/error theo workload | Không dùng toàn bộ API Node; license sửa/nhúng/phân phối cần xét đúng phạm vi; load generator cũng có giới hạn tài nguyên |

Đây là các lớp bổ sung nhau. Không cần cài tất cả cho mọi repo: Python không bắt buộc Vitest; ứng dụng nhỏ có thể dùng unit + vài integration/E2E đại diện trước khi thêm mutation hoặc load phân tán. Ngưỡng do rủi ro và SLO của sản phẩm quyết định.

## 3. Hồ sơ code-read tại phiên bản cụ thể

### 3.1 Vitest: runner và ca không thu được test

<a id="vitest-factory"></a>

Repo vitest-dev/vitest; SHA **289caab9cf9e9440e2a0be2d8783f7bd0f489a8b**, HEAD 2026-11-03. LICENSE MIT. Mã test-run.ts xác định thất bại khi module không ok/pending; khi không có module thì phụ thuộc **passWithNoTests**. Logger mô tả trường hợp cấu hình đó cho thoát 0 dù không có file test. Vì vậy CI phải kiểm **tập test dự kiến và số test đã chạy**, không bật passWithNoTests chỉ để làm pipeline xanh. Dùng chế độ run cho CI, reporter machine-readable và coverage theo vùng code quan trọng; giữ skipped/todo riêng. CI upstream có lint/typecheck và ma trận kiểm; chưa xác minh một lượt CI gần nhất hay tính tương thích của app cụ thể.

**Tích hợp đề xuất:** unit thuần cho logic → component/browser theo môi trường cần thiết → report JUnit/JSON và coverage của chính artifact ứng viên. Giữ snapshot có reviewer; không để agent tự duyệt snapshot mới do chính bản sửa tạo ra.

**Nguồn:** [LICENSE](https://github.com/vitest-dev/vitest/blob/289caab9cf9e9440e2a0be2d8783f7bd0f489a8b/LICENSE) · [packages/vitest/src/node/test-run.ts](https://github.com/vitest-dev/vitest/blob/289caab9cf9e9440e2a0be2d8783f7bd0f489a8b/packages/vitest/src/node/test-run.ts) · [packages/vitest/src/node/logger.ts](https://github.com/vitest-dev/vitest/blob/289caab9cf9e9440e2a0be2d8783f7bd0f489a8b/packages/vitest/src/node/logger.ts) · [.github/workflows/ci.yml](https://github.com/vitest-dev/vitest/blob/289caab9cf9e9440e2a0be2d8783f7bd0f489a8b/.github/workflows/ci.yml)

### 3.2 pytest: mã thoát và fixture có phạm vi

<a id="pytest-factory"></a>

Repo pytest-dev/pytest; SHA **8b005ed7f972987033ec34dc1e68b0635fb8142b**, HEAD 2026-11-02; MIT. _main thực hiện collection rồi runtestloop, trả TESTS_FAILED khi có failure và **NO_TESTS_COLLECTED = 5** khi không thu được test. Không dùng shell pipeline làm mất mã thoát, cũng không biến exit 5 thành thành công cho suite bắt buộc. Enum còn phân biệt interruption, internal/usage error; báo các kết quả đó như lỗi chạy kiểm, không như ứng dụng vượt qua test.

Fixture có scope và cleanup giúp quản dữ liệu/transaction/dependency theo vòng đời; người viết phải chọn phạm vi phù hợp, tránh session fixture làm test phụ thuộc thứ tự. Test plugin và cấu hình của sản phẩm trước khi áp kỳ vọng mã thoát cho mọi runner bọc ngoài. CI của pytest xây package và kiểm ma trận Python/OS; đó là bằng chứng có cơ chế kiểm upstream, chưa chứng minh fixture của xưởng đúng.

**Nguồn:** [LICENSE](https://github.com/pytest-dev/pytest/blob/8b005ed7f972987033ec34dc1e68b0635fb8142b/LICENSE) · [pytest config](https://github.com/pytest-dev/pytest/blob/8b005ed7f972987033ec34dc1e68b0635fb8142b/src/_pytest/config/__init__.py) · [src/_pytest/main.py](https://github.com/pytest-dev/pytest/blob/8b005ed7f972987033ec34dc1e68b0635fb8142b/src/_pytest/main.py) · [src/_pytest/fixtures.py](https://github.com/pytest-dev/pytest/blob/8b005ed7f972987033ec34dc1e68b0635fb8142b/src/_pytest/fixtures.py) · [.github/workflows/test.yml](https://github.com/pytest-dev/pytest/blob/8b005ed7f972987033ec34dc1e68b0635fb8142b/.github/workflows/test.yml)

### 3.3 Hypothesis: invariant và phản ví dụ giữ lại

<a id="hypothesis-factory"></a>

Repo HypothesisWorks/hypothesis; SHA **535f94db57d2248d4c0f799f319563c5c7fbbdbb**, HEAD 2026-11-03; MPL-2.0 theo LICENSE.txt, phần bên thứ ba có ghi chú riêng. Đọc settings, database và tutorial replay: example database lưu các trường hợp hữu ích để chạy lại; **không phải bản đặc tả đầy đủ của mọi lỗi đã biết**. Tài liệu khuyên dùng example rõ ràng cho regression quan trọng thay vì chỉ dựa cache. Ghim phiên bản Hypothesis, giữ phản ví dụ tối giản dưới dạng fixture/assertion và report settings/seed khi có; không hứa cùng seed tái tạo mọi bản sau nâng dependency.

Ví dụ thuộc tính phù hợp: decode(encode(x)) giữ dữ liệu theo miền đã khai báo; tổng tiền phân bổ bảo toàn theo quy tắc làm tròn; thao tác bị từ chối không đổi trạng thái. Phải nêu miền input và invariant nghiệp vụ độc lập với implementation; test cùng một hàm viết lại bằng công thức sai giống nhau vẫn có thể xanh. Settings về deadline/max_examples/derandomize cần chọn theo suite; timeout không phải assertion tính đúng đắn.

**Nguồn:** [LICENSE.txt](https://github.com/HypothesisWorks/hypothesis/blob/535f94db57d2248d4c0f799f319563c5c7fbbdbb/LICENSE.txt) · [hypothesis/src/hypothesis/_settings.py](https://github.com/HypothesisWorks/hypothesis/blob/535f94db57d2248d4c0f799f319563c5c7fbbdbb/hypothesis/src/hypothesis/_settings.py) · [hypothesis/src/hypothesis/database.py](https://github.com/HypothesisWorks/hypothesis/blob/535f94db57d2248d4c0f799f319563c5c7fbbdbb/hypothesis/src/hypothesis/database.py) · [hypothesis/docs/tutorial/replaying-failures.rst](https://github.com/HypothesisWorks/hypothesis/blob/535f94db57d2248d4c0f799f319563c5c7fbbdbb/hypothesis/docs/tutorial/replaying-failures.rst) · [.github/workflows/main.yml](https://github.com/HypothesisWorks/hypothesis/blob/535f94db57d2248d4c0f799f319563c5c7fbbdbb/.github/workflows/main.yml)

### 3.4 Testcontainers Python: integration với dependency thật

<a id="testcontainers-python-factory"></a>

Repo testcontainers/testcontainers-python; SHA **6146aa1170f415fcc825ed9bddc4eacbeb937a12**, HEAD 2026-10-07; Apache-2.0. Container.start khởi tạo Ryuk khi được bật, tạo container và gọi wait strategy; context manager có cleanup khi khởi động lỗi. PostgresContainer kiểm readiness qua truy vấn psql, mạnh hơn chỉ thấy PID/port. **Readiness của DB chưa chứng minh migration và nghiệp vụ ứng dụng đúng**: suite phải áp migration, ghi/đọc/query ranh giới và test transaction riêng.

Snapshot đọc cho thấy testcontainers.postgres đã deprecated, module mới là **testcontainers.community.postgres**; constructor PostgresContainer mặc định image **postgres:latest**. Khi tích hợp phải ghim image version/digest theo DB được hỗ trợ; không chép default latest rồi gọi môi trường tái lập. Ryuk có volume mapping Docker socket và quyền tùy cấu hình; chỉ dùng trong runner CI có phạm vi phù hợp, không coi nó là chỗ cô lập agent khỏi host. Chưa chạy Docker hay kiểm tương thích rootless/remote daemon.

**Nguồn:** [LICENSE.txt](https://github.com/testcontainers/testcontainers-python/blob/6146aa1170f415fcc825ed9bddc4eacbeb937a12/LICENSE.txt) · [src/testcontainers/core/container.py](https://github.com/testcontainers/testcontainers-python/blob/6146aa1170f415fcc825ed9bddc4eacbeb937a12/src/testcontainers/core/container.py) · [src/testcontainers/postgres.py](https://github.com/testcontainers/testcontainers-python/blob/6146aa1170f415fcc825ed9bddc4eacbeb937a12/src/testcontainers/postgres.py) · [Postgres community module](https://github.com/testcontainers/testcontainers-python/blob/6146aa1170f415fcc825ed9bddc4eacbeb937a12/src/testcontainers/community/postgres/__init__.py) · [.github/workflows/ci-core.yml](https://github.com/testcontainers/testcontainers-python/blob/6146aa1170f415fcc825ed9bddc4eacbeb937a12/.github/workflows/ci-core.yml)

### 3.5 Schemathesis: schema là nguồn sinh test, vẫn cần oracle nghiệp vụ

<a id="schemathesis-factory"></a>

Repo schemathesis/schemathesis; SHA **8033ef464ac7d1d12b527a6de5952defad2760d0**, HEAD 2026-11-04; MIT. README mô tả OpenAPI/GraphQL/gRPC và stateful sequences; đường checks.py chạy registry check, có hook/custom checks, not_a_server_error và max_response_time. Đọc thêm OpenAPI checks để phân biệt response-schema/status/content-type conformance với một assertion nghiệp vụ tự viết.

Giá trị: tạo dữ liệu biên và chuỗi request khó viết tay, lưu report/reproducer cho bug; bổ sung contract lint/diff ở mục 29. Giới hạn: schema cho phép một câu trả lời sai về tiền/quyền thì conformance vẫn có thể qua. Bộ ca hai principal/tenant và thay đổi trạng thái cần có kỳ vọng độc lập. README cảnh báo request tạo/sửa/xóa dữ liệu: dùng môi trường thử với tenant/dataset dùng xong được, giới hạn tốc độ và credential tối thiểu. Không quét production từ một ví dụ quickstart. Đợt này chưa xác minh tính năng BOLA/coverage toàn diện hay chạy request thật.

**Nguồn:** [LICENSE](https://github.com/schemathesis/schemathesis/blob/8033ef464ac7d1d12b527a6de5952defad2760d0/LICENSE) · [README.md](https://github.com/schemathesis/schemathesis/blob/8033ef464ac7d1d12b527a6de5952defad2760d0/README.md) · [src/schemathesis/checks.py](https://github.com/schemathesis/schemathesis/blob/8033ef464ac7d1d12b527a6de5952defad2760d0/src/schemathesis/checks.py) · [src/schemathesis/specs/openapi/checks.py](https://github.com/schemathesis/schemathesis/blob/8033ef464ac7d1d12b527a6de5952defad2760d0/src/schemathesis/specs/openapi/checks.py) · [.github/workflows/build.yml](https://github.com/schemathesis/schemathesis/blob/8033ef464ac7d1d12b527a6de5952defad2760d0/.github/workflows/build.yml) · [.github/workflows/test-hypothesis.yml](https://github.com/schemathesis/schemathesis/blob/8033ef464ac7d1d12b527a6de5952defad2760d0/.github/workflows/test-hypothesis.yml)

### 3.6 k6: check thất bại và threshold làm CI thất bại là hai việc khác

<a id="k6-factory"></a>

Repo grafana/k6; SHA **48d8dbbc12be13c42ab63a40b2221223b6e7cb4d**, HEAD 2026-11-03; AGPL-3.0 theo README/LICENSE.md. Hàm Check trả boolean và phát metric checks; **một check trả false không tự quyết định mã thoát của cả lượt chạy**. Đường run.go tính threshold cuối lượt và gắn ThresholdsHaveFailed khi vượt ngưỡng. Vì vậy muốn CI chặn khi check lỗi, phải đặt threshold phù hợp trên checks và các metric latency/error; chỉ in “checks failed” chưa là hợp đồng exit status.

Khai báo workload theo tốc độ đến/concurrency, tỷ lệ thao tác, kích thước payload/dữ liệu, warmup/cache và thời gian; báo p50/p95/p99 cùng số mẫu, lỗi và dropped iterations khi có. Ngưỡng như p95 < 500 ms chỉ là ví dụ nếu chưa có SLO được chủ sản phẩm chấp nhận; không biến thành chuẩn cho mọi dịch vụ. Giữ chức năng đúng dưới tải và giới hạn của generator bên cạnh throughput. Chưa chạy load hay xác minh hiệu năng của dịch vụ nào.

**Nguồn:** [LICENSE.md](https://github.com/grafana/k6/blob/48d8dbbc12be13c42ab63a40b2221223b6e7cb4d/LICENSE.md) · [README.md](https://github.com/grafana/k6/blob/48d8dbbc12be13c42ab63a40b2221223b6e7cb4d/README.md) · [internal/js/modules/k6/k6.go](https://github.com/grafana/k6/blob/48d8dbbc12be13c42ab63a40b2221223b6e7cb4d/internal/js/modules/k6/k6.go) · [internal/cmd/run.go](https://github.com/grafana/k6/blob/48d8dbbc12be13c42ab63a40b2221223b6e7cb4d/internal/cmd/run.go) · [metrics/thresholds.go](https://github.com/grafana/k6/blob/48d8dbbc12be13c42ab63a40b2221223b6e7cb4d/metrics/thresholds.go) · [.github/workflows/test.yml](https://github.com/grafana/k6/blob/48d8dbbc12be13c42ab63a40b2221223b6e7cb4d/.github/workflows/test.yml)

## 4. Pipeline kiểm theo rủi ro và bằng chứng

| Tầng | Artifact/kiểm chứng | Điều kiện cổng cần nêu | Phần vẫn cần kiểm khác |
|---|---|---|---|
| Static/type/build | Source + compiler/lint + artifact build | Đúng target, không che lỗi/allow-failure | Code biên dịch chưa chứng minh đúng hành vi |
| Unit/property | Requirement ID, fixture, assertion, phản ví dụ | Suite bắt được lỗi đã biết; test counts/skips rõ | Mock không thay transaction hoặc dependency thật |
| Integration | Dependency image digest, migration, dữ liệu thử, report | Đường ghi/đọc thực, transaction và lỗi dependency | Chưa bao phủ browser/khả năng dùng hoặc tải |
| API/schema/contract | Schema version, request/response/reproducer | Conformance + assertion quyền/nghiệp vụ | Schema không tự mô tả đủ mọi ràng buộc domain |
| Component/E2E/a11y | Story/route, persona/locale, trace/ảnh | Luồng critical và ca từ chối quyền chạy thật | Test tự động chưa chứng nhận accessibility toàn bộ |
| Mutation | Mutant/survivor, thời gian và phạm vi thay đổi | Survivor quan trọng được phân tích, không chỉ tăng coverage | Equivalent mutant và timeout cần phân loại |
| Load/soak/resilience | Workload, p95/p99/error, tài nguyên, recovery | Threshold có mã thoát + chức năng đúng trong điều kiện đã khai báo | Không suy khả năng chịu tải production từ máy/tải khác |

**Giữ một lỗi cố ý làm đối chứng:** ví dụ bỏ kiểm tra quyền, làm sai làm tròn hoặc bỏ một migration trong fixture riêng; cổng liên quan phải từ chối. Đây là kiểm hiệu lực của cổng, không yêu cầu sửa/xóa code production để làm demo. Agent viết code có thể đề xuất test, nhưng reviewer/requirement oracle cần độc lập với cùng giả định sai của implementation.

## 5. Độ tin cậy của suite, flakiness và dữ liệu thử

- **Không đánh đổi lỗi lấy xanh:** retry phải được ghi riêng first-attempt fail/retry-pass; quarantine có chủ, lý do và hạn xử lý, không biến thành bỏ qua vô thời hạn.
- **Đúng lần chạy:** report mang commit/build/config, suite/target, thời điểm, số executed/passed/failed/skipped/expected-failure. Artifact cũ hay suite không có test không đủ nghiệm thu.
- **Test data:** synthetic hoặc đã khử thông tin; seed/reset rõ, tenant tách biệt, clock/timezone được kiểm soát. Không sao chép dữ liệu khách hàng vào report CI công khai.
- **Coverage đúng nghĩa:** line/branch coverage cho biết code được thực thi; mutation và phản ví dụ giúp tìm assertion yếu; cả hai vẫn không thay thiếu yêu cầu. So sánh theo vùng thay đổi/rủi ro thay vì một con số toàn repo.
- **Snapshot có người duyệt:** diff hiển thị đúng phiên bản, font/browser/viewport/locale; ngưỡng so ảnh không được tăng chỉ để bỏ lỗi mới.
- **Ngân sách kiểm:** PR chạy bộ critical/unit và integration đại diện; suite sâu/load/resilience theo lịch hoặc trước release. Bản đồ chọn suite phải kiểm được để thay đổi nhạy cảm không lọt khỏi cổng bắt buộc.

## 6. Nối vào xưởng phát triển phần mềm

1. Product/BA chốt acceptance IDs và tác vụ critical → kiến trúc/API ở mục 29 xác định invariant và ranh giới.
2. Developer dùng unit/property ở vòng nhanh; QA/reviewer kiểm test có oracle độc lập và bổ sung ca âm.
3. Integration dùng dependency thật; API/schema và E2E kiểm sản phẩm đã ghép; eval LLM ở mục 07 tách khỏi test tất định.
4. Pipeline mục 32 lưu cùng artifact được test và phát hành; checklist mục 09 đối chiếu evidence thay lời tự khai.
5. SLO/incident mục 33 và migration/data mục 34 bổ sung phục hồi; lỗi thật được chuyển thành regression có version.

**Còn chưa xác minh:** chưa thực thi sáu công cụ, chưa chạy benchmark tương đối, chưa kiểm hết plugin/extension hoặc bản phát hành stable tương thích cho từng stack. Các ngưỡng và thiết kế pipeline ở đây là đề xuất kiến trúc; việc chọn/cài/chạy thuộc repo sản phẩm.
