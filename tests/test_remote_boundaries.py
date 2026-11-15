"""Offline regressions for remote validation and cache representation boundaries."""

import json

import httpx
import pytest
from test_cache import BLOB, DATA, TREE, GitHub, scan

from repolens.cache import DiskCache
from repolens.models import Limits
from repolens.sources import GitHubSource, RepoLensError


@pytest.mark.parametrize(
    "entry",
    [
        None,
        [],
        {},
        {"path": ["bad"]},
        {"path": "a.py", "type": [], "mode": "100644"},
        {"path": "a.py", "type": "blob", "mode": []},
        *[
            {"path": "a.py", "type": "blob", "mode": "100644", "size": size, "sha": BLOB}
            for size in [-1, None, "12", True]
        ],
        {"path": "a.py", "type": "blob", "mode": "100644", "size": 12, "sha": "bad"},
        {"path": "main.py", "type": "blob", "mode": "100644", "size": 12, "sha": BLOB},
    ],
)
def test_malformed_tree_fails_safely_without_persisting(tmp_path, entry):
    api = GitHub()
    api.extra_entries = [entry]
    for _ in range(2):
        with pytest.raises(RepoLensError, match="元数据"):
            scan(api, tmp_path)
    assert api.calls[-1][1] is None
    assert DiskCache(tmp_path).get(f"acme/app:1:blob:{BLOB}", len(DATA)) is None


def test_semantically_invalid_cached_tree_is_refetched(tmp_path):
    api = GitHub()
    scan(api, tmp_path)
    key = f"acme/app:1:tree:/repos/acme/app/git/trees/{TREE}?recursive=1"
    # Valid storage digest, invalid API representation.
    DiskCache(tmp_path).put(
        key,
        json.dumps(
            {
                "sha": TREE,
                "truncated": False,
                "tree": [None],
            }
        ).encode(),
        '"tree-v1"',
    )
    report = scan(api, tmp_path)
    assert report.content_complete
    assert report.remote_reads.not_modified == 1
    assert api.calls[-1][1] is None


@pytest.mark.parametrize(
    "headers",
    [
        {"Vary": "*"},
        {"Vary": "Cookie"},
        {"Vary": "Authorization"},
        {"Cache-Control": "max-age=60, no-store"},
    ],
)
@pytest.mark.parametrize("warm", [False, True])
def test_unsupported_cache_representation_is_not_reused(tmp_path, headers, warm):
    api = GitHub()
    if warm:
        scan(api, tmp_path)
    api.tree_headers = headers
    scan(api, tmp_path)
    report = scan(api, tmp_path)
    assert report.remote_reads.not_modified == 1
    assert api.calls[-1][1] is None


def test_supported_vary_keeps_conditional_requests(tmp_path):
    api = GitHub()
    api.tree_headers = {"Vary": "Accept, Accept-Encoding, X-GitHub-Api-Version, X-Requested-With"}
    scan(api, tmp_path)
    assert scan(api, tmp_path).remote_reads.not_modified == 2


@pytest.mark.parametrize("license_info", [[], "MIT", 3])
def test_malformed_license_has_safe_error(tmp_path, license_info):
    api = GitHub()

    def handler(request):
        response = api(request)
        if request.url.path == "/repos/acme/app":
            data = response.json()
            data["license"] = license_info
            return httpx.Response(200, json=data)
        return response

    with pytest.raises(RepoLensError, match="元数据"):
        scan(handler, tmp_path)


@pytest.mark.parametrize("status", [201, 202, 204, 206])
def test_unexpected_success_status_is_rejected(tmp_path, status):
    with pytest.raises(RepoLensError, match=str(status)):
        scan(lambda _: httpx.Response(status, json={"default_branch": "main"}), tmp_path)


def test_retries_consume_budget_and_preserve_partial_scan(tmp_path, monkeypatch):
    api = GitHub()
    api.blob_response = httpx.Response(503)
    monkeypatch.setattr("repolens.sources.time.sleep", lambda _: None)
    report = scan(api, tmp_path, limits=Limits(max_requests=4))
    assert report.requests == 4
    assert report.remote_reads.request_budget_exhausted
    assert report.inventory_complete and not report.content_complete


def test_cached_content_still_respects_file_and_byte_limits(tmp_path):
    api = GitHub()
    api.extra_entries = [
        {"path": "copy.py", "type": "blob", "mode": "100644", "size": len(DATA), "sha": BLOB}
    ]
    scan(api, tmp_path)
    for limits in [Limits(max_files=1), Limits(max_total_bytes=len(DATA))]:
        report = scan(api, tmp_path, limits=limits)
        assert len(report.analyzed_files) == 1
        assert report.remote_reads.blob_cache_hits == 1
        assert report.bytes_read == len(DATA)
        assert report.inventory_complete and not report.content_complete


def test_cache_never_bypasses_fresh_metadata_on_second_snapshot(tmp_path):
    api = GitHub()
    with GitHubSource(Limits(), transport=httpx.MockTransport(api), cache_dir=tmp_path) as client:
        first = client.snapshot("acme/app")
        second = client.snapshot("acme/app")
    assert first.requests == 4 and second.requests == 3
    assert first.remote_reads.blob_cache_hits == 0
    assert second.remote_reads.blob_cache_hits == 1
