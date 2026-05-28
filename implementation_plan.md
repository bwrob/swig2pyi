# Implementation Plan: Parameterization, Test Restructuring, and GDAL OSR Verification

This document outlines the detailed plan to remove hardcoded library-specific assumptions from `swig2pyi`, restructure the test suite to separate lightweight and heavy integration tests, and verify the generator against a second mature SWIG-wrapped project: GDAL's Spatial Reference System (OSR) module.

## User Review Required

> [!IMPORTANT]
> Based on prioritization, test restructuring and synthetic tests are placed first in the implementation sequence to establish a fast, lightweight feedback loop (<1s execution) before modifying core parser/emitter logic.

## Open Questions

> [!NOTE]
> None at this time. All requirements are clear.

## Proposed Changes

---

### Component A: Test Suite Reorganization & CI Integration (Priority 1)

1.  **Move QuantLib Integration Tests**:
    Move these slow files to the existing `tests/quantlib_tests/` directory:
    *   `tests/test_integration_quantlib_full.py` $\rightarrow$ `tests/quantlib_tests/test_integration_quantlib_full.py`
    *   `tests/test_integration_quantlib_mini.py` $\rightarrow$ `tests/quantlib_tests/test_integration_quantlib_mini.py`
    *   `tests/test_integration_quantlib_versions.py` $\rightarrow$ `tests/quantlib_tests/test_integration_quantlib_versions.py`
    *   `tests/test_static_verification.py` $\rightarrow$ `tests/quantlib_tests/test_static_verification.py`
2.  **Ignore Heavy Tests by Default**:
    Configure `pytest` in [pyproject.toml](file:///home/bwrob/dev/swig2pyi/pyproject.toml) to ignore the `tests/quantlib_tests/` directory during default runs:
    ```toml
    [tool.pytest.ini_options]
    addopts = "--ignore=tests/quantlib_tests"
    ```
3.  **Define Dedicated Tasks**:
    Update [poe_tasks.toml](file:///home/bwrob/dev/swig2pyi/poe_tasks.toml) to configure `test` and `test-heavy`.
    *Note*: We override `addopts` with `-o addopts=""` to make sure `--ignore` is disabled when running the heavy test suite.
    ```toml
    [tool.poe.tasks]
    test = { cmd = "pytest", help = "Run lightweight unit and synthetic tests." }
    test-heavy = { cmd = "pytest -o addopts=\"\" tests/quantlib_tests", help = "Run heavy integration tests including QuantLib." }
    ```
4.  **Update CI Workflows**:
    Update the GitHub Action configuration in [.github/workflows/python_tests.yaml](file:///home/bwrob/dev/swig2pyi/.github/workflows/python_tests.yaml) to run both the lightweight and the heavy test suites:
    ```yaml
          - name: 🐍 Run pytest (Lightweight)
            if: always()
            run: uv run poe test

          - name: 🐍 Run pytest (Heavy Integration)
            if: always()
            run: uv run poe test-heavy
    ```

---

### Component B: Synthetic Test Suite (Priority 2)

Create a self-contained test case that verifies all parser and emitter features using a mock SWIG interface file.

#### [NEW] [synthetic.i](file:///home/bwrob/dev/swig2pyi/tests/data/synthetic/synthetic.i)
A SWIG interface exposing:
*   A C++ namespace prefix (e.g. `Synthetic::`).
*   A base class and a derived class.
*   An enum inside a class.
*   Methods with default parameters.
*   An overloaded operator (e.g. `operator+`).
*   A template class (e.g. `SmartPtr<T>`).

#### [NEW] [test_integration_synthetic.py](file:///home/bwrob/dev/swig2pyi/tests/test_integration_synthetic.py)
Integration test that compiles `synthetic.i`, generates stubs, and verifies output structure.

---

### Component C: Core Configuration & Schema (Priority 3)

#### [MODIFY] [config.py](file:///home/bwrob/dev/swig2pyi/src/swig2pyi/core/config.py)
Add the following fields to the Pydantic `Config` class to allow customizing namespace cleaning and proxy handling:
*   `namespaces_to_remove: list[str] = []`
    *   *Purpose*: A list of namespaces that should be cleaned from C++ types during processing (e.g., `["QuantLib::", "ext::"]`).
*   `delegate_templates: list[str] = []`
    *   *Purpose*: A list of C++ template names that represent smart pointer or handle proxies (e.g., `["Handle", "RelinkableHandle"]`).

---

### Component D: Core Parser & Emitter (Priority 4)

#### [MODIFY] [emitter.py](file:///home/bwrob/dev/swig2pyi/src/swig2pyi/core/emitter.py)
*   **Namespace Stripping**:
    Update the `clean_cpp_type` method to dynamically iterate over and remove prefixes listed in `config.namespaces_to_remove`.
    ```python
    def clean_cpp_type(self, cpp_type: str) -> str:
        for ns in self.tm.config.namespaces_to_remove:
            cpp_type = cpp_type.replace(ns, "")
        cpp_type = cpp_type.replace("const ", "").replace("volatile ", "")
        cpp_type = cpp_type.replace("(", "").replace(")", "")
        return "".join(cpp_type.split())
    ```
*   **Smart Pointer Delegation**:
    Update `_delegate_single_handle` to build its template-matching regular expression dynamically based on `config.delegate_templates` and `config.namespaces_to_remove`.
    ```python
    def _delegate_single_handle(self, cls: Class, name_to_class: dict[str, Class]) -> None:
        if not cls.cpp_type or not self.tm.config.delegate_templates:
            return

        escaped_templates = "|".join(re.escape(t) for t in self.tm.config.delegate_templates)
        ns_prefixes = "|".join(re.escape(ns) for ns in self.tm.config.namespaces_to_remove if ns.endswith("::"))
        ns_pattern = f"(?:{ns_prefixes})?" if ns_prefixes else ""

        pattern = rf"^{ns_pattern}(?:{escaped_templates})<\s*(.*?)\s*>$"
        match = re.match(pattern, cls.cpp_type)
        if not match:
            return

        target_type = match.group(1).strip("() ")
        cleaned_target = self.clean_cpp_type(target_type)
        py_target_name = self._cpp_to_py_class_names.get(cleaned_target)
        if not py_target_name:
            return

        collected = self._collect_class_methods(py_target_name, name_to_class, set())
        existing_names = {self.nm.get_python_name(m.name) for m in cls.cdecls}
        for method in collected:
            py_name = self.nm.get_python_name(method.name)
            if py_name and py_name not in existing_names:
                cls.cdecls.append(method.model_copy(deep=True))
                existing_names.add(py_name)
    ```
*   **Dynamic Template Base Names Extraction**:
    Update `_add_cpp_type_base` and `_get_base_names` to dynamically handle templates from configuration instead of hardcoding `Handle`, `RelinkableHandle`, or `TimeSeries`.
    ```python
    def _add_cpp_type_base(self, cpp_type: str, base_names: list[str]) -> None:
        resolved = self.tm.to_python(cpp_type)
        is_generic = self._is_container_type(resolved)
        # Handle generic template types dynamically (e.g. Handle[X], TimeSeries[X])
        if "[" in resolved and resolved.endswith("]"):
            is_generic = True
        if is_generic and resolved not in base_names:
            base_names.append(resolved)

    def _get_base_names(self, base_type: str) -> list[str]:
        names: list[str] = []
        cleaned = self.clean_cpp_type(base_type)
        if cleaned in self._cpp_to_py_class_names:
            normalized_base = self._cpp_to_py_class_names[cleaned]
        else:
            normalized_base = self.tm.to_python(base_type)
        names.append(normalized_base)

        # Extract wrapped type from delegate templates
        if self.tm.config.delegate_templates:
            escaped_templates = "|".join(re.escape(t) for t in self.tm.config.delegate_templates)
            pattern = rf"(?:^|\.)(?:{escaped_templates})\[(.+)\]$"
            match = re.search(pattern, normalized_base)
            if match:
                wrapped_type = match.group(1)
                if wrapped_type not in names:
                    names.append(wrapped_type)
        return names
    ```

#### [MODIFY] [quantlib.json](file:///home/bwrob/dev/swig2pyi/src/swig2pyi/rules/quantlib.json)
Update the JSON configuration file to externalize the QuantLib rules:
```json
{
    "module_name": "QuantLib",
    "includes": [
        "tests/data/quantlib-1.40"
    ],
    "namespaces_to_remove": [
        "QuantLib::",
        "ext::"
    ],
    "delegate_templates": [
        "Handle",
        "RelinkableHandle"
    ],
    ...
}
```

---

### Component E: GDAL OSR Integration & Multi-Project Test (Priority 5)

#### [NEW] [gdal_osr.json](file:///home/bwrob/dev/swig2pyi/src/swig2pyi/rules/gdal_osr.json)
Configure rules for GDAL OSR (e.g., mapping type name changes).

#### [NEW] [osr.xml](file:///home/bwrob/dev/swig2pyi/tests/data/osr/osr.xml)
A pre-generated SWIG XML file for GDAL OSR to run tests without requiring the GDAL development library on the testing host.

#### [NEW] [test_integration_osr.py](file:///home/bwrob/dev/swig2pyi/tests/test_integration_osr.py)
Run generation on `osr.xml` and assert structural correctness of `SpatialReference` and `CoordinateTransformation`.

#### [MODIFY] [test_handle_inheritance.py](file:///home/bwrob/dev/swig2pyi/tests/test_handle_inheritance.py)
Update config initialization in this test to define `delegate_templates=["Handle", "RelinkableHandle"]` explicitly.

---

## Verification Plan

### Automated Tests
*   Run lightweight test suite (<1s execution time):
    ```bash
    uv run pytest
    ```
*   Run heavy integration suite:
    ```bash
    uv run poe test-heavy
    ```
*   Run full code quality:
    ```bash
    uv run poe code-quality
    ```

### Manual Verification
*   Verify that generated stubs from `osr.xml` parse cleanly with `ast.parse` and can be formatted by `ruff`.
