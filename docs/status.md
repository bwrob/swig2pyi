# Project Status - Swig2Pyi Refactor

**Date:** December 1, 2025
**Status:** Operational. Major refactor to XML-based pipeline is complete. Focus shifting to robustness, usability, and code quality.

## Achievements

### 1. Architecture Complete
The "Universal Pipeline" described in `GUIDELINES.md` is fully implemented:
*   **SWIG Runner:** Successfully executes `swig -xml` with injected mocks and preamble to bypass Python-specific directive errors.
*   **XML Parser:** Robustly parses SWIG 4.x XML output, handling classes, methods, enums, and inheritance.
*   **Type System:** Configuration-driven mapping (`quantlib.json`) with smart pointer unwrapping and container mapping.
*   **Stub Emitter:** Emits Python 3 code with type hints, overloads, and sanitized parameter names.

### 2. Integration Verified
*   Validated against a significant subset of QuantLib 1.40 interfaces (`ql_mini.i` extended).
*   **Test Coverage:** 13 passing tests covering parser edge cases, type normalization, and integration.

## Known Issues
*   **Parameter Name Sanitation:** The `yield` keyword and other Python reserved words need consistent sanitation.
*   **Complex Templates:** Some complex template types might still require manual mapping.

## Roadmap

This roadmap outlines the prioritized steps for further development, addressing newly identified requirements and enhancing the tool's robustness and usability.

1.  **QA Integration (High Priority):**
    *   **Objective:** Ensure generated `.pyi` files conform to Python coding standards and type-checking rules.
    *   **Action:** Implement a `QAValidator` class or module. This component will run `ruff` (for linting and formatting) and `basedpyright` (for strict type checking) on generated `.pyi` files. The generation process should fail or emit clear warnings if validation checks are not passed.
2.  **Full Library Stress Test (High Priority):**
    *   **Objective:** Identify and resolve all remaining parsing errors, type resolution issues, and edge cases.
    *   **Action:** Run `swig2pyi` against the *entire* QuantLib interface (`quantlib.i`), not just the previously validated subset. This will serve as a comprehensive integration test.
3.  **CLI & API Separation with Documentation:**
    *   **Objective:** Provide both a clear programmatic API for integration into other tools and a user-friendly command-line interface, both thoroughly documented.
    *   **Action:** Refactor the existing `main.py` into distinct `swig2pyi.api` (for the programmatic interface) and `swig2pyi.cli` (for command-line parsing and execution) modules. This includes adding comprehensive Python docstrings for the API and detailed usage instructions for the CLI.
4.  **Direct XML Input Mode:**
    *   **Objective:** Enable the tool to process pre-generated SWIG XML files directly, decoupling the stub generation from the SWIG execution step.
    *   **Action:** Implement functionality to accept an `.xml` file as input, bypassing the `SwigRunner` component. This allows for greater flexibility in build pipelines.
5.  **Enhancements:**
    *   **Docstrings:** Extract and emit docstrings from SWIG comments into the `.pyi` files for improved code clarity.
    *   **Properties:** Detect and correctly emit public member variables as properties in the generated stubs.