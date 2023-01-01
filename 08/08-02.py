from tools import import_input_file
import pprint

lines = import_input_file()

def compute_line_visibility(line):
    for i, curr_tree in enumerate(line):
        max_j = 0
        for j, other_tree in enumerate(line[i+1:], start=1):
            max_j = j
            if curr_tree["height"] <= other_tree["height"]:
                break
        curr_tree["score"] *= max_j


def compute_square_visibility(square):
    # compute horizontally
    for line in square:
        # from left
        compute_line_visibility(line)
        # from right: left reversed
        compute_line_visibility(line[::-1])
    
    # compute vertically
    flipped_line_and_column = list(zip(*square))
    for line in flipped_line_and_column:
        # from top
        compute_line_visibility(line)
        # from bottom
        compute_line_visibility(line[::-1])

def main():
    square = [[{"height": int(c), "score": 1} for c in l] for l in lines]
    compute_square_visibility(square)
    max_score = max(tree["score"] for line in square for tree in line)
    print(max_score)

main()
