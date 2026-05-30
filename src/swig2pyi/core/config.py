"""Configuration management for swig2pyi."""

from pathlib import Path

from pydantic import BaseModel


class Config(BaseModel):
    """Configuration schema for swig2pyi."""

    module_name: str
    includes: list[str]
    type_map: dict[str, str]
    smart_pointers: list[str]
    containers: dict[str, str]
    rename_operators: bool = False
    extra_code: list[str] = []
    namespaces_to_remove: list[str] = []
    delegate_templates: list[str] = []
    generic_templates: list[str] = []
    pythoncode_signatures: dict[str, str] = {}

    @classmethod
    def from_file(cls, path: Path) -> "Config":
        """Load configuration from a JSON file."""
        with path.open("r") as f:
            json_content = f.read()
        return cls.model_validate_json(json_content)
