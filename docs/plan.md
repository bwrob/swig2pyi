# swig2pyi: Future Development Plan

This plan tracks remaining future tasks for `swig2pyi`.

## 1. Active Tasks (Working On)
- [ ] **Component G: Explicit Import Tracking:** Track required imports dynamically in `StubEmitter` and `TypeManager` during stub generation, removing the heuristic post-emission regex scans.
- [ ] **Component H: Type Cleaning Unification:** Unify C++ type sanitization and cleaning logic, centralizing it inside `TypeManager`.

## 2. Future Tasks (Next Steps)
- [ ] **Type Mapping Refinement:** Improve the mapping of C++ templates like `std::vector<T>` to `list[T]` and `Handle<T>` to `Handle[T]`.
- [ ] **Strict Type Validation:** Run `basedpyright` in strict mode against real QuantLib Python tests and iteratively resolve emitter gaps.
- [ ] **Full QuantLib Verification:** Achieve zero type-checking errors on all 50+ QuantLib Python test files using the generated stubs.

## 3. Engineering Standards
* **TDD:** Every fix for a type-check error must be accompanied by a small unit test or a verified change in the generated QuantLib stub.
* **Code Quality:** Ensure all changes pass `uv run poe code-quality` before committing.
