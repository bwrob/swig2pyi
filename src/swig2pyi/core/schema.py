from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship

class BaseClass(SQLModel, table=True):
    __tablename__ = "bases"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    node_id: Optional[int] = Field(default=None, foreign_key="nodes.id")
    name: str
    
    node: Optional["Node"] = Relationship(back_populates="bases")

class EnumItem(SQLModel, table=True):
    __tablename__ = "enums"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    node_id: Optional[int] = Field(default=None, foreign_key="nodes.id")
    name: str
    value: Optional[str] = None
    
    node: Optional["Node"] = Relationship(back_populates="enum_items")

class Parm(SQLModel, table=True):
    __tablename__ = "parms"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    node_id: Optional[int] = Field(default=None, foreign_key="nodes.id")
    name: Optional[str] = None
    type: Optional[str] = None
    idx: int
    
    node: Optional["Node"] = Relationship(back_populates="parms")

class Node(SQLModel, table=True):
    __tablename__ = "nodes"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    parent_class_id: Optional[int] = Field(default=None, foreign_key="nodes.id")
    parent_template_id: Optional[int] = Field(default=None, foreign_key="nodes.id")
    tag: str
    name: str
    kind: Optional[str] = None
    type: Optional[str] = None
    decl: Optional[str] = None
    feature_ignore: bool = Field(default=False)
    is_template: bool = Field(default=False)

    # Relationships
    bases: List[BaseClass] = Relationship(back_populates="node")
    enum_items: List[EnumItem] = Relationship(back_populates="node")
    parms: List[Parm] = Relationship(back_populates="node")
    
class TopInfo(SQLModel, table=True):
    __tablename__ = "top_info"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    module_name: str
