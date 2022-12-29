import sys
from pathlib import Path


def import_input_file(is_test=False):
    full_path = sys.argv[0]
    script_file_name = Path(sys.argv[0]).stem
    input_file = f"{script_file_name[:3]}input"
    if is_test:
        input_file += "-test"
    with open(input_file) as file:
        lines = file.read().splitlines()
    return lines


def import_input_file_raw(is_test=False):
    full_path = sys.argv[0]
    script_file_name = Path(sys.argv[0]).stem
    input_file = f"{script_file_name[:3]}input"
    if is_test:
        input_file += "-test"
    with open(input_file) as file:
        lines = file.read()
    return lines

