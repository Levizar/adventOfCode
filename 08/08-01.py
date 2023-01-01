from tools import import_input_file
import pprint

lines = import_input_file()

def get_square_representation(square):
    lines = []
    for i, line in enumerate(square):
        curr = []
        for j, tree in enumerate(line):
            v = "V" if tree["visible"] else "X"
            curr.append(f"{v}-{tree['height']}-{i}{j}")

        lines.append(" ".join(curr))
    return "\n\n".join(lines)

def compute_line_visibility(lines, visibility_point):
    max_height = -99
    print(f"\nnew line check, pov: {visibility_point}\n")
    print("before")
    pprint.pp(lines)
    for tree in lines:
        # print(f"max height: {max_height}, tree: {tree['height']}")
        if tree["height"] > max_height:
            max_height = tree["height"]
            tree["visible"] = True
    print("after:")
    pprint.pp(lines)

def main():
    square = [[{"height": int(c), "visible": None} for c in l] for l in lines]
    lenght = len(square)
    
    # compute horizontally
    for line in square:
        # from left
        compute_line_visibility(line, "left")
        # from right: left reversed
        compute_line_visibility(line[::-1], "right")
    
    # compute vertically
    flipped_line_and_column = list(zip(*square))
    for line in flipped_line_and_column:
        # from top
        compute_line_visibility(line, "top")
        # from bottom
        compute_line_visibility(line[::-1], "bottom")

    nbr_visible = sum(1 for line in square for tree in line if tree["visible"])
    print(nbr_visible)

    
main()
