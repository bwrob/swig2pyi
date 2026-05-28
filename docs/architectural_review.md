# Thermonuclear Code Quality & Architectural Review

This document contains a strict architectural audit of the `swig2pyi` core package, focusing on abstraction quality, simplification opportunities ("code judo"), and structural debt.

---

## Major Architecture Weaknesses

### 1. Unnecessary Database Layer & Dependency Bloat
* **Issue:** The pipeline streams SWIG XML elements via `ET.iterparse`, dumps them into a SQLite database using `SQLModel` and `SQLAlchemy`, and then queries SQLite to reconstruct the Pydantic AST.
* **Why it is weak:** This introduces massive structural complexity:
  * Requires database connection pooling, schema migrations, and relational mapping.
  * Spreads parsing state across three separate files: `schema.py`, `ingestion.py`, and `builder.py`.
  * Introduces heavy external dependencies (`sqlmodel`, `sqlalchemy`) for a task that is conceptually a pure hierarchical AST transformation.
  * Severe performance overhead (disk/memory I/O for DB writes and queries) compared to direct memory mapping.
* **Impact:** High maintenance cost, slow execution, complex test setups.

### 2. Heuristic Pre-Emission & Post-Emission Code Scanning
* **Issue:** `StubEmitter` scans the generated `.pyi` file's body using regular expressions to decide which symbols from `typing` to import (e.g. `Any`, `overload`, `Union`).
* **Why it is weak:** This is a brittle post-processing heuristic. If a C++ class, member variable, or docstring happens to mention `Any` or `Union`, it triggers a regex match and prepends the import, even if not actually required for typing.
* **Impact:** Risk of emitting unused or invalid imports in type stubs.

### 3. Duplicate C++ Type Cleaning Logic
* **Issue:** C++ type cleaning and normalization are duplicated in multiple places:
  * `StubEmitter.clean_cpp_type`
  * `TypeManager._clean_cpp_type`
  * `TypeManager._clean_basic`
* **Why it is weak:** Clean-up rules (removing namespaces, `const`, `volatile`, and brackets) are not unified. Changes to namespace removal rules or type mapping must be updated in multiple systems.
* **Impact:** High risk of divergence in type resolution logic between the emitter and the type system.

### 4. Brittle Hand-Rolled Bracket Parsing
* **Issue:** `TypeManager` implements custom bracket-counting and parenthesis-counting algorithms (`_split_template_args`, `_split_scopes`, `_find_matching_paren_index`, `_get_matching_bracket_index`) to parse template signatures.
* **Why it is weak:** Hand-rolled string parsers with manual index incrementing are prone to edge-case failures on complex C++ types (e.g. nested template-template parameters, function pointers, reference qualifiers).
* **Impact:** Maintenance difficulty and risk of silent parsing failures on complex C++ types.

---

## Code Judo Moves

### Judo Move 1: Demolish SQLite/SQLModel Database Layer
* **Action:** Delete `schema.py`, `ingestion.py`, and `builder.py`.
* **Replacement:** Traverse the XML tree (`xml.etree.ElementTree`) directly in memory in a single recursive pass to construct Pydantic `Top`, `Module`, and `Class` models.
* **Result:**
  * Eliminates three modules (~700 lines of code).
  * Removes `sqlmodel` and `sqlalchemy` dependencies.
  * Significantly increases parsing speed.
  * Unifies ingestion and AST building.

### Judo Move 2: Explicit Import Tracking
* **Action:** Modify `TypeManager` and `StubEmitter` to register imports as they resolve types (e.g., when a method signature requires `Sequence`, register `Sequence` as a required import).
* **Result:** Eliminates the post-processing regex scanning of generated stubs, ensuring 100% accurate imports without heuristic false positives.

### Judo Move 3: Unify Type Sanitization
* **Action:** Consolidate all name sanitization and C++ type cleaning under `TypeManager` or a shared helper in `naming.py`.
* **Result:** Eliminates duplicate string manipulation, ensuring consistent namespace and keyword handling.

---

## Micro-improvements

* **Dead Code in `StubEmitter`:** `_collect_properties` and `_collect_class_methods` contain unused parameters and debug-like placeholders.
* **Hardcoded Magic Strings:** Configuration defaults and SWIG command flags are scattered inside `runner.py` and `emitter.py`. They should be centralized in `config.py`.
* **Logging Opacity:** SWIG execution failures during `runner.py` subprocess execution do not log stdout/stderr to files under `.temp/` by default, making debugging remote SWIG environment failures difficult.
