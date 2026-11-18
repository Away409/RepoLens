# RepoLens

**用可追溯的源码证据，快速了解一个 GitHub 仓库。**

RepoLens 是面向学习者和开发者的只读命令行工具：输入公开 GitHub 地址或本地目录，生成中文 Markdown 分析报告，也可导出结构化 JSON。不需要大模型 API、不克隆或执行被分析项目、不安装其依赖。

> v0.3.0 新增 C++ 源码和头文件分析。中文 Markdown 和 JSON 都包含符号、`#include` 和 `main` 入口线索及源码行号。

## 能做什么

| 功能 | 实现范围 |
| --- | --- |
| 远端仓库分析 | GitHub REST API；支持分支、tag、SHA，解析后固定同一提交 |
| 本地目录分析 | 不依赖 Git；读取当前目录，支持根 `.gitignore` |
| 工程概览 | 文件清单、按扩展名统计语言、README / LICENSE / 测试 / CI 线索 |
| 依赖解析 | PEP 621 / Poetry / dependency-groups、requirements、setup.cfg、package.json |
| CMake 线索 | 正则提取 find_package / add_executable，明确标为推断 |
| Python AST | 类、函数、方法、异步函数、静态导入、入口守卫、调用表达式行号 |
| C++ 语法树 | 命名空间、类、结构体、联合体、枚举、函数定义，`#include` 和全局 `main` 候选入口 |
| 源码追溯 | 远端报告附固定提交和行号链接 |
| 输出 | 中文 Markdown、带 `schema_version` 的 JSON |
| 资源控制 | 文件数、单文件大小、总字节、目录条目、API 请求预算与超时 |
| 失败处理 | 网络重试、限流提示、部分报告告警、禁止默认覆盖输出文件 |

## Windows 快速开始

需要 Python 3.11 或更高版本。解压源码包后，进入含 `pyproject.toml` 的 `repolens` 文件夹，打开 PowerShell：

```powershell
py -3 --version
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
.\.venv\Scripts\python.exe -m repolens version
```

这些命令直接使用虚拟环境的 Python，无需激活脚本或修改 PowerShell 执行策略。若 `py -3 --version` 低于 3.11，先安装新版 Python。

先运行附带的离线示例（只需安装本工具的依赖，不需要 GitHub Token）：

```powershell
.\.venv\Scripts\python.exe -m repolens analyze .\examples\demo_repo --local -o demo-report.md
```

再分析真实仓库：

```powershell
.\.venv\Scripts\python.exe -m repolens analyze https://github.com/pallets/click -o click-report.md
```

用 VS Code 或其他 Markdown 阅读器打开报告。已附示例见 [examples/demo-report.md](examples/demo-report.md)。

真实项目样本报告：[Click 8.1.7](examples/reports/click-8.1.7.md)（由校验过哈希的真实源码数据回放生成；直连验证遇到匿名限流，细节见验证记录）。

## macOS / Linux 安装

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -e '.[dev]'
.venv/bin/python -m repolens analyze examples/demo_repo --local -o demo-report.md
```

激活虚拟环境后可直接使用 `repolens`，与 `python -m repolens` 等价。

## 更多用法

以下示例假设已经激活虚拟环境；也可将 `repolens` 替换为上面的完整 Python 路径加 `-m repolens`。

```bash
# 1. GitHub 默认分支
repolens analyze https://github.com/pallets/click -o click.md

# 2. 本地项目，JSON 可供其他工具消费
repolens analyze ./examples/demo_repo --local --format json -o demo.json

# 3. 指定 tag；owner/repo 简写也支持
repolens analyze pallets/click --ref 8.1.7 -o click-8.1.7.md

# 4. 分析本项目，增加文件预算
repolens analyze . --local --max-files 100 -o self-report.md

# 5. 覆盖已有报告（必须显式指定）
repolens analyze ./examples/demo_repo --local -o demo.md --force

# 6. 分析 C++ 项目，导出符号和头文件引用
repolens analyze ./examples/cpp_demo --local --format json -o cpp-report.json

# 查看全部参数
repolens analyze --help
```

存在的本地目录优先识别为本地模式。远端请优先使用完整 GitHub URL，以免与同名目录混淆。URL 只接受仓库首页；`/tree/...`、`/blob/...` 地址请改用 `--ref`。本地目录包含空格时加引号。

### GitHub Token（可选）

公开仓库可以匿名读取，但匿名配额通常为每个 IP 每小时 60 次；受共享 IP、其他程序及 GitHub 二级限流影响。默认一次任务最多 50 个请求、最多尝试读取 35 个文件。重复分析仍会联系 GitHub 校验元数据、提交和目录树。

仅在需要时设置环境变量 `GITHUB_TOKEN`。推荐使用细粒度 Token，对指定仓库开放 Metadata 和 Contents 的读取权限，无需写权限。不要将 Token 写入代码、README、报告或命令参数。Windows 可使用安全输入：

```powershell
$tokenInput = Read-Host "GitHub Token" -AsSecureString
$env:GITHUB_TOKEN = [System.Net.NetworkCredential]::new("", $tokenInput).Password
.\.venv\Scripts\python.exe -m repolens analyze pallets/click -o click.md
Remove-Item Env:GITHUB_TOKEN
Remove-Variable tokenInput
```

私有仓库仅在 Token 有权限时可读；程序不为 Token 赋予任何额外权限。若网络无法访问 GitHub，可在自己电脑上下载或克隆可信仓库后使用 `--local`。

### 远端缓存

对未设置 `GITHUB_TOKEN` 的公开仓库，默认缓存经过 Git blob SHA 和大小校验的内容，并为仓库元数据、未截断的目录树发送 ETag 条件请求。每次仍重新解析 `--ref`（默认使用本次 GitHub 确认的默认分支）。有效的 304 复用对应响应正文，仍占用一次 RepoLens 请求预算。匿名条件请求是否节省 GitHub 自身配额，以 GitHub 响应为准。

| 参数或设置 | 用途 |
| --- | --- |
| `--no-cache` | 跳过磁盘缓存和 ETag 条件请求 |
| `--cache-dir PATH` | 为这次分析指定缓存目录，优先于环境变量 |
| `REPOLENS_CACHE_DIR` | 设置默认缓存目录 |

Windows 默认目录为 `%LOCALAPPDATA%\RepoLens\Cache`，macOS / Linux 默认目录为 `$XDG_CACHE_HOME/repolens` 或 `~/.cache/repolens`。缓存使用 `github-v1.sqlite3`，最多保留 64 MiB 数据正文和 4,096 条记录，超限时优先淘汰最久未使用的记录。SQLite 会复用空闲页，数据库文件还包含索引和页开销。在所有 RepoLens 进程退出后可删除该数据库以清空缓存。

带 Token 的请求和本地扫描绕过磁盘缓存。缓存保存匿名可读的源码和元数据，请使用自己控制的目录。缓存不可用或条目损坏时，工具按正常 API 请求预算重新读取；API 请求失败时，报告保留已经读到的内容。

### 预算和完整性

| 参数 | 默认值 | 含义 |
| --- | ---: | --- |
| `--max-files` | 35 | 最多尝试读取的候选文件数 |
| `--max-file-bytes` | 256000 | 单文件大小上限 |
| `--max-total-bytes` | 5000000 | 内容读取总预算 |
| `--max-entries` | 20000 | 目录清单条目上限 |
| `--max-requests` | 50 | 含重试的 API 请求预算 |
| `--timeout` | 20 | 单次网络操作超时秒数，不是任务总时限 |

优先读取配置、README 和常见入口文件（含 `main.cpp` 等），再读取一般 Python 和 C++ 文件，最后读取测试与示例。只下载需要的 blob，优先级相同按目录深度和路径排序。

远端至少需要元数据、提交和目录树请求。目录树截断、文件过大、语法错误、内容阶段断网或限流均在报告中注明；**“未发现”仅针对已扫描范围**。元数据阶段失败返回退出码 1；有效但有告警的部分报告返回 0；参数错误返回 2。自动化调用需同时检查 JSON 的 `inventory_complete`、`eligible_files`、`analyzed_files` 和 `warnings`。

JSON schema 1.1 新增 `content_complete` 和 `remote_reads`，原有字段保留。本地模式的 `remote_reads` 为 `null`。远端统计包括：

- `requests` 为本次尝试的 HTTP 请求总数，含 304、失败和重试。
- `remote_reads.blob_cache_hits` / `blob_cache_misses` 按尝试读取的候选文件计数。未启用缓存时两项均为零。
- `blob_network_reads` 只计已通过 SHA 和大小校验的网络 Blob。`not_modified` 计成功复用已校验正文的 304。
- `request_budget_exhausted` / `rate_limited` 表示请求预算或限流实际阻止了读取。`bytes_read` 同时计入缓存和网络的内容字节。

有导入边时，Markdown 图展示最多 40 个模块、80 对模块关系，重复导入合并为一条图边；JSON 的 `import_edges` 保留全部已提取边和行号。

### C++ 源码分析

扫描 `.cpp`、`.cc`、`.cxx`、`.c++`、`.hpp`、`.hh`、`.hxx`、`.h++` 和 `.h`，扩展名匹配忽略大小写。`.h` 用同一套 C++ 语法解析。涉及宏、条件编译或语法错误的文件可能只有部分结果，报告会给出告警。`main` 和 CMake 可执行目标都只是入口线索。

JSON schema 1.2 新增 `cpp_files`。每个文件包含 `path`、`has_parse_errors`、`symbols` 和 `includes`。旧字段继续可用，`modules` 和 `import_edges` 仍用于 Python。

`includes[].kind` 区分引号（`quoted`）、尖括号（`angled`）和宏表达式（`macro`）。引号引用先匹配源文件所在目录，再检查仓库根目录、`include/` 和 `src/`。尖括号只检查这三个候选目录。缺失或歧义时 `target` 为 `null`。匹配仅使用文件清单，不额外读取头文件。条件分支中的指令都算作语法线索，宏展开、实际编译参数和编译器搜索路径留待构建时确定。

## 验证与开发

```bash
python -m pytest --cov=repolens --cov-report=term-missing
python -m ruff check .
python -m ruff format --check .
python -m build
python tools/verify_wheel.py
```

测试使用临时目录和 HTTP 模拟响应，无需 GitHub Token 或联网；默认不会对真实仓库发请求。CI 配置覆盖 Ubuntu / Windows 的 Python 3.11、3.12、3.13。是否实际跑过以及本次结果见 [docs/VALIDATION.md](docs/VALIDATION.md)。

核心结构：`sources.py` 获取快照；`analyzer.py` 提取证据；`cpp.py` 提取 C++ 语法证据；`models.py` 定义 JSON 契约；`render.py` 生成报告；`cli.py` 处理参数和输出。

详细设计见 [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)，发布步骤见 [docs/GITHUB_GUIDE.md](docs/GITHUB_GUIDE.md)，学习及项目经历整理见 [docs/LEARNING.md](docs/LEARNING.md)。

## 边界

- Python 和 C++ 支持静态语法分析。Java、TypeScript 等暂提供扩展名统计和已有的配置线索。
- import 关系仅静态匹配常见根目录和 `src/` 布局；不解释动态导入、`sys.path` 修改和复杂 monorepo 包映射。
- 不读取所有文件；不展开依赖锁文件、递归 requirements 引用或远端依赖 URL；`setup.py` 仅分析符号，不提取其中的依赖声明。
- 本地只读取根 `.gitignore`，不调用 Git；忽略规则并不等价于完整 Git 工作树语义。
- 不跟随符号链接、子模块，不解压下载的项目，不执行安装脚本。不要在分析期间主动改写目录中的链接；这不是针对恶意并发文件系统变更的沙箱。
- 常见 `.env` / 私钥文件被排除，但普通源码、配置、路径中仍可能含敏感信息。报告公开前请自行审阅。
- 当前以本地运行的 CLI 为主。

## 路线图

- [x] GitHub + 本地目录，中文 Markdown + JSON
- [x] 预算控制、失败处理、源码证据、离线测试
- [x] 固定 blob SHA 缓存、ETag 验证和模块导入图
- [x] C++ 语法解析、符号、头文件引用和入口线索
- [ ] TypeScript 解析器
- [ ] 可选 LLM 解释层，要求引用静态证据并显示费用预算

MIT License。欢迎通过 Issue 和 Pull Request 提出问题；不要提交包含真实密钥的测试样本。

参考：[Git trees](https://docs.github.com/en/rest/git/trees)、[Git blobs](https://docs.github.com/en/rest/git/blobs)、[API 限流](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api)、[Python AST](https://docs.python.org/3/library/ast.html)。
