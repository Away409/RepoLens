# v0.2.0 验证记录

验证日期为 2026-11-15。

## 本地验证

环境为 Windows / Python 3.13.7。测试通过临时目录和 `httpx.MockTransport` 运行。

| 检查 | 结果 |
| --- | --- |
| pytest 离线测试 | 126 通过，1 跳过 |
| 覆盖率（启用分支覆盖） | 94%（终端显示的总覆盖率） |
| Ruff 静态检查及格式检查 | 通过 |
| sdist + wheel 构建 | 通过 |
| 新虚拟环境安装 wheel 并运行离线示例 | 通过，确认版本为 0.2.0，Markdown 含 Mermaid 图 |

Windows 本地环境缺少创建符号链接的权限，因此跳过对应本地测试。远端符号链接过滤另有模拟测试。新增测试覆盖缓存命中和绕过、Git 内容哈希和损坏、容量淘汰、并发事务、ETag 304、限流、预算及报告图和统计。

本轮新增 33 项回归检查，涵盖异常目录树、重复路径、无效大小和 SHA、语义损坏的缓存正文、HTTP Vary、非预期状态码、重试预算、缓存命中时的文件与字节预算，以及根目录 src.py 的导入关系。

## GitHub Actions

[RepoLens CI 工作流](https://github.com/Away409/RepoLens/actions/workflows/ci.yml)在 Ubuntu / Windows 分别运行 Python 3.11、3.12、3.13，每项执行安装、离线测试与覆盖率、Ruff 检查、格式检查、构建，以及新虚拟环境安装 wheel 后的 JSON / Markdown CLI 验证。[首次分支验证运行](https://github.com/Away409/RepoLens/actions/runs/43712956656)的六项均通过，包含三项 GitHub 托管的 Windows 作业。最新提交另见 [PR #1 Checks](https://github.com/Away409/RepoLens/pull/1/checks)。

工作流固定到官方发布的 [actions/checkout v7.0.1](https://github.com/actions/checkout/releases/tag/v7.0.1) 和 [actions/setup-python v7.0.0](https://github.com/actions/setup-python/releases/tag/v7.0.0) 的完整提交 SHA。

## 真实 GitHub REST API 冒烟测试

使用 v0.2.0 CLI 匿名访问公开仓库 `Away409/RepoLens` 的固定提交 `b627c0515eddd20a8df1cdf12e613098d40fa905`。使用空的专用缓存目录，连续分析两次。两次文件清单均完整（28 个文件），均根据文件预算读取了 17 个候选文本中的 5 个，共 14,453 字节。

| 指标 | 首次 | 再次 |
| --- | ---: | ---: |
| HTTP 请求总数 | 8 | 3 |
| 已校验的网络 Blob 读取 | 5 | 0 |
| Blob 缓存命中 | 0 | 5 |
| 条件请求返回 304 | 0 | 2 |
| 候选文本全部读取 | 否 | 否 |

复现时将缓存目录换成一个空目录，确认运行环境未设置 `GITHUB_TOKEN`：

```powershell
python -m repolens analyze Away409/RepoLens --ref b627c0515eddd20a8df1cdf12e613098d40fa905 --max-files 5 --cache-dir ./repolens-smoke-cache --format json -o smoke-cold.json
python -m repolens analyze Away409/RepoLens --ref b627c0515eddd20a8df1cdf12e613098d40fa905 --max-files 5 --cache-dir ./repolens-smoke-cache --format json -o smoke-warm.json
```

两次运行都通过网络确认元数据、固定提交和目录树。请求数反映 RepoLens 的预算消耗，GitHub 匿名配额消耗取决于服务端。真实私有仓库权限及长时间断网恢复尚未实测。

本轮修改 HTTP 缓存处理后，使用新的专用缓存目录再次运行上述真实网络测试，冷缓存 8 次请求、热缓存 3 次请求，5 次 Blob 命中和 2 个 304，结果一致。

## v0.1.0 历史样例

[Click 的 Markdown 样例](../examples/reports/click-8.1.7.md)和 [JSON 样例](../examples/reports/click-8.1.7.json)来自 v0.1.0。样例将 Click 8.1.7 的 15 个真实文件按 Git blob 规则核对 SHA 后，通过模拟 HTTP 回放生成。当时直连 GitHub 遇到匿名限流。
