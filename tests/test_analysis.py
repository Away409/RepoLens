import json

import pytest

from repolens.analyzer import analyze, import_edges, parse_manifest, python_module
from repolens.models import FileEntry, Limits, Report, Snapshot
from repolens.render import markdown


def test_pep621_poetry_groups_and_scripts():
    content = """
[project]
dependencies = ["httpx>=0.27"]
dynamic = ["dependencies"]
[project.optional-dependencies]
dev = ["pytest>=8"]
[project.scripts]
demo = "demo.cli:main"
[dependency-groups]
test = ["coverage", {include-group = "dev"}]
[build-system]
requires = ["setuptools"]
[tool.poetry.dependencies]
python = "^3.11"
rich = "^13"
[tool.poetry.group.docs.dependencies]
mkdocs = "*"
"""
    deps, entries, warnings = parse_manifest("pyproject.toml", content)
    assert {d.name for d in deps} == {"httpx", "pytest", "coverage", "setuptools", "rich", "mkdocs"}
    assert "demo.cli:main" in entries[0].detail
    assert len(warnings) == 2


def test_package_json():
    deps, entries, _ = parse_manifest(
        "package.json",
        json.dumps(
            {
                "dependencies": {"react": "^19"},
                "devDependencies": {"vite": "^6"},
                "main": "index.js",
                "scripts": {"test": "node --test"},
            }
        ),
    )
    assert [(d.name, d.group) for d in deps] == [
        ("react", "dependencies"),
        ("vite", "devDependencies"),
    ]
    assert len(entries) == 2


def test_requirements_do_not_follow_files_or_urls():
    deps, _, warnings = parse_manifest(
        "requirements.txt",
        """
# comment
requests>=2 # trailing
-r other.txt
https://example.com/a.whl
thing @ https://example.com/pkg
numpy; python_version >= '3.11'
""",
    )
    assert [d.name for d in deps] == ["requests", "numpy"]
    assert len(warnings) == 3


def test_setup_cfg_and_cmake():
    deps, entries, _ = parse_manifest(
        "setup.cfg",
        """
[options]
install_requires =
    requests>=2
[options.extras_require]
test = pytest
[options.entry_points]
console_scripts =
    tool = demo:main
""",
    )
    assert len(deps) == 2 and len(entries) == 1
    deps, entries, warnings = parse_manifest(
        "CMakeLists.txt",
        """
# find_package(NotReal)
find_package(Threads REQUIRED)
add_executable(demo main.cpp)
""",
    )
    assert [d.name for d in deps] == ["Threads"]
    assert entries[0].line == 4
    assert warnings


def test_ast_nested_async_imports_main():
    module, entries = python_module(
        "src/pkg/__main__.py",
        """from .core import run
class Worker:
    async def process(self):
        def nested():
            return run()
        return nested()
if "__main__" == __name__:
    run()
""",
    )
    assert [s.name for s in module.symbols] == ["Worker", "Worker.process", "Worker.process.nested"]
    assert module.symbols[1].kind == "async function"
    assert module.imports[0].level == 1
    assert module.calls[0].line == 5
    assert len(entries) == 2
    edges = import_edges([module], ["src/pkg/__main__.py", "src/pkg/core.py"])
    assert len(edges) == 1
    assert edges[0].target == "src/pkg/core.py"


def test_import_resolution_relative_parent_and_ambiguous():
    module, _ = python_module("src/pkg/sub/mod.py", "from ..core import run\nimport pkg.duplicate")
    paths = [module.path, "src/pkg/core.py", "src/pkg/duplicate.py", "pkg/duplicate.py"]
    edges = import_edges([module], paths)
    assert len(edges) == 1 and edges[0].target == "src/pkg/core.py"


def test_from_package_import_submodule():
    module, _ = python_module("app.py", "from pkg import core")
    edges = import_edges([module], ["app.py", "pkg/__init__.py", "pkg/core.py"])
    assert {e.target for e in edges} == {"pkg/__init__.py", "pkg/core.py"}


@pytest.mark.parametrize(
    ("path", "content"),
    [
        ("bad.py", "def (:"),
        ("pyproject.toml", "[invalid"),
        ("package.json", "[]"),
        ("package.json", '{"dependencies":[]}'),
        ("setup.cfg", "[broken"),
    ],
)
def test_malformed_files_produce_warnings(path, content):
    snap = Snapshot(name="demo", source="local", contents={path: content})
    report = analyze(snap, Limits())
    assert any("解析失败" in w for w in report.warnings)


def test_full_report_roundtrip_and_source_evidence():
    files = ["main.py", "README.md", "LICENSE", "tests/test_main.py", ".github/workflows/ci.yml"]
    snap = Snapshot(
        name="acme/demo",
        source="github",
        url="https://github.com/acme/demo",
        revision="a" * 40,
        entries=[FileEntry(path=p) for p in files],
        contents={"main.py": "def main():\n    pass\n"},
    )
    report = analyze(snap, Limits())
    result = markdown(report)
    assert report.languages == {"Python": 2}
    assert report.signals["CI"] == [".github/workflows/ci.yml"]
    assert f"/blob/{'a' * 40}/main.py#L1" in result
    assert Report.model_validate_json(report.model_dump_json()).name == "acme/demo"


def test_markdown_escapes_untrusted_metadata():
    snap = Snapshot(name="<script>alert(1)</script>", source="local", description="[x](bad)\n|hi|")
    result = markdown(analyze(snap, Limits()))
    assert "<script>" not in result
    assert "\\[x\\]" in result
    assert "\\|hi\\|" in result


def test_readme_excerpt_prefers_root_and_is_bounded():
    snap = Snapshot(
        name="demo",
        source="local",
        contents={
            "docs/README.md": "nested",
            "README.md": "# Demo\n" + "x\n" * 100,
        },
    )
    report = analyze(snap, Limits())
    assert report.readme_excerpt.path == "README.md"
    assert len(report.readme_excerpt.detail.splitlines()) == 16
    assert "非自动总结" in markdown(report)
    assert all(line == line.rstrip() for line in markdown(report).splitlines())


def test_setup_py_dependency_limitation_is_visible():
    snap = Snapshot(
        name="demo", source="local", contents={"setup.py": "setup(install_requires=['x'])"}
    )
    report = analyze(snap, Limits())
    assert any("依赖声明未提取" in w for w in report.warnings)
