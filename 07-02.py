from tools import import_input_file
import pprint

lines = import_input_file(True)


HARDWARE_SIZE = 70000000
REQUIRED_SPACE_FOR_UPDATE = 30000000
datas = {
    "/": {
       "type": "directory",
       "path": "/",
       "content": [],
    }
}

path_stack = []
def cd(path):
    if path == "/":
        path_stack.clear()
    elif path == "..":
        path_stack.pop()
    else:
        path_stack.append(path)

def ls(line_iter):
    line = next(line_iter)
    current_path = "/" + "/".join(path_stack)
    current_dir = datas[current_path]
    while line[0] != "$":
        line = line.split()
        name = line[1]
        path = f"{current_path}/{name}" if current_path != "/" else f"/{name}"
        current_dir["content"].append(path)
        if line[0] == "dir":
            datas[path] = {
                "type": "directory",
                "path": path,
                "content": [],
                "size": None,
            }
        else:
            datas[path] = {
                "type": "file",
                "path": path,
                "size": int(line[0]),
            }
        try:
            line = next(line_iter)
        except StopIteration:
            return

    return line

def compute_size_recursively(path):
    data = datas[path]
    if data["type"] == "file":
        return data["size"]
    elif data["type"] != "directory":
        raise Exception

    # it's a directory
    contents_size = [compute_size_recursively(path) for path in data["content"]]
    data["size"] = sum(contents_size)
    return data["size"]

def find_directory_to_delete(min_size_to_free):
    candidate_directories = [d for d in datas.values() if d["type"] == "directory" and d["size"] >= min_size_to_free]
    smallest_directory = min(candidate_directories, key=lambda d:d["size"])
    return smallest_directory

def main():
    line_iter = iter(lines)
    line = next(line_iter)
    while line:
        line = line.split()
        if line[0] == "$":
            if line[1] == "cd":
                cd(line[2])
                line = next(line_iter)
            elif line[1] == "ls":
                line = ls(line_iter)
    compute_size_recursively("/")
    
    occupied_space = datas["/"]["size"]
    free_space = HARDWARE_SIZE - occupied_space
    space_needed = REQUIRED_SPACE_FOR_UPDATE - free_space
    directory_to_delete = find_directory_to_delete(space_needed)
    pprint.pp(datas)
    print(directory_to_delete)
    

main()
