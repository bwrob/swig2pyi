from swig2pyi.core.config import Config
from swig2pyi.core.emitter import StubEmitter
from swig2pyi.core.parser import Class, Module, Top
from swig2pyi.core.type_system import TypeManager


def test_handle_inheritance() -> None:
    cfg = Config(
        module_name="test",
        includes=[],
        type_map={},
        smart_pointers=[],
        containers={},
        rename_operators=False,
    )
    tm = TypeManager(cfg)
    emitter = StubEmitter(tm)

    classes: list[Class] = []

    # Case 1: Handle<MyClass>
    classes.append(
        Class(
            name="MyHandle", bases=["Handle<MyClass>"], kind="class", is_template=False
        )
    )

    # Case 2: RelinkableHandle<MyClass>
    classes.append(
        Class(
            name="MyRelinkableHandle",
            bases=["RelinkableHandle<MyClass>"],
            kind="class",
            is_template=False,
        )
    )

    # Case 3: RelinkableHandle<(Quote)> (Checking type system normalization + inheritance)
    classes.append(
        Class(
            name="QuoteHandle",
            bases=["RelinkableHandle<(Quote)>"],
            kind="class",
            is_template=False,
        )
    )

    mod = Module(name="test", classes=classes)
    top = Top(module=mod)

    emitter.emit(top)
    output = emitter.get_output()

    assert "class MyHandle(Handle[MyClass], MyClass):" in output
    assert "class MyRelinkableHandle(RelinkableHandle[MyClass], MyClass):" in output
    assert "class QuoteHandle(RelinkableHandle[Quote], Quote):" in output


if __name__ == "__main__":
    test_handle_inheritance()
