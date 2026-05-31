# Changelog

## v0.1.0 (2026-05-31)

### Features

*   **Universal SWIG to Python Stub Generator**: Compile SWIG interface `.i` files or parse SWIG XML definitions into strongly-typed Pydantic AST representations.
*   **C++ Template & smart pointer Resolution**: Supports `std::vector`, `std::shared_ptr`, and custom templates mapping to Python typing annotations (e.g. `Sequence`, `Generic`, `Union`).
*   **Operator Mapping**: Map C++ operator definitions (such as `operator==` and `operator[]`) to Python dunders (`__eq__`, `__getitem__`).
*   **Dunder Iteration Generator**: Detects index subscription (`__getitem__`) and generates corresponding `__iter__` method hooks automatically.
*   **Proxy Class Delegation**: Allows template classes (like `Handle[T]`) to dynamically delegate and proxy underlying template argument type methods.
*   **SWIG cvar Emulation**: Exposes C++ global and static variables inside a module-level `cvar` instance of a custom `cvar_class` wrapper.
*   **Stub Coverage Checker CLI**: Introduces `swig2pyi coverage` command to audit generated stubs against importable Python runtime packages, reporting missed symbols and matching allowlists.
