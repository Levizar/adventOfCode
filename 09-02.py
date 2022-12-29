from tools import import_input_file
import pprint

instructions = import_input_file()

vector_mapping = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}

possible_moves = {
    (x, y)
    for x in range(-1, 2)
    for y in range(-1, 2)
}

def compute_diff_vector(p1, p2):
    """compute vector going from p1 to p2"""
    return p2[0] - p1[0], p2[1] - p1[1]


def compute_add_vector(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])


def l1_norm(vector):
    return sum(map(abs, vector))


class Node():
    def __init__(self, position=(0, 0)):
        self.position = position
        self.next_node = None

    def is_distance_next_node_close_enough(self):
        if not self.next_node:
            return True

        dx, dy = compute_diff_vector(self.position, self.next_node.position)
        return abs(dx) <= 1 and abs(dy) <= 1

    def compute_possible_destination(self):
        return [compute_add_vector(self.position, move) for move in possible_moves]

    def move(self, previous_node_position):
        destination_distance_couple = [
            (destination, l1_norm(compute_diff_vector(destination, previous_node_position)))
            for destination in self.compute_possible_destination()
        ]
        closest_position = min(destination_distance_couple, key=lambda x: x[1])[0]
        self.position = closest_position

    def pull_next_node(self):
        if self.next_node and not self.is_distance_next_node_close_enough():
            self.next_node.move(self.position)


class Rope():
    def __init__(self, length):
        self.head = Node()
        node = self.head
        for _ in range(length - 1):
            node.next_node = Node()
            node = node.next_node
        self.tail = node

    def __iter__(self):
        self.next_node = self.head
        return self

    def __next__(self):
        current_node = self.next_node
        if current_node is None:
            raise StopIteration
        self.next_node = current_node.next_node
        return current_node

    def move(self, move):
        self.head.position = compute_add_vector(self.head.position, move)
        for node in self:
            node.pull_next_node()

    def assert_integrity(self):
        node = self.head
        while node:
            if node.next_node:
                assert node.is_distance_next_node_close_enough()
            node = node.next_node


def draw(rope):
    length = 40

    def transpose_in_graph(position):
        x, y = position
        return x + int(length / 2), y + int(length / 2)

    grid = [["." for _ in range(length)] for _ in range(length)]
    for i, node in enumerate(rope):
        x, y = transpose_in_graph(node.position)
        grid[-y][x] = str(i)

    for i, row in enumerate(grid):
        print(" ".join([f"{i:02d}"] + row))


def main():
    visited_coordinate = set()
    rope = Rope(10)
    # draw(rope)
    for instruction in instructions:
        rope.assert_integrity()
        direction, steps = instruction.split()
        for i in range(int(steps)):
            rope.assert_integrity()
            move = vector_mapping.get(direction)
            rope.move(move)
            visited_coordinate.add(rope.tail.position)
            # i = f" {i+1:02d} "
            # print(f"{' ' + instruction + str(i):=^80}")
            # draw(rope)
        # print(f"{' ' + instruction + ' ':=^80}")
        # draw(rope)

    print(len(visited_coordinate))


main()
