# swig2pyi: Future Tasks

This document tracks remaining future tasks and long-term goals for `swig2pyi`.

## 1. Active Tasks (Working On)
- [x] **Component G: Explicit Import Tracking [Priority: High]:** Track required imports dynamically in `StubEmitter` and `TypeManager` during stub generation, removing the heuristic post-emission regex scans.
- [x] **Component H: Type Cleaning Unification [Priority: High]:** Unify C++ type sanitization and cleaning logic, centralizing it inside `TypeManager`.
- [x] **QA: Strict Type Validation [Priority: High]:** Run `basedpyright` in strict mode against real QuantLib Python tests and iteratively resolve emitter gaps.
- [x] **QA: Full QuantLib Verification [Priority: High]:** Achieve zero type-checking errors on all 50+ QuantLib Python test files using the generated stubs.
- [x] **QA: Verify Multi-Library Portability [Priority: High]:** Execute `swig2pyi` on at least 2 additional, non-QuantLib SWIG interface examples (e.g., GDAL or standard SWIG examples) and verify zero `basedpyright` errors in generated stubs.
- [x] **Component runner: Optimize SWIG Dependency Hashing [Priority: High]:** Delegate include dependencies tracking directly to `swig -MM` rather than recursively walking include directories with `os.walk` to avoid hangs/OOM on system/vendor paths.
  * **Acceptance Criteria:**
    - [x] `os.walk` include dependency walking code is deleted from `runner.py`.
    - [x] Execution command executes `swig -MM` with include/preprocessor flags via `subprocess`.
    - [x] Hashing reads only the exact file dependencies returned by `swig -MM`.
    - [x] Hashing an include path with thousands of unreferenced files executes in under 100ms.
- [x] **Component parser: Transition AST to Dataclasses [Priority: Medium]:** Migrate AST models from Pydantic `BaseModel` to standard Python `@dataclass(slots=True)` to dramatically optimize memory footprints and parse speeds for large SWIG XML inputs.
  * **Acceptance Criteria:**
    - [x] No AST models in `ast_models.py` inherit from Pydantic `BaseModel`.
    - [x] Dataclasses utilize `slots=True` to minimize object memory footprint.
    - [x] Memory consumption and XML parser instantiation speed demonstrate measurable improvements.
    - [x] Strict type safety of the AST is verified by `basedpyright`.
- [x] **Component qa: Stabilize Live Coverage Check [Priority: Low]:** Refactor dynamic wrapper importing and metadata checking in `StubCoverageChecker` to run in a safe sandbox or inspect modules via `inspect` to handle runtime failures and false positives gracefully.
  * **Acceptance Criteria:**
    - [x] `ImportError` during dynamic imports is caught and printed as a clear warning without crashing or silent exit.
    - [x] Non-native imported symbols are filtered out from coverage calculations (using module checks or `__file__`).
- [x] **Component cli: Enhance CLI Diagnostics and Logging [Priority: High]:** Prevent silent CLI exits on invalid configurations, missing input files, or validation errors, and display missing symbol lists in the `coverage` command instead of calling `pass`.
  * **Acceptance Criteria:**
    - [x] Error messages for invalid JSON configurations or missing input files are written to `sys.stderr` before exit.
    - [x] Missing symbols are printed to standard output/error during the coverage check rather than being skipped with `pass`.
    - [x] Integration tests verify CLI output presence and correct exit code propagation.
- [x] **Component runner/naming: Unification & Deduplication of Runner and NameManager [Priority: Medium]:** Eliminate duplicate wrapper file generation logic and path resolution in `runner.py`, and promote set/dict lookups in `naming.py` to class/module-level constants to avoid allocation overhead.
  * **Acceptance Criteria:**
    - [x] `_write_temp_wrapper` is deleted and unified into `_create_wrapper` in `runner.py`.
    - [x] `_build_command` uses `_get_swig_exe` for SWIG path resolution instead of repeating the logic.
    - [x] `reserved` set and `mapping` dict in `naming.py` are converted to class/module-level constants.
    - [x] All code quality and pytest checks pass.
- [x] **Component runner: Robust User Cache Directory Fallback [Priority: Medium]:** Refactor caching directory resolution in `runner.py` to use a standard user cache path instead of a fragile relative parent walk-up which fails when installed as a package.
  * **Acceptance Criteria:**
    - [x] Caching logic resolves to an OS-appropriate user cache directory (e.g. `~/.cache/swig2pyi/`) or standard system temp folder fallback.
    - [x] Project walk-up `.temp/` caching path fallback is removed or gracefully ignored if unwriteable without warnings.
    - [x] Test suite verifies successful compilation caching.
- [x] **Component parser/type_system: Automated Typedef Mapping [Priority: Medium]:** Parse `<typedef>` elements directly from the SWIG XML in `SwigXmlParser` to build a dynamic typedef type map, reducing the need for manual configuration JSON mapping overrides.
  * **Acceptance Criteria:**
    - [x] `SwigXmlParser` parses `<typedef>` XML elements and registers them in the AST or TypeManager.
    - [x] `TypeManager` dynamically resolves typedefs from the parsed map during type normalization.
    - [x] Complex typedef configurations in test files are resolved automatically without requiring `type_map` config overrides.
    - [x] No regressions in typing and unit/integration tests.




## 2. Future Tasks (Next Steps)
- [x] **Architecture: Generalize Assumptions [Priority: Medium]:** Re-review the codebase to identify any hardcoded library-specific assumptions (e.g. QuantLib's `Handle` proxy templates or GDAL's OSR patterns) and extract them into configurable rules.
- [x] **Type System: Type Mapping Refinement [Priority: Medium]:** Improve the mapping of C++ templates like `std::vector<T>` to `list[T]` and `Handle<T>` to `Handle[T]`.
- [x] **Type System: Nested Template Resolution [Priority: Medium]:** Enhance the `TypeManager` to handle complex nested templates (e.g. `std::vector<std::vector<std::shared_ptr<T>>>`) and custom template argument resolvers.
- [x] **CLI: Stub Coverage Command [Priority: Low]:** Expose the coverage-checking logic as a first-class CLI command (e.g., `swig2pyi coverage --stub QuantLib.pyi --module QuantLib`).
- [x] **CI: Dynamic CI Integrations [Priority: Low]:** Extend GitHub Actions to build and verify GDAL OSR stubs dynamically in addition to QuantLib.
- [x] **Research: Analyze SWIG Specifications [Priority: Medium]:** Download SWIG documentation to `.temp/`, review C++ mapping specifications, identify gaps or divergence in current parser/emitter features, and plan/implement coverage for them.
- [x] **Type System: Const to Final Mapping [Priority: Low]:** Map C++ `const` variables and public member variables to Python `Final[T]` type annotations to preserve C++ immutability semantics.
- [x] **Type System: Emulate SWIG cvar Object [Priority: Medium]:** Generate a `cvar` class and module-level `cvar` instance in stubs to support access to C++ global and static variables.

## 3. Package Release & Quality Tasks
- [x] **QA: Literal Code Coverage Target [Priority: Medium]:** Run `uv run poe coverage` and ensure the code coverage for the `swig2pyi` codebase meets or exceeds 90%.
- [x] **Packaging: Repository Cleanup & Presentability [Priority: Medium]:** Verify the documentation structure, ensure README matches the tool's final API, and check dependency configurations.
- [x] **Packaging: PyPI Publishing [Priority: Medium]:** Perform a TestPyPI deployment verification, followed by publishing the first official release to PyPI.

## 4. Engineering Standards
* **TDD:** Every fix for a type-check error must be accompanied by a small unit test or a verified change in the generated QuantLib stub.
* **Code Quality:** Ensure all changes pass `uv run poe code-quality` before committing.
* **Project Documentation:** Update all relevant project tracking files in `.project/` (such as `plan.md` to check off tasks, `achievements.md` to record completed deliverables, and `design.md` if the architecture changes) after finishing each task.
