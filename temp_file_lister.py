import os
from pathlib import Path

directory = Path("tests/data/quantlib-1.40")

print(f"Directory exists: {directory.exists()}")
print(f"Directory is a directory: {directory.is_dir()}")

print("\nFiles in directory using os.listdir:")
for item in os.listdir(directory):
    path = directory / item
    print(f"  {item}: exists={path.exists()}, is_file={path.is_file()}")

print("\nFiles in directory using Path.iterdir():")
for path in directory.iterdir():
    print(f"  {path.name}: exists={path.exists()}, is_file={path.is_file()}")

sorted()
