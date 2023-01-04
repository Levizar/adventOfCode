from tools import import_input_file
import pprint

instructions = import_input_file()

command = {
    "R": lambda x,y: (x+1,y),
    "L": lambda x,y: (x-1,y),
    "U": lambda x,y: (x,y+1),
    "D": lambda x,y: (x,y-1),
}


def compute_vector(p1, p2):
    return p1[0] - p2[0], p1[1] - p2[1]


def is_distance_close_enough(head, tail):
    dx, dy = compute_vector(head, tail)
    return abs(dx) <= 1 and abs(dy) <= 1


def move_head(head, direction):
    action = command.get(direction)
    return action(*head)


def move_tail(head, tail, previous_head):
    mx, my = compute_vector(head, tail)        
    if is_distance_close_enough(head, tail):
        # tail touches head, no move
        return tail

    # tails always take the previous place of head
    return previous_head
    

def move(head, tail, instruction):
    new_head = move_head(head, instruction)
    new_tail = move_tail(new_head, tail, head)
    return new_head, new_tail


def main():
    head = tail = (0, 0)
    visited_coordinate = set()
    for instruction in instructions:
        assert is_distance_close_enough(head, tail)
        direction, steps = instruction.split()
        for _ in range(int(steps)):
            head, tail = move(head, tail, direction)
            visited_coordinate.add(tail)
    print(len(visited_coordinate))
    
main()
