from pathlib import Path

import pytest

from repolens.analyzer import analyze
from repolens.models import Limits, Report
from repolens.render import markdown
from repolens.sources import local_snapshot
from repolens.typescript import relative_target, typescript_file


def test_tsx_declarations_and_static_references():
    content = """import type { User } from './types.js';
export * from '../common';
import 'package';
interface Card { title(): string; }
export const View = () => <div/>;
export abstract class Page { abstract render(): void; }
declare function setup(): void;
export type ID = number;
export enum State { Ready }
function outer() { function inner() {} }
// import 'comment';
const text = "export * from 'example'";
import('./lazy');
"""
    result = typescript_file("src/page.TSX", content, {"src/types.ts", "common/index.mts"})
    assert not result.has_parse_errors
    assert [(s.name, s.kind, s.line) for s in result.symbols] == [
        ("Card", "interface", 4),
        ("Card.title", "method", 4),
        ("View", "function", 5),
        ("Page", "class", 6),
        ("Page.render", "method", 6),
        ("setup", "function", 7),
        ("ID", "type", 8),
        ("State", "enum", 9),
        ("outer", "function", 10),
    ]
    assert [(r.kind, r.line, r.specifier, r.target) for r in result.references] == [
        ("import", 1, "./types.js", "src/types.ts"),
        ("re-export", 2, "../common", "common/index.mts"),
        ("import", 3, "package", None),
    ]


@pytest.mark.parametrize(
    ("specifier", "target"),
    [
        ("./a", None),
        ("./a/", "dir/a/index.ts"),
        ("./a.ts", "dir/a.ts"),
        ("./b.mjs", "dir/b.mts"),
        ("./c.cjs", "dir/c.cts"),
        ("./a.js", None),
        ("../missing", None),
        ("../../escape", None),
        ("@alias/a", None),
        (".", "dir/index.ts"),
    ],
)
def test_relative_targets(specifier, target):
    paths = {"dir/a.ts", "dir/a/index.ts", "dir/b.mts", "dir/c.cts", "dir/a.js", "dir/index.ts"}
    assert relative_target("dir/view.tsx", specifier, paths) == target


def test_local_partial_report_and_schema_compatibility(tmp_path: Path):
    (tmp_path / "a.MTS").write_text("export interface A {}\nexport const incomplete = ;")
    (tmp_path / "other.cts").write_text("export type T = string;")
    limits = Limits(max_files=1)
    report = analyze(local_snapshot(tmp_path, limits), limits)
    assert report.schema_version == "1.3" and report.eligible_files == 2
    assert report.languages == {"TypeScript": 2} and not report.content_complete
    (item,) = report.typescript_files
    assert item.has_parse_errors and item.symbols[0].name == "A"
    assert "a.MTS:1" in markdown(report)
    assert any("TypeScript 语法树" in warning for warning in report.warnings)
    old = report.model_dump(exclude={"typescript_files"})
    old["schema_version"] = "1.2"
    assert Report.model_validate(old).typescript_files == []
