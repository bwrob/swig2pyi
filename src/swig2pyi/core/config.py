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

    @classmethod
    def from_file(cls, path: Path) -> "Config":
        """Load configuration from a JSON file."""
        with path.open("r") as f:
            json_content = f.read()
        return cls.model_validate_json(json_content)
