# Contributing

1. 创建独立分支，说明要解决的实际问题。
2. 使用 Python 3.11+，执行 `python -m pip install -e '.[dev]'`。
3. 添加必要的离线回归测试，不让测试依赖外网、真实 Token 或目标项目执行。
4. 运行 `python -m pytest`、`python -m ruff check .` 和 `python -m ruff format --check .`。
5. 行为或字段变化时同步 README 与 JSON schema_version 策略。
6. PR 说明改动原因、验证方式和已知限制；不要上传私有报告、凭据或未经授权的源码。
