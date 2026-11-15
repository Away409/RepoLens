# Changelog

## 0.2.0 — 2026-11-15

- 补强异常目录树、缓存正文和 HTTP Vary 校验，拒绝非预期成功状态；修复根目录 src.py 的模块解析。
- CI 增加新虚拟环境安装 wheel 后的 JSON / Markdown 端到端验证。
- GitHub Actions 验证 Ubuntu / Windows 上的 Python 3.11、3.12 和 3.13，执行安装、测试和覆盖率、Ruff 检查及构建。
- 匿名公开仓库默认启用有容量上限的 Git blob SHA 缓存，支持 `--no-cache` 和自定义缓存目录；仓库元数据、完整目录树支持 ETag 条件请求。
- JSON schema 1.1 增加内容读取完整性和远端读取统计。Markdown 增加缓存统计及有展示上限的 Mermaid 模块导入图。
- 增加离线缓存、HTTP 条件请求和报告回归测试，更新开发和发布验证记录。

## 0.1.0 — 2026-11-14

- GitHub 固定提交及本地目录只读分析。
- Python AST、依赖声明、工程结构、源码证据与 README 开头摘录。
- 中文 Markdown 与版本化 JSON 输出。
- 资源预算、代理支持、错误提示及输出覆盖保护。
- 离线测试、Windows 使用说明与项目学习路线。
