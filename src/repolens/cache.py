"""Bounded, best-effort storage for anonymous public GitHub reads."""

import hashlib
import os
import re
import sqlite3
from contextlib import closing, contextmanager
from pathlib import Path

DEFAULT_CACHE_BYTES = 64 * 1024 * 1024
DEFAULT_CACHE_ENTRIES = 4096
GIT_SHA = re.compile(r"(?:[0-9a-f]{40}|[0-9a-f]{64})", re.IGNORECASE | re.ASCII)


def default_cache_dir() -> Path:
    if os.name == "nt":
        root = Path(os.environ.get("LOCALAPPDATA") or Path.home() / "AppData" / "Local")
        return root / "RepoLens" / "Cache"
    root = Path(os.environ.get("XDG_CACHE_HOME") or Path.home() / ".cache")
    if not root.is_absolute():
        root = Path.home() / ".cache"
    return root / "repolens"


def matches_blob(data: bytes, sha: str, size: int) -> bool:
    if len(data) != size or not GIT_SHA.fullmatch(sha):
        return False
    digest = hashlib.sha1(usedforsecurity=False) if len(sha) == 40 else hashlib.sha256()
    digest.update(f"blob {len(data)}\0".encode("ascii"))
    digest.update(data)
    return digest.hexdigest() == sha.lower()


def entry_digest(key: str, data: bytes, etag: str | None) -> bytes:
    digest = hashlib.sha256(f"{key}\0{etag or ''}\0".encode())
    digest.update(data)
    return digest.digest()


class DiskCache:
    def __init__(
        self,
        directory: Path,
        max_bytes: int = DEFAULT_CACHE_BYTES,
        max_entries: int = DEFAULT_CACHE_ENTRIES,
    ):
        self.path = directory.expanduser() / "github-v1.sqlite3"
        self.max_bytes = max_bytes
        self.max_entries = max_entries

    @contextmanager
    def connect(self):
        self.path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
        if self.path.is_symlink():
            raise OSError("cache database is a symlink")
        with closing(sqlite3.connect(self.path, timeout=1)) as db, db:
            db.execute(
                """
                CREATE TABLE IF NOT EXISTS entries (
                    key TEXT PRIMARY KEY, data BLOB NOT NULL, etag TEXT,
                    digest BLOB NOT NULL, touched INTEGER NOT NULL
                )
                """
            )
            yield db

    def get(self, key: str, max_bytes: int) -> tuple[bytes, str | None] | None:
        try:
            with self.connect() as db:
                row = db.execute(
                    """
                    SELECT data, etag, digest FROM entries
                    WHERE key = ? AND length(data) <= ?
                    """,
                    (key, min(max_bytes, self.max_bytes)),
                ).fetchone()
                if row is None:
                    return None
                data, etag, digest = row
                if (
                    not isinstance(data, bytes)
                    or (etag is not None and not isinstance(etag, str))
                    or digest != entry_digest(key, data, etag)
                ):
                    return None
                db.execute(
                    """
                    UPDATE entries SET touched = (SELECT max(touched) + 1 FROM entries)
                    WHERE key = ? AND digest = ?
                    """,
                    (key, digest),
                )
                return data, etag
        except (OSError, sqlite3.Error):
            return None

    def put(self, key: str, data: bytes, etag: str | None = None) -> None:
        if len(data) > self.max_bytes:
            return
        try:
            with self.connect() as db:
                # Insertion and eviction run in one serialized write transaction.
                db.execute(
                    """
                    INSERT OR REPLACE INTO entries (key, data, etag, digest, touched)
                    SELECT ?, ?, ?, ?, coalesce(max(touched), 0) + 1 FROM entries
                    """,
                    (
                        key,
                        data,
                        etag,
                        entry_digest(key, data, etag),
                    ),
                )
                count, size = db.execute(
                    "SELECT count(*), sum(length(data)) FROM entries"
                ).fetchone()
                if count <= self.max_entries and size <= self.max_bytes:
                    return
                oldest = db.execute(
                    "SELECT key, length(data) FROM entries ORDER BY touched, key"
                ).fetchall()
                for old_key, length in oldest:
                    db.execute("DELETE FROM entries WHERE key = ?", (old_key,))
                    count -= 1
                    size -= length
                    if count <= self.max_entries and size <= self.max_bytes:
                        break
        except (OSError, sqlite3.Error):
            return

    def discard(self, key: str) -> None:
        try:
            with self.connect() as db:
                db.execute("DELETE FROM entries WHERE key = ?", (key,))
        except (OSError, sqlite3.Error):
            return
