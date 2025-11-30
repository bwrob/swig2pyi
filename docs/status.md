# Project Status - Swig2Pyi Refactor

**Date:** November 30, 2025
**Status:** Operational. Major refactor to XML-based pipeline is complete and validated against QuantLib subset.

## Achievements

### 1. Architecture Complete
The "Universal Pipeline" described in `GUIDELINES.md` is fully implemented:
*   **SWIG Runner:** Successfully executes `swig -xml` with injected mocks and preamble to bypass Python-specific directive errors.
*   **XML Parser:** Robustly parses SWIG 4.x XML output, handling:
    *   Classes, Structs, Unions.
    *   Inheritance (`baselist`).
    *   Methods (`cdecl` with `kind="function"`), Constructors, Destructors.
    *   Nested Enums and Global Enums.
    *   Correctly handles complex nesting of parameters (e.g., `parm` inside `attributelist`).
*   **Type System:**
    *   Configuration-driven mapping (`quantlib.json`).
    *   Regex-based smart pointer unwrapping.
    *   Container mapping (`std::vector` -> `MutableSequence`).
    *   Namespace resolution and stripping (e.g., `QuantLib::Date` -> `Date`).
    *   Typedef handling via direct type mapping aliases.
*   **Stub Emitter:**
    *   Emits valid Python 3 code with type hints.
    *   Handles Overloads via `@overload`.
    *   Groups methods and constructors.
    *   Emits Enums as `int` subclasses.
    *   Handles inheritance.

### 2. Integration Verified
*   Validated against a significant subset of QuantLib 1.40 interfaces (`ql_mini.i` extended).
*   **Test Coverage:** 13 passing tests covering:
    *   Parser edge cases (nested lists, overloads).
    *   Type normalization.
    *   Enum parsing and emission.
    *   Full integration test generating `quantlib_mini.pyi`.

## Current Capabilities
The tool can now generate high-quality `.pyi` stubs for complex C++ libraries exposed via SWIG, supporting:
*   **Smart Pointers:** Automatically unwraps `boost::shared_ptr` etc.
*   **STL Containers:** Maps `std::vector` to `MutableSequence`, `std::set` to `AbstractSet`.
*   **Operator Overloading:** Renames C++ operators (`operator+`) to Python dunder methods (`__add__`).
*   **Enum Classes:** Emits Python enums compatible with pybind11/SWIG runtime behavior.
*   **Inheritance:** Preserves class hierarchy in Python stubs.

## Next Steps / Roadmap
1.  **Full Library Test:** Run against the *complete* QuantLib interface (not just the mini subset) to identify any remaining edge cases.
2.  **Docstrings:** Extract docstrings from SWIG comments or `%feature("docstring")` (if available in XML) and emit them.
3.  **Template Expansion:** Improve handling of template instantiations that might be implicit or require `%template` directives.
4.  **Properties:** Detect public member variables (`kind="variable"`) and emit them as class attributes.