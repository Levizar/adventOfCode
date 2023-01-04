from tools import import_input_file
import pprint
from queue import PriorityQueue
from collections import defaultdict
import heapq
import copy
import os
import time


lines = import_input_file()

height_map = [[c for c in line] for line in lines]
size_mapping = {chr(x): x - 96 for x in range(97, 97 + 26)}
size_mapping.update({"S": 1, "E": 26})
X_SIZE = len(height_map)
Y_SIZE = len(height_map[0])

space = "    "

def display_path_taken(current, a, came_from):
    i, j = current
    c = a[i][j]
    a[i][j] = "\N{ESC}[31m" + height_map[i][j] + "\u001b[0m"
    os.system("clear")
    print("")
    
    acopy = copy.deepcopy(a)
    path = reconstruct_path(came_from, current)
    for i, j in path[:-1]:
        acopy[i][j] = "\N{ESC}[94m" + height_map[i][j] + "\u001b[0m"
    
    to_print = []
    for line in acopy:
        to_print.append(space + "".join(line))
    
    print("\n".join(to_print))
    time.sleep(0.05)
    a[i][j] = "\N{ESC}[93m" + height_map[i][j] + "\u001b[0m"

def is_usable(current, target):
    (i, j), (x, y) = current, target
    if not ((0 <= x < X_SIZE) and (0 <= y < Y_SIZE)):
        return False

    current = height_map[i][j]
    target = height_map[x][y]
    return size_mapping[current] + 1 >=  size_mapping[target]
    
def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.insert(0, current)
    return path

def A_star(start, goal, h):
    open_queue = PriorityQueue()
    open_queue.put((0, start))

    came_from = dict()

    g_score = defaultdict(lambda : float('inf'))
    g_score[start] = 0

    f_score = defaultdict(lambda : float('inf'))
    f_score[start] = h(start)

    # for display purpose
    a = copy.deepcopy(height_map)

    while not open_queue.empty():
        current = open_queue.get()[1]
        
        # display_path_taken(current, a, came_from)

        if current == goal:
            display_path_taken(current, a, came_from)
            return reconstruct_path(came_from, current)
        
        i, j = current
        possible_goto_neighbours = tuple(
            neighbour for neighbour in (
                (i - 1, j), # left
                (i + 1, j), # right
                (i, j - 1), # up
                (i, j + 1), # down
            ) if is_usable(current, neighbour)
        )

        for neighbour in possible_goto_neighbours:
            tentative_g_score = g_score[current] + 1 # 1 is the function d(current, neighbour)
            if tentative_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = tentative_g_score
                f_score[neighbour] = tentative_g_score + h(neighbour)

                oqueue = [item for priority, item in open_queue.queue]
                if neighbour not in oqueue :
                    open_queue.put((f_score[neighbour], neighbour))

    raise Exception("No path possible")


def main():
    start = 0
    goal = 0
    for i, line in enumerate(height_map):
        for j, c in enumerate(line):
            if c == "S":
                start = (i, j)
            if c == "E":
                goal = (i, j)


    def heuristic_function(node):
        # manhattan distance
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    t = time.process_time()
    fastest_solution = A_star(start, goal, heuristic_function)
    print(len(fastest_solution) - 1)
    elapsed_time = time.process_time() - t
    print(f"{elapsed_time=}")


main()
