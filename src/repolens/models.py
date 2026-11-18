"""Versioned report contract, shared by sources, analysis and renderers."""

from datetime import UTC, datetime
from typing import Literal

from pydantic import BaseModel, Field


class Limits(BaseModel):
    max_files: int = Field(default=35, ge=1, le=1000)
    max_file_bytes: int = Field(default=256_000, ge=1, le=2_000_000)
    max_total_bytes: int = Field(default=5_000_000, ge=1, le=100_000_000)
    max_entries: int = Field(default=20_000, ge=1, le=100_000)
    max_requests: int = Field(default=50, ge=3, le=5000)
    timeout: float = Field(default=20, gt=0, le=120)


class FileEntry(BaseModel):
    path: str
    size: int = Field(default=0, ge=0)
    sha: str | None = None


class RemoteReads(BaseModel):
    cache_enabled: bool = False
    blob_cache_hits: int = 0
    blob_cache_misses: int = 0
    blob_network_reads: int = 0
    not_modified: int = 0
    request_budget_exhausted: bool = False
    rate_limited: bool = False


class Snapshot(BaseModel):
    name: str
    source: str
    url: str | None = None
    revision: str | None = None
    description: str = ""
    license: str | None = None
    entries: list[FileEntry] = Field(default_factory=list)
    contents: dict[str, str] = Field(default_factory=dict)
    warnings: list[str] = Field(default_factory=list)
    inventory_complete: bool = True
    eligible_files: int = 0
    bytes_read: int = 0
    requests: int = 0
    remote_reads: RemoteReads | None = None


class Evidence(BaseModel):
    path: str
    line: int | None = None
    detail: str


class Dependency(BaseModel):
    name: str
    specification: str
    group: str
    path: str


class Symbol(BaseModel):
    name: str
    kind: str
    line: int
    end_line: int


class Import(BaseModel):
    module: str
    names: list[str] = Field(default_factory=list)
    level: int = 0
    line: int


class CallSite(BaseModel):
    expression: str
    line: int


class PythonModule(BaseModel):
    path: str
    symbols: list[Symbol] = Field(default_factory=list)
    imports: list[Import] = Field(default_factory=list)
    calls: list[CallSite] = Field(default_factory=list)


class CppInclude(BaseModel):
    name: str
    kind: Literal["quoted", "angled", "macro"]
    line: int
    target: str | None = None


class CppFile(BaseModel):
    path: str
    has_parse_errors: bool = False
    symbols: list[Symbol] = Field(default_factory=list)
    includes: list[CppInclude] = Field(default_factory=list)


class Edge(BaseModel):
    source: str
    target: str
    line: int


class Report(BaseModel):
    schema_version: str = "1.0"
    generated_at: str = Field(default_factory=lambda: datetime.now(UTC).isoformat())
    name: str
    source: str
    url: str | None = None
    revision: str | None = None
    description: str = ""
    readme_excerpt: Evidence | None = None
    license: str | None = None
    inventory_complete: bool
    content_complete: bool | None = None
    file_count: int
    eligible_files: int
    analyzed_files: list[str]
    bytes_read: int
    requests: int
    remote_reads: RemoteReads | None = None
    limits: Limits
    languages: dict[str, int]
    files: list[str]
    signals: dict[str, list[str]]
    dependencies: list[Dependency] = Field(default_factory=list)
    entry_points: list[Evidence] = Field(default_factory=list)
    modules: list[PythonModule] = Field(default_factory=list)
    import_edges: list[Edge] = Field(default_factory=list)
    cpp_files: list[CppFile] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
