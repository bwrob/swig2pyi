# Project Status - Swig2Pyi Refactor

**Date:** December 4, 2025
**Status:** Operational & Validated. Full QuantLib generation successful. Type system significantly hardened.

## Achievements

### 1. Architecture Complete
The "Universal Pipeline" described in `GUIDELINES.md` is fully implemented:
*   **SWIG Runner:** Successfully executes `swig -xml` with injected mocks and preamble to bypass Python-specific directive errors.
*   **XML Parser:** Robustly parses SWIG 4.x XML output, handling classes, methods, enums, and inheritance.
*   **Type System:** Configuration-driven mapping (`quantlib.json`) with smart pointer unwrapping and container mapping.
*   **Stub Emitter:** Emits Python 3 code with type hints, overloads, and sanitized parameter names.

### 2. Integration Verified (Updated)
*   **Full QuantLib Suite:** Successfully generated stubs for the entire `quantlib.i` interface (approx. 33k lines of stubs).
*   **Type Checker Validation:** Generated stubs passed manual `pyright` (strict mode) validation for core usage patterns.
*   **Test Coverage:** Integration tests updated to run against the full QuantLib library. New unit tests added for inheritance logic and enum typing.

### 3. Feature Enhancements (New)
*   **Handle/RelinkableHandle Support:** Implemented sophisticated inheritance logic. `Handle[T]` now inherits from `T`, exposing wrapped methods to type checkers (e.g., `YieldTermStructureHandle` exposes `discount()`).
*   **IntEnum Support:** Enums now inherit from `enum.IntEnum` instead of `int`, ensuring better semantic correctness and type safety.
*   **PEP 561 Compliance:** Output structure adjusted to `QuantLib/__init__.pyi` for automatic stub discovery by type checkers.

## Known Issues
*   **Parameter Name Sanitation:** The `yield` keyword and other Python reserved words need consistent sanitation (Mostly addressed, but needs monitoring).
*   **Complex Templates:** Some deeply nested templates might still require manual mapping, though coverage is good.

## Roadmap

This roadmap outlines the prioritized steps for further development.

1.  **CLI & API Separation + Direct XML Input (Next):**
    *   **Objective:** Refactor `main.py` into `swig2pyi.api` and `swig2pyi.cli`. Implement "Direct XML Input" mode to bypass `swig` execution if XML is pre-generated.
    *   **Action:** 
        *   Create `src/swig2pyi/cli.py` and `src/swig2pyi/api.py`.
        *   Add `--xml-input` flag to CLI.
        *   Document usage.

2.  **QA Integration (Formalize):**
    *   **Objective:** Ensure generated `.pyi` files conform to Python coding standards and type-checking rules automatically.
    *   **Action:** Implement a `QAValidator` class or module. This component will run `ruff` (for linting and formatting) and `basedpyright` (for strict type checking) on generated `.pyi` files. The generation process should fail or emit clear warnings if validation checks are not passed.

3.  **Enhancements:**
    *   **Docstrings:** Extract and emit docstrings from SWIG comments into the `.pyi` files for improved code clarity.
    *   **Properties:** Detect and correctly emit public member variables as properties in the generated stubs.
