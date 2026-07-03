import ast
from pathlib import Path
from typing import Any

from swig2pyi.core.config import Config
from swig2pyi.core.emitter import StubEmitter
from swig2pyi.core.parser import SwigXmlParser
from swig2pyi.core.type_system import TypeManager


def _is_special_method(name: str) -> bool:
    return name in (
        "__init__",
        "__str__",
        "__repr__",
        "__getitem__",
        "__setitem__",
        "__len__",
        "__eq__",
        "__ne__",
        "__lt__",
        "__gt__",
        "__le__",
        "__ge__",
        "__neg__",
        "__add__",
        "__sub__",
        "__mul__",
        "__rmul__",
        "__hash__",
        "__bool__",
        "__nonzero__",
    )


def _extract_class_methods(node: ast.ClassDef) -> dict[str, list[dict[str, Any]]]:
    methods: dict[str, list[dict[str, Any]]] = {}
    for item in node.body:
        if isinstance(item, ast.FunctionDef):
            if item.name.startswith("_") and not _is_special_method(item.name):
                continue
            args = [arg.arg for arg in item.args.args]
            has_self = args and args[0] == "self"
            param_count = len(args) - 1 if has_self else len(args)
            is_vararg = bool(item.args.vararg)

            if item.name not in methods:
                methods[item.name] = []
            methods[item.name].append(
                {
                    "param_count": param_count,
                    "is_vararg": is_vararg,
                    "is_static": not has_self,
                }
            )
    return methods


def _process_node_symbols(
    node: ast.AST,
    classes: dict[str, Any],
    functions: dict[str, Any],
) -> None:
    if isinstance(node, ast.ClassDef) and not (
        node.name.startswith("_") and not node.name.startswith("__")
    ):
        classes[node.name] = {
            "methods": _extract_class_methods(node),
            "is_container": False,
        }
    elif isinstance(node, ast.FunctionDef) and not (
        node.name.startswith("_") and not node.name.startswith("__")
    ):
        args = [arg.arg for arg in node.args.args]
        functions[node.name] = {"param_count": len(args)}


def _extract_symbols(tree: ast.Module) -> dict[str, Any]:
    """Statically extract classes and functions from AST."""
    classes: dict[str, Any] = {}
    functions: dict[str, Any] = {}

    for node in tree.body:
        _process_node_symbols(node, classes, functions)

    return {"classes": classes, "functions": functions}


def test_osr_static_stub_matches_reference() -> None:
    """Compare the generated OSR stub against the reference osr.py statically using AST."""
    base_dir = Path(__file__).parent.parent
    xml_file = base_dir / "data" / "osr" / "osr.xml"
    config_file = base_dir.parent / "src" / "swig2pyi" / "rules" / "gdal_osr.json"
    reference_py_file = base_dir / "data" / "osr" / "osr.py"

    assert xml_file.exists()
    assert config_file.exists()
    assert reference_py_file.exists()

    config = Config.from_file(config_file)
    parser = SwigXmlParser()
    top = parser.parse_file(xml_file)

    tm = TypeManager(config, top=top)
    emitter = StubEmitter(tm)
    emitter.emit(top)
    stub_text = emitter.get_output()

    # Parse ASTs
    stub_ast = ast.parse(stub_text)
    ref_ast = ast.parse(reference_py_file.read_text(encoding="utf-8"))

    stub_syms = _extract_symbols(stub_ast)
    ref_syms = _extract_symbols(ref_ast)

    stub_classes = stub_syms["classes"]
    ref_classes = ref_syms["classes"]

    # Verify no extra classes are generated
    extra_classes = set(stub_classes.keys()) - set(ref_classes.keys())
    assert not extra_classes, (
        f"Stub has extra classes not in reference: {extra_classes}"
    )

    # Verify all generated methods are in the reference classes, and parameter counts match
    for cls in stub_classes:
        assert cls in ref_classes, f"Class {cls} missing from reference"
        stub_methods = stub_classes[cls]["methods"]
        ref_methods = ref_classes[cls]["methods"]

        extra_methods = (
            set(stub_methods.keys()) - set(ref_methods.keys()) - {"__init__"}
        )
        assert not extra_methods, (
            f"Class {cls} in stub has extra methods not in reference: {extra_methods}"
        )

        for method in stub_methods:
            if method == "__init__" or method not in ref_methods:
                continue

            stub_overloads = stub_methods[method]
            ref_overloads = ref_methods[method]

            # If any reference overload is varargs (*args), skip parameter count check
            if any(o["is_vararg"] for o in ref_overloads):
                continue

            stub_counts = {o["param_count"] for o in stub_overloads}
            ref_counts = {o["param_count"] for o in ref_overloads}
            assert stub_counts.intersection(ref_counts), (
                f"Parameter mismatch in {cls}.{method}: stub parameter counts "
                f"{stub_counts} do not match reference {ref_counts}"
            )

    # Verify no extra global functions are generated
    stub_funcs = stub_syms["functions"]
    ref_funcs = ref_syms["functions"]

    extra_funcs = set(stub_funcs.keys()) - set(ref_funcs.keys())
    assert not extra_funcs, f"Stub has extra functions not in reference: {extra_funcs}"

    for func in stub_funcs:
        assert func in ref_funcs, f"Global function {func} missing from reference"
        stub_count = stub_funcs[func]["param_count"]
        ref_count = ref_funcs[func]["param_count"]
        assert stub_count == ref_count, (
            f"Parameter mismatch in function {func}: stub {stub_count} vs reference {ref_count}"
        )
