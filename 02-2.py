SEPERATOR = "\n"
IN_BETWEEN_SEPERATOR = " "

def chose_shape(theirs, desired_result):
    beated_by_map = {
        "rock": "paper",
        "paper": "scissors",
        "scissors": "rock",
    }
    if desired_result == "draw":
        return theirs
    elif desired_result == "win":
        return beated_by_map[theirs]
    else:
        for shape in beated_by_map.keys():
            if shape not in (theirs, beated_by_map[theirs]):
                return shape

def compute_all_points(string):
    alias = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "lose",
        "Y": "draw",
        "Z": "win",
    }
    points = {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
        "lose": 0,
        "draw": 3,
        "win": 6,
    }
    rounds = string.split(SEPERATOR)
    my_points_per_round = []
    for r in rounds:
        their_coded_shape, coded_match_result = r.split(IN_BETWEEN_SEPERATOR)
        their_shape, match_result = alias[their_coded_shape], alias[coded_match_result]
        my_shape = chose_shape(their_shape, match_result)
        round_points = points[my_shape] + points[match_result]
        my_points_per_round.append(round_points)
    return sum(my_points_per_round)

a = compute_all_points(
"""B Z
A X
C X
C X
C Z
C X
C X
A Z
C X
B Z
B Z
C X
A X
C X
C X
C X
C Y
C X
C Z
C X
C X
C X
C X
C X
C Z
C X
C X
A X
C X
B Y
A X
B X
A Z
C X
B Y
A X
C Z
C X
C Z
A X
A Y
B Z
A Z
C X
A Z
A Z
A Y
C Y
A Y
A Z
C X
A Y
B Y
A Z
B Y
C Z
A X
C X
C Z
B Z
C X
B Y
C X
A Z
C X
A X
C X
C X
A Z
B Z
C X
C X
C Z
C X
B X
C X
A Z
A X
A Y
A Y
A Z
C X
C Z
C X
B Y
C X
C X
A X
A X
C Z
C X
B X
C Z
C X
C X
C X
B Z
B Y
A Z
C X
A Z
C X
C Z
A Z
C X
A X
C X
C Z
C Z
C X
C Z
A Y
C X
A X
A Z
A X
C Y
B X
C X
A X
A Y
A X
B Y
A X
C X
B Y
A Z
C X
B X
C X
A Y
C Z
C X
C Z
C X
A Y
A Z
C X
A Z
B Y
C X
A Z
C X
C Z
B Z
C X
C Z
C X
C Z
C X
A Y
C X
C X
A Z
C Z
C X
A X
C X
C X
B Y
C X
C X
C X
C X
C X
A Y
C Z
C X
C X
C Z
B X
C X
C X
C Z
B Y
B Y
C X
C X
A Z
C Z
C X
C Z
C X
A Y
A X
A X
A Y
C X
C X
C X
A Z
B Z
C Z
A Y
A Y
C X
C X
B Y
C X
C X
C X
A Z
B Y
B Y
C X
C Y
C X
C Z
B Y
C X
C X
C Z
A X
B Y
C X
A Z
C X
A Z
C X
A Z
C X
C Z
C X
A Z
C X
A X
C Z
A Z
A Y
C X
C Z
B Y
A Z
C X
B Y
B X
A Z
C X
C Y
A X
C Z
A X
C Z
C Z
C Z
A Z
C X
C X
A Z
C X
A X
C X
B X
C X
C X
C Z
C X
C X
C Z
C X
A Y
C Z
C Z
A X
A Z
B X
C X
C X
B X
C Y
C X
A Y
C Z
A X
C X
A Y
A Z
C X
A Y
A Z
A Z
C Z
C X
A Y
C X
A X
C X
C X
C X
A Z
C X
C X
A Z
A X
C X
B Y
B X
C X
C X
A Y
A Z
B Z
C Z
A Z
A X
C Z
A X
C X
B X
C X
B X
C X
A X
C Z
C X
A Z
A Y
C X
C Z
C X
A X
C X
B Y
A Z
C X
C Z
A X
C X
A Z
C X
B Y
C X
C Y
C Y
B Z
C Z
A X
B Z
C X
C X
A Z
A X
C X
A X
B Z
A Z
B Y
B Y
C X
C X
A Z
A Z
B Z
A Z
A Z
A Z
B Y
C Z
A Y
A X
C X
C X
C X
C X
C Z
B Y
C X
A Z
B Y
B Y
C X
C X
A X
C X
C Z
C X
A X
A Z
C Z
C Z
B Z
B Y
C Z
C Z
A X
B Y
C X
C Z
B Y
C X
C X
C X
C X
B Z
C X
B X
C Y
C Z
A Z
C X
C X
C X
A Z
C X
B Z
C Z
C Z
C X
C Z
A Z
C X
C X
C X
C Z
C Z
C X
C X
C Z
C X
C Z
C X
A Z
C X
B Z
B X
B Z
A Z
A Z
B Y
C Y
C X
C X
C X
C X
A X
C X
A X
C X
C X
A Z
C X
C X
B Y
C Z
C X
C X
A Y
A X
C Z
C Z
C X
C X
C X
B X
C Z
C X
C X
C X
B X
A Y
B Z
C X
B Y
C X
C X
C X
B X
B Y
A Z
A Z
A Z
C X
A Z
C Z
B Z
C X
A Z
C X
C X
C X
A Y
B Y
C X
B Y
C Z
C X
B X
A Z
C X
A X
C X
C Z
C Z
B Y
C Z
C X
C X
B X
C X
C X
C X
C X
A Z
B Y
A X
C X
A Y
B X
A Z
A Z
C X
A Y
C Z
A Z
A X
A Y
C X
C Z
C Z
C Z
C X
B Y
C X
A Y
C X
A Z
C X
C Z
C X
B X
C Z
C Y
C X
B Z
A X
B X
C X
B Y
C Z
C Z
C Z
C X
A Z
C Z
C X
C X
C X
B Z
C X
C X
A Z
C X
A Z
C Z
A Z
A Z
A Z
C X
A X
C X
A Z
A Y
C X
A Z
C X
B Y
A X
C Z
A Z
C Z
A Y
C X
A Z
C Z
C X
C X
C X
C Y
C X
A Y
A Z
A X
C Z
C Z
A Y
C X
C X
B Y
B Z
C X
B Y
C Z
C Z
C X
C Z
B Y
C Z
B Y
C Z
B Y
C X
A X
A X
C X
A Z
A Z
C X
C X
B Y
A Z
C Z
A X
C Z
C X
C Y
A Z
A Z
C X
C X
A X
C X
C Z
C X
B Z
C X
A Z
A Z
C X
A Z
A X
A Z
C Y
B Y
C X
C X
C Z
C Z
C Z
C Z
C X
A X
C X
B Y
C X
B Y
B Y
B X
C X
C X
C X
C X
C X
C Z
A X
C X
C X
A Z
A Z
C X
A Z
C X
C Z
C X
B Z
A Z
C X
C X
C X
C Z
A Z
B Y
C X
C X
C Z
C X
C X
C X
A Z
B Z
A X
C Z
C X
C X
A X
C X
C X
C X
A Z
A Y
C Y
C Z
C X
C Z
C Z
A Z
C X
C X
B X
C Z
A Y
C X
C X
C X
C Z
C X
C Z
C X
C X
C X
B X
C X
A Z
B X
B Y
C X
A Z
A Z
C X
A Y
C X
C Z
A Z
B Z
A Z
B Y
A X
A Y
B X
C X
B Z
C Z
B Y
C X
A Z
C Z
C Z
C Z
B X
C X
A X
B Y
C X
C X
A X
B Z
B X
C X
C X
A X
C X
C X
C X
C X
C Z
C X
A Z
B Y
A Y
B Y
A X
C X
A Y
A Z
C X
C X
B Y
C X
B Y
C Z
C X
C X
B Y
C X
A Z
C Z
C X
C X
C Z
C X
C X
B Y
B Y
C X
C X
C X
C X
C X
A Z
C X
C X
B Z
B Y
A Z
C X
C X
C X
A Y
C X
A Y
A X
A Z
B X
C X
A X
B X
A Z
C Z
C X
A Z
A X
C X
C X
C X
C X
B Z
A X
A X
C Z
C X
C X
A Y
C Z
C X
B Y
C X
B Y
C X
C X
B X
C X
A Z
C Z
C X
C X
C X
C X
A Z
A Y
C Z
C X
B X
A Y
A X
A X
B X
C X
C X
A X
C X
C Z
A X
C Z
C X
B Y
C X
C X
C Z
C X
B Z
C X
C X
C Z
B Z
C X
C Z
A Z
C X
B X
C X
C X
C X
C X
C X
C X
A Z
A Z
B Z
A Y
A Z
B X
A Y
B Y
C X
C X
C Z
C X
C X
C X
A Y
C X
C X
B X
C Z
C X
C X
C X
C X
B Y
A Y
C X
A Z
C X
C X
C Z
C X
C Z
C X
C X
B Y
A Z
B X
A X
C X
C Z
C X
C X
C X
C X
C X
B Z
C X
C X
C Z
B Y
C X
B Y
C X
C X
C X
C X
C Z
C X
A Y
C X
C Z
A Y
A X
B Z
C Z
C X
A X
C X
A Y
C X
C X
B X
C X
B X
B Z
A Z
A X
C X
A Z
C X
C X
C X
C X
A Y
C Y
A X
C Z
A Y
C X
A Z
C X
C X
C X
A Y
C X
C X
C X
C X
A X
C X
A Z
A Z
A X
A Z
C Z
C X
B Y
A Y
C X
C X
C X
C X
A Z
C X
A Z
B X
B Y
C X
A Z
A X
C X
C Z
C X
C X
C Z
C X
C Z
B X
C X
C X
C X
A X
A Z
C Z
C Y
C X
A Y
B Y
C X
B Y
C X
C X
C X
A Z
C X
B Z
A Y
C X
C X
B Y
A X
C Z
C X
B Y
C Z
A Y
B Y
B Z
C X
C X
A Z
C X
C Z
C Y
A X
B Y
C Y
A X
C Z
C Y
C X
A Y
B Z
C X
A Z
C X
B Y
C X
C Y
C X
C Z
C X
A Z
C Z
C X
C X
C X
B X
A Z
C X
C X
C Z
C Y
C Z
C X
C X
C Z
A X
C Z
C Y
B Y
C X
B Y
C Z
C X
C X
C X
A X
B X
C X
B Z
A Y
C X
C Z
B Y
C X
C X
C X
C Z
C X
C X
C X
C X
A Y
C X
B X
C Y
A X
B Y
A Z
C X
C X
A Z
C Z
C X
C Z
A Y
A X
C Z
A Z
C Y
A Z
B Y
C X
A Z
C X
C Z
C X
C X
C X
C X
C X
C X
C X
C X
C X
C X
C X
C X
C Z
B X
A Y
C X
C X
C Z
A Y
A Z
A Z
B Y
C X
C Z
C X
C Z
C X
C X
C X
C X
A Z
A X
A Z
C X
A Y
B Y
C X
C Y
A Z
B X
C Z
A X
C X
C X
C X
C X
C X
A Y
A Z
C X
C X
A X
C Z
A Z
A X
C X
B Y
A X
C Z
B Y
C X
A Z
B Z
C X
C Z
C Z
B X
B Y
C Z
A X
C Z
C Z
A Y
A Y
C X
C X
C X
C X
A Y
C X
A Z
C X
C X
C X
C X
C X
B Y
C Z
C X
C X
C Z
C X
C X
B Z
C X
A Z
A Z
C X
A X
C X
C X
B Z
C X
A Z
C X
B X
C X
C Z
C X
A X
C X
B Y
A X
C Z
C Z
C X
C X
C Z
C X
C X
C X
A Z
A X
C X
B X
C Z
A Z
C Z
B Z
C X
A X
C X
C X
C Z
C X
A Y
A Y
C Z
C X
B Y
B Z
C X
B X
C X
C X
A Z
C Z
C Z
C X
B X
A Z
C X
C Z
A X
C Z
C Z
A Z
A Y
A Z
C X
C X
C X
A Z
A Y
C X
A Z
B Z
C X
B X
B X
C Z
C Z
C Z
C X
C X
C X
A Z
C X
C X
C X
C X
A Z
C X
C Y
A X
C X
C X
B Y
C X
C X
A X
C Z
C Z
C Z
A Z
C X
C X
C X
A Y
C Z
C X
C X
C X
C Y
C Z
C X
C X
C X
C X
A Z
C X
C X
A X
C X
A X
C X
C X
A Z
C X
C X
A Y
C Z
A X
A Y
C X
A Z
B Y
B Y
A X
C Z
C X
C X
C X
A X
A Z
B Y
C X
A Y
C X
C X
B Y
C X
C X
C X
B Y
C X
C Z
C X
C Z
A Y
B Y
C X
C Z
C X
B X
A Z
C Z
C Z
C Z
C X
B Z
C X
B X
C Y
C Z
C X
C X
C Z
A Z
B X
C X
C X
A Z
C X
A Z
C X
A Y
C X
C Z
A Z
A X
C X
B X
C X
C X
C X
C Y
B X
C X
B Y
C X
C Y
A Z
A Y
C X
A Z
C Z
A Y
B Y
C Z
A X
A X
B X
C X
C X
C Z
A X
B Y
A X
C Z
C X
C X
C X
A X
C X
C X
C X
C Y
C X
C X
C Z
C X
C X
C X
A Z
B X
A Z
C X
A X
C X
B Y
B Z
C X
C X
A Z
C X
A Y
B X
C X
C X
C Z
B Y
C X
A Y
C X
B Z
C X
A Z
C Z
C X
C X
C X
C Z
A X
B X
C Z
B Y
C Z
C X
B Y
A Z
C X
C X
C X
C X
C Z
A X
A Y
A Z
C X
C X
B Y
B Y
C X
A X
B Y
A Y
C X
C X
C X
A X
B X
B Y
A Z
C X
C X
C Z
A X
C X
A X
A Z
C X
A Z
C X
C Z
C Z
B Z
C X
B Y
C Z
C X
A Z
C X
C X
C X
C X
C X
C Y
C X
C X
A Z
C X
A X
A Y
B Y
C X
A Y
B X
C Z
C X
A Z
C X
C X
C X
A Z
B Z
C Z
B Z
C X
C X
C Y
C Z
C X
C Z
C X
C X
C X
B X
C X
C X
A Z
B Y
C Z
C Z
C X
A Z
B Y
A X
C X
A Z
C Z
C X
C X
A Z
A X
C Y
B Z
A X
C X
A Z
C X
C Z
A Z
C X
A Y
C X
C X
B Z
C X
C Z
A Z
A Z
C X
B Z
B X
A Z
A X
C X
C X
C X
C Z
C X
A X
C X
C X
B X
C Z
C X
C X
C Y
A Z
B Y
A Z
B Y
C X
A Z
C Z
C Y
B Z
A X
C X
C X
A Y
B Y
A X
C Z
A Z
C X
C X
B Y
B Y
C X
C X
C X
C X
C X
C Z
A X
A X
A X
C Z
C X
A X
C Z
B Z
C Z
C X
A X
A Y
C X
A Z
C X
C X
C Z
C Z
C X
A X
A X
C Y
A Y
C X
C Z
A X
A Y
A Z
B Y
C X
B Y
A Z
B X
C X
C Z
C X
B Z
A Z
A Z
C Z
C X
C X
C Y
C X
B X
C X
C Z
A X
C Y
A Z
C X
C X
A Z
A Z
A Z
C Z
A Z
C X
B X
B Y
C X
A Z
C Z
C X
C X
C X
A X
B Y
A Z
B Y
C X
B Z
A Z
C Z
C Z
C X
C X
C X
A Z
C X
A X
C Z
A Y
C X
A Y
C X
C Z
C X
C X
C X
B Y
C X
B Y
C Z
B Y
B Z
A Z
A X
C Z
C X
C X
B Y
B Y
A Z
C X
C Z
C Z
C Z
B Z
B Y
B X
C X
C X
C X
C Z
C X
C X
B Y
C X
C X
B Y
C X
C X
C X
C X
A Y
C X
C X
A Z
C Z
A Z
A Z
A Y
A Z
C Z
C X
C X
C X
C X
B Y
A Z
C X
C X
B Y
A Y
A Z
A Z
C Z
C X
C Y
C X
C X
B Y
C X
A X
B X
B Y
C Z
A X
C X
C X
A X
C X
A Y
A Y
C X
C X
B Y
C X
A Z
C Z
A X
C X
A Z
C X
C X
C X
C Z
A Z
B X
C X
A Z
C Z
B Y
C X
C X
B X
C X
C X
A Y
B Z
B Y
C X
C X
C X
C Z
C X
C X
C X
B Y
C X
C Z
C X
A Z
B Y
A X
B Y
A Z
C X
C X
A Z
B Y
C X
A Z
C X
A Z
A Z
B Z
A Y
A Z
C X
C Z
C X
A X
C X
B Y
B X
C Z
C X
B Y
C Z
C X
B Y
C X
C Y
C Z
A X
B Z
C X
C X
C Z
A Z
C X
C Z
A Z
C X
C X
C Z
C Z
B Y
A Z
C X
B X
B Y
C X
C X
C X
C X
B Z
A Z
C X
A Z
A X
A Z
C X
A X
C Z
A Z
C Z
B Z
B Y
C X
A X
C Z
C Z
A Y
B X
C X
C X
A X
C X
C X
C X
A Z
A Z
C X
A Z
C Z
C Z
C X
C Z
B Y
C X
C X
C X
A Z
A Z
C X
C X
C X
C Z
A Z
C X
A X
C Z
C X
B Y
C X
C Z
C X
C X
A X
A X
B Y
C Z
C X
C Z
A Z
C X
A X
A Z
C X
C X
C Y
C X
A Z
C X
A Z
B X
A X
A Z
A Z
A Z
A Y
A X
C X
C X
A Z
C Z
C X
C X
A Z
C Z
C X
C X
C X
C X
C X
C X
A Z
A Y
C Z
C X
A Z
A X
C X
C Z
A Z
C X
B Y
A Z
A Z
C X
A Z
C X
C X
A Z
C X
C Y
C X
C X
B Y
A Y
A Z
C X
C X
B Y
C X
C X
C Z
C Z
C X
B X
C X
C Z
A Y
C Z
B Y
C X
C X
B Y
A Z
B Y
C Z
A Y
A Z
B Y
A X
C X
C X
C Z
C X
A X
C X
C X
C Z
A Z
A Z
A Z
C Z
B X
A Z
A Z
C X
C X
C X
A Y
A Z
C Z
C X
C Z
C X
A Z
C Z
A Z
C X
B Y
C Z
C X
C X
A Z
C Z
C Z
B X
C Z
C Z
A Z
A Y
C X
C X
C Z
C X
A X
C X
C X
C X
C Z
B Y
B Y
C X
B Y
C X
C X
C X
A Z
B Z
C X
C X
C X
C X
C Z
C X
C X
C X
A Z
C X
B Y
C X
A Y
B Z
A Z
C X
B X
A Y
C Z
C X
C X
C X
C Z
A Y
C Y
C X
A Y
A Y
C X
C X
C X
C X
C Z
B X
C X
C X
C X
A Z
B X
C X
C X
B Y
C X
C X
C X
A Z
C X
C X
C X
B Y
C X
B Z
B X
C Z
C X
C Z
C X
B X
A Z
C X
C X
A Z
C Z
C X
A Z
B Z
C X
A X
A Z
C Z
C X
C X
B X
B X
C X
B X
C X
C Z
C X
C X
A Y
A X
A X
C Z
C Z
A Z
C Z
C X
C X
C X
C Z
A X
C Z
A X
C Z
C X
C X
A Y
C Z
A Z
A X
A Z
B Y
C X
C Z
C X
C X
A X
A X
C X
C X
C X
C X
A Z
C X
C Z
A X
C X
B Y
C Z
C X
A X
C X
C Z
C X
A X
A X
A X
C X
A Z
A X
C Z
C Z
C X
C Y
A Y
C X
C X
B X
C X
C X
C Z
B Y
A Z
C X
B Y
A Z
C Z
A Z
A Y
C Z
B Z
A X
B Z
C Z
A X
C Z
A Z
A Z
B Z
C X
C X
C X
C X
A X
C X
C X
C X
C X
C X
B Y
C X
C X
C X
B Z
A Y
A X
C Z
C X
A Y
B Y
C X
A Y
A Z
B X
A Z
C X
B Y
C X
A Z
A Z
C X
A Z
A Z
C X
A X
A Z
C Z
B Z
C X
A X
C Y
A Y
C X
A Z
C X
C X
C X
C Z
C X
C X
C X
A Y
B Z
A X
A Z
A Z
C X
A X
B X
C X
B X
C X
A Z
A X
C X
A X
A Y
A Y
A Z
A Z
C X
B X
C X
A Y
C Z
A Z
C X
C X
A Y
A Z
B Y
C X
C X
C X
C X
C X
A Z
C Z
C X
C X
C Z
C X
C Z
B Y
C X
A Z
B X
C Z
C X
C Z
C Z
C Z
C X
C X
C Z
C X
C Z
B Y
C X
C X
A Z
C X
C X
B Y
C X
C Z
C X
B X
C Z
A X
C X
C Z
C X
C Z
B Y
C X
A Z
A Y
C X
C Y
B Z
B X
C X
C X
C Z
C X
B Y
C X
A Z
A Y
C X
B Y
C X
C Z
B Y
C X
A Y
C X
C X
C X
A Z
C Z
C X
C X
A X
A Z
C X
C X
A Y
C X
B Y
C Z
C Z
C Z
B Y
C X
C X
C X
C X
A Y
A Z
A X
C Z
A Z
A Z
A Z
C X
A Y
B X
A Z
C X
C X
B X
C X
C X
C X
B Y
A Z
A X
A Z
C X
B X
A X
C X
C X
C X
C X
C X
C Z
A Z
C X
C X
C Z
C X
A Y
A Z
C X
A Z
C X
A Z
C Z
A Z
C X
C X
C X
C X
C X
C X
C X
C X
C X
C X
C X
C X
C X
C X
C X
C X
B Z
C X
A X
C Z
C X
A X
C Z
A X
B Y
A Y
C X
A Z
C X
C X
C X
C X
C X"""
)

print(a)