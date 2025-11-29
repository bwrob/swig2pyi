from typing import List, Optional, Union
from pathlib import Path
import xml.etree.ElementTree as ET
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

    def parse_file(self, file_path: 'Path') -> Top:
        import xml.etree.ElementTree as ET
        
        # We use iterparse to find the top module and its children.
        # However, pydantic-xml is designed to parse the whole tree or sub-trees.
        # Since we have a huge file, we want to parse <module> piece by piece if possible,
        # or at least parse the <top> and populate it incrementally.
        
        # But our Top model defines: module: Optional[Module]
        # And Module defines: classes: List[Class], cdecls: List[CDecl]
        
        # If we instantiate Top(), we can append to it.
        
        top = Top()
        current_module = None
        
        # We iterate over events.
        # 'start': when a tag opens.
        # 'end': when a tag closes.
        
        # For large lists (classes, cdecls), we want to parse them individually and clear the element.
        
        context = ET.iterparse(str(file_path), events=("start", "end"))
        context = iter(context)
        
        # Helper to parse a single element into a Pydantic model
        def parse_node(element, model_cls):
             # We need to convert the element to bytes to feed into from_xml,
             # or construct from element if pydantic-xml supports it?
             # pydantic-xml `from_xml` takes string or bytes.
             # serializing element back to string is expensive?
             # Maybe pydantic-xml has a way to bind to an existing element?
             # Inspecting pydantic-xml docs (memory): it usually parses from bytes/str.
             # But we can use ET.tostring(element).
             xml_bytes = ET.tostring(element)
             return model_cls.from_xml(xml_bytes)

        # We need to track depth or context?
        # Structure: <top> <module> <class> ... </class> <cdecl> ... </cdecl> </module> </top>
        
        # Optimization: We only care about direct children of <module> for now?
        # Or do we need full depth?
        # Classes have nested <cdecl> (methods).
        
        # If we use 'end' event for <class>, the whole <class> subtree is built in memory.
        # A single class is not 2GB. The 2GB is thousands of classes.
        # So if we handle 'end' of <class>, parse it, add to our list, and then clear it, we are good.
        
        for event, elem in context:
            if event == "start":
                if elem.tag == "module":
                    # We found the module start. Initialize our Module object.
                    # We need its attributes.
                    name = elem.get("name", "Unknown")
                    current_module = Module(name=name)
                    top.module = current_module
            
            elif event == "end":
                if elem.tag == "class":
                    if current_module:
                        # Parse the class subtree
                        try:
                            cls_obj = parse_node(elem, Class)
                            current_module.classes.append(cls_obj)
                        except Exception:
                            # Log error or skip
                            pass
                        
                        # Clear element to free memory
                        elem.clear()
                
                elif elem.tag == "cdecl":
                    # Check if this cdecl is a direct child of module
                    # If it's inside a class, it's handled when class ends?
                    # No, iterparse 'end' triggers for inner cdecl BEFORE outer class end.
                    # We need to distinguish module-level cdecls vs class-level cdecls.
                    # But here we don't have parent pointer easily in iterparse (unless we track stack).
                    
                    # However, if we parse 'cdecl' here, we are double parsing if it's inside class?
                    # Wait. If we clear 'cdecl', it is removed from parent? 
                    # If we remove it from parent, then 'class' element won't have it when we parse 'class'.
                    # THIS IS TRICKY.
                    
                    # Strategy: 
                    # 1. Only handle Top-Level elements.
                    # But how to know if it's top level?
                    # We can't easily know without stack tracking.
                    
                    # Alternative: 
                    # We only clear elements that are direct children of <module>.
                    # But we don't know parent.
                    
                    pass

                elif elem.tag == "module":
                    # Module ended. 
                    pass
        
        # This generic iterparse is hard with nested structures if we want to use `from_xml` on subtrees.
        # Because `from_xml` expects the subtree to exist.
        
        # If we clear nested elements, the parent (Class) won't have them.
        # So we CANNOT clear children of Class.
        # We CAN clear Class after we parse it.
        
        # But how do we prevent parsing `cdecl` that are children of `class`?
        # We just don't have a handler for `cdecl` in the loop?
        # But we NEED module-level cdecls (global functions).
        
        # If we skip `cdecl` handler, we miss global functions.
        # If we have `cdecl` handler, we catch class methods too.
        
        # Solution:
        # Use a stack to track current parent tag.
        
        return self._parse_file_streaming(file_path)

    def _parse_file_streaming(self, file_path: 'Path') -> Top:
        import xml.etree.ElementTree as ET
        
        top = Top()
        
        # We need to build the Module manually because we can't instantiate it fully at once.
        # Let's assume valid SWIG XML has one <module> inside <top>.
        
        # We will accumulate classes and cdecls into lists and assign them to module at the end?
        # Or create a partial Module.
        
        module_name = "Unknown"
        classes = []
        cdecls = []
        
        # Stack of (tag, element) to track nesting
        # Actually, we can check depth.
        
        # Iterate
        context = ET.iterparse(str(file_path), events=("start", "end"))
        context = iter(context)
        
        # Root element
        _, root = next(context) 
        
        # We want to identify children of 'module'.
        # <top> -> <module> -> children
        
        in_module = False
        
        for event, elem in context:
            if event == "start":
                if elem.tag == "module":
                    in_module = True
                    module_name = elem.get("name", module_name)
            
            elif event == "end":
                if elem.tag == "module":
                    in_module = False
                
                if in_module:
                    # We are inside module.
                    # We want to catch direct children.
                    # But 'end' event happens for deep children too.
                    # We need to check if the parent of 'elem' is the 'module' element.
                    # But iterparse doesn't give parent.
                    
                    # However, we can use a trick: 
                    # If we are at 'class' end, we check if we should process it.
                    # If we process it, we assume it's a top-level class?
                    # Nested classes exist in C++. SWIG XML represents them how?
                    # <class> <class> ... </class> </class> ?
                    # Yes.
                    
                    # If it is a nested class, we want it to be part of the parent class's definition.
                    # If we parse it here and clear it, the parent class won't see it.
                    # So we must ONLY clear TOP-LEVEL classes.
                    
                    # How to detect top-level?
                    # Use a depth counter?
                    # <top> (depth 0) -> <module> (depth 1) -> <class> (depth 2)
                    # If we are at depth 2, it is top-level.
                    pass
                
                # To implement depth, we need 'start' events to increment and 'end' to decrement.
        
        # Reset iterator for proper implementation with depth
        del context
        context = ET.iterparse(str(file_path), events=("start", "end"))
        context = iter(context)
        
        depth = 0
        
        for event, elem in context:
            if event == "start":
                depth += 1
                if elem.tag == "module":
                    module_name = elem.get("name", module_name)
            
            elif event == "end":
                # process element
                if elem.tag == "class":
                    # If depth is 3 (<top><module><class>), it is a direct child of module.
                    if depth == 3:
                        xml_bytes = ET.tostring(elem)
                        try:
                            cls = Class.from_xml(xml_bytes)
                            classes.append(cls)
                        except Exception as e:
                            print(f"Error parsing class: {e}")
                            pass
                        elem.clear()
                        # Also clear references from root/parent to avoid memory leak if possible?
                        # In iterparse, the tree is built. Clearing 'elem' clears its children.
                        # But 'module' still holds a reference to 'elem'.
                        # We can't easily remove it from 'module' without access to 'module' element here.
                        # But actually, 'root' is top. 
                        # If we don't clear from parent, parent grows.
                        # But preventing parent growth is hard in iterparse without custom logic.
                        
                        # Actually, for 'end' event, 'elem' is fully populated.
                        # Use 'root.clear()' ? No.
                
                elif elem.tag == "cdecl":
                    # Direct child of module (global function)
                    if depth == 3:
                        xml_bytes = ET.tostring(elem)
                        try:
                            func = CDecl.from_xml(xml_bytes)
                            cdecls.append(func)
                        except Exception as e:
                            print(f"Error parsing cdecl: {e}")
                            pass
                        elem.clear()

                depth -= 1
                
        # Construct the full structure
        # Note: The 'classes' and 'cdecls' lists are populated.
        # But 'module' element was not fully parsed (we skipped its children via clear?).
        # We create the Pydantic objects manually.
        
        mod = Module(name=module_name, classes=classes, cdecls=cdecls)
        t = Top(module=mod)
        return t
