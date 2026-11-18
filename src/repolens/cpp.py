"""Extract C++ syntax evidence without preprocessing or compiling repository code."""

import posixpath
import re
from pathlib import PurePosixPath

import tree_sitter_cpp
from tree_sitter import Language, Node, Parser

from .models import CppFile, CppInclude, Evidence, Symbol

CPP_SOURCE_SUFFIXES = {".cpp", ".cc", ".cxx", ".c++"}
CPP_SUFFIXES = CPP_SOURCE_SUFFIXES | {".h", ".hpp", ".hh", ".hxx", ".h++"}
CPP_LANGUAGE = Language(tree_sitter_cpp.language())
MAX_SYMBOL_NAME = 512
TYPE_NODES = {
    "class_specifier": "class",
    "struct_specifier": "struct",
    "union_specifier": "union",
    "enum_specifier": "enum",
}
NAME_NODES = {
    "identifier",
    "field_identifier",
    "qualified_identifier",
    "destructor_name",
    "operator_name",
    "template_function",
    "template_method",
}


def node_text(node: Node) -> str:
    return node.text.decode("utf-8")


def function_name(node: Node) -> str | None:
    current = node.child_by_field_name("declarator")
    while current and not current.is_missing:
        if current.type in NAME_NODES:
            return None if current.has_error else node_text(current)
        child = current.child_by_field_name("declarator")
        if child is None and current.type in {"parenthesized_declarator", "reference_declarator"}:
            child = current.named_child(0)
        current = child
    return None


def include_target(path: str, name: str, kind: str, inventory: set[str]) -> str | None:
    if not name or name.startswith("/") or any(char in name for char in "\\:\n\r"):
        return None

    def match(directory: str) -> str | None:
        candidate = posixpath.normpath(posixpath.join(directory, name))
        if not candidate.startswith("../") and candidate in inventory:
            return candidate
        return None

    if kind == "quoted":
        adjacent = match(posixpath.dirname(path))
        if adjacent is not None:
            return adjacent
    if ".." in PurePosixPath(name).parts:
        return None
    matches = {target for root in ("", "include", "src") if (target := match(root)) is not None}
    return matches.pop() if len(matches) == 1 else None


def parse_include(node: Node, path: str, inventory: set[str]) -> CppInclude | None:
    value = node.child_by_field_name("path")
    if value is None or value.is_missing or value.has_error:
        return None
    text = node_text(value)
    line = node.start_point.row + 1
    if value.type == "string_literal" and text.startswith('"') and text.endswith('"'):
        kind = "quoted"
    elif value.type == "system_lib_string" and text.startswith("<") and text.endswith(">"):
        kind = "angled"
    else:
        return CppInclude(name=text, kind="macro", line=line)
    name = text[1:-1]
    target = include_target(path, name, kind, inventory)
    return CppInclude(name=name, kind=kind, line=line, target=target)


def cpp_file(path: str, content: str, inventory: set[str]) -> tuple[CppFile, list[Evidence]]:
    root = Parser(CPP_LANGUAGE).parse(content.encode("utf-8")).root_node
    result = CppFile(path=path, has_parse_errors=root.has_error)
    entries: list[Evidence] = []
    pending = [(root, "", False)]
    while pending:
        node, scope, recovered = pending.pop()
        recovered = recovered or node.is_error
        kind = TYPE_NODES.get(node.type)
        name = None
        if node.type == "preproc_include":
            include = parse_include(node, path, inventory)
            if include is not None:
                result.includes.append(include)
        elif node.type == "function_definition":
            kind, name = "function", function_name(node)
            if name == "main" and not scope and not recovered and not node.has_error:
                entries.append(
                    Evidence(path=path, line=node.start_point.row + 1, detail="候选 C++ main 定义")
                )
        elif node.type == "namespace_definition" or kind:
            if node.child_by_field_name("body") is not None:
                kind = kind or "namespace"
                identifier = node.child_by_field_name("name")
                if identifier and not identifier.has_error:
                    name = node_text(identifier)
            else:
                kind = None

        child_scope = scope
        if kind:
            name = re.sub(r"\s*::\s*", "::", name) if name else None
            qualified = scope + (name or "(anonymous)")
            if len(qualified) > MAX_SYMBOL_NAME:
                qualified = "…" + qualified[-(MAX_SYMBOL_NAME - 1) :]
            child_scope = f"{qualified}::"
            if name:
                result.symbols.append(
                    Symbol(
                        name=qualified,
                        kind=kind,
                        line=node.start_point.row + 1,
                        end_line=node.end_point.row + 1,
                    )
                )
        pending.extend((child, child_scope, recovered) for child in reversed(node.named_children))
    return result, entries
