from typing import List, Optional, Union
from pydantic_xml import BaseXmlModel, attr, element

# Forward declarations
class Class(BaseXmlModel):
    pass

class Parm(BaseXmlModel, tag='parm'):
    name: Optional[str] = attr(default=None)
    type: Optional[str] = attr(default=None)

class CDecl(BaseXmlModel, tag='cdecl'):
    name: str = attr()
    type: Optional[str] = attr(default=None)
    kind: Optional[str] = attr(default=None)
    parms: List[Parm] = element(default=[])
    
    # For typedefs, the type attribute holds the source type.
    # For functions, type holds return type.

class Constructor(BaseXmlModel, tag='constructor'):
    name: str = attr()
    parms: List[Parm] = element(default=[])

class Destructor(BaseXmlModel, tag='destructor'):
    name: str = attr()

class Class(BaseXmlModel, tag='class'):
    name: str = attr()
    kind: Optional[str] = attr(default=None)
    
    # Flattened list of members. 
    # Note: This strict separation might miss items if the XML is interleaved 
    # and pydantic-xml expects strict ordering matching the field definition order.
    # However, we will rely on pydantic-xml's ability to find tags.
    
    classes: List['Class'] = element(default=[])
    constructors: List[Constructor] = element(default=[])
    destructors: List[Destructor] = element(default=[])
    cdecls: List[CDecl] = element(default=[])

class Module(BaseXmlModel, tag='module'):
    name: str = attr()
    classes: List[Class] = element(default=[])
    cdecls: List[CDecl] = element(default=[])

class Top(BaseXmlModel, tag='top'):
    module: Optional[Module] = element(default=None)

class SwigXmlParser:
    def parse(self, xml_content: str) -> Top:
        return Top.from_xml(xml_content)
