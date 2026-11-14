"""Read bounded snapshots. Never clone, install or execute target repository code."""

import base64
import binascii
import io
import json
import logging
import os
import re
import stat
import time
import tokenize
from pathlib import Path, PurePosixPath
from urllib.parse import quote, urlsplit

import httpx
import pathspec

from .models import FileEntry, Limits, Snapshot

log = logging.getLogger(__name__)
IGNORED = {
    ".git",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    "dist",
    "build",
    ".mypy_cache",
    ".tox",
    ".next",
    "vendor",
}
MANIFESTS = {"pyproject.toml", "package.json", "setup.cfg", "cmakelists.txt"}


class RepoLensError(Exception):
    """Actionable error safe to display (never contains HTTP headers or tokens)."""


def parse_repository(value: str) -> tuple[str, str]:
    """Accept HTTPS github.com root URLs or owner/repo, never arbitrary hosts."""
    if "://" in value:
        url = urlsplit(value)
        if url.scheme != "https" or url.netloc.lower() != "github.com" or url.query or url.fragment:
            raise RepoLensError("请输入 https://github.com/owner/repo；分支请通过 --ref 指定。")
        value = url.path.strip("/")
    value = value.removesuffix(".git")
    parts = value.split("/")
    if (
        len(parts) != 2
        or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9-]{0,38}", parts[0])
        or not re.fullmatch(r"[A-Za-z0-9_.-]{1,100}", parts[1])
        or parts[1] in {".", ".."}
    ):
        raise RepoLensError("仓库格式应为 owner/repo 或 GitHub 仓库首页 URL。")
    return parts[0], parts[1]


def safe_path(value: str) -> bool:
    path = PurePosixPath(value)
    return (
        bool(value)
        and not path.is_absolute()
        and not any(part in {".", ".."} for part in value.split("/"))
        and not any(ord(c) < 32 or c == "\\" for c in value)
    )


def excluded(path: str) -> bool:
    parts = PurePosixPath(path).parts
    name = parts[-1].lower()
    return (
        any(p in IGNORED or p.endswith(".egg-info") for p in parts)
        or name == ".env"
        or name.startswith(".env.")
        or name.endswith((".pem", ".key", ".p12", ".pfx"))
    )


def candidate(path: str) -> bool:
    name = PurePosixPath(path).name.lower()
    return (
        name in MANIFESTS
        or (name.startswith("requirements") and name.endswith(".txt"))
        or path.endswith(".py")
        or name.startswith("readme")
    )


def priority(entry: FileEntry) -> tuple[int, int, str]:
    name = PurePosixPath(entry.path).name.lower()
    is_example = any(
        p in {"tests", "test", "examples", "docs"} for p in PurePosixPath(entry.path).parts
    )
    if is_example:
        rank = 4
    elif name in MANIFESTS or (name.startswith("requirements") and name.endswith(".txt")):
        rank = 0
    elif name.startswith("readme") and "/" not in entry.path:
        rank = 1
    elif name in {"__main__.py", "cli.py", "main.py", "app.py"}:
        rank = 2
    elif name.startswith("readme"):
        rank = 4
    else:
        rank = 3
    return rank, entry.path.count("/"), entry.path


def decode_text(data: bytes, path: str) -> str:
    if b"\x00" in data:
        raise ValueError("binary file")
    if path.endswith(".py"):
        encoding, _ = tokenize.detect_encoding(io.BytesIO(data).readline)
        return data.decode(encoding)
    return data.decode("utf-8-sig")


def load_contents(snapshot: Snapshot, limits: Limits, reader) -> None:
    candidates = sorted((e for e in snapshot.entries if candidate(e.path)), key=priority)
    snapshot.eligible_files = len(candidates)
    attempted = 0
    for entry in candidates:
        if attempted >= limits.max_files:
            snapshot.warnings.append(
                f"内容读取达到 {limits.max_files} 个文件上限；剩余候选未读取。"
            )
            break
        if entry.size > limits.max_file_bytes:
            snapshot.warnings.append(f"跳过过大文件：{entry.path}")
            continue
        if snapshot.bytes_read + entry.size > limits.max_total_bytes:
            snapshot.warnings.append("达到总读取字节预算；其余文件未读取。")
            break
        attempted += 1
        try:
            data = reader(entry)
            snapshot.bytes_read += len(data)
            if len(data) > limits.max_file_bytes or snapshot.bytes_read > limits.max_total_bytes:
                snapshot.warnings.append(f"文件实际大小超过预算：{entry.path}")
                break
            snapshot.contents[entry.path] = decode_text(data, entry.path)
        except (UnicodeError, ValueError, SyntaxError):
            snapshot.warnings.append(f"无法解码文本：{entry.path}")
        except OSError:
            snapshot.warnings.append(f"文件读取失败或已变化：{entry.path}")
        except RepoLensError as error:
            snapshot.warnings.append(f"内容获取已停止：{error}")
            break


def local_snapshot(root: Path, limits: Limits) -> Snapshot:
    root = root.expanduser().resolve()
    if not root.is_dir():
        raise RepoLensError("本地路径不存在或不是目录。")
    snapshot = Snapshot(name=root.name, source="local")
    snapshot.warnings.append("本地模式读取当前工作目录内容（含未提交文件），不是 Git 提交快照。")
    # Only the root ignore file is loaded; no subprocess or git hooks are invoked.
    spec = pathspec.GitIgnoreSpec.from_lines([])
    ignore = root / ".gitignore"
    if ignore.is_file() and not ignore.is_symlink():
        try:
            with ignore.open("rb") as handle:
                raw = handle.read(limits.max_file_bytes + 1)
            if len(raw) <= limits.max_file_bytes:
                spec = pathspec.GitIgnoreSpec.from_lines(raw.decode("utf-8-sig").splitlines())
            else:
                snapshot.warnings.append("根 .gitignore 过大，未读取。")
        except (OSError, UnicodeError, ValueError):
            snapshot.warnings.append("无法读取根 .gitignore，使用默认排除规则。")
    seen = 0

    def walk_error(_error):
        snapshot.inventory_complete = False
        snapshot.warnings.append("部分目录无法访问，文件清单不完整。")

    for directory, dirs, files in os.walk(root, followlinks=False, onerror=walk_error):
        base = Path(directory)
        kept = []
        for name in sorted(dirs):
            item = base / name
            rel = item.relative_to(root).as_posix()
            if item.is_symlink() or item.resolve() != item.absolute():
                continue
            if not excluded(rel) and not spec.match_file(rel + "/"):
                kept.append(name)
        dirs[:] = kept
        seen += len(dirs) + len(files)
        if seen > limits.max_entries:
            snapshot.inventory_complete = False
            snapshot.warnings.append("目录扫描达到条目上限，文件清单不完整。")
            break
        for name in sorted(files):
            item = base / name
            rel = item.relative_to(root).as_posix()
            if not safe_path(rel) or excluded(rel) or spec.match_file(rel):
                continue
            try:
                info = item.lstat()
                if not stat.S_ISREG(info.st_mode):
                    continue
                snapshot.entries.append(FileEntry(path=rel, size=info.st_size))
            except OSError:
                walk_error(None)
    snapshot.entries.sort(key=lambda e: e.path)

    def read(entry):
        path = root / entry.path
        if path.resolve() != path.absolute() or not path.resolve().is_relative_to(root):
            raise OSError("symlink or escaped root")
        # O_NOFOLLOW where available also protects against a final-component symlink race.
        fd = os.open(
            path,
            os.O_RDONLY
            | getattr(os, "O_NOFOLLOW", 0)
            | getattr(os, "O_NONBLOCK", 0)
            | getattr(os, "O_BINARY", 0),
        )
        with os.fdopen(fd, "rb") as handle:
            if not stat.S_ISREG(os.fstat(handle.fileno()).st_mode):
                raise OSError("not a regular file")
            return handle.read(limits.max_file_bytes + 1)

    load_contents(snapshot, limits, read)
    return snapshot


class GitHubSource:
    def __init__(self, limits: Limits, token: str | None = None, transport=None):
        self.limits = limits
        self.requests = 0
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "RepoLens/0.1",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if token:
            headers["Authorization"] = f"Bearer {token}"
        try:
            self.client = httpx.Client(
                base_url="https://api.github.com",
                headers=headers,
                timeout=limits.timeout,
                follow_redirects=False,
                transport=transport,
            )
        except (ImportError, ValueError):
            raise RepoLensError(
                "HTTP 客户端初始化失败；检查代理配置并重新安装项目依赖（含 SOCKS 支持）。"
            ) from None

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        self.client.close()

    def get(self, path: str, max_bytes: int = 12_000_000) -> dict:
        for attempt in range(3):
            if self.requests >= self.limits.max_requests:
                raise RepoLensError("API 请求预算已用尽；增大 --max-requests 或使用本地模式。")
            self.requests += 1
            log.info("GitHub GET request %d", self.requests)
            try:
                with self.client.stream("GET", path) as response:
                    status = response.status_code
                    if status == 429 or (
                        status == 403
                        and (
                            response.headers.get("x-ratelimit-remaining") == "0"
                            or "retry-after" in response.headers
                        )
                    ):
                        raise RepoLensError("GitHub API 限流；稍后重试，或设置 GITHUB_TOKEN。")
                    if status in {502, 503, 504} and attempt < 2:
                        time.sleep(0.5 * (attempt + 1))
                        continue
                    errors = {
                        401: "GitHub Token 无效或已过期。",
                        403: "GitHub 拒绝访问（权限不足或二级限流）；检查 Token 或稍后重试。",
                        404: "仓库或分支不存在、私有仓库无权限；请检查地址、--ref 和 Token。",
                        409: "仓库为空或 Git 数据尚不可用。",
                        422: "GitHub 无法解析该引用；请检查 --ref。",
                    }
                    if 300 <= status < 400:
                        raise RepoLensError("仓库可能已迁移；请使用 GitHub 显示的最新地址。")
                    if status >= 400:
                        raise RepoLensError(errors.get(status, f"GitHub API 返回 HTTP {status}。"))
                    raw = bytearray()
                    for chunk in response.iter_bytes():
                        raw.extend(chunk)
                        if len(raw) > max_bytes:
                            raise RepoLensError("GitHub 响应超过大小上限；建议本地分析。")
                    data = json.loads(raw)
                    if not isinstance(data, dict):
                        raise ValueError("expected object")
                    return data
            except (httpx.TimeoutException, httpx.NetworkError):
                if attempt == 2:
                    raise RepoLensError(
                        "连接 GitHub 超时或失败；请检查网络或使用本地模式。"
                    ) from None
                time.sleep(0.5 * (attempt + 1))
            except httpx.HTTPError:
                raise RepoLensError("GitHub HTTP 传输失败；请检查网络连接。") from None
            except (ValueError, UnicodeError):
                raise RepoLensError("GitHub 返回了无法解析的数据。") from None
        raise RepoLensError("GitHub 请求失败。")

    def snapshot(self, target: str, ref: str | None = None) -> Snapshot:
        owner, repo = parse_repository(target)
        prefix = f"/repos/{owner}/{repo}"
        meta = self.get(prefix)
        try:
            commit = self.get(f"{prefix}/commits/{quote(ref or meta['default_branch'], safe='')}")
            sha = commit["sha"]
            tree_sha = commit["commit"]["tree"]["sha"]
            if not all(re.fullmatch(r"[a-fA-F0-9]{40,64}", s) for s in (sha, tree_sha)):
                raise ValueError("invalid sha")
            tree = self.get(f"{prefix}/git/trees/{tree_sha}?recursive=1")
            snapshot = Snapshot(
                name=f"{owner}/{repo}",
                source="github",
                url=f"https://github.com/{owner}/{repo}",
                revision=sha,
                description=meta.get("description") or "",
                license=(meta.get("license") or {}).get("spdx_id"),
            )
            entries = tree["tree"]
            if not isinstance(entries, list):
                raise ValueError("invalid tree")
            if tree.get("truncated") or len(entries) > self.limits.max_entries:
                snapshot.inventory_complete = False
                snapshot.warnings.append("远端目录树被截断或超过条目上限；不能据此判定文件不存在。")
            for entry in entries[: self.limits.max_entries]:
                path = entry["path"]
                if (
                    entry["type"] == "blob"
                    and entry.get("mode") in {"100644", "100755"}
                    and safe_path(path)
                    and not excluded(path)
                ):
                    snapshot.entries.append(
                        FileEntry(path=path, size=entry.get("size", 0), sha=entry["sha"])
                    )
            snapshot.entries.sort(key=lambda e: e.path)

            def read(entry):
                if not entry.sha or not re.fullmatch(r"[a-fA-F0-9]{40,64}", entry.sha):
                    raise RepoLensError("无效的 Git blob 标识。")
                blob = self.get(
                    f"{prefix}/git/blobs/{entry.sha}",
                    max_bytes=self.limits.max_file_bytes * 2 + 10_000,
                )
                if blob.get("encoding") != "base64" or not isinstance(blob.get("content"), str):
                    raise RepoLensError("GitHub blob 格式不受支持。")
                try:
                    return base64.b64decode("".join(blob["content"].split()), validate=True)
                except (ValueError, binascii.Error):
                    raise RepoLensError("GitHub blob 内容损坏。") from None

            load_contents(snapshot, self.limits, read)
            snapshot.requests = self.requests
            return snapshot
        except (KeyError, TypeError, ValueError):
            raise RepoLensError("GitHub 元数据格式异常，无法构建仓库快照。") from None
