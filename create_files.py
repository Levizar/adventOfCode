#!/usr/bin/env python3
import sys
import os


if __name__ == "__main__":
    
    folder_name = sys.argv[1]
    path = f"./{folder_name}"
    if not os.path.exists(path):
        os.makedirs(path)

    for file_name in ("input", "input-test"):
        with open(f"{path}/{file_name}", "w") as file:
            pass

    for file_name in ("01", "02"):
        lines = [
            "from tools import import_input_file",
            "import pprint",
            "",
            "",
            "lines = import_input_file(True)",
            "",
            "",
        ]
        with open(f"{path}/{path}-{file_name}.py", "w") as file:
            file.writelines("\n".join(lines))

