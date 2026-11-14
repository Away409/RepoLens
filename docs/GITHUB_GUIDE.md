# 放到你的 GitHub

这个交付包包含源码、离线样例、真实样例报告、测试、CI 和 MIT License。没有绑定远端账号，也没有替你公开发布。

## 先检查

1. 在 Windows 按 README 安装并运行离线示例。
2. 运行测试；检查真实示例报告的“分析范围”和“限制与告警”。
3. 阅读 `sources.py`、`analyzer.py` 的关键设计，能够解释提交固定和 AST 分析。
4. 检查待发布文件，确保没有你自己的 Token、私有项目报告或个人路径。

## 新建空仓库

在 GitHub 新建仓库，名称可以用 `repolens`。是否公开由你选择。创建时不勾选自动添加 README、.gitignore 和 License，因为本项目已经包含这些文件。

安装 Git 后，在项目根目录运行以下 PowerShell 命令。将远端 URL 中的 `YOUR_USERNAME` 替换成自己的用户名：

```powershell
git init -b main
git add .
git status
git commit -m "feat: initial RepoLens static repository analyzer"
git remote add origin https://github.com/YOUR_USERNAME/repolens.git
git push -u origin main
```

如果 Git 提示缺少提交身份，按其提示设置你自己的 `user.name` 和 `user.email`；可以使用 GitHub 提供的 noreply 邮箱。不需要将 GitHub Token 添加到远端 URL。

这是新仓库首次导入的流程；后续开发先 `git switch -c feature/你的功能名`，通过 PR 合并到 main。若要上传到已有仓库，不要直接覆盖，先在独立分支整合。

## 发布后检查

- 打开 Actions，确认 Ubuntu / Windows 的 Python 3.11–3.13 工作流实际通过。
- About 可填写：`Evidence-based GitHub repository inspector with Python AST analysis and Chinese reports.`
- Topics 可填写：`python`、`github-api`、`static-analysis`、`cli`、`developer-tools`。
- 在 README 首屏展示离线示例和真实报告链接，不标注未经验证的性能或用户数量。
- 待 CI 通过后，可创建 `v0.1.0` Release，附源码包和变更说明。

## 常见问题

**PowerShell 不允许执行激活脚本**：无需修改执行策略，直接运行 `.\.venv\Scripts\python.exe`。

**GitHub 访问失败**：工具支持 HTTP / SOCKS 代理环境变量。请按你自己的代理设置配置 `HTTPS_PROXY` 或 `ALL_PROXY`；不要盲目复制别人的端口。Windows 系统代理并不一定自动转为 Python 的环境变量。

**pip 下载失败**：先确认 Python、网络和包源可用。不要从不明来源下载可执行安装脚本。

**报告提示限流**：稍后再试；需要时设置只读 `GITHUB_TOKEN`，或者使用本地模式。

**有些 Python 文件未分析**：查看预算，按需要增加 `--max-files` 和 `--max-requests`，不要将部分报告理解为完整审计。
