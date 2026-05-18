from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class BaseClass(SQLModel, table=True):
    __tablename__ = "bases"

    id: int | None = Field(default=None, primary_key=True)
    node_id: int | None = Field(default=None, foreign_key="nodes.id")
    name: str

    node: Optional["Node"] = Relationship(back_populates="bases")

class EnumItem(SQLModel, table=True):
    __tablename__ = "enums"

    id: int | None = Field(default=None, primary_key=True)
    node_id: int | None = Field(default=None, foreign_key="nodes.id")
    name: str
    value: str | None = None

    node: Optional["Node"] = Relationship(back_populates="enum_items")

class Parm(SQLModel, table=True):
    __tablename__ = "parms"

    id: int | None = Field(default=None, primary_key=True)
    node_id: int | None = Field(default=None, foreign_key="nodes.id")
    name: str | None = None
    type: str | None = None
    idx: int

    node: Optional["Node"] = Relationship(back_populates="parms")

class Node(SQLModel, table=True):
    __tablename__ = "nodes"

    id: int | None = Field(default=None, primary_key=True)
    parent_class_id: int | None = Field(default=None, foreign_key="nodes.id")
    parent_template_id: int | None = Field(default=None, foreign_key="nodes.id")
    tag: str
    name: str
    kind: str | None = None
    type: str | None = None
    decl: str | None = None
    feature_ignore: bool = Field(default=False)
    is_template: bool = Field(default=False)
    is_static: bool = Field(default=False)

    # Relationships
    bases: list[BaseClass] = Relationship(back_populates="node")
    enum_items: list[EnumItem] = Relationship(back_populates="node")
    parms: list[Parm] = Relationship(back_populates="node")

class TopInfo(SQLModel, table=True):
    __tablename__ = "top_info"

    id: int | None = Field(default=None, primary_key=True)
    module_name: str
