"""Name mapping and sanitization logic for SWIG-generated wrappers."""

from typing import ClassVar


class NameManager:
    """Handles sanitization of C++ names and mapping of operators to Python dunders."""

    RESERVED: ClassVar[set[str]] = {
        "False",
        "None",
        "True",
        "and",
        "as",
        "assert",
        "async",
        "await",
        "break",
        "class",
        "continue",
        "def",
        "del",
        "elif",
        "else",
        "except",
        "finally",
        "for",
        "from",
        "global",
        "if",
        "import",
        "in",
        "is",
        "lambda",
        "nonlocal",
        "not",
        "or",
        "pass",
        "raise",
        "return",
        "try",
        "while",
        "with",
        "yield",
    }

    OPERATOR_MAPPING: ClassVar[dict[str, str]] = {
        "operator+": "__add__",
        "operator-": "__sub__",
        "operator*": "__mul__",
        "operator/": "__truediv__",
        "operator==": "__eq__",
        "operator!=": "__ne__",
        "operator<": "__lt__",
        "operator>": "__gt__",
        "operator<=": "__le__",
        "operator>=": "__ge__",
        "operator()": "__call__",
        "operator[]": "__getitem__",
        "operator->": "__deref__",
    }

    def __init__(self, *, rename_operators: bool = True) -> None:
        """Initialize with configuration."""
        self.rename_operators = rename_operators

    def sanitize(self, name: str) -> str:
        """Sanitize a name to avoid Python reserved words."""
        return name + "_" if name in self.RESERVED else name

    def map_operator(self, name: str) -> str:
        """Map C++ operator name to Python dunder method name."""
        normalized = name.replace(" ", "")
        return self.OPERATOR_MAPPING.get(normalized, name)

    def get_python_name(self, cpp_name: str) -> str | None:
        """Get the Pythonic name for a C++ symbol."""
        name = cpp_name.rsplit("::", maxsplit=1)[-1]
        if self.rename_operators and name.startswith("operator"):
            mapped = self.map_operator(name)
            if mapped == name:
                return None
            return mapped

        if name.startswith("operator"):
            return None

        if not name.startswith("__"):
            name = self.sanitize(name)
        return name
