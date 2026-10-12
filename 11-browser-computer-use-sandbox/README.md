# 11 · Browser Agents, Computer Use & Agent Sandboxes

> Agent thao tác trình duyệt/máy tính và hạ tầng chạy code an toàn cho agent.

## 1. Browser agents / automation cho LLM

| Dự án | Repo | License | ★ (2026) | Cách hoạt động | Ghi chú |
|---|---|---|---|---|---|
| **Browser Use** | browser-use/browser-use | MIT | ~114k (9/2026) | Agent Python điều khiển Playwright, DOM + vision | Lớn nhất; có cloud |
| **agent-browser** (Vercel Labs) | vercel-labs/agent-browser | – | ~29.5k | CLI Rust cho agent điều khiển trình duyệt | Mới, tăng nhanh |
| **Stagehand** (Browserbase) | browserbase/stagehand | MIT | ~25.6k | SDK `act/extract/observe`, v4 dùng CDP trực tiếp (không Playwright) | Tích hợp Claude Code, Codex, Mastra |
| **Skyvern** | Skyvern-AI/skyvern | AGPL-3.0 | – | Vision + LLM, workflow form | |
| **Playwright MCP** | microsoft/playwright-mcp | Apache-2.0 | – | MCP server, làm việc trên accessibility tree (không screenshot) | Server MCP phổ biến nhất nhóm browser |
| **Steel / Browserbase / Hyperbrowser** | – | – | – | Browser-as-a-service cho agent | Hạ tầng |
| **Expect / Passmark** | – | – | – | AI testing trên browser | QA |

**Nhận định:** DOM/accessibility-tree rẻ và ổn định hơn vision; vision cần cho canvas/ứng dụng lạ. Chọn Browser Use để thử nhanh, Stagehand khi cần SDK có kiểm soát trong TypeScript.

## 2. Computer use (điều khiển máy tính)

| Nhà cung cấp / dự án | Ghi chú |
|---|---|
| Anthropic Computer Use (tool `computer_20xx`) | API tool chính thức; reference implementation + quickstart container |
| OpenAI Operator / CUA (Computer-Using Agent) | Sản phẩm trong ChatGPT + API `computer-use-preview` |
| Open Interpreter, UI-TARS (ByteDance), OS-Copilot | Mã mở, kiểm soát desktop |
| Benchmark | OSWorld, WebArena, Mind2Web, AgentDojo (bảo mật) |

## 3. Sandbox chạy code cho agent

| Nền tảng | Mã mở? | Cách cô lập | Cold start | Điểm nổi bật | Giá tham khảo |
|---|---|---|---|---|---|
| **E2B** | Apache-2.0 (SDK + infra) | Firecracker microVM, kernel riêng | ~0.5s (đo độc lập, nhanh nhất) | SDK đơn giản, nhiều template | ~$0.0504/vCPU-giờ |
| **Modal** | SDK mở, nền tảng đóng | gVisor (user-space kernel), tùy chọn VM | nhanh | **Có GPU** trong sandbox, serverless Python | ~$0.071/vCPU-giờ |
| **Daytona** | Từng mở; một nguồn nói đóng từ 6/2026 **(chưa xác minh)** | Container (tùy chọn VM) | Claim 90ms, đo được ~0.75s | Snapshot/fork stateful | |
| **Fly Machines** | Nền tảng | Firecracker | | Máy ảo nhanh, giá theo giây | |
| **Vercel Sandbox / Cloudflare Sandbox** | Nền tảng | microVM / isolate | | Gắn hệ sinh thái | |
| **microsandbox** | mã mở (`superradcompany/microsandbox`, ~8,7k★, beta, 12/10/2026) | microVM | | Self-host | |

**Chọn:** cần kernel riêng & mở → E2B; cần GPU → Modal; cần snapshot/fork → Daytona; tự host → microsandbox/Firecracker. Nghiên cứu bảo mật: arXiv 2606.08433 (so sánh engine: attack surface, CVE, patch cadence).

## 3b. Repo nổi tiếng bổ sung: computer use, crawl cho LLM, sandbox (đã xác minh 2026-10-12)

| Nhóm | Repo | ★ (12/10) | License | Hoạt động gần nhất | Vì sao chất lượng | Lưu ý |
|---|---|---|---|---|---|---|
| Computer use | **bytedance/UI-TARS-desktop** | 39,2k | Apache-2.0 | v0.3.1, commit 9/10/2026 | Agent GUI desktop chạy trên VLM UI-TARS của ByteDance, kèm Agent TARS (CLI/Web UI dựa trên MCP) | Phát hành thưa (v0.3.0 11/2025 → v0.3.1 10/2026); 350 issue mở |
| Computer use | **trycua/cua** | 29,5k | MIT (một phần FSL-1.1-MIT; extension tuỳ chọn có AGPL) | 10/10/2026 | Hạ tầng computer use mở: driver đa hệ điều hành, VM Lume trên Apple Silicon, bộ đánh giá Cua Bench; 5.373 commit | License trộn; README ghi `cuabot` (đã bỏ) có lỗi bảo mật đã biết |
| Computer use | **simular-ai/Agent-S** | 12,6k | Apache-2.0 | 8/10/2026 | Agent S3 báo 72,6% trên OSWorld (Best-of-N); paper TMLR 2026, COLM 2025 | Điểm tự báo cáo; commit gần đây chủ yếu sửa README, quảng bá API Simular |
| Crawl cho LLM | **firecrawl/firecrawl** | 190,7k | AGPL-3.0 (core), MIT (SDK) | commit 11/10/2026 (v2.11.0, 19/6/2026) | API scrape/crawl/map/search/agent trả dữ liệu sẵn cho LLM; SDK 9 ngôn ngữ, CLI, MCP server; mặc định tôn trọng robots.txt | AGPL: cung cấp qua mạng phải công bố mã; hướng tới bản hosted; 482 PR mở |
| Crawl cho LLM | **unclecode/crawl4ai** | 85,4k | Apache-2.0 | v0.9.4 (23/9/2026), commit 11/10 | Crawler xuất Markdown sẵn cho LLM, license thoáng, phát hành đều, có chính sách bảo mật | README tự mâu thuẫn về ghi công ("recommended" và "must"); mới có gói cloud trả phí |
| Browser MCP | **ChromeDevTools/chrome-devtools-mcp** | 53,3k | Apache-2.0 | v1.10.1 (23/9/2026) | MCP chính thức của nhóm Chrome DevTools: agent điều khiển và soi Chrome thật, debug, trace hiệu năng | Thu thống kê sử dụng mặc định; có thể gửi URL trong trace tới CrUX API |
| Sandbox | **google/gvisor** | 19,6k | Apache-2.0 | release 20261005.0 (8/10/2026) | Kernel user-space (`runsc`) cắm vào Docker/Kubernetes; Google bảo trì, phát hành gần như hằng tuần | Chỉ Linux; tương thích syscall và overhead hiệu năng **(chưa xác minh)** |
| Sandbox | **firecracker-microvm/firecracker** | 37,3k | Apache-2.0 | v1.17.0 (10/9/2026) | VMM microVM viết bằng Rust, AWS làm cho Lambda/Fargate, bề mặt tấn công nhỏ; nền của E2B (bảng §3) | Cần host Linux/KVM; mức thấp, không phải sandbox agent dùng ngay |
| Sandbox | **anthropics/sandbox-runtime** (trước ở anthropic-experimental) | 5,5k | Apache-2.0 | 10/10/2026 | Sandbox mức hệ điều hành cho tiến trình, không cần container: Seatbelt (macOS), bubblewrap (Linux); mạng chặn mặc định, chỉ mở domain allowlist qua proxy; làm cho Claude Code | Beta research preview; Windows mới alpha; định dạng config có thể đổi |

**Nhận xét:**

- `anthropics/sandbox-runtime` là mẫu đối chiếu tốt cho hai phát hiện ở mục 12 §4 (context-mode, Personal Jarvis): sandbox thật phải chặn mạng mặc định và lọc ở tầng hệ điều hành, không phải một tiến trình con mang theo env.
- Cập nhật bảng §3: microsandbox đã chuyển sang `superradcompany/microsandbox` (8,7k★, còn beta).
- Firecrawl (190,7k★) lớn gấp đôi crawl4ai nhưng là AGPL; nếu tự host làm dịch vụ cho người khác, crawl4ai (Apache-2.0) an toàn hơn về license.
- Đã cân nhắc nhưng không thêm: microsoft/OmniParser (25,5k★; code thật ra là CC-BY-4.0 dù badge ghi MIT, chỉ 2 commit từ 9/2025), browserless (13,8k★, SSPL-1.0, không OSI), jina-ai/reader (12,1k★, commit cuối 22/5/2026), steel-browser (7,8k★, beta), openai-cua-sample-app (1,9k★), OpenAdapt (1,8k★).

## 4. Nguồn

- https://gist.github.com/kevinmichaelchen/9d77b8a681238cc45297dff969686175 · https://www.firecrawl.dev/blog/best-browser-agents · https://scrapfly.io/blog/posts/stagehand-vs-browser-use · https://agentscamp.com/guides/comparisons/browser-agents-compared-2026 · https://bug0.com/blog/expect-vs-agent-browser-vs-stagehand-vs-passmark · https://github.com/browserbase/stagehand · https://kanopylabs.com/blog/stagehand-vs-browserbase-vs-steel-browser-ai
- https://www.superagent.sh/blog/ai-code-sandbox-benchmark-2026 · https://blog.logrocket.com/comparing-ai-agent-sandbox-platforms-e2b-modal-daytona-and-more/ · https://devtoollab.com/blog/best-ai-code-execution-sandboxes · https://bex.co/blog/2026/09/25/four-companies-one-sandbox-market-agent-code-execution · https://www.developersdigest.tech/blog/ai-agent-code-sandbox-comparison-2026 · https://www.beri.net/article/e2b-vs-modal-vs-daytona-agent-sandbox-pricing-isolation-2026 · https://particula.tech/blog/modal-vs-e2b-vs-daytona-vs-vercel-sandbox-ai-code-execution · https://arxiv.org/pdf/2606.08433
- §3b (12/10/2026): https://github.com/bytedance/UI-TARS-desktop · https://github.com/trycua/cua · https://github.com/simular-ai/Agent-S · https://github.com/firecrawl/firecrawl · https://github.com/unclecode/crawl4ai · https://github.com/ChromeDevTools/chrome-devtools-mcp · https://github.com/google/gvisor · https://github.com/firecracker-microvm/firecracker · https://github.com/anthropics/sandbox-runtime · https://github.com/superradcompany/microsandbox · https://github.com/microsoft/OmniParser · https://github.com/browserless/browserless · https://github.com/jina-ai/reader · https://github.com/steel-dev/steel-browser
