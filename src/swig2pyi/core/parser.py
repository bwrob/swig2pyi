from __future__ import annotations

import sqlite3
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import TYPE_CHECKING
from contextlib import closing
import tempfile
import os

from pydantic import BaseModel

if TYPE_CHECKING:
    pass

# --- Models ---
class Parm(BaseModel):
    name: str | None = None
    type: str | None = None

class CDecl(BaseModel):
    name: str
    type: str | None = None
    kind: str | None = None
    parms: list[Parm] = []
    decl: str | None = None

class Constructor(BaseModel):
    name: str
    parms: list[Parm] = []

class Destructor(BaseModel):
    name: str

class EnumItem(BaseModel):
    name: str
    value: str | None = None

class Enum(BaseModel):
    name: str
    items: list[EnumItem] = []

class Class(BaseModel):
    name: str
    kind: str | None = None
    is_template: bool = False
    bases: list[str] = []
    classes: list[Class] = []
    enums: list[Enum] = []
    constructors: list[Constructor] = []
    destructors: list[Destructor] = []
    cdecls: list[CDecl] = []

class Module(BaseModel):
    name: str
    classes: list[Class] = []
    enums: list[Enum] = []
    cdecls: list[CDecl] = []

class Top(BaseModel):
    module: Module | None = None


# --- Parser ---
class SwigXmlParser:
    def __init__(self):
        pass

    def parse_file(self, file_path: Path) -> Top:
        return self._run_parser(str(file_path))

    def parse_string(self, xml_content: str) -> Top:
        import io
        return self._run_parser(io.StringIO(xml_content))

    def _run_parser(self, source) -> Top:
        db_fd, db_path = tempfile.mkstemp(suffix=".sqlite")
        os.close(db_fd)
        
        try:
            conn = sqlite3.connect(db_path)
            self._init_db(conn)
            self._stream_to_db(source, conn)
            top = self._build_ast_from_db(conn)
            conn.close()
            return top
        finally:
            if os.path.exists(db_path):
                os.remove(db_path)

    def _init_db(self, conn: sqlite3.Connection):
        with closing(conn.cursor()) as cur:
            cur.executescript('''
                CREATE TABLE nodes (
                    id INTEGER PRIMARY KEY,
                    parent_class_id INTEGER,
                    parent_template_id INTEGER,
                    tag TEXT,
                    name TEXT,
                    kind TEXT,
                    type TEXT,
                    decl TEXT,
                    feature_ignore BOOLEAN,
                    is_template BOOLEAN
                );
                
                CREATE TABLE parms (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    node_id INTEGER,
                    name TEXT,
                    type TEXT,
                    idx INTEGER
                );
                
                CREATE TABLE enums (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    node_id INTEGER,
                    name TEXT,
                    value TEXT
                );
                
                CREATE TABLE bases (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    node_id INTEGER,
                    name TEXT
                );
                
                CREATE TABLE top_info (
                    module_name TEXT
                );
            ''')

    def _get_attrs(self, node: ET.Element) -> dict[str, str]:
        attrs = {}
        attr_list = node.find("attributelist")
        if attr_list is not None:
            for a in attr_list.findall("attribute"):
                attrs[a.get("name")] = a.get("value")
        return attrs

    def _extract_parms(self, node: ET.Element, node_id: int, cur: sqlite3.Cursor):
        def extract(p_node: ET.Element, idx: int):
            p_attrs = self._get_attrs(p_node)
            cur.execute('INSERT INTO parms (node_id, name, type, idx) VALUES (?, ?, ?, ?)', 
                        (node_id, p_attrs.get("name"), p_attrs.get("type"), idx))

        def scan(parent: ET.Element, idx_counter: list[int]):
            for child in parent:
                if child.tag == "parm":
                    extract(child, idx_counter[0])
                    idx_counter[0] += 1
                elif child.tag == "parmlist":
                    scan(child, idx_counter)
                    
        counter = [0]
        scan(node, counter)
        attr_list = node.find("attributelist")
        if attr_list is not None:
            scan(attr_list, counter)

    def _stream_to_db(self, source, conn: sqlite3.Connection):
        context = ET.iterparse(source, events=("start", "end"))
        
        stack = []
        class_stack = []
        template_stack = []
        node_id_seq = 1
        
        cur = conn.cursor()
        
        for event, elem in context:
            if event == "start":
                node_id = node_id_seq
                stack.append((elem, node_id))
                node_id_seq += 1
                
                if elem.tag == "class":
                    class_stack.append(node_id)
                elif elem.tag == "template":
                    template_stack.append(node_id)
                    
            elif event == "end":
                elem, node_id = stack.pop()
                
                if elem.tag == "class":
                    class_stack.pop()
                elif elem.tag == "template":
                    template_stack.pop()
                
                parent_class_id = class_stack[-1] if class_stack else None
                parent_template_id = template_stack[-1] if template_stack else None
                
                is_template_node = parent_template_id is not None
                
                if elem.tag == "top":
                    attrs = self._get_attrs(elem)
                    module_name = attrs.get("module", "Unknown")
                    cur.execute('INSERT INTO top_info (module_name) VALUES (?)', (module_name,))
                
                if elem.tag in ("class", "cdecl", "enum", "constructor", "destructor"):
                    attrs = self._get_attrs(elem)
                    ignore = attrs.get("feature_ignore") == "1"
                    name = attrs.get("name", "")
                    
                    if not name and elem.tag == "class":
                        pass # Ignore anonymous
                    else:
                        cur.execute('''
                            INSERT INTO nodes (id, parent_class_id, parent_template_id, tag, name, kind, type, decl, feature_ignore, is_template)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        ''', (node_id, parent_class_id, parent_template_id, elem.tag, name, attrs.get("kind"), 
                              attrs.get("type"), attrs.get("decl"), ignore, is_template_node))
                        
                        if elem.tag in ("cdecl", "constructor"):
                            self._extract_parms(elem, node_id, cur)
                            
                        if elem.tag == "enum":
                            for child in elem:
                                if child.tag == "enumitem":
                                    item_attrs = self._get_attrs(child)
                                    cur.execute('INSERT INTO enums (node_id, name, value) VALUES (?, ?, ?)',
                                                (node_id, item_attrs.get("name"), item_attrs.get("enumvalue")))
                                                
                        if elem.tag == "class":
                            def extract_bases(bl_node):
                                for base in bl_node.findall("base"):
                                    b_name = base.get("name")
                                    if b_name:
                                        cur.execute('INSERT INTO bases (node_id, name) VALUES (?, ?)', (node_id, b_name))
                            attr_list = elem.find("attributelist")
                            if attr_list is not None:
                                bl = attr_list.find("baselist")
                                if bl is not None: extract_bases(bl)
                            bl = elem.find("baselist")
                            if bl is not None: extract_bases(bl)

                # Always clear memory for these major tags
                if elem.tag in ("class", "cdecl", "enum", "constructor", "destructor", "template", "include", "namespace", "module"):
                    elem.clear()
                    if stack:
                        stack[-1][0].remove(elem)
                        
        # Prune cdecls inside templates that also have a class child
        cur.execute('''
            DELETE FROM nodes 
            WHERE tag = 'cdecl' 
            AND parent_template_id IN (
                SELECT parent_template_id FROM nodes 
                WHERE tag = 'class' AND parent_template_id IS NOT NULL
            )
        ''')
        conn.commit()

    def _build_ast_from_db(self, conn: sqlite3.Connection) -> Top:
        cur = conn.cursor()
        
        cur.execute('SELECT module_name FROM top_info LIMIT 1')
        row = cur.fetchone()
        module_name = row[0] if row else "Unknown"
        
        module = Module(name=module_name)
        
        # Load parms
        parms_by_node = {}
        cur.execute('SELECT node_id, name, type FROM parms ORDER BY node_id, idx')
        for node_id, name, type_ in cur.fetchall():
            parms_by_node.setdefault(node_id, []).append(Parm(name=name, type=type_))
            
        # Load enums items
        enum_items_by_node = {}
        cur.execute('SELECT node_id, name, value FROM enums')
        for node_id, name, value in cur.fetchall():
            enum_items_by_node.setdefault(node_id, []).append(EnumItem(name=name, value=value))
            
        # Load bases
        bases_by_node = {}
        cur.execute('SELECT node_id, name FROM bases')
        for node_id, name in cur.fetchall():
            bases_by_node.setdefault(node_id, []).append(name)
            
        nodes_by_id = {}
        
        cur.execute('SELECT id, parent_class_id, tag, name, kind, type, decl, feature_ignore, is_template FROM nodes WHERE feature_ignore = 0')
        rows = cur.fetchall()
        
        for r in rows:
            id_, parent_class_id, tag, name, kind, type_, decl, feature_ignore, is_template = r
            
            model = None
            if tag == "cdecl":
                if kind in ("function", "variable"):
                    model = CDecl(name=name, type=type_, kind=kind, decl=decl, parms=parms_by_node.get(id_, []))
            elif tag == "constructor":
                model = Constructor(name=name, parms=parms_by_node.get(id_, []))
            elif tag == "destructor":
                model = Destructor(name=name)
            elif tag == "enum":
                model = Enum(name=name, items=enum_items_by_node.get(id_, []))
            elif tag == "class":
                model = Class(name=name, kind=kind, is_template=is_template, bases=bases_by_node.get(id_, []))
                
            if model:
                nodes_by_id[id_] = (parent_class_id, tag, model)

        for id_, (parent_class_id, tag, model) in nodes_by_id.items():
            if parent_class_id is None:
                # Top level
                if tag == "cdecl": module.cdecls.append(model)
                elif tag == "class": module.classes.append(model)
                elif tag == "enum": module.enums.append(model)
            else:
                # Nested in class
                parent_data = nodes_by_id.get(parent_class_id)
                if parent_data:
                    parent_model = parent_data[2]
                    if tag == "cdecl": parent_model.cdecls.append(model)
                    elif tag == "constructor": parent_model.constructors.append(model)
                    elif tag == "destructor": parent_model.destructors.append(model)
                    elif tag == "enum": parent_model.enums.append(model)
                    elif tag == "class": parent_model.classes.append(model)
                    
        return Top(module=module)
