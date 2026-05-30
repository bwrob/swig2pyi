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
        parts: list[str] = []
        for i, p in enumerate(parms):
            p_name = self.nm.sanitize(p.name or f"arg{i}")
            if p.type:
                p_type = self.tm.to_python(p.type, is_parameter=True)
            else:
                self.tm.needed_imports.add("Any")
                p_type = "Any"

            if p_type in self.tm.enums:
                self.tm.needed_imports.add("Union")
                p_type = f"Union[{p_type}, int]"
            if p.value is not None:
                parts.append(f"{p_name}: {p_type} = ...")
            else:
                parts.append(f"{p_name}: {p_type}")
        return parts

    def _get_param_parts(
        self, func: CDecl, *, is_method: bool, mapped_name: str | None
    ) -> list[str]:
        is_cmp = is_method and mapped_name in ("__eq__", "__ne__")
        if is_cmp:
            return ["other: object"]
        return self.format_params(func.parms)

    def _format_params_string(
        self,
        param_parts: list[str],
        *,
        is_method: bool,
        is_static: bool,
        num_parms: int,
        indent_level: int,
    ) -> str:
        if is_method and not is_static:
            param_parts.insert(0, "self")

        if len(param_parts) > 1 or (is_method and not is_static and num_parms > 0):
            params_str = ",\n".join(
                (indent_level + 1) * "    " + p for p in param_parts
            )
            return f"\n{params_str},\n" + indent_level * "    "
        if len(param_parts) == 1:
            return param_parts[0]
        return ""

    def _get_return_type(self, func_type: str | None) -> str:
        if not func_type:
            self.tm.needed_imports.add("Any")
            return "Any"
        ret_type = self.tm.to_python(func_type)
        if ret_type == "void":
            return "None"
        return ret_type

    def get_signature(
        self, func: CDecl, *, is_method: bool, indent_level: int = 0
    ) -> tuple[str, str]:
        """Get the parameters string and return type for a function/method."""
        mapped_name = self.nm.get_python_name(func.name) if is_method else func.name
        param_parts = self._get_param_parts(
            func, is_method=is_method, mapped_name=mapped_name
        )
        is_static = getattr(func, "is_static", False)
        full_params = self._format_params_string(
            param_parts,
            is_method=is_method,
            is_static=is_static,
            num_parms=len(func.parms),
            indent_level=indent_level,
        )
        ret_type = self._get_return_type(func.type)
        return (full_params, ret_type)
