# swig2pyi: Future Development Plan

This plan tracks remaining future tasks and long-term goals for `swig2pyi`.

## 1. Active Tasks (Working On)
- [ ] **Component G: Explicit Import Tracking:** Track required imports dynamically in `StubEmitter` and `TypeManager` during stub generation, removing the heuristic post-emission regex scans.
- [ ] **Component H: Type Cleaning Unification:** Unify C++ type sanitization and cleaning logic, centralizing it inside `TypeManager`.

## 2. Future Tasks (Next Steps)
- [ ] **Type Mapping Refinement:** Improve the mapping of C++ templates like `std::vector<T>` to `list[T]` and `Handle<T>` to `Handle[T]`.
- [ ] **Strict Type Validation:** Run `basedpyright` in strict mode against real QuantLib Python tests and iteratively resolve emitter gaps.
- [ ] **Full QuantLib Verification:** Achieve zero type-checking errors on all 50+ QuantLib Python test files using the generated stubs.
- [ ] **Nested Template Resolution:** Enhance the `TypeManager` to handle complex nested templates (e.g. `std::vector<std::vector<std::shared_ptr<T>>>`) and custom template argument resolvers.
- [ ] **Stub Coverage Command:** Expose the coverage-checking logic as a first-class CLI command (e.g., `swig2pyi coverage --stub QuantLib.pyi --module QuantLib`).
- [ ] **Dynamic CI Integrations:** Extend GitHub Actions to build and verify GDAL OSR stubs dynamically in addition to QuantLib.

## 3. Package Release & Quality Goals
- [ ] **Literal Code Coverage Target:** Run `uv run poe coverage` and ensure the code coverage for the `swig2pyi` codebase meets or exceeds 90%.
- [ ] **Repository Cleanup & Presentability:** Verify the documentation structure, ensure README matches the tool's final API, and check dependency configurations.
- [ ] **PyPI Publishing:** Perform a TestPyPI deployment verification, followed by publishing the first official release to PyPI.

## 4. Engineering Standards
* **TDD:** Every fix for a type-check error must be accompanied by a small unit test or a verified change in the generated QuantLib stub.
* **Code Quality:** Ensure all changes pass `uv run poe code-quality` before committing.
