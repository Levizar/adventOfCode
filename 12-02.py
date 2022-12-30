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

    while not open_queue.empty():
        current = open_queue.get()[1]
        
        if current == goal:
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

    return []

def main():
    possible_start = []
    goal = 0
    for i, line in enumerate(height_map):
        for j, c in enumerate(line):
            if c in ("S", "a"):
                possible_start.append((i, j))
            if c == "E":
                goal = (i, j)


    def heuristic_function(node):
        # manhattan distance
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])
    
    solutions = [A_star(start, goal, heuristic_function) for start in possible_start]
    print(min([len(sol) - 1 for sol in solutions if sol]))


main()
