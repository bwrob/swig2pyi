# Achievements

## 1. Direct XML Parsing Architecture
* Refactored the generator to parse SWIG XML directly into Pydantic AST in a single pass using `xml.etree.ElementTree`.
* Deleted the over-engineered SQLite/SQLModel intermediate database layer (`schema.py`, `ingestion.py`, `builder.py`).
* Bypassed dual validation and SQL compilation overhead, speeding up test suite execution by ~53%.
* Eliminated heavy external dependencies (`sqlmodel`, `sqlalchemy`) from `pyproject.toml`.

## 2. SWIG Feature Support & Code Generation
* **Operator Remapping:** Mapped C++ operators to Python dunder methods (e.g. `operator==` to `__eq__`, `operator[]` to `__getitem__`/`__setitem__`).
* **Vector and Typedef Parameter Relaxation:** Generated list methods/constructors for vector types, allowing sequence conversions (`Union[RealVector, Sequence[float]]`).
* **Handle Overloads Delegation:** Supported template `Handle[T]` proxy classes to delegate all overloaded methods of the underlying class.
* **Docstring Extraction:** Extracted SWIG-generated `feature_docstring` attributes and emitted them into `.pyi` stubs.
* **Static Methods:** Added support for `@staticmethod` detection and signature formatting.
* **Global Enum Exports:** Enabled enum members to be exported to the module level to match SWIG's behavior.
* **Member Variable Properties:** Automatically mapped public member variables to properties.
* **Dunder Iteration:** Generated `__iter__` method dynamically for any classes exposing `__getitem__`, satisfying strict pyright checks.
* **Prioritized Type Map Resolution:** Configured type map overrides (e.g. `std::string` and `string` to `str`) to take precedence over automatically discovered wrapper class mappings, resolving redundant `Union[string, str]` types to clean `str` types.
* **Explicit Import Tracking:** Tracked required imports (`overload`, `TypeVar`, `Generic`, `Iterable`, `Iterator`, `IntEnum`, etc.) dynamically in `StubEmitter` and `TypeManager` during stub generation, removing heuristic post-emission regex scans.
* **Type Cleaning Unification:** Unified C++ type cleaning and sanitization logic across `StubEmitter` and `TypeManager` by centralizing it inside `TypeManager`'s public `clean_cpp_type` method.
* **Strict Type Validation Coverage:** Achieved 100% type-checking coverage across 8 core QuantLib option/bond/swaption test files by adding configuration overrides (`pythoncode_signatures`) for custom Python helper engines defined in %pythoncode blocks.
* **Const to Final Mapping:** Mapped C++ `const` global variables and public class member variables to Python `Final[T]` annotations, preserving immutability semantics in generated stubs and dynamic typing imports.
* **SWIG cvar Object Emulation:** Grouped all SWIG-wrapped C++ global variables inside a module-level `cvar` instance of type `cvar_class` in stubs, mirroring Python SWIG wrapper access semantics.


## 3. Package & Tooling Readiness
* **Packaging Configuration:** Configured setuptools build backend in `pyproject.toml` and specified rules JSON files as package-data for PyPI.
* **MkDocs Documentation Setup:** Configured a complete user-facing documentation site using MkDocs and the `material` theme, integrated python API documenters (`mkdocstrings`), and documented configuration schemas, command-line usage references, changelogs, and project indices.
* **Code Quality Overhaul:** Fixed all Ruff lints and resolved basedpyright strict-mode errors across the core package.
* **Architectural Review:** Conducted a thermonuclear review of `src/swig2pyi/core/` and documented improvements in `docs/architectural_review.md`.
* **GDAL OSR Verification:** Integrated static AST verification tests for GDAL's Spatial Reference System (OSR) module to ensure portability.
* **QuantLib Test Suite Verification:** Achieved zero pyright errors across 30 strict Python test files of the QuantLib test suite (verified by 21/21 integration tests in `uv run poe test-heavy`).
* **Full QuantLib Test Suite Type Verification:** Verified the entire QuantLib SWIG Python test suite (35+ test files, tag v1.40) using the generated stubs under strict typing constraints with zero type checking errors originating from the stub definitions.
* **Multi-Library Portability Verification:** Verified portability by executing `swig2pyi` on GDAL OSR and 4 synthetic SWIG interface examples (handle overloads, custom operators, vector typedefs, and general features). Implemented automated programmatic strict `basedpyright` verification for all of them, achieving zero type-checking errors.
* **Config-driven Architectural Generalization:** Eliminated hardcoded QuantLib-specific assumptions (like `Matrix`/`Array` parameter relaxation and skipped module-level functions) from the core codebase. Extracted these behaviors into generic `parameter_relaxation` and `skip_functions` configuration schema fields, migrating QuantLib specifications into `quantlib.json`.
* **Template Mapping Refinement:** Refined translation mappings for unmapped std::vector parameters to map directly to PEP 484 `Sequence[T]` annotations instead of redundant `Union[list[T], Sequence[T]]`. Updated the test suite and expected stub files accordingly.
* **Nested Template Resolution & Argument Limiting:** Enhanced the `TypeManager` to resolve deeply nested templates (e.g. nested vectors of smart pointers) and limit template arguments dynamically. Introduced the `template_arg_counts` configuration option to limit template arguments to their expected counts (e.g. keeping only the first argument for `std::vector` or first two for `std::map`), preventing C++ default allocator/comparator args from polluting Python type hints.
* **Stub Coverage CLI Command:** Implemented a new command line action `swig2pyi coverage` to check stub files against importable runtime modules. Exposes checks for missing symbols, supports allowlists, prints coverage statistics, and exits with code 1 if missing symbols exist (for CI integration).
* **Test Coverage Target:** Achieved 100% code coverage for the entire `swig2pyi` codebase, and verified that all code quality checks (pre-commit, formatting, linting, strict basedpyright, complexity) pass cleanly.
* **CI & Publishing Setup:** Configured standard GitHub Actions workflows modeling `debug-dojo`'s infrastructure. Added `docs.yaml` for automated gh-pages documentation deployment, `pypi.yaml` for automatic packaging and release to PyPI on version tags, and expanded the `python_tests.yaml` matrix to test across Python versions 3.12, 3.13, and 3.14.
* **Strict CLI-to-Core Boundary Enforcement:** Re-routed all core configuration (`Config`) and verification (`StubCoverageChecker`) imports inside the CLI layer through `swig2pyi.api`. Configured strict module dependency rules inside `tach.toml` to mandate that `swig2pyi.cli` depends only on `swig2pyi.api`, completely preventing the CLI from importing from the Core layer. Checked and validated with `tach check`.
* **Optimized Dependency Hashing via `swig -MM`:** Replaced the recursive include path directory walking (`os.walk`) with direct execution of `swig -MM` via `subprocess`. This delegates dependency tracking directly to the SWIG preprocessor, ensuring that only the files actually processed are hashed, preventing OOMs or hangs on system/vendor directories and executing under 100ms.
* **CLI Diagnostics and Logging Enhancements:** Upgraded CLI commands to write detailed diagnostics/errors directly to `sys.stderr` and exit with code 1 upon failure (e.g. invalid config, missing files, runtime exceptions). Enhanced the `coverage` subcommand to print missing symbols. Refactored commands to delegate logic to helpers, ensuring cyclomatic complexity is well below the target limit of 10, and expanded unit tests with `capsys` asserts.
* **Transitioned AST to Dataclasses:** Migrated all models in `ast_models.py` from Pydantic `BaseModel` to standard Python `@dataclass(slots=True)`. This minimizes the memory footprint of parsed elements and accelerates XML parsing of large SWIG output, with strict type safety fully validated under `basedpyright` and zero quality check warnings.
* **Stabilized Live Coverage Check:** Hardened dynamic wrapper importing to gracefully catch, log, and print warnings to `sys.stderr` for any import or runtime failures during dynamic module loading, avoiding unhandled crashes. Implemented robust module/package checking to filter out external imported symbols (e.g. from the standard library or third-party dependencies) from the runtime coverage list, ensuring highly accurate coverage diagnostics. Simplified code paths to keep complexity well below 10, verified by new unit tests.
* **Unification & Deduplication of Runner and NameManager:** Eliminated duplicate code and resources across `runner.py` and `naming.py`. Unified temporary interface wrapper creation under a single `_create_wrapper` helper and consolidated SWIG executable resolution using `_get_swig_exe`. Converted reserved keyword lookups and operator mappings to class/module-level `ClassVar` constants to eliminate allocation overhead.
* **Robust User Cache Directory Fallback:** Refactored compile cache directory lookup in `runner.py` to target OS-appropriate standard user cache folders (such as `~/.cache/swig2pyi` or Windows `LOCALAPPDATA`) with standard system temporary directories as safe fallbacks, avoiding relative walk-ups that fail when the tool is installed as a package.
* **Automated Typedef Mapping:** Added support for parsing `<typedef>` XML nodes directly from SWIG AST outputs in `SwigXmlParser`. Extracted pointers and reference symbols from SWIG `decl` attributes and enabled recursive lookup/resolution in `TypeManager` to correctly normalise custom typedef types without manual config overrides.
* **Transitive Stub Filtering:** Implemented high-performance transitive filtering of stubs by computing the transitive closure of classes, enums, and functions from a given seed file (`--filter-file`). Leveraged BFS queue-based traversal of AST node references, nested types, parameter types, and return types, stripping unreferenced components to dramatically reduce stub complexity. Achieved 100% code coverage on the filtering traversal logic and fully integrated options with the `typer`-based CLI and public API.

## 4. Robustness Hardening (Thermonuclear Review)
* **Cache Layer Removal:** Deleted the custom XML caching layer from `runner.py` (~150 LOC), simplifying it to a stateless subprocess wrapper. Callers manage temporary file lifecycle directly.
* **Circular Typedef Detection:** Added `visited` set cycle detection in `TypeManager.normalize_type` to prevent infinite recursion on mutually recursive or self-referencing typedefs.
* **Expanded C++ Primitive Coverage:** Added 20+ missing primitive types to `BASIC_TYPES` including `unsigned char`, `unsigned short`, `wchar_t`, `long double`, `int8_t`–`int64_t`, `uint8_t`–`uint64_t`, `size_t`, `ptrdiff_t`, and `ssize_t`.
* **Invalid Scope Syntax Prevention:** Fixed `_resolve_scopes` to strip template arguments from prefix scope components, preventing invalid Python syntax like `A[B].C`.
* **`%pythoncode` Preservation:** Enhanced `%pythoncode` parsing to preserve type annotations on function parameters and class-level variable assignments (`Assign`/`AnnAssign`/`Import` nodes).
* **Duplicate Overload Elimination:** Fixed duplicate `@overload` generation in Handle delegation by normalizing parameter types before signature comparison.
* **Memory Leak Fix:** Corrected `children_by_parent` cleanup in `parser.py` to clear entries for ignored classes during iterparse.
* **API Cleanup:** Removed unused `validate` parameter from public API functions `generate_from_xml` and `generate_from_interface`.
* **Lint Compliance:** Resolved all remaining FBT001 (boolean positional args), SIM102 (collapsible ifs), and basedpyright `reportArgumentType` errors across `emitter.py` and `type_system.py`.
