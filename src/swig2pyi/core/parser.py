from typing import List, Optional, Dict, Any
from pathlib import Path
import xml.etree.ElementTree as ET
from pydantic import BaseModel

# --- Models ---

class Parm(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None

class CDecl(BaseModel):
    name: str
    type: Optional[str] = None
    kind: Optional[str] = None
    parms: List[Parm] = []
    decl: Optional[str] = None # e.g. f(int)

class Constructor(BaseModel):
    name: str
    parms: List[Parm] = []

class Destructor(BaseModel):
    name: str

class Class(BaseModel):
    name: str
    kind: Optional[str] = None # class, struct
    classes: List['Class'] = []
    constructors: List[Constructor] = []
    destructors: List[Destructor] = []
    cdecls: List[CDecl] = [] # methods and members

class Module(BaseModel):
    name: str
    classes: List[Class] = []
    cdecls: List[CDecl] = []

class Top(BaseModel):
    module: Optional[Module] = None

# --- Parser ---

class SwigXmlParser:
    def parse_file(self, file_path: Path) -> Top:
        # Load whole tree into memory (2.8MB is fine)
        try:
            tree = ET.parse(str(file_path))
            root = tree.getroot()
            return self._parse_root(root)
        except ET.ParseError as e:
            raise RuntimeError(f"Failed to parse XML: {e}")

    def _get_attributes(self, node: ET.Element) -> Dict[str, str]:
        """Extracts attributes from <attributelist> child."""
        attrs = {}
        # SWIG XML puts attributes in a child <attributelist>
        # <attributelist> contains <attribute name="..." value="..."/>
        attr_list = node.find("attributelist")
        if attr_list is not None:
            for attr_node in attr_list.findall("attribute"):
                name = attr_node.get("name")
                value = attr_node.get("value")
                if name and value is not None:
                    attrs[name] = value
        
        return attrs

    def _parse_parms(self, node: ET.Element) -> List[Parm]:
        parms = []
        # parms can be in <parmlist> or direct?
        # Let's check direct children 'parm' and children of direct 'parmlist'
        
        def extract_parm(p_node):
            p_attrs = self._get_attributes(p_node)
            return Parm(
                name=p_attrs.get("name"),
                type=p_attrs.get("type")
            )

        for child in node:
            if child.tag == "parm":
                parms.append(extract_parm(child))
            elif child.tag == "parmlist":
                for p_child in child:
                    if p_child.tag == "parm":
                        parms.append(extract_parm(p_child))
                        
        return parms

    def _parse_cdecl(self, node: ET.Element, attrs: Dict[str, str]) -> CDecl:
        return CDecl(
            name=attrs.get("name", ""),
            type=attrs.get("type"),
            kind=attrs.get("kind"),
            decl=attrs.get("decl"),
            parms=self._parse_parms(node)
        )

    def _parse_constructor(self, node: ET.Element, attrs: Dict[str, str]) -> Constructor:
        return Constructor(
            name=attrs.get("name", ""),
            parms=self._parse_parms(node)
        )
    
    def _parse_destructor(self, node: ET.Element, attrs: Dict[str, str]) -> Destructor:
        return Destructor(name=attrs.get("name", ""))

    def _parse_class(self, node: ET.Element, attrs: Dict[str, str]) -> Class:
        cls = Class(
            name=attrs.get("name", ""),
            kind=attrs.get("kind")
        )
        
        for child in node:
            if child.tag == "attributelist":
                continue
                
            c_attrs = self._get_attributes(child)
            
            # SWIG XML often nests 'cdecl' for methods
            if child.tag == "cdecl":
                # Method or member
                kind = c_attrs.get("kind")
                if kind in ("function", "variable"): 
                     cls.cdecls.append(self._parse_cdecl(child, c_attrs))
                     
            elif child.tag == "constructor":
                cls.constructors.append(self._parse_constructor(child, c_attrs))
            elif child.tag == "destructor":
                cls.destructors.append(self._parse_destructor(child, c_attrs))
            elif child.tag == "class":
                 # Nested class
                 cls.classes.append(self._parse_class(child, c_attrs))
        
        return cls

    def _parse_root(self, root: ET.Element) -> Top:
        # Find module name
        top_attrs = self._get_attributes(root)
        module_name = top_attrs.get("module", "Unknown")
        
        module = Module(name=module_name)
        top = Top(module=module)
        
        # Recursive traversal
        def visit(node):
            for child in node:
                tag = child.tag
                if tag == "attributelist":
                    continue
                
                if tag == "class":
                    attrs = self._get_attributes(child)
                    if attrs.get("feature_ignore") == "1":
                        continue
                    # If name is missing, it might be anonymous struct or something
                    if not attrs.get("name"):
                        continue
                        
                    cls = self._parse_class(child, attrs)
                    module.classes.append(cls)
                
                elif tag == "cdecl":
                    attrs = self._get_attributes(child)
                    if attrs.get("feature_ignore") == "1":
                        continue
                        
                    kind = attrs.get("kind")
                    # We strictly want global functions/variables here
                    if kind in ("function", "variable"):
                        func = self._parse_cdecl(child, attrs)
                        module.cdecls.append(func)
                
                elif tag in ("include", "namespace", "module", "top", "insert"):
                    visit(child)
        
        visit(root)
        return top