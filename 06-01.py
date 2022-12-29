from tools import import_input_file

lines = import_input_file()

line = lines[0]

def get_end_marker_index(line):
    for i, _ in enumerate(line):
        marker = line[i:i+4]
        if len(set(marker)) == 4:
            return i + 4

for line in lines:
    print(get_end_marker_index(line))

