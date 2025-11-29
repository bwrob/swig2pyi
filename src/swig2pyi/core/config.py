from pathlib import Path
from typing import Dict, List

from pydantic import BaseModel


class Config(BaseModel):
    module_name: str
    includes: List[str]
    type_map: Dict[str, str]
    smart_pointers: List[str]
    containers: Dict[str, str]
    rename_operators: bool = False

    @classmethod
    def from_file(cls, path: Path) -> "Config":
        with open(path, "r") as f:
            json_content = f.read()
        return cls.model_validate_json(json_content)
