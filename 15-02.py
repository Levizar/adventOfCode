from tools import import_input_file_raw
import re


def main():
    test = False
    lines = import_input_file_raw(test)
    detection_range = parse_input(lines)
    print("")

    bob = 4_000_000
    if test:
        bob = 20
    # line_range = {x for x in range(bob + 1)}
    print(f"{bob=}")

    lines = dict()  # set of range
    for sensor, _range in detection_range.items():
        s_x, s_y = sensor

    print(lines)


def parse_input(lines):
    # the regex will match twice in the following example
    # Sensor at x=2, y=18: closest beacon is at x=-2, y=15
    # this regex match sensor and beacon one by one
    # regex = re.compile(r"(?P<type>Sensor|beacon).*?x=(?P<x>-?\d+), y=(?P<y>-?\d+)")
    # this regex match senser and beacon together:
    regex = re.compile(r"x=(?P<xs>-?\d+), y=(?P<ys>-?\d+).*?x=(?P<xb>-?\d+), y=(?P<yb>-?\d+)")
    # try to match the whole raw string
    detection_range = dict()
    for matches in regex.finditer(lines):
        p_sensor = (int(matches.group("xs")), int(matches.group("ys")))
        p_beacon = (int(matches.group("xb")), int(matches.group("yb")))
        detection_range.update({p_sensor: manhattan_distance(p_sensor, p_beacon)})

    return detection_range


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


if __name__ == "__main__":
    main()
