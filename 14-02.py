from tools import import_input_file
from collections import defaultdict
from copy import deepcopy
import pprint
import os
import time


def main():
    rock_lines_raw = import_input_file(True)
    rock_coordinates = compute_rocks_coordinates(rock_lines_raw)
    
    cave_representation = {(x, y): "rock" for (x, y) in rock_coordinates}
    cave_representation.update({
        "xmin": min(rock_coordinates, key=lambda p: p[0])[0],
        "xmax": max(rock_coordinates, key=lambda p: p[0])[0],
        # "ymin": min(rock_coordinates, key=lambda p: p[1])[1],
        "ymin": 0,
        "ymax": max(rock_coordinates, key=lambda p: p[1])[1] + 2,
    })
    
    add_sand(cave_representation)

    print(sum(1 for v in cave_representation.values() if v == "sand"))

def compute_rocks_coordinates(rock_lines_raw):
    rocks_coordinates = set()
    for rock_line_raw in rock_lines_raw:
        points = [tuple(map(int, x.split(","))) for x in rock_line_raw.split(" -> ")]
        
        a = points.pop(0)
        while points:
            b = points.pop(0)
            
            xa, ya = a
            xb, yb = b
            if xa > xb:
                xa, xb = xb, xa
            if ya > yb:
                ya, yb = yb, ya

            rocks_coordinates.update([(x, y) for x in range(xa, xb + 1) for y in range(ya, yb + 1)])
            a = b

    return rocks_coordinates


def add_sand(cave_representation):
    sand_spawn_point = (500, 0)
    sand = get_falling_position(sand_spawn_point, cave_representation)
    while sand:
        cave_representation.update({sand: "sand"})
        if sand == sand_spawn_point:
            break
        sand = get_falling_position(sand_spawn_point, cave_representation)

def get_falling_position(sand, cave_representation):
    previous_position = sand
    sand = next_position(sand, cave_representation)
    while sand != previous_position:
        previous_position = sand
        sand = next_position(sand, cave_representation)
        
        cp = deepcopy(cave_representation)
        cp.update({sand: "sand"})
        draw_stuff(cp)

    return sand

def next_position(sand, cave_representation):
    if sand[1] == cave_representation.get("ymax") - 1:
        # below, it's the floor, can't go further
        return sand

    below_left, below, below_right = ((sand[0] + x, sand[1] + 1) for x in (-1, 0, 1))
    for next_position in (below, below_left, below_right):
        if next_position not in cave_representation:
            return next_position

    return sand


def draw_stuff(cave_representation):
    added = 7
    # get min and max x and y
    xmin = cave_representation.get("xmin")
    xmax = cave_representation.get("xmax")
    ymin = cave_representation.get("ymin")
    ymax = cave_representation.get("ymax")

    rep = {
        k: "#" if v == "rock" else "+"
        for k, v in cave_representation.items()
    }
    
    os.system("clear")
    for y in range(ymin - added, ymax + added):
        line = "".join([rep.get((x, y), ".") for x in range(xmin - added, xmax + added)])
        if y == ymax:
            line = "".join(["#" for x in range(xmin - added, xmax + added)])
        print(line)
    time.sleep(0.05)

main()
    
