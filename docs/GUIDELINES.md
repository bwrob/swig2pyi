# Project Guidelines for swig2pyi

This document outlines the development guidelines, project practices, and architectural decisions for the `swig2pyi` project.

## 1. Project Overview

`swig2pyi` is a tool designed to generate high-quality Python typing stubs (`.pyi`) from SWIG interface files (`.i`).

### 1.1. Core Philosophy: "Universal Pipeline"

`swig2pyi` leverages SWIG itself to produce an intermediate representation (XML), converting the parsing problem into a data transformation problem.

**The Pipeline:**
1.  **Input Source:**
    *   *Standard Mode:* `.i` file -> `SwigRunner` executes `swig -xml`.
    *   *XML Mode:* Pre-existing `.xml` file -> Bypasses SWIG execution.
2.  **Middle-End (Normalization):** Parse the XML stream (SAX) and persist nodes to a temporary SQLite database using `sqlmodel`. This solves memory exhaustion on massive XML trees. Normalize C++ types to Python types using `TypeManager`.
3.  **Backend (Emission):** Query the database to construct an AST and emit valid, idiomatic Python type stubs (`.pyi`).
4.  **Verification:** Generated stubs must be valid Python syntax and strictly typed.

### 1.2. Tech Stack & Tooling

*   **Language:** Python 3.12+
*   **Package Management:** `uv`
*   **Core Dependencies:** `swig` (Python wrapper), `sqlmodel`.
*   **Testing:** `pytest`.
*   **Linting/Types:** `ruff` & `basedpyright`.

## 2. Architectural Components

### 2.1. The Configuration (`config.json`)
Driven by configuration to avoid hardcoded library rules. Includes module name, includes, type maps, smart pointers, and container mappings.

### 2.2. The API & CLI (`swig2pyi.api`, `swig2pyi.cli`)
*   **API:** A programmatic interface for integrating `swig2pyi` into other Python build tools.
*   **CLI:** A command-line wrapper around the API.
*   **Documentation:** Both must be fully documented.

### 2.3. The Runner (`SwigRunner`)
Executes `swig -xml -DSWIGPYTHON`. Injects mocks and preambles to silence errors caused by the lack of full Python runtime libraries during XML generation.

### 2.4. The Parser (`SwigXmlParser` & `sqlmodel`)
SAX streams the SWIG XML into a temporary SQLite database. The schema is defined declaratively using `sqlmodel` to ensure type safety. AST queries resolve relationships (inheritance, templates) from the DB.

### 2.5. The Type System (`TypeManager`)
Translates C++ types to Python types (unwrapping smart pointers, resolving typedefs, mapping templates).

## 3. Development Guidelines

### 3.1. Generated Code Standards
The generated `.pyi` files are **first-class citizens**. They must:
1.  **Pass `ruff`:** No syntax errors, undefined names, or unused imports.
2.  **Pass `basedpyright`:** Correct type variance, valid overrides, and resolvable imports.

### 3.2. Setting up the Environment
```bash
uv sync
source .venv/bin/activate
```

### 3.3. Running Tests
```bash
pytest
# Functional test
swig2pyi tests/data/quantlib-1.40/quantlib.i --config src/swig2pyi/rules/quantlib.json
```

### 3.4. Adding New Features
*   **New Directives:** Add silencing macros to `SwigRunner` if `swig -xml` fails.
*   **New Type Rules:** Update `TypeManager` and `quantlib.json`.

## 4. Contribution
See `CONTRIBUTING.md`.
