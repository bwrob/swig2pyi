# Project Guidelines for swig-pyi

This document outlines the development guidelines, project practices, and contribution guide for the `swig-pyi` project.

## 1. Project Overview

`swig-pyi` is a command-line tool written in Python to generate Python typing stubs (`.pyi`) from SWIG interface files (`.i`).

### 1.1. Tech Stack & Tooling

*   **Language:** Python (versions 3.10-3.14)
*   **Package Management:** `uv`
*   **Task Runner:** `poethepoet`
*   **Testing:** `pytest`
*   **Linting & Formatting:** `ruff`
*   **Type Checking:** `basedpyright`
*   **Documentation:** `mkdocs`
*   **Dependency Analysis:** `tach`

### 1.2. Motivation

The primary motivation for this project is to automate the generation of fully annotated Python wrappers, specifically for libraries like Quantlib, which utilize SWIG. The goal is to provide a deterministic and programmable solution for generating `.pyi` stubs, moving beyond manual or AI-assisted methods (like Copilot-generated stubs) to integrate this process directly into a development workflow.

## 2. Core Functionality

This section details the expected behavior and features of `swig-pyi`.

1.  **Input:**
    The `swig-pyi` command should accept:
    *   A single `.i` file path.
    *   A directory path, in which case `.i` files within that directory (and potentially subdirectories, if recursive discovery is enabled) should be processed.
    *   All included files (via SWIG's `%include` directive) should be taken into account and processed as part of the input.
    *   Optionally, a list of specific class and/or function names can be provided. In this scenario, only those named objects and any other objects recursively required for their type definitions should be processed to generate stubs.

2.  **Output:**
    The expected output is a single `.pyi` file. This single file is intended to serve as a consolidated stub for an entire module, such as an `__init__.pyi` file, which would provide typing information for an unannotated SWIG-wrapped Python library (e.g., `__init__.py` importing from the SWIG-generated module).
    The generated `.pyi` file should be placed in a user-specified output directory or printed to standard output.

3.  **SWIG Features:**
    Based on the analysis of QuantLib-SWIG interface files, the `swig-pyi` tool should support the following SWIG features and address their implications for Python type hint generation:
    *   **Core Directives:**
        *   `%module`: For defining the module name.
        *   `%include`: To handle included interface files and their definitions.
        *   `%shared_ptr`: To correctly represent C++ `std::shared_ptr` (or aliased versions like `ext::shared_ptr`) as their Python equivalent with proper type hints (e.g., indicating non-nullable types or custom smart pointer wrappers).
        *   `%template`: To generate type hints for specific instantiations of C++ template classes (e.g., `std::vector<int>` -> `list[int]`, `Handle<T>` -> `Handle[T_co]`).
        *   `%extend`: To generate type hints for methods, properties, and constructors added to Python-wrapped classes via `%extend` blocks.
        *   `%feature("kwargs")`: To reflect the ability to call constructors/methods with keyword arguments in the type hints.
        *   `%feature("director")`: To generate correct type hints for Python classes that act as directors, inheriting from C++ base classes and overriding virtual methods. This requires representing Python-side implementations of C++ abstract interfaces.
        *   `%pythoncode`: To parse and understand raw Python code injected into the wrappers, especially for factory functions that dynamically create templated classes.
        *   `%typemap`: To interpret and generate type hints based on custom type conversions defined by `typemap` directives (e.g., `ext::optional<T>` to `Optional[T]`, `Array` to `list`).
        *   `%rename`: To correctly map the C++ names to their Python-renamed counterparts in the type stubs.
        *   `%define`: To understand and expand SWIG macros, as they encapsulate reusable wrapping patterns.

    *   **Wrapped C++ Features:**
        *   **Templates:** Support for various template instantiations, including STL containers (`std::vector`, `std::pair`) and custom library templates.
        *   **Smart Pointers:** Accurate typing for objects managed by `shared_ptr`.
        *   **Operator Overloading:** Proper representation of overloaded operators (`operator()`, arithmetic, comparison) as Python methods.
        *   **STL and Custom Containers:** Correctly map C++ containers to their Python type hint equivalents.
        *   **Callbacks/Delegates:** Type hints for Python callable objects used as callbacks for C++ functions/methods via directors.

    *   **Implications for `swig-pyi`:**
        Generating accurate type hints will require `swig-pyi` to:
        *   Perform robust parsing of `.i` files to extract all relevant SWIG directives and their arguments.
        *   Understand the C++ type system and how SWIG maps it to Python.
        *   Be able to follow `%include` chains and resolve type dependencies across multiple files.
        *   Interpret and apply `typemap` rules to transform C++ types into Python type hints.
        *   Handle the dynamic nature of `%extend` and `%pythoncode` to correctly infer types for added Python functionality.
        *   Address the complexities introduced by directors and template instantiations to provide precise type annotations.

## 3. Development Guidelines

This section outlines the coding style, architectural principles, testing strategy, and other development practices for `swig-pyi`.

### 3.1. Coding Style & Architecture

*   **Style:** The coding style should be modern and functional, adhering strictly to the rules defined by `ruff` for formatting/linting and `pyright` for type checking.
*   **Type Annotations:** All code must be fully and strictly type-annotated.
*   **Constants:** Avoid hard-coded values within the code. Instead, use top-level constants or dedicated configuration modules.
*   **Architecture:** The project should follow a clear, layered architecture to ensure separation of concerns and extensibility:
    1.  **Helpers/Backend:** Common utilities and core logic for parsing SWIG files and generating stub content.
    2.  **Execution Loop:** The main application logic that orchestrates the parsing, generation, and output processes.
    3.  **Interface:** The command-line interface (CLI) that interacts with the user.
*   **Extensibility:** The design must be modern and easy to extend, allowing for the addition of new SWIG functionality coverage in the future.

### 3.2. Testing

*   **Framework:** Use `pytest` for all unit and functional testing.
*   **Style:** Tests should be written in a functional style (no test classes), leveraging `pytest` features like fixtures and parametrization.
*   **Scope:** The project should have extensive test coverage to ensure correctness and stability.
*   **Testing Ground:**
    *   The initial development and testing will be performed against the SWIG interface files of **QuantLib version 1.40**.
    *   The long-term goal is to ensure compatibility with all QuantLib versions from **1.30 to 1.40**.

### 3.3. Documentation

*   **Framework:** Project documentation will be created and maintained using `mkdocs`.

### 3.4. Dependency Management

*   **Tooling:** Use `uv` for all dependency management and package building tasks.
*   **Dependency Range:** The project should aim to minimize its dependency range.
*   **Python Version:**
    *   The `swig-pyi` tool itself should be written for **Python 3.12+**.
    *   The generated type annotations (`.pyi` files) must be compliant with **Python 3.10+**.

### 3.5. Branching and Pull Requests

*   **Branching Model:** The project will follow a trunk-based development model, with the `main` branch serving as the single source of truth.
*   **Pull Requests (PRs):**
    *   All changes must be submitted via a pull request.
    *   PRs must pass all continuous integration (CI) checks before they can be merged.
    *   The existing GitHub workflow in `.github/workflows` should be reviewed and improved to ensure robust CI.

## 4. Contribution & Community

This project is open to contributions from the community.

### 4.1. Contributor Guidelines

All contributions are welcome, from bug reports to pull requests. For detailed information on how to contribute, please see the [CONTRIBUTING.md](https://github.com/bwrob/swig-pyi/blob/main/CONTRIBUTING.md) file.

Key guidelines include:
*   Follow the project's [Code of Conduct](https://github.com/bwrob/swig-pyi/blob/main/CODE_OF_CONDUCT.md).
*   Use the issue tracker to report bugs and suggest enhancements.
*   Submit pull requests with clear descriptions of the changes.
*   Follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification for commit messages.

### 4.2. Code of Conduct

All participants in the `swig-pyi` community are expected to adhere to the [Contributor Covenant Code of Conduct](https://github.com/bwrob/swig-pyi/blob/main/CODE_OF_CONDUCT.md). Please read the full text to understand what actions will and will not be tolerated.