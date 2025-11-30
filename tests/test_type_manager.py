from pathlib import Path

import pytest

from swig2pyi.core.config import Config
from swig2pyi.core.type_system import TypeManager


@pytest.fixture
def config() -> Config:
    # Load the actual quantlib.json for realistic testing
    return Config.from_file(Path("src/swig2pyi/rules/quantlib.json"))


@pytest.fixture
def type_manager(config: Config) -> TypeManager:
    return TypeManager(config)


def test_basic_types(type_manager) -> None:
    assert type_manager.to_python("QuantLib::Real") == "float"
    assert type_manager.to_python("std::string") == "str"
    assert type_manager.to_python("bool") == "bool"


def test_strip_qualifiers(type_manager) -> None:
    assert type_manager.to_python("const QuantLib::Real &") == "float"
    assert type_manager.to_python("const std::string *") == "str"
    assert (
        type_manager.to_python("volatile int") == "int"
    )  # int defaults to int if not mapped? Wait, int is not in map but "QuantLib::Integer" is.
    # "int" is not in the provided quantlib.json type_map.
    # The function returns the input if no match. So "int" -> "int".
    assert type_manager.to_python("int") == "int"


def test_smart_pointers(type_manager) -> None:
    assert type_manager.to_python("boost::shared_ptr<QuantLib::Date>") == "Date"


def test_templates(type_manager) -> None:
    # Templates not in type_map or containers are just passed through (or handled generically if I add that)
    # For now, they might be strings
    pass


def test_containers(type_manager) -> None:
    assert (
        type_manager.to_python("std::vector<QuantLib::Real>")
        == "typing.MutableSequence[float]"
    )
    assert (
        type_manager.to_python("std::vector<std::string>")
        == "typing.MutableSequence[str]"
    )

    # Container with smart pointer
    assert (
        type_manager.to_python("std::vector<boost::shared_ptr<QuantLib::Date>>")
        == "typing.MutableSequence[Date]"
    )


def test_complex_stripping(type_manager) -> None:
    # const shared_ptr<const T> &
    # 1. Strip outer const/& -> shared_ptr<const T>
    # 2. Unwrap -> const T
    # 3. Strip const -> T
    assert (
        type_manager.to_python("const boost::shared_ptr<const QuantLib::Real> &")
        == "float"
    )
