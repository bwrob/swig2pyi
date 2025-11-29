# Project Guidelines for swig2pyi

This document outlines the development guidelines, project practices, and architectural decisions for the `swig2pyi` project.

## 1. Project Overview

`swig2pyi` is a tool designed to generate high-quality Python typing stubs (`.pyi`) from SWIG interface files (`.i`).

### 1.1. Core Philosophy: "Universal Pipeline"

Unlike previous iterations or similar tools that parse `.i` files directly (which is fragile due to SWIG's complexity), `swig2pyi` leverages SWIG itself to produce an intermediate representation (XML).

**The Pipeline:**
1.  **SWIG Frontend:** Execute `swig -xml ...` to generate a comprehensive AST of the exposed C++ interface.
2.  **Middle-End (Normalization):** Parse the XML into structured data objects using `pydantic-xml`. Normalize "dirty" C++ types (e.g., `boost::shared_ptr<QuantLib::Date>`) into clean Python types (e.g., `Date`) using a robust, configuration-driven Type Manager.
3.  **Backend (Emission):** Iterate over the normalized AST to emit valid, idiomatic Python type stubs (`.pyi`).

### 1.2. Tech Stack & Tooling

*   **Language:** Python 3.12+
*   **Package Management:** `uv`
*   **Core Dependencies:**
    *   `swig` (The Python module, used to locate the SWIG binary and environment)
    *   `pydantic` & `pydantic-xml` (For declarative XML parsing)
*   **Testing:** `pytest` (Unit tests and functional integration tests against QuantLib data)
*   **Linting/Types:** `ruff` & `basedpyright`

## 2. Architectural Components

### 2.1. The Configuration (`config.json`)

The tool is completely driven by configuration, avoiding hardcoded library rules. A typical config includes:
*   **`module_name`**: The target Python module name.
*   **`includes`**: Paths to C++ headers or SWIG interfaces.
*   **`type_map`**: Direct C++ to Python type mappings (e.g., `QuantLib::Real` -> `float`).
*   **`smart_pointers`**: Regex-capable list of smart pointers to unwrap.
*   **`containers`**: Mapping of C++ templates to Python ABCs (e.g., `std::vector` -> `typing.MutableSequence`).

### 2.2. The Runner (`SwigRunner`)

**Challenge:** SWIG's `-xml` output mode is mutually exclusive with language backends like `-python`. However, we need the XML to reflect the Python interface (including specific directives like `feature("autodoc")`).

**Solution:**
*   The runner executes `swig -xml -DSWIGPYTHON`.
*   **Mocks & Preamble:** Since we aren't loading the full standard `python.swg` library (which contains directives that crash the XML parser or are invalid in XML mode), the Runner injects:
    1.  **Mocks:** Minimal `.i` files (e.g., `std_vector.i`, `boost_shared_ptr.i`) located in `src/swig2pyi/mocks`. These satisfy `%include` requirements without pulling in complex logic.
    2.  **Preamble:** A dynamically generated set of macros (`%define`) to silence known directives that cause errors in XML mode (e.g., `%apply_cpptypes`, `%pythoncode`).

### 2.3. The Parser (`SwigXmlParser`)

Uses `pydantic-xml` to define a declarative schema for the SWIG XML format. This avoids imperative XML traversal and ensures the AST is strongly typed before processing.

### 2.4. The Type System (`TypeManager`)

Responsible for the "C++ -> Python" translation layer.
*   **Unwrapping:** Recursively unwraps smart pointers defined in the config.
*   **Stripping:** Removes `const`, `volatile`, `&`, `*`.
*   **Templating:** Translates `std::vector<T>` to `MutableSequence[T]` based on config rules.

## 3. Development Guidelines

### 3.1. Setting up the Environment

```bash
# Install dependencies
uv sync

# Activate virtual environment
source .venv/bin/activate
```

### 3.2. Running Tests

We rely on a snapshot of QuantLib interface files located in `tests/data/quantlib-1.40`.

```bash
# Run all tests
pytest

# Run a specific functional test (checking SWIG integration)
swig2pyi tests/data/quantlib-1.40/quantlib.i --config src/swig2pyi/rules/quantlib.json
```

### 3.3. Adding New Features

1.  **New SWIG Directive Support:**
    *   If `swig -xml` fails on a new directive, add a silencing macro to `SwigRunner`'s preamble or improve the `mocks/` to handle it if it's essential for type info.
2.  **New Type Rules:**
    *   Update `TypeManager` logic and add the rule to `quantlib.json` (or the relevant config).

### 3.4. Known Limitations

*   **Complex Templates:** Nested template parsing is currently rudimentary.
*   **Directives:** Directives that rely on Python runtime logic (`%pythoncode`) are currently ignored/silenced to allow XML generation. Future work may involve parsing these blocks separately if they contain type info.

## 4. Contribution

See `CONTRIBUTING.md` for details on how to submit PRs.