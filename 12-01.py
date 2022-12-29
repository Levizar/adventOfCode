from tools import import_input_file
import pprint


lines = import_input_file(True)

height_map = [[c for c in line] for line in lines]
size_mapping = {chr(x): x - 96 for x in range(97, 97 + 26)}
size_mapping.update({"S": 1, "E": 26})
X_SIZE = len(height_map)
Y_SIZE = len(height_map[0])

def is_usable(i, j, x, y):
    if not ((0 <= x < X_SIZE) and (0 <= y < Y_SIZE)):
        return False

    current = height_map[i][j]
    target = height_map[x][y]
    return size_mapping[current] + 1 >=  size_mapping[target]
    
import copy
import os
import time

space = "    "
def display_path_taken(i, j, a):
    c = a[i][j]
    a[i][j] = "\N{ESC}[31m" + c + "\u001b[0m"
    os.system("clear")
    print("")
    to_print = []
    for line in a:
        to_print.append(space + "".join(line))
    print("\n".join(to_print))
    time.sleep(0.1)
    a[i][j] = "\N{ESC}[93m" + c + "\u001b[0m"

def find_way(parent_path, i, j, a=None, mem={}):
    # if (i, j) in mem:
    #     return mem[(i, j)]

    # path: [(0,0), (1,0), (1,1), ...]
    # solutions: [path1, path2]

    # if a is None:
    #     a = copy.deepcopy(height_map)
    # else:
    #     a = copy.deepcopy(a)
    # display_path_taken(i, j, a)

    local_path = parent_path + [(i, j)]
    if height_map[i][j] == "E": # target reached
        return [[(i,j)]]

    possibilities = tuple(
        (x, y) for x, y in (
            (i - 1, j), # left
            (i + 1, j), # right
            (i, j - 1), # up
            (i, j + 1), # down
        ) if is_usable(i, j, x, y) and (x, y) not in parent_path
    )

    solutions = []
    for x, y in possibilities:
        paths = find_way(local_path, x, y, a)
        for path in paths:
            sol = [(i, j)] + path
            solutions.append(sol)

    solutions = tuple(solutions)
    mem[(i, j)] = solutions

    return solutions
    

def main():
    for i, line in enumerate(height_map):
        for j, c in enumerate(line):
            if c == "S":
                break
        if c == "S":
            break

    t = time.process_time()
    solutions = find_way([], i, j)
# elapsed_time=0.004279105000000005
    elapsed_time = time.process_time() - t
    print(f"{elapsed_time=}")

    a = [len(s) - 1 for s in solutions]
    print(min(a))
    solutions = tuple(tuple(sol) for sol in solutions)
    solutions = set(solutions)


    pprint.pprint(solutions)


    print(f"{len(solutions)=}")

main()
