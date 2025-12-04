import time
from pathlib import Path
import sys

# Ensure the project root is in the path to find swig2pyi modules
sys.path.insert(0, str(Path(__file__).parent))

from src.swig2pyi.core.config import Config
from src.swig2pyi.api import generate_from_interface

def run_full_test() -> None:
    base_dir = Path(__file__).parent / "tests"
    # Point to the FULL quantlib.i
    interface_file = base_dir / "data" / "quantlib-1.40" / "quantlib.i"
    config_file = base_dir.parent / "src" / "swig2pyi" / "rules" / "quantlib.json"
    output_dir = base_dir / "expected_output" / "QuantLib"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "__init__.pyi"

    assert interface_file.exists(), f"Interface file not found: {interface_file}"
    assert config_file.exists(), f"Config file not found: {config_file}"

    config = Config.from_file(config_file)

    start_time = time.time()
    
    try:
        generate_from_interface(interface_file, config, output_file)
        print(f"Generation completed in {time.time() - start_time:.2f} seconds.")
        print(f"Output written to {output_file}")
    except Exception:
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    run_full_test()