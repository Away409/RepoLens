"""Chinese Markdown reports with source links and bounded presentation."""

import html
import re
from urllib.parse import quote

from . import __version__
from .models import Report


def clean(value: object) -> str:
    text = re.sub(r"[\x00-\x1f\x7f]", " ", str(value))
    text = html.escape(text, quote=False)
    for char in ("\\", "`", "*", "_", "[", "]", "|", "#"):
        text = text.replace(char, "\\" + char)
    return text


def source(report: Report, path: str, line: int | None = None) -> str:
    label = clean(path + (f":{line}" if line else ""))
    if report.url and report.revision:
        url = f"{report.url}/blob/{report.revision}/{quote(path, safe='/')}"
        if line:
            url += f"#L{line}"
        return f"[{label}]({url})"
    return label


def mermaid(report: Report) -> list[str]:
    max_nodes, max_edges = 40, 80
    pairs = sorted({(edge.source, edge.target) for edge in report.import_edges})
    nodes: dict[str, str] = {}
    edges: list[str] = []
    for source_path, target_path in pairs:
        new_nodes = dict.fromkeys(p for p in (source_path, target_path) if p not in nodes)
        if len(nodes) + len(new_nodes) > max_nodes:
            continue
        for path in new_nodes:
            nodes[path] = f"m{len(nodes)}"
        edges.append(f"  {nodes[source_path]} --> {nodes[target_path]}")
        if len(edges) >= max_edges:
            break
    if not edges:
        return []

    labels = []
    for path, node in nodes.items():
        short = path if len(path) <= 160 else path[:159] + "…"
        short = re.sub(r"[\x00-\x1f\x7f-\x9f\u2028\u2029]", " ", short)
        label = re.sub(r"""["'#&<>\[\]\x60\\%]""", lambda m: f"#{ord(m[0])};", short)
        labels.append(f'  {node}["{label}"]')
    out = ["", "```mermaid", "flowchart LR", *labels, *edges, "```"]
    if len(edges) < len(pairs):
        out += ["", f"图中展示 {len(edges)} / {len(pairs)} 对模块关系；全部导入边见 JSON。"]
    return out


def markdown(report: Report) -> str:
    description = (
        clean(report.description) if report.description else "未提供；请结合 README 判断用途。"
    )
    out = [
        f"# RepoLens · {clean(report.name)}",
        "",
        "> 根据文件清单、配置、Python AST 和 C++ 语法树生成的静态分析报告。",
        "",
        "## 项目概览",
        "",
        f"- 来源：{report.source}",
        f"- 描述：{description}",
        f"- 提交：{report.revision or '本地工作目录（无提交固定）'}",
        f"- 生成时间（UTC）：{report.generated_at}",
        f"- 许可证元数据：{clean(report.license or '未提供；请阅读 LICENSE 原文')}",
        "",
        "## 分析范围",
        "",
        "| 指标 | 结果 |",
        "| --- | --- |",
        f"| 纳入清单的文件 | {report.file_count} |",
        f"| 内容候选（Python / C++ / 支持的配置 / README） | {report.eligible_files} |",
        f"| 实际读取文本 | {len(report.analyzed_files)} |",
        f"| 读取字节 | {report.bytes_read} |",
        f"| API 请求次数（含重试） | {report.requests} |",
        f"| 清单状态 | {'完整（应用排除规则后）' if report.inventory_complete else '不完整'} |",
    ]
    if report.content_complete is not None:
        status = "全部候选文本已读取" if report.content_complete else "部分候选文本未读取"
        out.append(f"| 内容状态 | {status} |")
    if report.remote_reads is not None:
        stats = report.remote_reads
        cache = "已启用" if stats.cache_enabled else "未启用"
        out += [
            f"| 远端磁盘缓存 | {cache} |",
            f"| Blob 缓存命中 / 未命中 | {stats.blob_cache_hits} / {stats.blob_cache_misses} |",
            f"| 已校验的网络 Blob 读取 | {stats.blob_network_reads} |",
            f"| 条件请求返回 304 | {stats.not_modified} |",
            f"| 请求预算耗尽 | {'是' if stats.request_budget_exhausted else '否'} |",
            f"| GitHub API 限流 | {'是' if stats.rate_limited else '否'} |",
        ]
    out += [
        "",
        "语言统计按清单中的扩展名计文件数，不代表代码行数或 GitHub Linguist 结果。",
        "",
        "## 技术栈线索",
        "",
        "| 语言 | 文件数 |",
        "| --- | ---: |",
    ]
    out.extend(f"| {clean(k)} | {v} |" for k, v in report.languages.items())
    if not report.languages:
        out.append("| 未识别 | 0 |")
    if report.readme_excerpt:
        excerpt = report.readme_excerpt
        out += [
            "",
            "## README 开头摘录",
            "",
            f"来源：{source(report, excerpt.path, excerpt.line)}"
            "（最多 16 行 / 1200 字符；非自动总结）",
            "",
        ]
        out.extend(f"> {clean(line)}".rstrip() for line in excerpt.detail.splitlines())
    out += ["", "## 工程结构检查", "", "检测到文件只说明它存在；不会声称测试通过或配置有效。", ""]
    for key, paths in report.signals.items():
        if paths:
            detail = "、".join(source(report, p) for p in paths[:5])
            if len(paths) > 5:
                detail += f" 等 {len(paths)} 个"
        else:
            detail = "在已扫描范围内未发现"
        out.append(f"- **{key}**：{detail}")
    out += ["", "## 文件目录（最多 120 项）", ""]
    out.extend(f"- {source(report, p)}" for p in report.files[:120])
    if len(report.files) > 120:
        out.append(f"- …另有 {len(report.files) - 120} 项；完整清单见 JSON。")
    out += [
        "",
        "## 声明依赖",
        "",
        "仅解析已读取的清单，不解析传递依赖或锁文件，不验证版本能否安装。",
        "",
        "| 名称 | 声明 | 分组 | 来源 |",
        "| --- | --- | --- | --- |",
    ]
    for dep in report.dependencies[:150]:
        out.append(
            f"| {clean(dep.name)} | {clean(dep.specification)} | {clean(dep.group)} | "
            f"{source(report, dep.path)} |"
        )
    if not report.dependencies:
        out.append("| 未提取到 | — | — | — |")
    if len(report.dependencies) > 150:
        out.append("\n更多声明见 JSON。")
    out += ["", "## 入口证据", ""]
    for item in report.entry_points[:80]:
        out.append(f"- {source(report, item.path, item.line)}：{clean(item.detail)}")
    if not report.entry_points:
        out.append("未发现可识别的入口声明；库项目也可能没有独立可执行入口。")
    out += ["", "## Python 模块与符号", "", "方法与嵌套函数使用限定名称。", ""]
    for module in report.modules:
        out += [f"### {clean(module.path)}", "", f"源码：{source(report, module.path)}", ""]
        for symbol in module.symbols[:40]:
            out.append(
                f"- {clean(symbol.kind)} **{clean(symbol.name)}** — "
                f"{source(report, module.path, symbol.line)}"
            )
        if len(module.symbols) > 40:
            out.append("- 更多符号见 JSON。")
        if not module.symbols:
            out.append("- 未定义类或函数。")
        out.append("")
    if not report.modules:
        out.append("本次未成功解析 Python 模块。\n")
    if report.cpp_files:
        out += [
            "## C++ 源文件与头文件",
            "",
            "头文件路径按清单推断。条件分支中的指令也会计入，宏和编译器搜索路径未展开。",
            "",
        ]
        for cpp in report.cpp_files[:40]:
            out += [f"### {clean(cpp.path)}", "", f"源码：{source(report, cpp.path)}", ""]
            for symbol in cpp.symbols[:20]:
                out.append(
                    f"- {clean(symbol.kind)} **{clean(symbol.name)}** — "
                    f"{source(report, cpp.path, symbol.line)}"
                )
            for include in cpp.includes[:20]:
                name = {
                    "quoted": f'"{include.name}"',
                    "angled": f"<{include.name}>",
                    "macro": include.name,
                }[include.kind]
                target = f" → {source(report, include.target)}" if include.target else ""
                out.append(
                    f"- `#include` {clean(name)} — {source(report, cpp.path, include.line)}{target}"
                )
            if not cpp.symbols and not cpp.includes:
                out.append("- 未识别到支持的定义或头文件引用。")
            if len(cpp.symbols) > 20 or len(cpp.includes) > 20:
                out.append("- 更多符号和头文件引用见 JSON。")
            out.append("")
        if len(report.cpp_files) > 40:
            out += ["更多 C++ 文件见 JSON。", ""]
    out += [
        "## 模块导入关系",
        "",
        "依据静态 import 语句匹配常见根目录 / src 布局；"
        "不是运行时调用图。条件导入、类型检查导入也会计入；动态导入和自定义搜索路径不解析。",
        "",
        "| 来源 | 导入目标 |",
        "| --- | --- |",
    ]
    for edge in report.import_edges[:100]:
        out.append(f"| {source(report, edge.source, edge.line)} | {source(report, edge.target)} |")
    if not report.import_edges:
        out.append("| 未解析到仓库内模块连接 | — |")
    out.extend(mermaid(report))
    out += [
        "",
        "调用表达式及其行号保存在 JSON 的 modules[].calls；未做动态绑定或调用目标解析。",
        "",
        "## 建议阅读顺序",
        "",
        "1. 阅读 README，明确项目用途和运行前提。",
        "2. 阅读依赖清单和已识别的入口声明。",
        "3. 从入口所在文件沿模块导入或头文件引用阅读实现，再结合测试核对行为。",
        "4. 亲自运行可信项目的测试；本报告没有执行目标仓库代码。",
        "",
        "## 限制与告警",
        "",
        "- Python 和 C++ 支持语法分析；其他语言提供文件统计、配置和工程结构线索。",
        "- 根 .gitignore 仅在本地模式生效；嵌套 .gitignore 不解析。",
        "- 固定排除依赖、构建产物、符号链接、子模块和常见密钥文件；不构成全面敏感信息扫描。",
        "- Markdown 为阅读摘要，部分列表有展示上限；完整已提取结果和预算见 JSON。",
    ]
    out.extend(f"- {clean(warning)}" for warning in report.warnings)
    out += ["", "---", f"Generated by RepoLens {__version__}", ""]
    return "\n".join(out)
