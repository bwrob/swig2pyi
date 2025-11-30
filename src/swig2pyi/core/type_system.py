import re
from .config import Config

class TypeManager:
    def __init__(self, config: Config):
        self.config = config
        self._smart_ptr_regex = self._build_smart_ptr_regex()
        # Regex to strip SWIG type prefixes like p., r., q(const)., a(10).
        self._swig_prefix_regex = re.compile(r"([pqra](\([^)]*\))?\.)")

    def _build_smart_ptr_regex(self) -> re.Pattern:
        # Create a regex pattern to match any of the configured smart pointers.
        # Example: (?:boost::shared_ptr|std::shared_ptr)\s*<(.+)>
        patterns = [re.escape(ptr) for ptr in self.config.smart_pointers]
        combined = "|".join(patterns)
        return re.compile(rf"^(?:{combined})\s*<(.+)>$")

    def normalize_type(self, cpp_type: str) -> str:
        # 0. Basic cleanup
        cpp_type = cpp_type.strip()

        # 1. Remove SWIG internal type prefixes
        # e.g. p.q(const).char -> char
        # e.g. r.QuantLib::Date -> QuantLib::Date
        # We iterate because multiple prefixes can exist (e.g. p.r.)
        while True:
            new_type = self._swig_prefix_regex.sub("", cpp_type)
            if new_type == cpp_type:
                break
            cpp_type = new_type

        # 1b. Strip standard C++ qualifiers (const, volatile) that might remain or exist
        # We replace "const " with empty string. 
        cpp_type = cpp_type.replace("const ", "")
        cpp_type = cpp_type.replace("volatile ", "")
        cpp_type = cpp_type.strip()

        # Remove trailing reference (&) and pointer (*) characters.
        while cpp_type and (cpp_type.endswith("&") or cpp_type.endswith("*")):
            cpp_type = cpp_type[:-1].strip()
        
        # 1c. Strip surrounding parentheses if present
        # e.g. (Date) -> Date
        while cpp_type.startswith("(") and cpp_type.endswith(")"):
            cpp_type = cpp_type[1:-1].strip()

        # 2. Unwrap Smart Pointers
        # Check if the type matches a smart pointer pattern.
        match = self._smart_ptr_regex.match(cpp_type)
        if match:
            inner_type = match.group(1)
            return self.normalize_type(inner_type)

        # 3. Resolve Typedefs (Type Map)
        if cpp_type in self.config.type_map:
            return self.config.type_map[cpp_type]

        # 3a. Check module namespace prefix for typedefs
        # e.g. Integer -> QuantLib::Integer
        if self.config.module_name:
            namespaced_type = f"{self.config.module_name}::{cpp_type}"
            if namespaced_type in self.config.type_map:
                return self.config.type_map[namespaced_type]

        # 3b. Basic C++ types fallback
        basic_types = {
            "int": "int",
            "long": "int",
            "short": "int",
            "unsigned int": "int",
            "unsigned long": "int",
            "long long": "int",
            "unsigned long long": "int",
            "double": "float",
            "float": "float",
            "char": "str",
            "void": "None",
            "bool": "bool"
        }
        if cpp_type in basic_types:
            return basic_types[cpp_type]

        # 4. Handle Templates (Containers)
        for cpp_container, py_abc in self.config.containers.items():
            prefix = cpp_container + "<"
            if cpp_type.startswith(prefix) and cpp_type.endswith(">"):
                inner_content = cpp_type[len(prefix):-1].strip()
                normalized_inner = self.normalize_type(inner_content)
                return f"{py_abc}[{normalized_inner}]"
        
        # 5. Namespace resolution
        py_type = cpp_type.replace("::", ".")

        # 6. Strip module name if it's the current module
        if self.config.module_name and py_type.startswith(self.config.module_name + "."):
            py_type = py_type[len(self.config.module_name) + 1:]
        
        return py_type

    def to_python(self, cpp_type_str: str) -> str:
        """
        Public interface to convert a C++ type string to a Python type hint.
        """
        return self.normalize_type(cpp_type_str)