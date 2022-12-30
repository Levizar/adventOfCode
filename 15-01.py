from tools import import_input_file_raw
import itertools
import re


def main():
    lines = import_input_file_raw()
    space_positions, sensor_position, beacon_position, wtf = parse_input(lines)
    # covered_position = get_sensor_coverage(space_positions)
    print("")
    # print(sum(1 for p in covered_position if p[1] == 10))
    # sp = copy.deepcopy(space_positions)
    # get_sensor_coverage(sp)
    # draw_stuff(sp)
    # print("---------")

    positions = [key for key in space_positions.keys()]

    xmin = min(positions, key=lambda p: p[0])[0]
    xmax = max(positions, key=lambda p: p[0])[0]
    ymin = min(positions, key=lambda p: p[1])[1]
    ymax = max(positions, key=lambda p: p[1])[1]

    covered = set()
    bob = 2000000
    # bob = 10
    # for y in range(ymin, ymax + 1):
    for y in range(bob, bob + 1):
        plop = set()
        for (i, j), sensor_range in wtf.items():
            xrange = sensor_range - abs(y - j)
            if xrange > 0:
                a = {*range(i - xrange, i + xrange + 1)}
                plop |= a
        covered |= {x for x in plop if (x, y) not in space_positions}
    # print(covered)
    # draw_stuff(space_positions)
    print(len(covered))


def parse_input(lines):
    # the regex will match twice in the following example
    # Sensor at x=2, y=18: closest beacon is at x=-2, y=15
    # this regex match sensor and beacon one by one
    # regex = re.compile(r"(?P<type>Sensor|beacon).*?x=(?P<x>-?\d+), y=(?P<y>-?\d+)")
    # this regex match senser and beacon together:
    regex = re.compile(r"x=(?P<xs>-?\d+), y=(?P<ys>-?\d+).*?x=(?P<xb>-?\d+), y=(?P<yb>-?\d+)")
    # try to match the whole raw string
    space_positions = dict()
    sensor_position = set()
    beacon_position = set()
    wtf = dict()
    for matches in regex.finditer(lines):
        p_sensor = (int(matches.group("xs")), int(matches.group("ys")))
        p_beacon = (int(matches.group("xb")), int(matches.group("yb")))
        manhattan_distance = abs(p_sensor[0] - p_beacon[0]) + abs(p_sensor[1] - p_beacon[1])
        sensor_position.add(p_sensor)
        beacon_position.add(p_beacon)

        # overkill but useful to transport information to draw_stuff
        space_positions.update({
            p_sensor: {
                "type": "sensor",
                "range": manhattan_distance,
            },
            p_beacon: {
                "type": "beacon",
            },
        })

        wtf.update({p_sensor: manhattan_distance})

    return space_positions, sensor_position, beacon_position, wtf


def get_sensor_coverage(space_positions):
    # exponential complexity: doesn't work for bigger input
    covered_position = set()

    def fill_this_sensor_coverage(i, j, manhattan_distance):
        for k in range(0, manhattan_distance + 1):
            for l in range(0, manhattan_distance + 1 - k):
                m = manhattan_distance - l - k
                for n, o in itertools.product((l, -l), (m, -m)):
                    position = (i + n, j + o)
                    if position not in space_positions:
                        covered_position.add(position)
                    space_positions.setdefault(position, {"type": "covered"})
                    # space_positions.update({position: {"covered": True}})

    beacons = [(i, j, v.get("range")) for (i, j), v in space_positions.items() if v.get("type") == "sensor"]
    for i, j, manhattan_distance in beacons:
        fill_this_sensor_coverage(i, j, manhattan_distance)

    return covered_position


def draw_stuff(space_positions):
    positions = [key for key in space_positions.keys()]

    xmin = min(positions, key=lambda p: p[0])[0]
    xmax = max(positions, key=lambda p: p[0])[0]
    ymin = min(positions, key=lambda p: p[1])[1]
    ymax = max(positions, key=lambda p: p[1])[1]

    visual_map = {
        "beacon": "B",
        "sensor": "S",
        "covered": "#",
    }

    rep = {
        k: visual_map.get(v.get("type"), ".")
        for k, v in space_positions.items()
    }
    
    print("")
    for y in range(ymin, ymax + 1):
        print(f"{y: >3} " + "".join([rep.get((x, y), ".") for x in range(xmin - 5, xmax + 5)]))


if __name__ == "__main__":
    main()
