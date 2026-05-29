# swig2pyi: Future Tasks

This document tracks remaining future tasks and long-term goals for `swig2pyi`.

## 1. Active Tasks (Working On)
- [ ] **Component G: Explicit Import Tracking:** Track required imports dynamically in `StubEmitter` and `TypeManager` during stub generation, removing the heuristic post-emission regex scans.
- [ ] **Component H: Type Cleaning Unification:** Unify C++ type sanitization and cleaning logic, centralizing it inside `TypeManager`.

## 2. Future Tasks (Next Steps)
- [ ] **Architecture: Generalize Assumptions:** Re-review the codebase to identify any hardcoded library-specific assumptions (e.g. QuantLib's `Handle` proxy templates or GDAL's OSR patterns) and extract them into configurable rules.
- [ ] **Type System: Type Mapping Refinement:** Improve the mapping of C++ templates like `std::vector<T>` to `list[T]` and `Handle<T>` to `Handle[T]`.
- [ ] **QA: Strict Type Validation:** Run `basedpyright` in strict mode against real QuantLib Python tests and iteratively resolve emitter gaps.
- [ ] **QA: Full QuantLib Verification:** Achieve zero type-checking errors on all 50+ QuantLib Python test files using the generated stubs.
- [ ] **Type System: Nested Template Resolution:** Enhance the `TypeManager` to handle complex nested templates (e.g. `std::vector<std::vector<std::shared_ptr<T>>>`) and custom template argument resolvers.
- [ ] **CLI: Stub Coverage Command:** Expose the coverage-checking logic as a first-class CLI command (e.g., `swig2pyi coverage --stub QuantLib.pyi --module QuantLib`).
- [ ] **CI: Dynamic CI Integrations:** Extend GitHub Actions to build and verify GDAL OSR stubs dynamically in addition to QuantLib.
- [ ] **QA: Verify Multi-Library Portability:** Execute `swig2pyi` on at least 2 additional, non-QuantLib SWIG interface examples (e.g., GDAL or standard SWIG examples) and verify zero `basedpyright` errors in generated stubs.
- [ ] **Research: Analyze SWIG Specifications:** Download SWIG documentation to `.temp/`, review C++ mapping specifications, identify gaps or divergence in current parser/emitter features, and plan/implement coverage for them.



## 3. Package Release & Quality Tasks
- [ ] **QA: Literal Code Coverage Target:** Run `uv run poe coverage` and ensure the code coverage for the `swig2pyi` codebase meets or exceeds 90%.
- [ ] **Packaging: Repository Cleanup & Presentability:** Verify the documentation structure, ensure README matches the tool's final API, and check dependency configurations.
- [ ] **Packaging: PyPI Publishing:** Perform a TestPyPI deployment verification, followed by publishing the first official release to PyPI.

## 4. Engineering Standards
* **TDD:** Every fix for a type-check error must be accompanied by a small unit test or a verified change in the generated QuantLib stub.
* **Code Quality:** Ensure all changes pass `uv run poe code-quality` before committing.
