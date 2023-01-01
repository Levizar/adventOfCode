from tools import import_input_file
import pprint

instructions = import_input_file(True)

command = {
    "R": lambda x, y: (x + 1, y),
    "L": lambda x, y: (x - 1, y),
    "U": lambda x, y: (x, y + 1),
    "D": lambda x, y: (x, y - 1),
}

possible_moves = {
    (x, y)
    for x in range(-1, 2)
    for y in range(-1, 2)
}

def compute_vector(p1, p2):
    return p1[0] - p2[0], p1[1] - p2[1]


def compute_diff_vector(p1, p2):
    """compute vector going from p1 to p2"""
    return p2[0] - p1[0], p2[1] - p1[1]


def compute_add_vector(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])


def l1_norm(vector):
    return sum(map(abs, vector))


def is_distance_close_enough(head, tail):
    dx, dy = compute_vector(head, tail)
    return abs(dx) <= 1 and abs(dy) <= 1


def move_tail(head, tail):
    if is_distance_close_enough(head, tail):
        return tail

    possible_destinations = [compute_add_vector(tail, move) for move in possible_moves]
    closest_position = min(possible_destinations, key=lambda d: l1_norm(compute_diff_vector(d, head)))
    return closest_position


def move_head(head, direction):
    action = command.get(direction)
    return action(*head)


def move(nodes, direction):
    head, *nodes = nodes
    new_nodes = [move_head(head, direction)]
    for node in nodes:
        new_node = move_tail(new_nodes[-1], node)
        new_nodes.append(new_node)
    return new_nodes

def main():
    nodes = [(0, 0) for _ in range(10)]
    visited_coordinate = set()
    for instruction in instructions:
        direction, steps = instruction.split()
        for _ in range(int(steps)):
            nodes = move(nodes, direction)
            visited_coordinate.add(nodes[-1])
    print(len(visited_coordinate))


main()
