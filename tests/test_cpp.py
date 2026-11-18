import base64
import hashlib
from pathlib import Path

import httpx

from repolens.analyzer import analyze
from repolens.cpp import cpp_file
from repolens.models import Limits, Report
from repolens.render import markdown
from repolens.sources import GitHubSource, local_snapshot


def test_cpp_syntax_uses_definitions_and_preserves_scope_and_lines():
    content = """// #include "ignored.hpp"
const auto text = R"code(
#include "also-ignored.hpp"
int main() {}
)code";
namespace outer::inner {
template<class T> struct Runner {
    Runner() = default;
    ~Runner() {}
    auto run(T value) -> T { return value; }
    static int main() { return 1; }
    int declared();
    enum class State { ready };
};
template<class T> class Forward;
}
namespace { int main() { return 2; } }
int* factory() { return nullptr; }
int main(int argc, char**) { return argc; }
"""
    result, entries = cpp_file("source.cpp", content, set())
    assert not result.has_parse_errors and not result.includes
    assert [(s.name, s.kind, s.line, s.end_line) for s in result.symbols] == [
        ("outer::inner", "namespace", 6, 16),
        ("outer::inner::Runner", "struct", 7, 14),
        ("outer::inner::Runner::Runner", "function", 8, 8),
        ("outer::inner::Runner::~Runner", "function", 9, 9),
        ("outer::inner::Runner::run", "function", 10, 10),
        ("outer::inner::Runner::main", "function", 11, 11),
        ("outer::inner::Runner::State", "enum", 13, 13),
        ("(anonymous)::main", "function", 17, 17),
        ("factory", "function", 18, 18),
        ("main", "function", 19, 19),
    ]
    assert [entry.line for entry in entries] == [19]


def test_include_resolution_observes_inventory_and_preserves_ambiguity():
    content = """#include "same.h"
#include "../shared.h"
#include <project/api.hpp>
#if FLAG
#include <same.h>
#else
#include HEADER(name)
#endif
#include "../../outside.h"
#include <iostream>
"""
    result, _ = cpp_file(
        "src/app/main.cc",
        content,
        {
            "src/app/same.h",
            "src/shared.h",
            "src/same.h",
            "include/same.h",
            "include/project/api.hpp",
        },
    )
    assert [(i.name, i.kind, i.line, i.target) for i in result.includes] == [
        ("same.h", "quoted", 1, "src/app/same.h"),
        ("../shared.h", "quoted", 2, "src/shared.h"),
        ("project/api.hpp", "angled", 3, "include/project/api.hpp"),
        ("same.h", "angled", 5, None),
        ("HEADER(name)", "macro", 7, None),
        ("../../outside.h", "quoted", 9, None),
        ("iostream", "angled", 10, None),
    ]


def test_cpp_recovers_evidence_without_claiming_an_entry_inside_an_error():
    content = 'void broken( {\n#include "part.hpp"\nint main() { return 0; }\n'
    result, entries = cpp_file("main.cpp", content, {"part.hpp"})
    assert result.has_parse_errors and not entries
    assert [(i.target, i.line) for i in result.includes] == [("part.hpp", 2)]
    assert [(s.name, s.line) for s in result.symbols] == [("main", 3)]


def test_cpp_bounds_repeated_long_scope_names():
    name = "Long" * 500
    result, _ = cpp_file("long.hpp", f"struct {name} {{ int member() {{ return 1; }} }};", set())
    assert len(result.symbols) == 2 and not result.has_parse_errors
    assert all(len(s.name) == 512 and s.name.startswith("…") for s in result.symbols)
    assert result.symbols[-1].name.endswith("::member")


def test_local_cpp_report_respects_source_budgets_and_marks_parse_errors(tmp_path: Path):
    (tmp_path / "a.hpp").write_text("struct A {};\n", encoding="utf-8")
    (tmp_path / "main.CXX").write_text(
        '#include "a.hpp"\nint main() {}\nint broken(\n', encoding="utf-8"
    )
    (tmp_path / "a.c").write_text("int other(void) {}\n", encoding="utf-8")
    limits = Limits(max_files=1)
    report = analyze(local_snapshot(tmp_path, limits), limits)
    assert report.eligible_files == 2 and not report.content_complete
    assert report.analyzed_files == ["main.CXX"]
    assert report.cpp_files[0].has_parse_errors
    assert report.cpp_files[0].includes[0].target == "a.hpp"
    assert any("C++ 语法树未完整识别" in warning for warning in report.warnings)
    assert [entry.line for entry in report.entry_points] == [2]
    assert Report.model_validate_json(report.model_dump_json()) == report


def test_remote_cpp_report_links_to_fixed_revision_without_fetching_header():
    sha, tree = "a" * 40, "b" * 40
    content = b'#include "part.hpp"\nint main() {}\n'
    blob = hashlib.sha1(f"blob {len(content)}\0".encode() + content, usedforsecurity=False)
    requests = []

    def handler(request):
        requests.append(request.url.path)
        paths = {
            "/repos/acme/demo": {"default_branch": "main"},
            "/repos/acme/demo/commits/main": {"sha": sha, "commit": {"tree": {"sha": tree}}},
            f"/repos/acme/demo/git/trees/{tree}": {
                "truncated": False,
                "tree": [
                    {
                        "type": "blob",
                        "mode": "100644",
                        "path": "src/main.cpp",
                        "size": len(content),
                        "sha": blob.hexdigest(),
                    },
                    {
                        "type": "blob",
                        "mode": "100644",
                        "path": "include/part.hpp",
                        "size": 20,
                        "sha": "c" * 40,
                    },
                ],
            },
            f"/repos/acme/demo/git/blobs/{blob.hexdigest()}": {
                "encoding": "base64",
                "content": base64.b64encode(content).decode(),
            },
        }
        return httpx.Response(200, json=paths[request.url.path])

    limits = Limits(max_files=1)
    with GitHubSource(limits, transport=httpx.MockTransport(handler), use_cache=False) as client:
        report = analyze(client.snapshot("acme/demo"), limits)
    assert len(requests) == 4
    assert report.schema_version == "1.2" and not report.modules and not report.import_edges
    rendered = markdown(report)
    assert f"/blob/{sha}/src/main.cpp#L1" in rendered
    assert f"/blob/{sha}/src/main.cpp#L2" in rendered
    assert f"/blob/{sha}/include/part.hpp" in rendered
