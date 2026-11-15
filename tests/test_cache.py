import base64
import hashlib
import sqlite3
from concurrent.futures import ThreadPoolExecutor, as_completed
from contextlib import closing
from threading import Barrier

import httpx
import pytest

from repolens.analyzer import analyze
from repolens.cache import DiskCache, matches_blob
from repolens.models import Limits, Report
from repolens.render import markdown
from repolens.sources import GitHubSource, RepoLensError

DATA = b"print('ok')\n"
SHA = "1" * 40
TREE = "2" * 40
BLOB = hashlib.sha1(b"blob 12\0" + DATA, usedforsecurity=False).hexdigest()
META_TAG = 'W/"repo-v1"'
TREE_TAG = '"tree-v1"'


class GitHub:
    def __init__(self):
        self.calls = []
        self.repository_id = 1
        self.default_branch = "main"
        self.meta_tag = META_TAG
        self.blob_response = None
        self.tree_truncated = False
        self.meta_error = None
        self.tree_headers = {}
        self.extra_entries = []

    def __call__(self, request):
        path = request.url.path
        etag = request.headers.get("If-None-Match")
        self.calls.append((path, etag))
        if "/commits/" in path:
            assert not etag
            assert path.endswith(f"/{self.default_branch}")
            return httpx.Response(200, json={"sha": SHA, "commit": {"tree": {"sha": TREE}}})
        if path.endswith(f"/git/trees/{TREE}"):
            assert request.url.query == b"recursive=1"
            if etag == TREE_TAG and not self.tree_truncated:
                return httpx.Response(304, headers=self.tree_headers)
            return httpx.Response(
                200,
                headers={"ETag": TREE_TAG, **self.tree_headers},
                json={
                    "sha": TREE,
                    "truncated": self.tree_truncated,
                    "tree": [
                        {
                            "path": "main.py",
                            "size": len(DATA),
                            "sha": BLOB,
                            "type": "blob",
                            "mode": "100644",
                        },
                        *self.extra_entries,
                    ],
                },
            )
        if path.endswith(f"/git/blobs/{BLOB}"):
            assert not etag
            if self.blob_response is not None:
                return self.blob_response
            return httpx.Response(
                200,
                json={
                    "sha": BLOB,
                    "encoding": "base64",
                    "content": base64.b64encode(DATA).decode("ascii"),
                },
            )
        assert path.count("/") == 3
        if self.meta_error:
            return httpx.Response(self.meta_error)
        if etag == self.meta_tag:
            return httpx.Response(304, headers={"ETag": self.meta_tag})
        return httpx.Response(
            200,
            headers={"ETag": self.meta_tag},
            json={
                "private": False,
                "visibility": "public",
                "id": self.repository_id,
                "default_branch": self.default_branch,
            },
        )


def scan(api, directory, *, target="acme/app", limits=None, **kwargs):
    limits = limits or Limits()
    with GitHubSource(
        limits, cache_dir=directory, transport=httpx.MockTransport(api), **kwargs
    ) as client:
        return analyze(client.snapshot(target), limits)


def test_cold_and_warm_cache_with_conditional_requests(tmp_path):
    api = GitHub()
    cold = scan(api, tmp_path)
    warm = scan(api, tmp_path, limits=Limits(max_requests=3))
    assert cold.analyzed_files == warm.analyzed_files == ["main.py"]
    assert cold.bytes_read == warm.bytes_read == len(DATA)
    assert (cold.requests, warm.requests) == (4, 3)
    assert cold.remote_reads.model_dump() == {
        "cache_enabled": True,
        "blob_cache_hits": 0,
        "blob_cache_misses": 1,
        "blob_network_reads": 1,
        "not_modified": 0,
        "request_budget_exhausted": False,
        "rate_limited": False,
    }
    assert warm.remote_reads.model_dump() == {
        "cache_enabled": True,
        "blob_cache_hits": 1,
        "blob_cache_misses": 0,
        "blob_network_reads": 0,
        "not_modified": 2,
        "request_budget_exhausted": False,
        "rate_limited": False,
    }
    assert warm.content_complete and warm.inventory_complete
    assert api.calls[4:] == [
        ("/repos/acme/app", META_TAG),
        ("/repos/acme/app/commits/main", None),
        (f"/repos/acme/app/git/trees/{TREE}", TREE_TAG),
    ]
    assert Report.model_validate_json(warm.model_dump_json()).remote_reads == warm.remote_reads
    rendered = markdown(warm)
    assert "| Blob 缓存命中 / 未命中 | 1 / 0 |" in rendered
    assert "| 已校验的网络 Blob 读取 | 0 |" in rendered
    assert "| 条件请求返回 304 | 2 |" in rendered


def test_changed_metadata_and_repo_identity_replace_cache_scope(tmp_path):
    api = GitHub()
    scan(api, tmp_path)
    api.default_branch = "next"
    api.meta_tag = '"repo-next"'
    updated = scan(api, tmp_path)
    assert updated.remote_reads.blob_cache_hits == 1
    assert updated.remote_reads.not_modified == 1
    api.repository_id = 2
    api.meta_tag = '"replacement"'
    replacement = scan(api, tmp_path)
    assert replacement.remote_reads.blob_cache_hits == 0
    assert replacement.remote_reads.blob_network_reads == 1
    assert replacement.remote_reads.not_modified == 0
    other = scan(api, tmp_path, target="other/app")
    assert other.remote_reads.blob_cache_misses == 1


def test_identical_blobs_for_multiple_paths_only_download_once(tmp_path):
    api = GitHub()
    api.extra_entries = [
        {"path": "copy.py", "size": len(DATA), "sha": BLOB, "type": "blob", "mode": "100644"}
    ]
    report = scan(api, tmp_path)
    assert report.remote_reads.blob_cache_hits == 1
    assert report.remote_reads.blob_network_reads == 1
    assert report.bytes_read == len(DATA) * 2
    assert report.analyzed_files == ["copy.py", "main.py"]


@pytest.mark.parametrize("kwargs", [{"use_cache": False}, {"token": "never-persist-me"}])
def test_disabled_or_authenticated_cache_bypasses_disk(tmp_path, kwargs):
    api = GitHub()
    directory = tmp_path / "not-created"
    report = scan(api, directory, **kwargs)
    assert not directory.exists()
    assert report.requests == 4
    assert report.remote_reads.blob_network_reads == 1
    assert not report.remote_reads.cache_enabled
    assert report.remote_reads.blob_cache_misses == 0
    scan(api, tmp_path)
    warm = scan(api, tmp_path, **kwargs)
    assert warm.requests == 4 and warm.remote_reads.not_modified == 0
    assert b"never-persist-me" not in DiskCache(tmp_path).path.read_bytes()


def test_no_fallback_to_stale_metadata_on_forbidden_access(tmp_path):
    api = GitHub()
    scan(api, tmp_path)
    api.meta_error = 404
    with pytest.raises(RepoLensError, match="不存在"):
        scan(api, tmp_path)
    assert api.calls[-1] == ("/repos/acme/app", META_TAG)


def test_corrupted_cache_refetched_and_repaired(tmp_path):
    api = GitHub()
    scan(api, tmp_path)
    with closing(sqlite3.connect(DiskCache(tmp_path).path)) as db, db:
        db.execute("UPDATE entries SET data = zeroblob(length(data)) WHERE key NOT LIKE '%:tree:%'")
    repaired = scan(api, tmp_path)
    assert repaired.remote_reads.blob_cache_misses == 1
    assert repaired.remote_reads.blob_network_reads == 1
    assert repaired.remote_reads.not_modified == 1
    assert api.calls[4] == ("/repos/acme/app", None)
    warm = scan(api, tmp_path)
    assert warm.remote_reads.not_modified == 2
    assert warm.remote_reads.blob_cache_hits == 1


def test_blob_cache_validates_git_hash_independently_of_cache_digest(tmp_path):
    api = GitHub()
    cache = DiskCache(tmp_path)
    cache.put(f"acme/app:1:blob:{BLOB}", b"x" * len(DATA))
    repaired = scan(api, tmp_path)
    assert repaired.analyzed_files == ["main.py"]
    assert repaired.remote_reads.blob_cache_misses == 1
    assert cache.get(f"acme/app:1:blob:{BLOB}", len(DATA)) == (DATA, None)


@pytest.mark.parametrize("algorithm", ["sha1", "sha256"])
def test_git_blob_hash_includes_header_and_size(algorithm):
    digest = hashlib.new(algorithm, b"blob 12\0" + DATA).hexdigest().upper()
    assert matches_blob(DATA, digest, 12)
    assert not matches_blob(DATA, digest, 11)
    assert not matches_blob(b"x" * len(DATA), digest, 12)
    assert not matches_blob(DATA, "0" * 41, 12)


@pytest.mark.parametrize(
    ("blob", "warning"),
    [
        ({"encoding": "base64", "content": base64.b64encode(b"x" * 12).decode()}, "SHA"),
        ({"encoding": "base64", "content": base64.b64encode(b"x").decode()}, "大小"),
        ({"encoding": "base64", "content": "!!"}, "损坏"),
        ({"encoding": "utf-8", "content": "pass"}, "格式"),
    ],
)
def test_invalid_network_blob_is_never_cached(tmp_path, blob, warning):
    api = GitHub()
    api.blob_response = httpx.Response(200, json=blob)
    report = scan(api, tmp_path)
    assert not report.content_complete
    assert report.remote_reads.blob_network_reads == 0
    assert any(warning in message for message in report.warnings)
    assert DiskCache(tmp_path).get(f"acme/app:1:blob:{BLOB}", len(DATA)) is None


def test_truncated_tree_and_hit_remain_incomplete(tmp_path):
    api = GitHub()
    scan(api, tmp_path)
    api.tree_truncated = True
    first = scan(api, tmp_path)
    again = scan(api, tmp_path)
    assert first.content_complete and not first.inventory_complete
    assert again.remote_reads.blob_cache_hits == 1
    assert again.remote_reads.not_modified == 1
    assert not again.inventory_complete
    assert "| 清单状态 | 不完整 |" in markdown(again)
    assert api.calls[-1][1] is None


def test_304_without_validator_fails(tmp_path):
    with pytest.raises(RepoLensError, match="304"):
        scan(lambda _: httpx.Response(304), tmp_path)


def test_304_with_mismatched_etag_fails(tmp_path):
    scan(GitHub(), tmp_path)
    with pytest.raises(RepoLensError, match="ETag"):
        scan(lambda _: httpx.Response(304, headers={"ETag": '"different"'}), tmp_path)


def test_no_store_304_invalidates_saved_response(tmp_path):
    api = GitHub()
    scan(api, tmp_path)
    api.tree_headers = {"Cache-Control": "no-store"}
    warm = scan(api, tmp_path)
    assert warm.remote_reads.not_modified == 2
    next_report = scan(api, tmp_path)
    assert next_report.remote_reads.not_modified == 1


def test_budget_exhaustion_after_conditional_reads(tmp_path):
    api = GitHub()
    scan(api, tmp_path)
    DiskCache(tmp_path).discard(f"acme/app:1:blob:{BLOB}")
    report = scan(api, tmp_path, limits=Limits(max_requests=3))
    assert report.requests == 3
    assert report.inventory_complete and not report.content_complete
    assert report.remote_reads.not_modified == 2
    assert report.remote_reads.request_budget_exhausted
    assert not report.remote_reads.rate_limited
    assert "| 请求预算耗尽 | 是 |" in markdown(report)


@pytest.mark.parametrize("warm", [False, True])
def test_rate_limit_remaining_zero_blocks_network_but_allows_cached_blob(tmp_path, warm):
    api = GitHub()
    if warm:
        scan(api, tmp_path)
    api.tree_headers = {"X-RateLimit-Remaining": "0"}
    report = scan(api, tmp_path)
    assert report.requests == 3
    assert report.content_complete is warm
    assert report.remote_reads.rate_limited is not warm
    assert not report.remote_reads.request_budget_exhausted


@pytest.mark.parametrize("status", [403, 429])
def test_rate_limit_response_retains_partial_report(tmp_path, status):
    api = GitHub()
    api.blob_response = httpx.Response(status, json={"message": "Secondary rate limit"})
    report = scan(api, tmp_path)
    assert report.requests == 4
    assert report.remote_reads.rate_limited
    assert not report.content_complete
    assert not report.remote_reads.request_budget_exhausted
    assert "| GitHub API 限流 | 是 |" in markdown(report)


def test_cache_evicts_least_recently_used_with_byte_and_count_caps(tmp_path):
    cache = DiskCache(tmp_path, max_bytes=7, max_entries=2)
    cache.put("a", b"aaa")
    cache.put("b", b"bbb")
    assert cache.get("a", 7) == (b"aaa", None)
    cache.put("c", b"cccc")
    assert cache.get("a", 7) == (b"aaa", None)
    assert cache.get("b", 7) is None
    assert cache.get("c", 7) == (b"cccc", None)
    cache.put("empty", b"")
    assert cache.get("c", 7) == (b"cccc", None)
    assert cache.get("a", 7) is None
    cache.put("oversized", b"x" * 8)
    assert cache.get("oversized", 8) is None


def test_concurrent_writes_and_reads_only_observe_whole_values(tmp_path):
    cache = DiskCache(tmp_path, max_bytes=18_000, max_entries=3)
    data = [bytes([i]) * 4_096 for i in range(1, 5)]
    barrier = Barrier(len(data))

    def write(payload):
        barrier.wait(timeout=10)
        for _ in range(12):
            cache.put("shared", payload)
            result = cache.get("shared", 4_096)
            # A busy SQLite database is a valid best-effort cache miss.
            # Any successful read must still contain a complete value.
            if result is not None:
                assert result[0] in data and result[1] is None

    with ThreadPoolExecutor(max_workers=len(data)) as pool:
        # Collect worker errors before starting eviction. A second barrier
        # can mask the original error or time out on a slower CI runner.
        for future in as_completed([pool.submit(write, payload) for payload in data]):
            future.result()
        result = cache.get("shared", 4_096)
        assert result is not None and result[0] in data
        futures = [pool.submit(cache.put, str(payload[0]), payload) for payload in data]
        for future in as_completed(futures):
            future.result()
    with closing(sqlite3.connect(cache.path)) as db:
        count, size = db.execute("SELECT count(*), sum(length(data)) FROM entries").fetchone()
    # Contended writes may be skipped, but capacity must never be exceeded.
    assert 1 <= count <= 3 and size == count * 4_096
    cache.put("after-contention", data[0])
    assert cache.get("after-contention", 4_096) == (data[0], None)


def test_locked_cache_is_best_effort_and_recovers(tmp_path):
    cache = DiskCache(tmp_path)
    cache.put("existing", DATA)
    with closing(sqlite3.connect(cache.path)) as db:
        db.execute("BEGIN EXCLUSIVE")
        try:
            assert cache.get("existing", len(DATA)) is None
            cache.put("blocked", DATA)
            cache.discard("existing")
        finally:
            db.rollback()
    assert cache.get("existing", len(DATA)) == (DATA, None)
    assert cache.get("blocked", len(DATA)) is None
    cache.put("recovered", DATA)
    assert cache.get("recovered", len(DATA)) == (DATA, None)


def test_unreadable_cache_is_best_effort(tmp_path):
    cache = DiskCache(tmp_path)
    cache.path.write_bytes(b"not a database")
    report = scan(GitHub(), tmp_path)
    assert report.content_complete and report.requests == 4
    assert cache.path.read_bytes() == b"not a database"
