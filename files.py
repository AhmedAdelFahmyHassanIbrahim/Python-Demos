from pathlib import Path

cwd = Path.cwd()

demo_file = Path(Path.joinpath(cwd, 'demo.txt'))

print(f"file name: {demo_file.name}")

print(f"Suffix is: {demo_file.suffix}")

print(f"Parent is: {demo_file.parent}")