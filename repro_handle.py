
from swig2pyi.core.config import Config
from swig2pyi.core.type_system import TypeManager


def test_handle_parens() -> None:
    config = Config(
        module_name="Test",
        includes=[],
        type_map={},
        smart_pointers=[],
        containers={},
        rename_operators=False
    )
    tm = TypeManager(config)

    # The issue: RelinkableHandle<(Quote)> should be RelinkableHandle[Quote]
    # Actually, RelinkableHandle is a template in C++, but if it's not in 'containers' config,
    # it's treated as a string.
    # Wait, the input type string from SWIG XML likely looks like "RelinkableHandle<(Quote)>".
    # TypeManager logic:
    # 1. Strip SWIG prefixes.
    # 2. Strip parens from whole string.
    # 3. Unwrap smart pointers.
    # 4. Handle templates (containers).

    input_type = "RelinkableHandle<(Quote)>"
    tm.to_python(input_type)

    # If RelinkableHandle isn't in containers map, it just returns the string normalized.
    # We need to ensure parens INSIDE the template args are also stripped or handled?
    # Or rather, parens are stripped from the *entire* type string if they wrap it.
    # Here parens wrap Quote inside <>.

    # If I add RelinkableHandle to containers, it might work.
    # But if it's not a container, it should probably just be RelinkableHandle[Quote] if it's a generic?
    # Python doesn't support RelinkableHandle<(Quote)> syntax.

if __name__ == "__main__":
    test_handle_parens()
