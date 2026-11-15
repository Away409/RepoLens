# GitHub 开发与发布

RepoLens 的上游仓库是 [Away409/RepoLens](https://github.com/Away409/RepoLens)。

## 开发分支与 PR

从最新的 `main` 创建功能分支，在该分支上提交并推送。以 v0.2.0 为例：

```powershell
git switch main
git pull --ff-only
git switch -c feature/v0.2.0
# 完成变更并提交后推送
git push -u origin feature/v0.2.0
```

以 `main` 为目标打开 PR。检查 PR 的 Checks 页和 [Actions 工作流](https://github.com/Away409/RepoLens/actions/workflows/ci.yml)，确认对应提交的 Ubuntu / Windows 各三个 Python 版本均运行并通过。开发机器上的测试、GitHub Actions 和真实 GitHub API 冒烟测试各有独立记录。详见 [验证记录](VALIDATION.md)。

## 发布检查

- 确认 `pyproject.toml` 和 CLI 版本一致，更新 CHANGELOG。
- 执行 `python -m build`，检查 sdist 和 wheel。用新虚拟环境安装 wheel 并运行离线示例。
- 检查待发布内容，移除私有仓库报告、缓存数据库和凭据。
- 审核并合并 PR 后，可在 GitHub 为对应提交创建 `v0.2.0` Release，附软件包和变更说明。

## 常见问题

**PowerShell 执行策略限制激活脚本**。可直接运行 `.\.venv\Scripts\python.exe`。

**GitHub API 访问失败**。按实际代理设置配置 `HTTPS_PROXY` 或 `ALL_PROXY`。Windows 系统代理设置可能需要手动同步到环境变量。

**GitHub API 限流**。等待配额恢复后重试；也可使用只读 `GITHUB_TOKEN` 或本地模式。设置 Token 后会绕过磁盘缓存。

**报告缺少部分 Python 文件**。先看清单状态、内容状态和告警，再按需要调整文件、字节和请求预算。
