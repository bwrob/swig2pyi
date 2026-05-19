"""Signature formatting logic for Python methods and functions."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .ast_models import CDecl, Parm
    from .naming import NameManager
    from .type_system import TypeManager


class SignatureFormatter:
    """Handles formatting of function/method signatures."""

    def __init__(self, type_manager: TypeManager, name_manager: NameManager) -> None:
        """Initialize with managers."""
        self.tm = type_manager
        self.nm = name_manager

    def format_params(self, parms: list[Parm]) -> list[str]:
        """Format parameter list for Python function signature."""
        parts = []
        for i, p in enumerate(parms):
            p_name = self.nm.sanitize(p.name or f"arg{i}")
            p_type = self.tm.to_python(p.type) if p.type else "Any"
            parts.append(f"{p_name}: {p_type}")
        return parts

    def get_signature(
        self, func: CDecl, *, is_method: bool, indent_level: int = 0
    ) -> tuple[str, str]:
        """Get the parameters string and return type for a function/method."""
        param_parts = self.format_params(func.parms)
        is_static = getattr(func, "is_static", False)
        if is_method and not is_static:
            param_parts.insert(0, "self")

        if len(param_parts) > 1 or (
            is_method and not is_static and len(func.parms) > 0
        ):
            params_str = ",\n".join(
                (indent_level + 1) * "    " + p for p in param_parts
            )
            full_params = f"\n{params_str},\n" + indent_level * "    "
        elif len(param_parts) == 1:
            full_params = param_parts[0]
        else:
            full_params = ""

        ret_type = self.tm.to_python(func.type) if func.type else "Any"
        if ret_type == "void":
            ret_type = "None"
        return (full_params, ret_type)
