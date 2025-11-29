# Progress Report - Swig2Pyi Refactor

**Date:** November 29, 2025
**Status:** Phase 2 Complete (Infrastructure & XML Generation), Phase 3 (Parsing) Blocked.

## Achievements
1.  **Architecture Pivot:** Successfully moved to a `swig -xml` based pipeline to avoid fragile regex parsing of `.i` files.
2.  **Infrastructure:**
    *   `SwigRunner`: Robustly handles SWIG execution. It injects custom "mocks" for standard libraries (like `std_vector.i`) and a preamble to bypass Python-backend specific directives (like `%pythoncode`) that cause `swig -xml` to fail.
    *   `Mocks`: Created minimal SWIG interface mocks in `src/swig2pyi/mocks` to satisfy `%include` dependencies without pulling in the full, incompatible SWIG standard library.
    *   `Config`: Implemented a configuration-driven approach (`quantlib.json`) to define type mappings and rules.
3.  **XML Generation:** The tool successfully generates valid XML from SWIG interface files.
    *   Test case `quantlib_mini.i` (subset of QuantLib) produces ~2.8MB of XML.

## Current Issue
The generated `.pyi` output is empty (containing only imports).

*   **Diagnosis:** The `SwigXmlParser` is failing to populate the Internal Representation (AST) from the generated XML.
*   **Root Cause:** The `iterparse` optimization in `src/swig2pyi/core/parser.py`, intended to handle large XML files efficiently, is likely incorrect. It is failing to correctly capture or attach `class` and `cdecl` nodes to the parent `Module` object. The `pydantic-xml` models might also need adjustment to match the exact attribute names produced by SWIG 4.x (e.g., `name` vs `sym_name`).
*   **Symptoms:** Input is a 2.8MB XML file, but the parsed `Top` object contains 0 classes and 0 functions, leading the `StubEmitter` to produce an empty file.

## Next Steps
1.  **Debug Parser Logic:**
    *   **Inspect XML:** Capture a snippet of the generated XML to verify the tag structure (e.g., are classes nested in `<module>` or `<namespace>`? SWIG XML structure can be deep).
    *   **Simplify Parsing:** Temporarily revert the complex `iterparse` logic in `SwigXmlParser` and load the "mini" XML entirely into memory. This will isolate whether the issue is the *streaming logic* or the *data model* (pydantic definitions).
    *   **Verify Data Model:** Ensure `pydantic-xml` models (`Class`, `CDecl`) align with the actual XML attributes (check for `kind`, `sym_name`, etc.).
2.  **Verify AST Population:** Add debug logging in `main.py` to print the count of parsed classes and functions before the emission step.
3.  **Refine Emitter:** Once the AST is populated, proceed to verify that `StubEmitter` and `TypeManager` correctly normalize C++ types to Python hints.
4.  **Testing:** Create unit tests for `SwigXmlParser` using small, controlled XML snippets to validate parsing logic independently of SWIG execution.
   