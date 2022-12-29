from tools import import_input_file

lines = import_input_file()

def get_marker_index(line, size=14):
    for i, _ in enumerate(line):
        marker = line[i:i+size]
        if len(set(marker)) == size:
            return i + size

for line in lines:
    print(get_marker_index(line))

