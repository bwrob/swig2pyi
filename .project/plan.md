# swig2pyi: Future Tasks

This document tracks remaining future tasks and long-term goals for `swig2pyi`.

## 1. Active Tasks (Working On)
- [x] **Component G: Explicit Import Tracking [Priority: High]:** Track required imports dynamically in `StubEmitter` and `TypeManager` during stub generation, removing the heuristic post-emission regex scans.
- [x] **Component H: Type Cleaning Unification [Priority: High]:** Unify C++ type sanitization and cleaning logic, centralizing it inside `TypeManager`.
- [x] **QA: Strict Type Validation [Priority: High]:** Run `basedpyright` in strict mode against real QuantLib Python tests and iteratively resolve emitter gaps.
- [x] **QA: Full QuantLib Verification [Priority: High]:** Achieve zero type-checking errors on all 50+ QuantLib Python test files using the generated stubs.
- [x] **QA: Verify Multi-Library Portability [Priority: High]:** Execute `swig2pyi` on at least 2 additional, non-QuantLib SWIG interface examples (e.g., GDAL or standard SWIG examples) and verify zero `basedpyright` errors in generated stubs.

## 2. Future Tasks (Next Steps)
- [x] **Architecture: Generalize Assumptions [Priority: Medium]:** Re-review the codebase to identify any hardcoded library-specific assumptions (e.g. QuantLib's `Handle` proxy templates or GDAL's OSR patterns) and extract them into configurable rules.
- [x] **Type System: Type Mapping Refinement [Priority: Medium]:** Improve the mapping of C++ templates like `std::vector<T>` to `list[T]` and `Handle<T>` to `Handle[T]`.
- [x] **Type System: Nested Template Resolution [Priority: Medium]:** Enhance the `TypeManager` to handle complex nested templates (e.g. `std::vector<std::vector<std::shared_ptr<T>>>`) and custom template argument resolvers.
- [x] **CLI: Stub Coverage Command [Priority: Low]:** Expose the coverage-checking logic as a first-class CLI command (e.g., `swig2pyi coverage --stub QuantLib.pyi --module QuantLib`).
- [ ] **CI: Dynamic CI Integrations [Priority: Low]:** Extend GitHub Actions to build and verify GDAL OSR stubs dynamically in addition to QuantLib.
- [x] **Research: Analyze SWIG Specifications [Priority: Medium]:** Download SWIG documentation to `.temp/`, review C++ mapping specifications, identify gaps or divergence in current parser/emitter features, and plan/implement coverage for them.
- [x] **Type System: Const to Final Mapping [Priority: Low]:** Map C++ `const` variables and public member variables to Python `Final[T]` type annotations to preserve C++ immutability semantics.
- [ ] **Type System: Emulate SWIG cvar Object [Priority: Medium]:** Generate a `cvar` class and module-level `cvar` instance in stubs to support access to C++ global and static variables.

## 3. Package Release & Quality Tasks
- [x] **QA: Literal Code Coverage Target [Priority: Medium]:** Run `uv run poe coverage` and ensure the code coverage for the `swig2pyi` codebase meets or exceeds 90%.
- [ ] **Packaging: Repository Cleanup & Presentability [Priority: Medium]:** Verify the documentation structure, ensure README matches the tool's final API, and check dependency configurations.
- [ ] **Packaging: PyPI Publishing [Priority: Medium]:** Perform a TestPyPI deployment verification, followed by publishing the first official release to PyPI.

## 4. Engineering Standards
* **TDD:** Every fix for a type-check error must be accompanied by a small unit test or a verified change in the generated QuantLib stub.
* **Code Quality:** Ensure all changes pass `uv run poe code-quality` before committing.
* **Project Documentation:** Update all relevant project tracking files in `.project/` (such as `plan.md` to check off tasks, `achievements.md` to record completed deliverables, and `design.md` if the architecture changes) after finishing each task.
