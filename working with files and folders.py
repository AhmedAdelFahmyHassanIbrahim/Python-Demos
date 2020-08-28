from pathlib import Path

cwd = Path.cwd()
print(f'Current Working directory : {cwd}')

new_file = Path.joinpath(cwd, 'new_file.txt')
print(f"Full Path: {new_file}")

print(f"does the file exist? {new_file.exists()}")

parent = cwd.parent
print(f"is this a directory? {parent.is_dir()}")

# is this a file
print(f"is this a file? {parent.is_file()}")

#list Directory 
print("------------- directory contants -----------")
for child in parent.iterdir():
    if child.is_file():
        print(child)