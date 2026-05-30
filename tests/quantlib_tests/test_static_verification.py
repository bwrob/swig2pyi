import ast
import os
import tempfile
from pathlib import Path
from typing import Any

import pytest

from swig2pyi.core.config import Config
from swig2pyi.core.emitter import StubEmitter
from swig2pyi.core.parser import SwigXmlParser
from swig2pyi.core.runner import SwigRunner
from swig2pyi.core.type_system import TypeManager

TESTS_DIR = Path(__file__).parent.parent
DATA_DIR = TESTS_DIR / "data"
CONFIG_FILE = TESTS_DIR.parent / "src" / "swig2pyi" / "rules" / "quantlib.json"

# Find all quantlib version directories since 1.37
versions = sorted(
    [d.name for d in DATA_DIR.glob("quantlib-*") if d.is_dir()],
    key=lambda x: [int(c) for c in x.replace("quantlib-", "").split(".")],
)

# Filter by environment variable if set
test_version = os.environ.get("SWIG2PYI_TEST_VERSION")
if test_version:
    target = (
        test_version
        if test_version.startswith("quantlib-")
        else f"quantlib-{test_version}"
    )
    versions = [v for v in versions if v == target]


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


def _is_swig_container(node: ast.ClassDef) -> bool:
    for base in node.bases:
        if (isinstance(base, ast.Name) and base.id in ("list", "dict")) or (
            isinstance(base, ast.Subscript)
            and isinstance(base.value, ast.Name)
            and base.value.id in ("list", "dict")
        ):
            return True
    return (
        node.name.endswith("Vector")
        or node.name.endswith("Map")
        or node.name.endswith("Pair")
    )


def _process_node_symbols(
    node: ast.AST,
    classes: dict[str, Any],
    functions: dict[str, Any],
    globals_: set[str],
) -> None:
    if isinstance(node, ast.ClassDef):
        if not (node.name.startswith("_") and not node.name.startswith("__")):
            classes[node.name] = {
                "methods": _extract_class_methods(node),
                "is_container": _is_swig_container(node),
            }
    elif isinstance(node, ast.FunctionDef):
        if not (node.name.startswith("_") and not node.name.startswith("__")):
            args = [arg.arg for arg in node.args.args]
            functions[node.name] = {"param_count": len(args)}
    elif isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name) and not target.id.startswith("_"):
                globals_.add(target.id)
    elif (
        isinstance(node, ast.AnnAssign)
        and isinstance(node.target, ast.Name)
        and not node.target.id.startswith("_")
    ):
        globals_.add(node.target.id)


def extract_symbols(tree: ast.Module) -> dict[str, Any]:
    """Statically extract classes, functions, and globals from AST."""
    classes: dict[str, Any] = {}
    functions: dict[str, Any] = {}
    globals_: set[str] = set()

    for node in tree.body:
        _process_node_symbols(node, classes, functions, globals_)

    return {"classes": classes, "functions": functions, "globals": globals_}


def _verify_classes(ref_classes: dict[str, Any], stub_classes: dict[str, Any]) -> None:
    missing_classes = set(ref_classes.keys()) - set(stub_classes.keys())
    missing_classes -= {"SwigPyIterator", "SwigNonDynamicMeta"}
    assert not missing_classes, f"Stub is missing classes: {sorted(missing_classes)}"


def _verify_method_signatures(
    class_name: str,
    method_name: str,
    ref_overloads: list[dict[str, Any]],
    stub_overloads: list[dict[str, Any]],
) -> None:
    if any(o["is_vararg"] for o in ref_overloads):
        return
    ref_counts = {o["param_count"] for o in ref_overloads}
    stub_counts = {o["param_count"] for o in stub_overloads}
    assert ref_counts.intersection(stub_counts), (
        f"Method {class_name}.{method_name} parameter counts {stub_counts} "
        f"do not match reference {ref_counts}"
    )


def _verify_methods(ref_classes: dict[str, Any], stub_classes: dict[str, Any]) -> None:
    for class_name, ref_cls_info in ref_classes.items():
        if (
            class_name in ("SwigPyIterator", "SwigNonDynamicMeta")
            or class_name not in stub_classes
        ):
            continue

        if stub_classes[class_name].get("is_container"):
            continue

        ref_methods = ref_cls_info["methods"]
        stub_methods = stub_classes[class_name]["methods"]

        missing_methods = set(ref_methods.keys()) - set(stub_methods.keys())
        missing_methods -= {"thisown", "__init__"}

        assert not missing_methods, (
            f"Class {class_name} is missing methods: {sorted(missing_methods)}"
        )

        for method_name, ref_overloads in ref_methods.items():
            if method_name == "thisown" or method_name not in stub_methods:
                continue
            _verify_method_signatures(
                class_name, method_name, ref_overloads, stub_methods[method_name]
            )


def _verify_functions(
    ref_functions: dict[str, Any], stub_functions: dict[str, Any]
) -> None:
    missing_funcs = set(ref_functions.keys()) - set(stub_functions.keys())
    assert not missing_funcs, (
        f"Stub is missing global functions: {sorted(missing_funcs)}"
    )


@pytest.mark.parametrize("version_folder", versions)
def test_static_stub_matches_reference_py(version_folder: str) -> None:
    """Compare the generated .pyi stub against QuantLib.py statically using AST."""
    version_dir = DATA_DIR / version_folder
    interface_file = version_dir / "quantlib.i"
    reference_py_file = version_dir / "QuantLib.py"

    assert interface_file.exists(), f"quantlib.i not found in {version_dir}"
    assert reference_py_file.exists(), f"QuantLib.py not found in {version_dir}"
    assert CONFIG_FILE.exists()

    config = Config.from_file(CONFIG_FILE)
    config.includes = [str(version_dir)]

    # Run SWIG and generate stub
    runner = SwigRunner()
    xml_fd, xml_path = tempfile.mkstemp(suffix=".xml")
    os.close(xml_fd)
    xml_path_obj = Path(xml_path)

    try:
        runner.run(config.includes, interface_file, xml_path_obj)
        parser = SwigXmlParser()
        top = parser.parse_file(xml_path_obj)

        from swig2pyi.api import collect_enums
        enums = collect_enums(top)
        tm = TypeManager(config, enums=enums)
        emitter = StubEmitter(tm)
        emitter.emit(top)
        stub_text = emitter.get_output()
    finally:
        if xml_path_obj.exists():
            xml_path_obj.unlink()

    # Parse ASTs
    stub_ast = ast.parse(stub_text)
    ref_ast = ast.parse(reference_py_file.read_text(encoding="utf-8"))

    stub_syms = extract_symbols(stub_ast)
    ref_syms = extract_symbols(ref_ast)

    _verify_classes(ref_syms["classes"], stub_syms["classes"])
    _verify_methods(ref_syms["classes"], stub_syms["classes"])
    _verify_functions(ref_syms["functions"], stub_syms["functions"])
