"""Collect module-level TypeScript declarations and static module references."""

import posixpath
from pathlib import PurePosixPath

import tree_sitter_typescript
from tree_sitter import Language, Node, Parser

from .models import Symbol, TypeScriptFile, TypeScriptReference

TS_SUFFIXES = (".ts", ".tsx", ".mts", ".cts")
TS_CANDIDATES = (*TS_SUFFIXES, ".d.ts", ".d.mts", ".d.cts")
JS_EXTENSIONS = {
    ".js": (".ts", ".tsx", ".d.ts"),
    ".mjs": (".mts", ".d.mts"),
    ".cjs": (".cts", ".d.cts"),
}
IDENTIFIERS = {
    "identifier",
    "type_identifier",
    "property_identifier",
    "private_property_identifier",
}
TS_LANGUAGE = Language(tree_sitter_typescript.language_typescript())
TSX_LANGUAGE = Language(tree_sitter_typescript.language_tsx())
DECLARATIONS = {
    "class_declaration": "class",
    "abstract_class_declaration": "class",
    "interface_declaration": "interface",
    "type_alias_declaration": "type",
    "enum_declaration": "enum",
    "function_declaration": "function",
    "generator_function_declaration": "function",
    "function_signature": "function",
}


def relative_target(path: str, specifier: str, inventory: set[str]) -> str | None:
    if not (specifier in {".", ".."} or specifier.startswith(("./", "../"))) or "\\" in specifier:
        return None
    base = posixpath.normpath(posixpath.join(posixpath.dirname(path), specifier))
    if base == ".." or base.startswith("../"):
        return None
    suffix = PurePosixPath(base).suffix
    directory_only = specifier.rsplit("/", 1)[-1] in {"", ".", ".."}
    if not directory_only and suffix.lower() in TS_SUFFIXES:
        return base if base in inventory else None
    if not directory_only and suffix in JS_EXTENSIONS:
        candidates = [base.removesuffix(suffix) + ext for ext in JS_EXTENSIONS[suffix]]
        candidates.append(base)
    else:
        directory = posixpath.normpath(posixpath.join(base, "index"))
        candidates = [directory + ext for ext in TS_CANDIDATES]
        if not directory_only:
            candidates.extend(base + ext for ext in TS_CANDIDATES)
    matches = inventory.intersection(candidates)
    return matches.pop() if len(matches) == 1 else None


def add_symbol(result: TypeScriptFile, node: Node, kind: str, prefix: str = "") -> str | None:
    name = node.child_by_field_name("name")
    if name is None or name.is_missing or name.has_error or name.type not in IDENTIFIERS:
        return None
    qualified = prefix + name.text.decode("utf-8")
    if len(qualified) > 512:
        qualified = "…" + qualified[-511:]
    result.symbols.append(
        Symbol(
            name=qualified,
            kind=kind,
            line=node.start_point.row + 1,
            end_line=node.end_point.row + 1,
        )
    )
    return qualified


def declarations(result: TypeScriptFile, node: Node) -> None:
    if node.type == "ambient_declaration":
        for child in node.named_children:
            declarations(result, child)
    elif node.type in DECLARATIONS:
        name = add_symbol(result, node, DECLARATIONS[node.type])
        body = node.child_by_field_name("body")
        if name and body and body.type in {"class_body", "interface_body"}:
            for member in body.named_children:
                if member.type in {
                    "method_definition",
                    "method_signature",
                    "abstract_method_signature",
                }:
                    add_symbol(result, member, "method", name + ".")
    elif node.type in {"lexical_declaration", "variable_declaration"}:
        for binding in node.named_children:
            value = binding.child_by_field_name("value")
            if value and value.type in {
                "arrow_function",
                "function_expression",
                "generator_function",
            }:
                add_symbol(result, binding, "function")


def typescript_file(path: str, content: str, inventory: set[str]) -> TypeScriptFile:
    language = TSX_LANGUAGE if path.lower().endswith(".tsx") else TS_LANGUAGE
    root = Parser(language).parse(content.encode("utf-8")).root_node
    result = TypeScriptFile(path=path, has_parse_errors=root.has_error)
    for statement in root.named_children:
        if statement.type in {"import_statement", "export_statement"}:
            source = statement.child_by_field_name("source")
            if source and source.type == "string" and not source.has_error:
                specifier = source.text.decode("utf-8")[1:-1]
                result.references.append(
                    TypeScriptReference(
                        kind="import" if statement.type == "import_statement" else "re-export",
                        specifier=specifier,
                        line=statement.start_point.row + 1,
                        target=relative_target(path, specifier, inventory),
                    )
                )
            declaration = statement.child_by_field_name("declaration")
            if declaration is not None:
                declarations(result, declaration)
        else:
            declarations(result, statement)
    return result
