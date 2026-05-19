# swig2pyi: Development & Refactoring Plan

## 1. Current Progress (Completed)
- [x] **SQLite/SQLModel Parser:** Implemented SAX streaming parser that avoids memory exhaustion on massive XML (2GB+).
- [x] **Static Methods:** Added support for `@staticmethod` detection and signature formatting.
- [x] **Global Enum Exports:** Enums now export their members to the module level to match SWIG's Python behavior.
- [x] **Property Detection:** Automatically convert `getFoo`/`setFoo` pairs into Python `@property` blocks.
- [x] **Symbol Resolution:** Fixed parser to prefer `sym_name` to ensure correct Python-side naming.

## 2. Active Tasks (Working On)
- [ ] **Type Mapping Refinement:** Improving the mapping of C++ templates like `std::vector<T>` to `list[T]` and `Handle<T>` to `Handle[T]`.
- [ ] **Strict Type Validation:** Running `basedpyright` in strict mode against real QuantLib Python tests and iteratively fixing emitter gaps.
- [x] **Member Variable Properties:** Mapping public member variables (not just get/set pairs) to properties.

## 3. Remaining Tasks (Next Steps)
- [x] **Docstring Extraction:** Extract SWIG-generated docstrings from XML and emit them into the `.pyi` stubs.
- [x] **Code Quality Overhaul:**
    - Fix all `ruff` linting errors in the generator codebase.
    - Resolve major `basedpyright` strict-mode errors in the generator codebase.
- [x] **Refactoring for Elegance:**
    - Clean up `parser.py` (split into modular components: `ast_models.py`, `ingestion.py`, `builder.py`).
    - [x] Modularize `emitter.py` signature and formatting logic (into `naming.py` and `signature.py`).
    - [ ] Decouple the `TypeManager` from hardcoded QuantLib rules where possible.
- [ ] **Full QuantLib Verification:** Achieve "Zero Errors" on all 50+ QuantLib Python test files using the generated stubs.

## 4. Engineering Standards
- **TDD:** Every fix for a type-check error must be accompanied by a small unit test or a verified change in the generated QuantLib stub.
- **YOLO Mode Efficiency:** Commit often, validate against `ruff` and `pyright` every few turns.
