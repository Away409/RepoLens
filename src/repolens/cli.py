"""Command-line interface; report writes are atomic and opt-in for overwrites."""

import logging
import os
import tempfile
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Annotated

import httpx
import typer
from pydantic import ValidationError

from . import __version__
from .analyzer import analyze
from .explain import evidence_list, generate, preview
from .models import Limits, Report
from .render import markdown
from .sources import GitHubSource, RepoLensError, local_snapshot

app = typer.Typer(
    help="RepoLens：只读分析 GitHub / 本地仓库，生成中文 Markdown 或 JSON 报告。",
    no_args_is_help=True,
    pretty_exceptions_enable=False,
)


@app.callback()
def main():
    """Repository structure, dependency and Python source inspector."""


@app.command()
def version():
    """显示版本。"""
    typer.echo(__version__)


def write_report(path: Path, content: str, force: bool) -> None:
    if path.exists() and not force:
        raise RepoLensError("输出文件已存在；换一个路径或添加 --force。")
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=".repolens-", dir=path.parent)
    temporary = Path(name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
        if force:
            os.replace(temporary, path)
        else:
            # A hard link atomically fails if another process creates the output meanwhile.
            os.link(temporary, path)
    except FileExistsError:
        raise RepoLensError("输出文件已存在；未覆盖。") from None
    finally:
        temporary.unlink(missing_ok=True)


@app.command("explain")
def explain_command(
    report_path: Annotated[Path, typer.Argument(help="analyze 导出的 JSON 报告")],
    budget_usd: Annotated[
        str | None, typer.Option(help="单次生成预算（美元）。省略时离线预览证据")
    ] = None,
    output: Annotated[Path | None, typer.Option("--output", "-o", help="输出 Markdown")] = None,
    force: Annotated[bool, typer.Option(help="允许覆盖已有输出文件")] = False,
):
    """预览证据，或按预算向 OpenAI 请求带源码行号的阅读建议。"""
    try:
        if output and output.exists():
            if output.samefile(report_path):
                raise RepoLensError("请选择与输入报告不同的输出路径。")
            if not force:
                raise RepoLensError("输出文件已存在；换一个路径或添加 --force。")
        report = Report.model_validate_json(report_path.read_bytes())
        items = evidence_list(report)
        if budget_usd is None:
            content = preview(items)
        else:
            try:
                budget = Decimal(budget_usd)
            except InvalidOperation:
                raise RepoLensError("请用十进制金额指定 --budget-usd。") from None
            if not budget.is_finite() or budget <= 0:
                raise RepoLensError("生成预算必须是大于零的有限美元金额。")
            key = os.environ.get("OPENAI_API_KEY", "").strip()
            if not key or not key.isascii() or not key.isprintable():
                raise RepoLensError("请设置有效的 OPENAI_API_KEY，或省略预算进行离线预览。")
            with httpx.Client(headers={"Authorization": "Bearer " + key}, timeout=60) as client:
                content = generate(items, budget, client)
        if output:
            write_report(output, content, force)
            typer.echo(f"已保存：{output}", err=True)
        else:
            typer.echo(content, nl=False)
    except (OSError, ValidationError, RepoLensError) as error:
        message = (
            str(error)
            if isinstance(error, RepoLensError)
            else "无法读取报告或写入文件，请检查 JSON 格式及路径权限。"
        )
        typer.echo(f"错误：{message}", err=True)
        raise typer.Exit(code=1) from None


@app.command("analyze")
def analyze_command(
    target: Annotated[str, typer.Argument(help="GitHub URL、owner/repo 或本地目录")],
    output: Annotated[
        Path | None, typer.Option("--output", "-o", help="输出文件，默认写标准输出")
    ] = None,
    format: Annotated[str, typer.Option("--format", help="markdown 或 json")] = "markdown",
    local: Annotated[bool, typer.Option("--local", help="明确将 target 视为本地目录")] = False,
    ref: Annotated[str | None, typer.Option("--ref", help="远端分支、tag 或提交 SHA")] = None,
    no_cache: Annotated[bool, typer.Option("--no-cache", help="禁用远端磁盘缓存")] = False,
    cache_dir: Annotated[
        Path | None,
        typer.Option("--cache-dir", envvar="REPOLENS_CACHE_DIR", help="远端磁盘缓存目录"),
    ] = None,
    max_files: Annotated[int, typer.Option(min=1, max=1000)] = 35,
    max_file_bytes: Annotated[int, typer.Option(min=1, max=2_000_000)] = 256_000,
    max_total_bytes: Annotated[int, typer.Option(min=1, max=100_000_000)] = 5_000_000,
    max_entries: Annotated[int, typer.Option(min=1, max=100_000)] = 20_000,
    max_requests: Annotated[int, typer.Option(min=3, max=5000)] = 50,
    timeout: Annotated[float, typer.Option(min=0.1, max=120)] = 20,
    force: Annotated[bool, typer.Option("--force", help="允许覆盖已有报告")] = False,
    verbose: Annotated[bool, typer.Option("--verbose", "-v")] = False,
):
    """提取工程结构、依赖和 Python AST；不会安装或执行目标仓库代码。"""
    if format not in {"markdown", "json"}:
        raise typer.BadParameter("--format 必须是 markdown 或 json。")
    logging.basicConfig(level=logging.WARNING, format="%(levelname)s %(message)s")
    logging.getLogger("repolens").setLevel(logging.INFO if verbose else logging.WARNING)
    try:
        is_local = local or ("://" not in target and Path(target).expanduser().is_dir())
        if is_local and ref:
            raise RepoLensError("--ref 仅适用于 GitHub 模式；本地模式分析当前工作目录。")
        if output and output.exists() and not force:
            raise RepoLensError("输出文件已存在；换一个路径或添加 --force。")
        limits = Limits(
            max_files=max_files,
            max_file_bytes=max_file_bytes,
            max_total_bytes=max_total_bytes,
            max_entries=max_entries,
            max_requests=max_requests,
            timeout=timeout,
        )
        if is_local:
            snapshot = local_snapshot(Path(target), limits)
        else:
            with GitHubSource(
                limits,
                token=os.environ.get("GITHUB_TOKEN"),
                use_cache=not no_cache,
                cache_dir=cache_dir,
            ) as client:
                snapshot = client.snapshot(target, ref)
        report = analyze(snapshot, limits)
        content = report.model_dump_json(indent=2) + "\n" if format == "json" else markdown(report)
        if output:
            write_report(output, content, force)
            typer.echo(f"报告已保存：{output}", err=True)
        else:
            typer.echo(content, nl=False)
        typer.echo(
            f"已扫描 {report.file_count} 个文件，读取 {len(report.analyzed_files)} 个文本；"
            f"告警 {len(report.warnings)} 条（详见报告）。",
            err=True,
        )
    except (RepoLensError, OSError) as error:
        message = (
            str(error)
            if isinstance(error, RepoLensError)
            else "本地文件操作失败，请检查路径和权限。"
        )
        typer.echo(f"错误：{message}", err=True)
        raise typer.Exit(code=1) from None
