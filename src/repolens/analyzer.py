"""Evidence-based extraction; heuristics are labelled, never presented as execution."""

import ast
import configparser
import json
import re
import tomllib
from collections import Counter
from pathlib import PurePosixPath

from .cpp import CPP_SUFFIXES, cpp_file
from .models import (
    CallSite,
    Dependency,
    Edge,
    Evidence,
    Import,
    Limits,
    PythonModule,
    Report,
    Snapshot,
    Symbol,
)
from .typescript import TS_SUFFIXES, typescript_file

LANGUAGES = {
    ".py": "Python",
    ".pyi": "Python",
    **dict.fromkeys(CPP_SUFFIXES, "C++"),
    ".h": "C/C++ header",
    ".c": "C",
    ".js": "JavaScript",
    ".jsx": "JavaScript",
    **dict.fromkeys(TS_SUFFIXES, "TypeScript"),
    ".go": "Go",
    ".rs": "Rust",
    ".java": "Java",
    ".kt": "Kotlin",
    ".cs": "C#",
    ".rb": "Ruby",
    ".php": "PHP",
    ".swift": "Swift",
    ".sh": "Shell",
    ".ps1": "PowerShell",
    ".html": "HTML",
    ".css": "CSS",
    ".vue": "Vue",
    ".sql": "SQL",
}


def signals(files: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {k: [] for k in ("README", "LICENSE", "测试", "CI", "贡献指南")}
    for path in files:
        name = PurePosixPath(path).name.lower()
        if name.startswith("readme"):
            result["README"].append(path)
        if name.startswith(("license", "licence", "copying")):
            result["LICENSE"].append(path)
        if (
            any(p in {"tests", "test", "__tests__"} for p in PurePosixPath(path).parts)
            or name.startswith("test_")
            or name.endswith(("_test.py", ".test.ts", ".test.js"))
        ):
            result["测试"].append(path)
        if (
            (path.startswith(".github/workflows/") and name.endswith((".yml", ".yaml")))
            or name in {".gitlab-ci.yml", ".travis.yml", "jenkinsfile"}
            or path == ".circleci/config.yml"
        ):
            result["CI"].append(path)
        if name.startswith("contributing"):
            result["贡献指南"].append(path)
    return result


def requirement_name(spec: str) -> str:
    match = re.match(r"[A-Za-z0-9][A-Za-z0-9._-]*", spec)
    return match.group() if match else "未解析依赖"


def parse_manifest(path: str, content: str) -> tuple[list[Dependency], list[Evidence], list[str]]:
    deps: list[Dependency] = []
    entries: list[Evidence] = []
    warnings: list[str] = []
    name = PurePosixPath(path).name.lower()

    def add(spec: str, group: str, dep_name: str | None = None):
        deps.append(
            Dependency(
                name=dep_name or requirement_name(spec), specification=spec, group=group, path=path
            )
        )

    if name == "pyproject.toml":
        data = tomllib.loads(content)
        project = data.get("project", {})
        for dep in project.get("dependencies", []):
            add(dep, "runtime")
        for group, values in project.get("optional-dependencies", {}).items():
            for dep in values:
                add(dep, f"optional:{group}")
        for group, values in data.get("dependency-groups", {}).items():
            for dep in values:
                if isinstance(dep, str):
                    add(dep, f"group:{group}")
                else:
                    warnings.append(f"{path}：dependency-groups 的 include-group 未展开。")
        for dep in data.get("build-system", {}).get("requires", []):
            add(dep, "build")
        if "dependencies" in project.get("dynamic", []):
            warnings.append(f"{path}：动态依赖不会执行解析。")
        for group in ("scripts", "gui-scripts"):
            for command, target in project.get(group, {}).items():
                entries.append(Evidence(path=path, detail=f"声明入口 {command} → {target}"))
        poetry = data.get("tool", {}).get("poetry", {})
        for key in ("dependencies", "dev-dependencies"):
            for dep, value in poetry.get(key, {}).items():
                if dep != "python":
                    add(str(value), f"poetry:{key}", dep)
        for group, values in poetry.get("group", {}).items():
            for dep, value in values.get("dependencies", {}).items():
                add(str(value), f"poetry:{group}", dep)
        for command, target in poetry.get("scripts", {}).items():
            entries.append(Evidence(path=path, detail=f"Poetry 声明入口 {command} → {target}"))
    elif name == "package.json":
        data = json.loads(content)
        for group in (
            "dependencies",
            "devDependencies",
            "peerDependencies",
            "optionalDependencies",
        ):
            for dep, version in data.get(group, {}).items():
                add(str(version), group, dep)
        for key in ("main", "module", "bin"):
            if key in data:
                entries.append(Evidence(path=path, detail=f"package.json {key}: {data[key]}"))
        for command, target in data.get("scripts", {}).items():
            entries.append(Evidence(path=path, detail=f"npm script {command}: {target}（未执行）"))
    elif name.startswith("requirements") and name.endswith(".txt"):
        if "\\\n" in content:
            warnings.append(f"{path}：包含续行，当前逐行解析可能不完整。")
        for number, raw in enumerate(content.splitlines(), 1):
            value = re.split(r"\s+#", raw, maxsplit=1)[0].strip()
            if not value or value.startswith("#"):
                continue
            if value.startswith("-") or "://" in value or " @ " in value:
                warnings.append(
                    f"{path}:{number}：选项、包含文件或 URL 依赖未展开（不访问外部链接）。"
                )
                continue
            add(value, "requirements")
    elif name == "setup.cfg":
        parser = configparser.ConfigParser(interpolation=None)
        parser.read_string(content)
        for value in parser.get("options", "install_requires", fallback="").splitlines():
            if value.strip():
                add(value.strip(), "runtime")
        if parser.has_section("options.extras_require"):
            for group, value in parser.items("options.extras_require"):
                for dep in value.splitlines():
                    if dep.strip():
                        add(dep.strip(), f"optional:{group}")
        if parser.has_section("options.entry_points"):
            for group, value in parser.items("options.entry_points"):
                if group in {"console_scripts", "gui_scripts"}:
                    for item in value.splitlines():
                        if item.strip():
                            entries.append(Evidence(path=path, detail=f"声明入口 {item.strip()}"))
    elif name == "cmakelists.txt":
        warnings.append(
            f"{path}：CMake 仅正则提取 find_package / add_executable，未解释变量和条件。"
        )
        for number, line in enumerate(content.splitlines(), 1):
            code = line.split("#", 1)[0]
            dep = re.search(r"\bfind_package\s*\(\s*([\w.+-]+)", code, re.I)
            if dep:
                add(dep.group(1), "cmake:heuristic")
            exe = re.search(r"\badd_executable\s*\(\s*([\w.+-]+)", code, re.I)
            if exe:
                entries.append(
                    Evidence(
                        path=path,
                        line=number,
                        detail=f"候选 CMake 可执行目标：{exe.group(1)}（正则推断）",
                    )
                )
    return deps, entries, warnings


class PythonVisitor(ast.NodeVisitor):
    def __init__(self):
        self.scope: list[str] = []
        self.symbols: list[Symbol] = []
        self.imports: list[Import] = []
        self.calls: list[CallSite] = []

    def definition(self, node, kind):
        self.symbols.append(
            Symbol(
                name=".".join([*self.scope, node.name]),
                kind=kind,
                line=node.lineno,
                end_line=node.end_lineno or node.lineno,
            )
        )
        self.scope.append(node.name)
        self.generic_visit(node)
        self.scope.pop()

    def visit_ClassDef(self, node):
        self.definition(node, "class")

    def visit_FunctionDef(self, node):
        self.definition(node, "function")

    def visit_AsyncFunctionDef(self, node):
        self.definition(node, "async function")

    def visit_Import(self, node):
        for alias in node.names:
            self.imports.append(Import(module=alias.name, line=node.lineno))

    def visit_ImportFrom(self, node):
        self.imports.append(
            Import(
                module=node.module or "",
                names=[a.name for a in node.names],
                level=node.level,
                line=node.lineno,
            )
        )

    def visit_Call(self, node):
        if len(self.calls) < 200:
            self.calls.append(CallSite(expression=ast.unparse(node.func)[:160], line=node.lineno))
        self.generic_visit(node)


def python_module(path: str, text: str) -> tuple[PythonModule, list[Evidence]]:
    tree = ast.parse(text, filename=path)
    visitor = PythonVisitor()
    visitor.visit(tree)
    entries = []
    if PurePosixPath(path).name == "__main__.py":
        entries.append(Evidence(path=path, line=1, detail="Python -m 候选入口（依据文件名）"))
    for node in tree.body:
        if not isinstance(node, ast.If) or not isinstance(node.test, ast.Compare):
            continue
        test = node.test
        if len(test.ops) != 1 or not isinstance(test.ops[0], ast.Eq):
            continue
        left, right = test.left, test.comparators[0]
        if isinstance(left, ast.Constant):
            left, right = right, left
        if (
            isinstance(left, ast.Name)
            and left.id == "__name__"
            and isinstance(right, ast.Constant)
            and right.value == "__main__"
        ):
            entries.append(Evidence(path=path, line=node.lineno, detail="检测到 __main__ 守卫"))
    return PythonModule(
        path=path, symbols=visitor.symbols, imports=visitor.imports, calls=visitor.calls
    ), entries


def module_name(path: str) -> str:
    parts = list(PurePosixPath(path).with_suffix("").parts)
    if len(parts) > 1 and parts[0] == "src":
        parts.pop(0)
    if parts[-1] == "__init__":
        parts.pop()
    return ".".join(parts)


def import_edges(modules: list[PythonModule], paths: list[str]) -> list[Edge]:
    # Resolve only exact names under conventional root/src layouts. Never guess aliases.
    mapping: dict[str, list[str]] = {}
    for path in paths:
        if path.endswith(".py"):
            mapping.setdefault(module_name(path), []).append(path)
    edges = set()
    for module in modules:
        name = module_name(module.path)
        package = name if module.path.endswith("/__init__.py") else name.rpartition(".")[0]
        for imp in module.imports:
            base = imp.module
            if imp.level:
                parts = package.split(".") if package else []
                if imp.level > len(parts):
                    continue
                base = ".".join(parts[: len(parts) - imp.level + 1] + ([base] if base else []))
            candidates = [base, *[f"{base}.{n}" if base else n for n in imp.names if n != "*"]]
            for target_name in candidates:
                targets = mapping.get(target_name, [])
                if len(targets) == 1 and targets[0] != module.path:
                    edges.add((module.path, targets[0], imp.line))
    return [Edge(source=s, target=t, line=n) for s, t, n in sorted(edges)]


def analyze(snapshot: Snapshot, limits: Limits) -> Report:
    paths = sorted(entry.path for entry in snapshot.entries)
    report = Report(
        schema_version="1.3",
        name=snapshot.name,
        source=snapshot.source,
        url=snapshot.url,
        revision=snapshot.revision,
        description=snapshot.description,
        license=snapshot.license,
        inventory_complete=snapshot.inventory_complete,
        content_complete=len(snapshot.contents) == snapshot.eligible_files,
        file_count=len(paths),
        eligible_files=snapshot.eligible_files,
        analyzed_files=sorted(snapshot.contents),
        bytes_read=snapshot.bytes_read,
        requests=snapshot.requests,
        remote_reads=snapshot.remote_reads,
        limits=limits,
        languages=dict(
            Counter(
                LANGUAGES[PurePosixPath(p).suffix.lower()]
                for p in paths
                if PurePosixPath(p).suffix.lower() in LANGUAGES
            ).most_common()
        ),
        files=paths,
        signals=signals(paths),
        warnings=list(snapshot.warnings),
    )
    readmes = sorted(
        (p for p in snapshot.contents if PurePosixPath(p).name.lower().startswith("readme")),
        key=lambda p: (p.count("/"), p),
    )
    if readmes:
        path = readmes[0]
        report.readme_excerpt = Evidence(
            path=path,
            line=1,
            detail="\n".join(snapshot.contents[path].splitlines()[:16])[:1200],
        )
    inventory = set(paths)
    for path, content in sorted(snapshot.contents.items()):
        try:
            if path.endswith(".py"):
                module, entries = python_module(path, content)
                report.modules.append(module)
                report.entry_points.extend(entries)
                if PurePosixPath(path).name == "setup.py":
                    report.warnings.append(
                        f"{path}：仅分析 Python 符号；setup.py 中的依赖声明未提取。"
                    )
                if len(module.calls) == 200:
                    report.warnings.append(f"{path}：调用表达式最多展示前 200 个。")
            elif PurePosixPath(path).suffix.lower() in TS_SUFFIXES:
                module_ts = typescript_file(path, content, inventory)
                report.typescript_files.append(module_ts)
                if module_ts.has_parse_errors:
                    report.warnings.append(
                        f"{path}：TypeScript 语法树未完整识别，保留可识别的线索。"
                    )
            elif PurePosixPath(path).suffix.lower() in CPP_SUFFIXES:
                cpp, entries = cpp_file(path, content, inventory)
                report.cpp_files.append(cpp)
                report.entry_points.extend(entries)
                if cpp.has_parse_errors:
                    report.warnings.append(f"{path}：C++ 语法树未完整识别，保留可识别的线索。")
            else:
                deps, entries, warnings = parse_manifest(path, content)
                report.dependencies.extend(deps)
                report.entry_points.extend(entries)
                report.warnings.extend(warnings)
        except (
            SyntaxError,
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            configparser.Error,
            RecursionError,
        ):
            report.warnings.append(f"解析失败：{path}（格式无效、语法不兼容或结构过深）。")
    report.import_edges = import_edges(report.modules, paths)
    return report
