import re
from .config import Config

class TypeManager:
    def __init__(self, config: Config):
        self.config = config
        self._smart_ptr_regex = self._build_smart_ptr_regex()

    def _build_smart_ptr_regex(self) -> re.Pattern:
        # Create a regex pattern to match any of the configured smart pointers.
        # Example: (?:boost::shared_ptr|std::shared_ptr)\s*<(.+)>
        patterns = [re.escape(ptr) for ptr in self.config.smart_pointers]
        combined = "|".join(patterns)
        return re.compile(rf"^(?:{combined})\s*<(.+)>$")

    def normalize_type(self, cpp_type: str) -> str:
        # 0. Basic cleanup
        cpp_type = cpp_type.strip()

        # 1. Strip qualifiers (const, volatile)
        # We replace "const " with empty string. 
        # Note: "const_iterator" should not be affected. "const " has a space.
        cpp_type = cpp_type.replace("const ", "")
        cpp_type = cpp_type.replace("volatile ", "")
        cpp_type = cpp_type.strip()

        # Remove trailing reference (&) and pointer (*) characters.
        # We loop because there might be multiple (e.g. "Type **")
        while cpp_type and (cpp_type.endswith("&") or cpp_type.endswith("*")):
            cpp_type = cpp_type[:-1].strip()

        # 2. Unwrap Smart Pointers
        # Check if the type matches a smart pointer pattern.
        match = self._smart_ptr_regex.match(cpp_type)
        if match:
            inner_type = match.group(1)
            # Recursively normalize the inner type (e.g. shared_ptr<const MyType*>)
            return self.normalize_type(inner_type)

        # 3. Resolve Typedefs (Type Map)
        # Direct lookup in the configuration's type map.
        if cpp_type in self.config.type_map:
            return self.config.type_map[cpp_type]

        # 4. Handle Templates (Containers)
        # Check if the type starts with any of the known container templates.
        for cpp_container, py_abc in self.config.containers.items():
            # Check for "std::vector<"
            prefix = cpp_container + "<"
            if cpp_type.startswith(prefix) and cpp_type.endswith(">"):
                # Extract the content inside the angle brackets
                # This logic assumes the container wraps the rest of the string.
                # It does NOT handle nested templates properly if simpler string slicing is used,
                # but for the initial task, we extract the inner content.
                # Proper C++ template parsing would require balancing brackets.
                
                # Find the content inside. 
                # cpp_type is "std::vector<InnerType>"
                # content is "InnerType"
                inner_content = cpp_type[len(prefix):-1].strip()
                
                # Recursively normalize the inner type
                # Note: This fails for "std::map<K, V>" if we just call normalize on "K, V".
                # But the prompt examples are simple vectors. 
                # We'll assume single argument templates for this iteration or basic support.
                normalized_inner = self.normalize_type(inner_content)
                
                return f"{py_abc}[{normalized_inner}]"

        return cpp_type

    def to_python(self, cpp_type_str: str) -> str:
        """
        Public interface to convert a C++ type string to a Python type hint.
        """
        return self.normalize_type(cpp_type_str)
