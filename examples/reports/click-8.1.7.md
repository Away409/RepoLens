# RepoLens · pallets/click

> 基于文件清单、配置和 Python AST 的静态分析；不执行目标代码，不调用大模型。

## 项目概览

- 来源：github
- 描述：Python composable command line interface toolkit
- 提交：874ca2bc1c30d93a4ac6e36a15ed685eafe89097
- 生成时间（UTC）：2026-11-14T12:06:13.973362+00:00
- 许可证元数据：BSD-3-Clause

## 分析范围

| 指标 | 结果 |
| --- | --- |
| 纳入清单的文件 | 146 |
| 内容候选（Python / 支持的配置 / README） | 84 |
| 实际读取文本 | 15 |
| 读取字节 | 251129 |
| API 请求次数（含重试） | 18 |
| 清单状态 | 完整（应用排除规则后） |

语言统计按清单中的扩展名计文件数，不代表代码行数或 GitHub Linguist 结果。

## 技术栈线索

| 语言 | 文件数 |
| --- | ---: |
| Python | 71 |

## README 开头摘录

来源：[README.rst:1](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/README.rst#L1)（最多 16 行 / 1200 字符；非自动总结）

> \\$ click\\\_
> ==========
>
> Click is a Python package for creating beautiful command line interfaces
> in a composable way with as little code as necessary. It's the "Command
> Line Interface Creation Kit". It's highly configurable but comes with
> sensible defaults out of the box.
>
> It aims to make the process of writing command line tools quick and fun
> while also preventing any frustration caused by the inability to
> implement an intended CLI API.
>
> Click in three points:
>
> -   Arbitrary nesting of commands
> -   Automatic help page generation

## 工程结构检查

检测到文件只说明它存在；不会声称测试通过或配置有效。

- **README**：[README.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/README.rst)、[examples/README](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/README)、[examples/aliases/README](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/aliases/README)、[examples/colors/README](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/colors/README)、[examples/completion/README](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/completion/README) 等 12 个
- **LICENSE**：[LICENSE.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/LICENSE.rst)、[docs/license.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/license.rst)
- **测试**：[tests/conftest.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/tests/conftest.py)、[tests/test\_arguments.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/tests/test_arguments.py)、[tests/test\_basic.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/tests/test_basic.py)、[tests/test\_chain.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/tests/test_chain.py)、[tests/test\_command\_decorators.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/tests/test_command_decorators.py) 等 29 个
- **CI**：[.github/workflows/lock.yaml](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/.github/workflows/lock.yaml)、[.github/workflows/publish.yaml](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/.github/workflows/publish.yaml)、[.github/workflows/tests.yaml](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/.github/workflows/tests.yaml)
- **贡献指南**：[CONTRIBUTING.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/CONTRIBUTING.rst)

## 文件目录（最多 120 项）

- [.editorconfig](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/.editorconfig)
- [.github/ISSUE\_TEMPLATE/bug-report.md](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/.github/ISSUE_TEMPLATE/bug-report.md)
- [.github/ISSUE\_TEMPLATE/config.yml](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/.github/ISSUE_TEMPLATE/config.yml)
- [.github/ISSUE\_TEMPLATE/feature-request.md](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/.github/ISSUE_TEMPLATE/feature-request.md)
- [.github/dependabot.yml](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/.github/dependabot.yml)
- [.github/pull\_request\_template.md](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/.github/pull_request_template.md)
- [.github/workflows/lock.yaml](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/.github/workflows/lock.yaml)
- [.github/workflows/publish.yaml](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/.github/workflows/publish.yaml)
- [.github/workflows/tests.yaml](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/.github/workflows/tests.yaml)
- [.gitignore](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/.gitignore)
- [.pre-commit-config.yaml](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/.pre-commit-config.yaml)
- [.readthedocs.yaml](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/.readthedocs.yaml)
- [CHANGES.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/CHANGES.rst)
- [CODE\_OF\_CONDUCT.md](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/CODE_OF_CONDUCT.md)
- [CONTRIBUTING.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/CONTRIBUTING.rst)
- [LICENSE.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/LICENSE.rst)
- [MANIFEST.in](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/MANIFEST.in)
- [README.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/README.rst)
- [artwork/logo.svg](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/artwork/logo.svg)
- [docs/Makefile](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/Makefile)
- [docs/\_static/click-icon.png](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/_static/click-icon.png)
- [docs/\_static/click-logo-sidebar.png](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/_static/click-logo-sidebar.png)
- [docs/\_static/click-logo.png](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/_static/click-logo.png)
- [docs/advanced.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/advanced.rst)
- [docs/api.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/api.rst)
- [docs/arguments.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/arguments.rst)
- [docs/changes.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/changes.rst)
- [docs/commands.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/commands.rst)
- [docs/complex.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/complex.rst)
- [docs/conf.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/conf.py)
- [docs/contrib.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/contrib.rst)
- [docs/documentation.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/documentation.rst)
- [docs/exceptions.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/exceptions.rst)
- [docs/index.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/index.rst)
- [docs/license.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/license.rst)
- [docs/make.bat](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/make.bat)
- [docs/options.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/options.rst)
- [docs/parameters.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/parameters.rst)
- [docs/prompts.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/prompts.rst)
- [docs/quickstart.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/quickstart.rst)
- [docs/setuptools.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/setuptools.rst)
- [docs/shell-completion.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/shell-completion.rst)
- [docs/testing.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/testing.rst)
- [docs/unicode-support.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/unicode-support.rst)
- [docs/upgrading.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/upgrading.rst)
- [docs/utils.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/utils.rst)
- [docs/why.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/why.rst)
- [docs/wincmd.rst](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/docs/wincmd.rst)
- [examples/README](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/README)
- [examples/aliases/README](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/aliases/README)
- [examples/aliases/aliases.ini](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/aliases/aliases.ini)
- [examples/aliases/aliases.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/aliases/aliases.py)
- [examples/aliases/setup.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/aliases/setup.py)
- [examples/colors/README](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/colors/README)
- [examples/colors/colors.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/colors/colors.py)
- [examples/colors/setup.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/colors/setup.py)
- [examples/completion/README](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/completion/README)
- [examples/completion/completion.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/completion/completion.py)
- [examples/completion/setup.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/completion/setup.py)
- [examples/complex/README](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/complex/README)
- [examples/complex/complex/\_\_init\_\_.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/complex/complex/__init__.py)
- [examples/complex/complex/cli.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/complex/complex/cli.py)
- [examples/complex/complex/commands/\_\_init\_\_.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/complex/complex/commands/__init__.py)
- [examples/complex/complex/commands/cmd\_init.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/complex/complex/commands/cmd_init.py)
- [examples/complex/complex/commands/cmd\_status.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/complex/complex/commands/cmd_status.py)
- [examples/complex/setup.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/complex/setup.py)
- [examples/imagepipe/.gitignore](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/imagepipe/.gitignore)
- [examples/imagepipe/README](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/imagepipe/README)
- [examples/imagepipe/example01.jpg](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/imagepipe/example01.jpg)
- [examples/imagepipe/example02.jpg](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/imagepipe/example02.jpg)
- [examples/imagepipe/imagepipe.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/imagepipe/imagepipe.py)
- [examples/imagepipe/setup.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/imagepipe/setup.py)
- [examples/inout/README](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/inout/README)
- [examples/inout/inout.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/inout/inout.py)
- [examples/inout/setup.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/inout/setup.py)
- [examples/naval/README](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/naval/README)
- [examples/naval/naval.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/naval/naval.py)
- [examples/naval/setup.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/naval/setup.py)
- [examples/repo/README](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/repo/README)
- [examples/repo/repo.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/repo/repo.py)
- [examples/repo/setup.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/repo/setup.py)
- [examples/termui/README](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/termui/README)
- [examples/termui/setup.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/termui/setup.py)
- [examples/termui/termui.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/termui/termui.py)
- [examples/validation/README](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/validation/README)
- [examples/validation/setup.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/validation/setup.py)
- [examples/validation/validation.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/examples/validation/validation.py)
- [requirements/build.in](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/requirements/build.in)
- [requirements/build.txt](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/requirements/build.txt)
- [requirements/dev.in](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/requirements/dev.in)
- [requirements/dev.txt](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/requirements/dev.txt)
- [requirements/docs.in](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/requirements/docs.in)
- [requirements/docs.txt](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/requirements/docs.txt)
- [requirements/tests.in](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/requirements/tests.in)
- [requirements/tests.txt](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/requirements/tests.txt)
- [requirements/typing.in](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/requirements/typing.in)
- [requirements/typing.txt](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/requirements/typing.txt)
- [setup.cfg](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/setup.cfg)
- [setup.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/setup.py)
- [src/click/\_\_init\_\_.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py)
- [src/click/\_compat.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py)
- [src/click/\_termui\_impl.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py)
- [src/click/\_textwrap.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_textwrap.py)
- [src/click/\_winconsole.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py)
- [src/click/core.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py)
- [src/click/decorators.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py)
- [src/click/exceptions.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py)
- [src/click/formatting.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/formatting.py)
- [src/click/globals.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/globals.py)
- [src/click/parser.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py)
- [src/click/py.typed](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/py.typed)
- [src/click/shell\_completion.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py)
- [src/click/termui.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/termui.py)
- [src/click/testing.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/testing.py)
- [src/click/types.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/types.py)
- [src/click/utils.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/utils.py)
- [tests/conftest.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/tests/conftest.py)
- [tests/test\_arguments.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/tests/test_arguments.py)
- [tests/test\_basic.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/tests/test_basic.py)
- [tests/test\_chain.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/tests/test_chain.py)
- …另有 26 项；完整清单见 JSON。

## 声明依赖

仅解析已读取的清单，不解析传递依赖或锁文件，不验证版本能否安装。

| 名称 | 声明 | 分组 | 来源 |
| --- | --- | --- | --- |
| 未提取到 | — | — | — |

## 入口证据

未发现可识别的入口声明；库项目也可能没有独立可执行入口。

## Python 模块与符号

方法与嵌套函数使用限定名称。

### setup.py

源码：[setup.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/setup.py)

- 未定义类或函数。

### src/click/\_\_init\_\_.py

源码：[src/click/\_\_init\_\_.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py)

- 未定义类或函数。

### src/click/\_compat.py

源码：[src/click/\_compat.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py)

- function **\_make\_text\_stream** — [src/click/\_compat.py:15](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L15)
- function **is\_ascii\_encoding** — [src/click/\_compat.py:36](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L36)
- function **get\_best\_encoding** — [src/click/\_compat.py:44](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L44)
- class **\_NonClosingTextIOWrapper** — [src/click/\_compat.py:52](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L52)
- function **\_NonClosingTextIOWrapper.\_\_init\_\_** — [src/click/\_compat.py:53](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L53)
- function **\_NonClosingTextIOWrapper.\_\_del\_\_** — [src/click/\_compat.py:67](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L67)
- function **\_NonClosingTextIOWrapper.isatty** — [src/click/\_compat.py:73](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L73)
- class **\_FixupStream** — [src/click/\_compat.py:78](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L78)
- function **\_FixupStream.\_\_init\_\_** — [src/click/\_compat.py:88](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L88)
- function **\_FixupStream.\_\_getattr\_\_** — [src/click/\_compat.py:98](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L98)
- function **\_FixupStream.read1** — [src/click/\_compat.py:101](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L101)
- function **\_FixupStream.readable** — [src/click/\_compat.py:109](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L109)
- function **\_FixupStream.writable** — [src/click/\_compat.py:121](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L121)
- function **\_FixupStream.seekable** — [src/click/\_compat.py:136](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L136)
- function **\_is\_binary\_reader** — [src/click/\_compat.py:147](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L147)
- function **\_is\_binary\_writer** — [src/click/\_compat.py:156](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L156)
- function **\_find\_binary\_reader** — [src/click/\_compat.py:169](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L169)
- function **\_find\_binary\_writer** — [src/click/\_compat.py:187](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L187)
- function **\_stream\_is\_misconfigured** — [src/click/\_compat.py:205](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L205)
- function **\_is\_compat\_stream\_attr** — [src/click/\_compat.py:214](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L214)
- function **\_is\_compatible\_text\_stream** — [src/click/\_compat.py:223](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L223)
- function **\_force\_correct\_text\_stream** — [src/click/\_compat.py:234](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L234)
- function **\_force\_correct\_text\_reader** — [src/click/\_compat.py:280](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L280)
- function **\_force\_correct\_text\_writer** — [src/click/\_compat.py:296](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L296)
- function **get\_binary\_stdin** — [src/click/\_compat.py:312](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L312)
- function **get\_binary\_stdout** — [src/click/\_compat.py:319](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L319)
- function **get\_binary\_stderr** — [src/click/\_compat.py:326](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L326)
- function **get\_text\_stdin** — [src/click/\_compat.py:333](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L333)
- function **get\_text\_stdout** — [src/click/\_compat.py:342](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L342)
- function **get\_text\_stderr** — [src/click/\_compat.py:351](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L351)
- function **\_wrap\_io\_open** — [src/click/\_compat.py:360](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L360)
- function **open\_stream** — [src/click/\_compat.py:373](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L373)
- class **\_AtomicFile** — [src/click/\_compat.py:454](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L454)
- function **\_AtomicFile.\_\_init\_\_** — [src/click/\_compat.py:455](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L455)
- function **\_AtomicFile.name** — [src/click/\_compat.py:462](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L462)
- function **\_AtomicFile.close** — [src/click/\_compat.py:465](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L465)
- function **\_AtomicFile.\_\_getattr\_\_** — [src/click/\_compat.py:472](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L472)
- function **\_AtomicFile.\_\_enter\_\_** — [src/click/\_compat.py:475](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L475)
- function **\_AtomicFile.\_\_exit\_\_** — [src/click/\_compat.py:478](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L478)
- function **\_AtomicFile.\_\_repr\_\_** — [src/click/\_compat.py:481](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L481)
- 更多符号见 JSON。

### src/click/\_termui\_impl.py

源码：[src/click/\_termui\_impl.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py)

- class **ProgressBar** — [src/click/\_termui\_impl.py:37](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L37)
- function **ProgressBar.\_\_init\_\_** — [src/click/\_termui\_impl.py:38](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L38)
- function **ProgressBar.\_\_enter\_\_** — [src/click/\_termui\_impl.py:107](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L107)
- function **ProgressBar.\_\_exit\_\_** — [src/click/\_termui\_impl.py:112](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L112)
- function **ProgressBar.\_\_iter\_\_** — [src/click/\_termui\_impl.py:120](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L120)
- function **ProgressBar.\_\_next\_\_** — [src/click/\_termui\_impl.py:126](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L126)
- function **ProgressBar.render\_finish** — [src/click/\_termui\_impl.py:134](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L134)
- function **ProgressBar.pct** — [src/click/\_termui\_impl.py:141](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L141)
- function **ProgressBar.time\_per\_iteration** — [src/click/\_termui\_impl.py:147](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L147)
- function **ProgressBar.eta** — [src/click/\_termui\_impl.py:153](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L153)
- function **ProgressBar.format\_eta** — [src/click/\_termui\_impl.py:158](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L158)
- function **ProgressBar.format\_pos** — [src/click/\_termui\_impl.py:173](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L173)
- function **ProgressBar.format\_pct** — [src/click/\_termui\_impl.py:179](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L179)
- function **ProgressBar.format\_bar** — [src/click/\_termui\_impl.py:182](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L182)
- function **ProgressBar.format\_progress\_line** — [src/click/\_termui\_impl.py:201](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L201)
- function **ProgressBar.render\_progress** — [src/click/\_termui\_impl.py:228](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L228)
- function **ProgressBar.make\_step** — [src/click/\_termui\_impl.py:273](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L273)
- function **ProgressBar.update** — [src/click/\_termui\_impl.py:295](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L295)
- function **ProgressBar.finish** — [src/click/\_termui\_impl.py:321](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L321)
- function **ProgressBar.generator** — [src/click/\_termui\_impl.py:326](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L326)
- function **pager** — [src/click/\_termui\_impl.py:360](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L360)
- function **\_pipepager** — [src/click/\_termui\_impl.py:395](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L395)
- function **\_tempfilepager** — [src/click/\_termui\_impl.py:445](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L445)
- function **\_nullpager** — [src/click/\_termui\_impl.py:466](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L466)
- class **Editor** — [src/click/\_termui\_impl.py:476](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L476)
- function **Editor.\_\_init\_\_** — [src/click/\_termui\_impl.py:477](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L477)
- function **Editor.get\_editor** — [src/click/\_termui\_impl.py:489](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L489)
- function **Editor.edit\_file** — [src/click/\_termui\_impl.py:503](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L503)
- function **Editor.edit** — [src/click/\_termui\_impl.py:525](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L525)
- function **open\_url** — [src/click/\_termui\_impl.py:573](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L573)
- function **open\_url.\_unquote\_file** — [src/click/\_termui\_impl.py:576](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L576)
- function **\_translate\_ch\_to\_exc** — [src/click/\_termui\_impl.py:633](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L633)
- function **raw\_terminal** — [src/click/\_termui\_impl.py:650](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L650)
- function **getchar** — [src/click/\_termui\_impl.py:653](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L653)
- function **raw\_terminal** — [src/click/\_termui\_impl.py:705](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L705)
- function **getchar** — [src/click/\_termui\_impl.py:731](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L731)

### src/click/\_textwrap.py

源码：[src/click/\_textwrap.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_textwrap.py)

- class **TextWrapper** — [src/click/\_textwrap.py:6](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_textwrap.py#L6)
- function **TextWrapper.\_handle\_long\_word** — [src/click/\_textwrap.py:7](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_textwrap.py#L7)
- function **TextWrapper.extra\_indent** — [src/click/\_textwrap.py:26](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_textwrap.py#L26)
- function **TextWrapper.indent\_only** — [src/click/\_textwrap.py:38](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_textwrap.py#L38)

### src/click/\_winconsole.py

源码：[src/click/\_winconsole.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py)

- class **Py\_buffer** — [src/click/\_winconsole.py:75](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py#L75)
- function **get\_buffer** — [src/click/\_winconsole.py:93](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py#L93)
- class **\_WindowsConsoleRawIOBase** — [src/click/\_winconsole.py:105](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py#L105)
- function **\_WindowsConsoleRawIOBase.\_\_init\_\_** — [src/click/\_winconsole.py:106](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py#L106)
- function **\_WindowsConsoleRawIOBase.isatty** — [src/click/\_winconsole.py:109](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py#L109)
- class **\_WindowsConsoleReader** — [src/click/\_winconsole.py:114](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py#L114)
- function **\_WindowsConsoleReader.readable** — [src/click/\_winconsole.py:115](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py#L115)
- function **\_WindowsConsoleReader.readinto** — [src/click/\_winconsole.py:118](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py#L118)
- class **\_WindowsConsoleWriter** — [src/click/\_winconsole.py:149](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py#L149)
- function **\_WindowsConsoleWriter.writable** — [src/click/\_winconsole.py:150](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py#L150)
- function **\_WindowsConsoleWriter.\_get\_error\_message** — [src/click/\_winconsole.py:154](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py#L154)
- function **\_WindowsConsoleWriter.write** — [src/click/\_winconsole.py:161](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py#L161)
- class **ConsoleStream** — [src/click/\_winconsole.py:181](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py#L181)
- function **ConsoleStream.\_\_init\_\_** — [src/click/\_winconsole.py:182](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py#L182)
- function **ConsoleStream.name** — [src/click/\_winconsole.py:187](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py#L187)
- function **ConsoleStream.write** — [src/click/\_winconsole.py:190](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py#L190)
- function **ConsoleStream.writelines** — [src/click/\_winconsole.py:199](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py#L199)
- function **ConsoleStream.\_\_getattr\_\_** — [src/click/\_winconsole.py:203](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py#L203)
- function **ConsoleStream.isatty** — [src/click/\_winconsole.py:206](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py#L206)
- function **ConsoleStream.\_\_repr\_\_** — [src/click/\_winconsole.py:209](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py#L209)
- function **\_get\_text\_stdin** — [src/click/\_winconsole.py:213](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py#L213)
- function **\_get\_text\_stdout** — [src/click/\_winconsole.py:223](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py#L223)
- function **\_get\_text\_stderr** — [src/click/\_winconsole.py:233](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py#L233)
- function **\_is\_console** — [src/click/\_winconsole.py:250](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py#L250)
- function **\_get\_windows\_console\_stream** — [src/click/\_winconsole.py:263](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py#L263)

### src/click/core.py

源码：[src/click/core.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py)

- function **\_complete\_visible\_commands** — [src/click/core.py:48](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L48)
- function **\_check\_multicommand** — [src/click/core.py:67](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L67)
- function **batch** — [src/click/core.py:91](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L91)
- function **augment\_usage\_errors** — [src/click/core.py:96](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L96)
- function **iter\_params\_for\_processing** — [src/click/core.py:114](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L114)
- function **iter\_params\_for\_processing.sort\_key** — [src/click/core.py:123](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L123)
- class **ParameterSource** — [src/click/core.py:134](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L134)
- class **Context** — [src/click/core.py:160](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L160)
- function **Context.\_\_init\_\_** — [src/click/core.py:260](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L260)
- function **Context.to\_info\_dict** — [src/click/core.py:432](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L432)
- function **Context.\_\_enter\_\_** — [src/click/core.py:453](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L453)
- function **Context.\_\_exit\_\_** — [src/click/core.py:458](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L458)
- function **Context.scope** — [src/click/core.py:470](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L470)
- function **Context.meta** — [src/click/core.py:508](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L508)
- function **Context.make\_formatter** — [src/click/core.py:535](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L535)
- function **Context.with\_resource** — [src/click/core.py:549](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L549)
- function **Context.call\_on\_close** — [src/click/core.py:578](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L578)
- function **Context.close** — [src/click/core.py:590](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L590)
- function **Context.command\_path** — [src/click/core.py:600](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L600)
- function **Context.find\_root** — [src/click/core.py:618](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L618)
- function **Context.find\_object** — [src/click/core.py:625](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L625)
- function **Context.ensure\_object** — [src/click/core.py:637](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L637)
- function **Context.lookup\_default** — [src/click/core.py:647](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L647)
- function **Context.lookup\_default** — [src/click/core.py:653](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L653)
- function **Context.lookup\_default** — [src/click/core.py:658](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L658)
- function **Context.fail** — [src/click/core.py:678](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L678)
- function **Context.abort** — [src/click/core.py:686](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L686)
- function **Context.exit** — [src/click/core.py:690](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L690)
- function **Context.get\_usage** — [src/click/core.py:694](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L694)
- function **Context.get\_help** — [src/click/core.py:700](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L700)
- function **Context.\_make\_sub\_context** — [src/click/core.py:706](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L706)
- function **Context.invoke** — [src/click/core.py:715](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L715)
- function **Context.invoke** — [src/click/core.py:724](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L724)
- function **Context.invoke** — [src/click/core.py:732](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L732)
- function **Context.forward** — [src/click/core.py:785](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L785)
- function **Context.set\_parameter\_source** — [src/click/core.py:806](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L806)
- function **Context.get\_parameter\_source** — [src/click/core.py:815](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L815)
- class **BaseCommand** — [src/click/core.py:834](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L834)
- function **BaseCommand.\_\_init\_\_** — [src/click/core.py:867](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L867)
- function **BaseCommand.to\_info\_dict** — [src/click/core.py:884](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L884)
- 更多符号见 JSON。

### src/click/decorators.py

源码：[src/click/decorators.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py)

- function **pass\_context** — [src/click/decorators.py:27](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L27)
- function **pass\_context.new\_func** — [src/click/decorators.py:32](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L32)
- function **pass\_obj** — [src/click/decorators.py:38](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L38)
- function **pass\_obj.new\_func** — [src/click/decorators.py:44](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L44)
- function **make\_pass\_decorator** — [src/click/decorators.py:50](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L50)
- function **make\_pass\_decorator.decorator** — [src/click/decorators.py:75](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L75)
- function **make\_pass\_decorator.decorator.new\_func** — [src/click/decorators.py:76](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L76)
- function **pass\_meta\_key** — [src/click/decorators.py:99](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L99)
- function **pass\_meta\_key.decorator** — [src/click/decorators.py:114](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L114)
- function **pass\_meta\_key.decorator.new\_func** — [src/click/decorators.py:115](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L115)
- function **command** — [src/click/decorators.py:137](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L137)
- function **command** — [src/click/decorators.py:144](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L144)
- function **command** — [src/click/decorators.py:154](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L154)
- function **command** — [src/click/decorators.py:165](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L165)
- function **command** — [src/click/decorators.py:171](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L171)
- function **command.decorator** — [src/click/decorators.py:216](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L216)
- function **group** — [src/click/decorators.py:258](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L258)
- function **group** — [src/click/decorators.py:265](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L265)
- function **group** — [src/click/decorators.py:275](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L275)
- function **group** — [src/click/decorators.py:286](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L286)
- function **group** — [src/click/decorators.py:292](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L292)
- function **\_param\_memo** — [src/click/decorators.py:313](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L313)
- function **argument** — [src/click/decorators.py:323](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L323)
- function **argument.decorator** — [src/click/decorators.py:344](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L344)
- function **option** — [src/click/decorators.py:351](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L351)
- function **option.decorator** — [src/click/decorators.py:372](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L372)
- function **confirmation\_option** — [src/click/decorators.py:379](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L379)
- function **confirmation\_option.callback** — [src/click/decorators.py:388](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L388)
- function **password\_option** — [src/click/decorators.py:403](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L403)
- function **version\_option** — [src/click/decorators.py:420](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L420)
- function **version\_option.callback** — [src/click/decorators.py:484](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L484)
- function **help\_option** — [src/click/decorators.py:533](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L533)
- function **help\_option.callback** — [src/click/decorators.py:546](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py#L546)

### src/click/exceptions.py

源码：[src/click/exceptions.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py)

- function **\_join\_param\_hints** — [src/click/exceptions.py:15](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py#L15)
- class **ClickException** — [src/click/exceptions.py:24](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py#L24)
- function **ClickException.\_\_init\_\_** — [src/click/exceptions.py:30](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py#L30)
- function **ClickException.format\_message** — [src/click/exceptions.py:34](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py#L34)
- function **ClickException.\_\_str\_\_** — [src/click/exceptions.py:37](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py#L37)
- function **ClickException.show** — [src/click/exceptions.py:40](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py#L40)
- class **UsageError** — [src/click/exceptions.py:47](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py#L47)
- function **UsageError.\_\_init\_\_** — [src/click/exceptions.py:58](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py#L58)
- function **UsageError.show** — [src/click/exceptions.py:63](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py#L63)
- class **BadParameter** — [src/click/exceptions.py:86](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py#L86)
- function **BadParameter.\_\_init\_\_** — [src/click/exceptions.py:104](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py#L104)
- function **BadParameter.format\_message** — [src/click/exceptions.py:115](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py#L115)
- class **MissingParameter** — [src/click/exceptions.py:128](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py#L128)
- function **MissingParameter.\_\_init\_\_** — [src/click/exceptions.py:140](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py#L140)
- function **MissingParameter.format\_message** — [src/click/exceptions.py:151](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py#L151)
- function **MissingParameter.\_\_str\_\_** — [src/click/exceptions.py:189](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py#L189)
- class **NoSuchOption** — [src/click/exceptions.py:197](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py#L197)
- function **NoSuchOption.\_\_init\_\_** — [src/click/exceptions.py:204](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py#L204)
- function **NoSuchOption.format\_message** — [src/click/exceptions.py:218](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py#L218)
- class **BadOptionUsage** — [src/click/exceptions.py:231](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py#L231)
- function **BadOptionUsage.\_\_init\_\_** — [src/click/exceptions.py:241](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py#L241)
- class **BadArgumentUsage** — [src/click/exceptions.py:248](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py#L248)
- class **FileError** — [src/click/exceptions.py:257](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py#L257)
- function **FileError.\_\_init\_\_** — [src/click/exceptions.py:260](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py#L260)
- function **FileError.format\_message** — [src/click/exceptions.py:268](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py#L268)
- class **Abort** — [src/click/exceptions.py:274](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py#L274)
- class **Exit** — [src/click/exceptions.py:278](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py#L278)
- function **Exit.\_\_init\_\_** — [src/click/exceptions.py:287](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py#L287)

### src/click/formatting.py

源码：[src/click/formatting.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/formatting.py)

- function **measure\_table** — [src/click/formatting.py:12](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/formatting.py#L12)
- function **iter\_rows** — [src/click/formatting.py:22](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/formatting.py#L22)
- function **wrap\_text** — [src/click/formatting.py:29](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/formatting.py#L29)
- function **wrap\_text.\_flush\_par** — [src/click/formatting.py:70](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/formatting.py#L70)
- class **HelpFormatter** — [src/click/formatting.py:102](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/formatting.py#L102)
- function **HelpFormatter.\_\_init\_\_** — [src/click/formatting.py:114](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/formatting.py#L114)
- function **HelpFormatter.write** — [src/click/formatting.py:133](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/formatting.py#L133)
- function **HelpFormatter.indent** — [src/click/formatting.py:137](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/formatting.py#L137)
- function **HelpFormatter.dedent** — [src/click/formatting.py:141](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/formatting.py#L141)
- function **HelpFormatter.write\_usage** — [src/click/formatting.py:145](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/formatting.py#L145)
- function **HelpFormatter.write\_heading** — [src/click/formatting.py:185](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/formatting.py#L185)
- function **HelpFormatter.write\_paragraph** — [src/click/formatting.py:189](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/formatting.py#L189)
- function **HelpFormatter.write\_text** — [src/click/formatting.py:194](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/formatting.py#L194)
- function **HelpFormatter.write\_dl** — [src/click/formatting.py:210](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/formatting.py#L210)
- function **HelpFormatter.section** — [src/click/formatting.py:255](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/formatting.py#L255)
- function **HelpFormatter.indentation** — [src/click/formatting.py:270](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/formatting.py#L270)
- function **HelpFormatter.getvalue** — [src/click/formatting.py:278](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/formatting.py#L278)
- function **join\_options** — [src/click/formatting.py:283](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/formatting.py#L283)

### src/click/globals.py

源码：[src/click/globals.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/globals.py)

- function **get\_current\_context** — [src/click/globals.py:12](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/globals.py#L12)
- function **get\_current\_context** — [src/click/globals.py:17](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/globals.py#L17)
- function **get\_current\_context** — [src/click/globals.py:21](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/globals.py#L21)
- function **push\_context** — [src/click/globals.py:45](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/globals.py#L45)
- function **pop\_context** — [src/click/globals.py:50](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/globals.py#L50)
- function **resolve\_color\_default** — [src/click/globals.py:55](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/globals.py#L55)

### src/click/parser.py

源码：[src/click/parser.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py)

- function **\_unpack\_args** — [src/click/parser.py:49](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py#L49)
- function **\_unpack\_args.\_fetch** — [src/click/parser.py:66](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py#L66)
- function **split\_opt** — [src/click/parser.py:109](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py#L109)
- function **normalize\_opt** — [src/click/parser.py:118](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py#L118)
- function **split\_arg\_string** — [src/click/parser.py:125](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py#L125)
- class **Option** — [src/click/parser.py:159](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py#L159)
- function **Option.\_\_init\_\_** — [src/click/parser.py:160](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py#L160)
- function **Option.takes\_value** — [src/click/parser.py:194](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py#L194)
- function **Option.process** — [src/click/parser.py:197](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py#L197)
- class **Argument** — [src/click/parser.py:213](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py#L213)
- function **Argument.\_\_init\_\_** — [src/click/parser.py:214](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py#L214)
- function **Argument.process** — [src/click/parser.py:219](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py#L219)
- class **ParsingState** — [src/click/parser.py:245](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py#L245)
- function **ParsingState.\_\_init\_\_** — [src/click/parser.py:246](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py#L246)
- class **OptionParser** — [src/click/parser.py:253](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py#L253)
- function **OptionParser.\_\_init\_\_** — [src/click/parser.py:267](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py#L267)
- function **OptionParser.add\_option** — [src/click/parser.py:291](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py#L291)
- function **OptionParser.add\_argument** — [src/click/parser.py:316](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py#L316)
- function **OptionParser.parse\_args** — [src/click/parser.py:326](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py#L326)
- function **OptionParser.\_process\_args\_for\_args** — [src/click/parser.py:344](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py#L344)
- function **OptionParser.\_process\_args\_for\_options** — [src/click/parser.py:355](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py#L355)
- function **OptionParser.\_match\_long\_opt** — [src/click/parser.py:391](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py#L391)
- function **OptionParser.\_match\_short\_opt** — [src/click/parser.py:421](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py#L421)
- function **OptionParser.\_get\_value\_from\_state** — [src/click/parser.py:461](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py#L461)
- function **OptionParser.\_process\_opts** — [src/click/parser.py:499](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py#L499)

### src/click/shell\_completion.py

源码：[src/click/shell\_completion.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py)

- function **shell\_complete** — [src/click/shell\_completion.py:17](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L17)
- class **CompletionItem** — [src/click/shell\_completion.py:55](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L55)
- function **CompletionItem.\_\_init\_\_** — [src/click/shell\_completion.py:76](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L76)
- function **CompletionItem.\_\_getattr\_\_** — [src/click/shell\_completion.py:88](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L88)
- class **ShellComplete** — [src/click/shell\_completion.py:192](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L192)
- function **ShellComplete.\_\_init\_\_** — [src/click/shell\_completion.py:216](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L216)
- function **ShellComplete.func\_name** — [src/click/shell\_completion.py:229](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L229)
- function **ShellComplete.source\_vars** — [src/click/shell\_completion.py:236](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L236)
- function **ShellComplete.source** — [src/click/shell\_completion.py:248](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L248)
- function **ShellComplete.get\_completion\_args** — [src/click/shell\_completion.py:256](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L256)
- function **ShellComplete.get\_completions** — [src/click/shell\_completion.py:263](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L263)
- function **ShellComplete.format\_completion** — [src/click/shell\_completion.py:277](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L277)
- function **ShellComplete.complete** — [src/click/shell\_completion.py:285](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L285)
- class **BashComplete** — [src/click/shell\_completion.py:298](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L298)
- function **BashComplete.\_check\_version** — [src/click/shell\_completion.py:305](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L305)
- function **BashComplete.source** — [src/click/shell\_completion.py:330](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L330)
- function **BashComplete.get\_completion\_args** — [src/click/shell\_completion.py:334](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L334)
- function **BashComplete.format\_completion** — [src/click/shell\_completion.py:346](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L346)
- class **ZshComplete** — [src/click/shell\_completion.py:350](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L350)
- function **ZshComplete.get\_completion\_args** — [src/click/shell\_completion.py:356](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L356)
- function **ZshComplete.format\_completion** — [src/click/shell\_completion.py:368](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L368)
- class **FishComplete** — [src/click/shell\_completion.py:372](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L372)
- function **FishComplete.get\_completion\_args** — [src/click/shell\_completion.py:378](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L378)
- function **FishComplete.format\_completion** — [src/click/shell\_completion.py:390](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L390)
- function **add\_completion\_class** — [src/click/shell\_completion.py:407](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L407)
- function **get\_completion\_class** — [src/click/shell\_completion.py:427](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L427)
- function **\_is\_incomplete\_argument** — [src/click/shell\_completion.py:437](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L437)
- function **\_start\_of\_option** — [src/click/shell\_completion.py:462](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L462)
- function **\_is\_incomplete\_option** — [src/click/shell\_completion.py:471](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L471)
- function **\_resolve\_context** — [src/click/shell\_completion.py:495](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L495)
- function **\_resolve\_incomplete** — [src/click/shell\_completion.py:552](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py#L552)

## 模块导入关系

依据静态 import 语句匹配常见根目录 / src 布局；不是运行时调用图。条件导入、类型检查导入也会计入；动态导入和自定义搜索路径不解析。

| 来源 | 导入目标 |
| --- | --- |
| [src/click/\_\_init\_\_.py:7](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L7) | [src/click/core.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py) |
| [src/click/\_\_init\_\_.py:8](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L8) | [src/click/core.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py) |
| [src/click/\_\_init\_\_.py:9](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L9) | [src/click/core.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py) |
| [src/click/\_\_init\_\_.py:10](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L10) | [src/click/core.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py) |
| [src/click/\_\_init\_\_.py:11](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L11) | [src/click/core.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py) |
| [src/click/\_\_init\_\_.py:12](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L12) | [src/click/core.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py) |
| [src/click/\_\_init\_\_.py:13](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L13) | [src/click/core.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py) |
| [src/click/\_\_init\_\_.py:14](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L14) | [src/click/core.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py) |
| [src/click/\_\_init\_\_.py:15](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L15) | [src/click/core.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py) |
| [src/click/\_\_init\_\_.py:16](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L16) | [src/click/decorators.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py) |
| [src/click/\_\_init\_\_.py:17](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L17) | [src/click/decorators.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py) |
| [src/click/\_\_init\_\_.py:18](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L18) | [src/click/decorators.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py) |
| [src/click/\_\_init\_\_.py:19](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L19) | [src/click/decorators.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py) |
| [src/click/\_\_init\_\_.py:20](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L20) | [src/click/decorators.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py) |
| [src/click/\_\_init\_\_.py:21](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L21) | [src/click/decorators.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py) |
| [src/click/\_\_init\_\_.py:22](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L22) | [src/click/decorators.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py) |
| [src/click/\_\_init\_\_.py:23](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L23) | [src/click/decorators.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py) |
| [src/click/\_\_init\_\_.py:24](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L24) | [src/click/decorators.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py) |
| [src/click/\_\_init\_\_.py:25](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L25) | [src/click/decorators.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py) |
| [src/click/\_\_init\_\_.py:26](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L26) | [src/click/decorators.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py) |
| [src/click/\_\_init\_\_.py:27](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L27) | [src/click/exceptions.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py) |
| [src/click/\_\_init\_\_.py:28](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L28) | [src/click/exceptions.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py) |
| [src/click/\_\_init\_\_.py:29](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L29) | [src/click/exceptions.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py) |
| [src/click/\_\_init\_\_.py:30](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L30) | [src/click/exceptions.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py) |
| [src/click/\_\_init\_\_.py:31](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L31) | [src/click/exceptions.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py) |
| [src/click/\_\_init\_\_.py:32](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L32) | [src/click/exceptions.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py) |
| [src/click/\_\_init\_\_.py:33](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L33) | [src/click/exceptions.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py) |
| [src/click/\_\_init\_\_.py:34](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L34) | [src/click/exceptions.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py) |
| [src/click/\_\_init\_\_.py:35](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L35) | [src/click/exceptions.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py) |
| [src/click/\_\_init\_\_.py:36](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L36) | [src/click/formatting.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/formatting.py) |
| [src/click/\_\_init\_\_.py:37](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L37) | [src/click/formatting.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/formatting.py) |
| [src/click/\_\_init\_\_.py:38](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L38) | [src/click/globals.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/globals.py) |
| [src/click/\_\_init\_\_.py:39](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L39) | [src/click/parser.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py) |
| [src/click/\_\_init\_\_.py:40](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L40) | [src/click/termui.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/termui.py) |
| [src/click/\_\_init\_\_.py:41](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L41) | [src/click/termui.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/termui.py) |
| [src/click/\_\_init\_\_.py:42](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L42) | [src/click/termui.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/termui.py) |
| [src/click/\_\_init\_\_.py:43](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L43) | [src/click/termui.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/termui.py) |
| [src/click/\_\_init\_\_.py:44](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L44) | [src/click/termui.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/termui.py) |
| [src/click/\_\_init\_\_.py:45](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L45) | [src/click/termui.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/termui.py) |
| [src/click/\_\_init\_\_.py:46](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L46) | [src/click/termui.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/termui.py) |
| [src/click/\_\_init\_\_.py:47](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L47) | [src/click/termui.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/termui.py) |
| [src/click/\_\_init\_\_.py:48](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L48) | [src/click/termui.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/termui.py) |
| [src/click/\_\_init\_\_.py:49](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L49) | [src/click/termui.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/termui.py) |
| [src/click/\_\_init\_\_.py:50](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L50) | [src/click/termui.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/termui.py) |
| [src/click/\_\_init\_\_.py:51](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L51) | [src/click/termui.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/termui.py) |
| [src/click/\_\_init\_\_.py:52](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L52) | [src/click/types.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/types.py) |
| [src/click/\_\_init\_\_.py:53](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L53) | [src/click/types.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/types.py) |
| [src/click/\_\_init\_\_.py:54](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L54) | [src/click/types.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/types.py) |
| [src/click/\_\_init\_\_.py:55](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L55) | [src/click/types.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/types.py) |
| [src/click/\_\_init\_\_.py:56](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L56) | [src/click/types.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/types.py) |
| [src/click/\_\_init\_\_.py:57](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L57) | [src/click/types.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/types.py) |
| [src/click/\_\_init\_\_.py:58](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L58) | [src/click/types.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/types.py) |
| [src/click/\_\_init\_\_.py:59](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L59) | [src/click/types.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/types.py) |
| [src/click/\_\_init\_\_.py:60](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L60) | [src/click/types.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/types.py) |
| [src/click/\_\_init\_\_.py:61](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L61) | [src/click/types.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/types.py) |
| [src/click/\_\_init\_\_.py:62](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L62) | [src/click/types.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/types.py) |
| [src/click/\_\_init\_\_.py:63](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L63) | [src/click/types.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/types.py) |
| [src/click/\_\_init\_\_.py:64](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L64) | [src/click/types.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/types.py) |
| [src/click/\_\_init\_\_.py:65](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L65) | [src/click/types.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/types.py) |
| [src/click/\_\_init\_\_.py:66](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L66) | [src/click/utils.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/utils.py) |
| [src/click/\_\_init\_\_.py:67](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L67) | [src/click/utils.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/utils.py) |
| [src/click/\_\_init\_\_.py:68](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L68) | [src/click/utils.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/utils.py) |
| [src/click/\_\_init\_\_.py:69](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L69) | [src/click/utils.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/utils.py) |
| [src/click/\_\_init\_\_.py:70](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L70) | [src/click/utils.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/utils.py) |
| [src/click/\_\_init\_\_.py:71](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py#L71) | [src/click/utils.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/utils.py) |
| [src/click/\_compat.py:510](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py#L510) | [src/click/\_winconsole.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py) |
| [src/click/\_termui\_impl.py:16](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L16) | [src/click/\_compat.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py) |
| [src/click/\_termui\_impl.py:17](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L17) | [src/click/\_compat.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py) |
| [src/click/\_termui\_impl.py:18](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L18) | [src/click/\_compat.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py) |
| [src/click/\_termui\_impl.py:19](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L19) | [src/click/\_compat.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py) |
| [src/click/\_termui\_impl.py:20](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L20) | [src/click/\_compat.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py) |
| [src/click/\_termui\_impl.py:21](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L21) | [src/click/\_compat.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py) |
| [src/click/\_termui\_impl.py:22](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L22) | [src/click/\_compat.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py) |
| [src/click/\_termui\_impl.py:23](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L23) | [src/click/\_compat.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py) |
| [src/click/\_termui\_impl.py:24](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L24) | [src/click/exceptions.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py) |
| [src/click/\_termui\_impl.py:25](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_termui_impl.py#L25) | [src/click/utils.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/utils.py) |
| [src/click/\_winconsole.py:28](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_winconsole.py#L28) | [src/click/\_compat.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/_compat.py) |
| [src/click/core.py:16](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L16) | [src/click/\_\_init\_\_.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/__init__.py) |
| [src/click/core.py:1872](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L1872) | [src/click/decorators.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py) |
| [src/click/core.py:1923](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L1923) | [src/click/decorators.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/decorators.py) |
| [src/click/core.py:17](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L17) | [src/click/exceptions.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py) |
| [src/click/core.py:18](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L18) | [src/click/exceptions.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py) |
| [src/click/core.py:19](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L19) | [src/click/exceptions.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py) |
| [src/click/core.py:20](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L20) | [src/click/exceptions.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py) |
| [src/click/core.py:21](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L21) | [src/click/exceptions.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py) |
| [src/click/core.py:22](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L22) | [src/click/exceptions.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/exceptions.py) |
| [src/click/core.py:23](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L23) | [src/click/formatting.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/formatting.py) |
| [src/click/core.py:24](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L24) | [src/click/formatting.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/formatting.py) |
| [src/click/core.py:25](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L25) | [src/click/globals.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/globals.py) |
| [src/click/core.py:26](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L26) | [src/click/globals.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/globals.py) |
| [src/click/core.py:27](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L27) | [src/click/parser.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py) |
| [src/click/core.py:28](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L28) | [src/click/parser.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py) |
| [src/click/core.py:29](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L29) | [src/click/parser.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/parser.py) |
| [src/click/core.py:42](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L42) | [src/click/shell\_completion.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py) |
| [src/click/core.py:972](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L972) | [src/click/shell\_completion.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py) |
| [src/click/core.py:1150](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L1150) | [src/click/shell\_completion.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py) |
| [src/click/core.py:1445](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L1445) | [src/click/shell\_completion.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py) |
| [src/click/core.py:1771](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L1771) | [src/click/shell\_completion.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py) |
| [src/click/core.py:2440](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L2440) | [src/click/shell\_completion.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/shell_completion.py) |
| [src/click/core.py:30](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/core.py#L30) | [src/click/termui.py](https://github.com/pallets/click/blob/874ca2bc1c30d93a4ac6e36a15ed685eafe89097/src/click/termui.py) |

调用表达式及其行号保存在 JSON 的 modules[].calls；未做动态绑定或调用目标解析。

## 建议阅读顺序

1. 阅读 README，明确项目用途和运行前提。
2. 阅读依赖清单和已识别的入口声明。
3. 从入口所在模块沿导入关系阅读实现，再结合测试核对行为。
4. 亲自运行可信项目的测试；本报告没有执行目标仓库代码。

## 限制与告警

- 第一版深入解析 Python；其他语言主要提供文件统计、配置和工程结构线索。
- 根 .gitignore 仅在本地模式生效；嵌套 .gitignore 不解析。
- 固定排除依赖、构建产物、符号链接、子模块和常见密钥文件；不构成全面敏感信息扫描。
- Markdown 为阅读摘要，部分列表有展示上限；完整已提取结果和预算见 JSON。
- 验证方式：连接器获取的真实 GitHub 数据（15 个文件全部校验 blob SHA），通过 HTTP 模拟传输回放；不是直接联网 CLI 成功记录。
- 内容读取达到 15 个文件上限；剩余候选未读取。
- setup.py：仅分析 Python 符号；setup.py 中的依赖声明未提取。
- src/click/core.py：调用表达式最多展示前 200 个。

---
Generated by RepoLens 0.1.0
