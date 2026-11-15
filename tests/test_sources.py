import base64
import hashlib
from pathlib import Path

import httpx
import pytest

from repolens.models import FileEntry, Limits, Snapshot
from repolens.sources import (
    GitHubSource,
    RepoLensError,
    decode_text,
    load_contents,
    local_snapshot,
    parse_repository,
    priority,
)

SHA = "a" * 40
TREE = "b" * 40
DATA = b"print('ok')\n"
BLOB = hashlib.sha1(b"blob 12\0" + DATA, usedforsecurity=False).hexdigest()


@pytest.mark.parametrize(
    "value",
    [
        "octocat/Hello-World",
        "https://github.com/octocat/Hello-World",
        "https://github.com/octocat/Hello-World.git/",
    ],
)
def test_repository_url(value):
    assert parse_repository(value) == ("octocat", "Hello-World")


@pytest.mark.parametrize(
    "value",
    [
        "https://evil.com/a/b",
        "http://github.com/a/b",
        "a/..",
        "https://github.com/a/b/tree/main",
        "https://u@github.com/a/b",
        "https://github.com/a/b?token=secret",
        "a/b/c",
        "a/%2f",
    ],
)
def test_reject_unsafe_urls(value):
    with pytest.raises(RepoLensError):
        parse_repository(value)


def remote_handler(request):
    path = request.url.path
    assert request.url.host == "api.github.com"
    if path == "/repos/acme/demo":
        return httpx.Response(200, json={"default_branch": "main", "description": "Demo"})
    if path.startswith("/repos/acme/demo/commits/"):
        return httpx.Response(200, json={"sha": SHA, "commit": {"tree": {"sha": TREE}}})
    if path.endswith(f"/git/trees/{TREE}"):
        return httpx.Response(
            200,
            json={
                "truncated": False,
                "tree": [
                    {"path": "main.py", "type": "blob", "mode": "100644", "size": 12, "sha": BLOB},
                    {"path": "secret.py", "type": "blob", "mode": "120000", "sha": BLOB},
                    {"path": "sub", "type": "commit", "mode": "160000", "sha": BLOB},
                    {"path": "../escape.py", "type": "blob", "mode": "100644", "sha": BLOB},
                ],
            },
        )
    if path.endswith(f"/git/blobs/{BLOB}"):
        return httpx.Response(
            200, json={"encoding": "base64", "content": base64.b64encode(DATA).decode()}
        )
    raise AssertionError(path)


def test_remote_snapshot_is_commit_pinned_and_excludes_symlinks():
    requests = []

    def handler(request):
        requests.append(request)
        return remote_handler(request)

    with GitHubSource(Limits(), transport=httpx.MockTransport(handler), use_cache=False) as client:
        snap = client.snapshot("acme/demo", "feature/x")
    assert snap.revision == SHA
    assert snap.contents == {"main.py": "print('ok')\n"}
    assert len(snap.entries) == 1
    assert snap.requests == 4
    assert b"feature%2Fx" in requests[1].url.raw_path


@pytest.mark.parametrize(
    ("status", "headers", "message"),
    [
        (401, {}, "Token"),
        (403, {}, "拒绝"),
        (404, {}, "不存在"),
        (409, {}, "为空"),
        (422, {}, "引用"),
        (429, {}, "限流"),
        (403, {"x-ratelimit-remaining": "0"}, "限流"),
        (403, {"retry-after": "60"}, "限流"),
        (301, {"location": "https://evil.com"}, "迁移"),
    ],
)
def test_actionable_api_errors(status, headers, message):
    transport = httpx.MockTransport(lambda _: httpx.Response(status, headers=headers))
    with GitHubSource(Limits(), token="secret-token", transport=transport) as client:
        with pytest.raises(RepoLensError, match=message) as error:
            client.snapshot("acme/demo")
    assert "secret-token" not in str(error.value)


def test_retry_transient_failure(monkeypatch):
    monkeypatch.setattr("repolens.sources.time.sleep", lambda _: None)
    calls = []

    def handler(request):
        calls.append(request)
        return httpx.Response(503) if len(calls) < 3 else httpx.Response(200, json={"ok": True})

    with GitHubSource(Limits(), transport=httpx.MockTransport(handler), use_cache=False) as client:
        assert client.get("/test") == {"ok": True}
        assert client.requests == 3


def test_timeout_retries_bounded(monkeypatch):
    monkeypatch.setattr("repolens.sources.time.sleep", lambda _: None)

    def handler(request):
        raise httpx.ConnectTimeout("secret proxy details", request=request)

    with GitHubSource(Limits(), transport=httpx.MockTransport(handler), use_cache=False) as client:
        with pytest.raises(RepoLensError, match="超时") as error:
            client.get("/test")
        assert client.requests == 3
        assert "secret" not in str(error.value)


def test_request_budget_retains_partial_report():
    with GitHubSource(
        Limits(max_requests=3), transport=httpx.MockTransport(remote_handler), use_cache=False
    ) as client:
        snap = client.snapshot("acme/demo")
    assert snap.entries
    assert not snap.contents
    assert snap.requests == 3
    assert any("预算" in w for w in snap.warnings)


def test_truncated_tree_is_explicit():
    def handler(request):
        response = remote_handler(request)
        data = response.json()
        if "tree" in data:
            data["truncated"] = True
        return httpx.Response(200, json=data)

    with GitHubSource(Limits(), transport=httpx.MockTransport(handler), use_cache=False) as client:
        snap = client.snapshot("acme/demo")
    assert not snap.inventory_complete
    assert any("截断" in w for w in snap.warnings)


@pytest.mark.parametrize(
    "response", [httpx.Response(200, text="not JSON"), httpx.Response(200, json=[1, 2])]
)
def test_bad_json(response):
    with GitHubSource(Limits(), transport=httpx.MockTransport(lambda _: response)) as client:
        with pytest.raises(RepoLensError, match="无法解析"):
            client.get("/test")


def test_response_byte_limit():
    with GitHubSource(
        Limits(), transport=httpx.MockTransport(lambda _: httpx.Response(200, content=b"x" * 200))
    ) as client:
        with pytest.raises(RepoLensError, match="大小上限"):
            client.get("/test", max_bytes=100)


def put(root: Path, name: str, text: str = "pass\n"):
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def test_local_filters_and_never_executes(tmp_path):
    sentinel = tmp_path / "EXECUTED"
    put(tmp_path, "main.py", f"open({str(sentinel)!r}, 'w').write('oops')")
    for name in ("node_modules/x.py", ".venv/x.py", ".env", "private.key", "ignored.py"):
        put(tmp_path, name)
    put(tmp_path, ".gitignore", "ignored.py\n")
    snap = local_snapshot(tmp_path, Limits())
    assert snap.contents == {"main.py": f"open({str(sentinel)!r}, 'w').write('oops')"}
    assert not sentinel.exists()
    assert {e.path for e in snap.entries} == {"main.py", ".gitignore"}


def test_local_symlinks_are_not_followed(tmp_path):
    root = tmp_path / "repo"
    root.mkdir()
    put(tmp_path, "outside.py")
    try:
        (root / "link.py").symlink_to(tmp_path / "outside.py")
        (root / "linked-dir").symlink_to(tmp_path, target_is_directory=True)
    except OSError:
        pytest.skip("Creating symlinks requires platform permissions")
    assert not local_snapshot(root, Limits()).entries


def test_file_and_total_limits(tmp_path):
    put(tmp_path, "a.py", "pass\n")
    put(tmp_path, "b.py", "pass\n")
    put(tmp_path, "huge.py", "#" * 50)
    snap = local_snapshot(tmp_path, Limits(max_file_bytes=10, max_total_bytes=5))
    assert len(snap.contents) == 1
    assert any("总读取" in w for w in snap.warnings)
    snap = local_snapshot(tmp_path, Limits(max_file_bytes=10))
    assert any("过大" in w for w in snap.warnings)
    snap = local_snapshot(tmp_path, Limits(max_files=1))
    assert len(snap.contents) == 1
    assert any("文件上限" in w for w in snap.warnings)


def test_inventory_limit(tmp_path):
    put(tmp_path, "a.py")
    put(tmp_path, "b.py")
    assert not local_snapshot(tmp_path, Limits(max_entries=1)).inventory_complete


def test_python_source_encoding():
    assert "café" in decode_text(b"# coding: latin-1\ns = 'caf\xe9'", "test.py")
    with pytest.raises(ValueError):
        decode_text(b"\x00", "test.py")


def test_file_changed_or_invalid_text():
    snap = Snapshot(name="x", source="local", entries=[FileEntry(path="main.py", size=1)])
    load_contents(snap, Limits(), lambda _: b"\xff")
    assert not snap.contents
    assert snap.warnings
    load_contents(snap, Limits(max_file_bytes=1), lambda _: b"pass\n")
    assert any("实际大小" in w for w in snap.warnings)


def test_local_missing(tmp_path):
    with pytest.raises(RepoLensError, match="不存在"):
        local_snapshot(tmp_path / "missing", Limits())


def test_bad_proxy_config_has_safe_error(monkeypatch):
    def bad_client(**_kwargs):
        raise ValueError("proxy://user:password@host")

    monkeypatch.setattr("repolens.sources.httpx.Client", bad_client)
    with pytest.raises(RepoLensError, match="代理") as error:
        GitHubSource(Limits())
    assert "password" not in str(error.value)


def test_source_precedes_nested_example_readmes_and_configs():
    entries = [
        FileEntry(path=p)
        for p in (
            "examples/a/README",
            "examples/a/pyproject.toml",
            "examples/a/cli.py",
            "src/pkg/core.py",
            "README.md",
            "pyproject.toml",
        )
    ]
    assert [e.path for e in sorted(entries, key=priority)][:3] == [
        "pyproject.toml",
        "README.md",
        "src/pkg/core.py",
    ]
