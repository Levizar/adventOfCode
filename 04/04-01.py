
with open("./04-input") as file:
    assignment_pairs = file.read().splitlines()

assignements = []
contained = 0
for assignment_pair in assignment_pairs:
    assignment_str = assignment_pair.split(",")
    [[a1, a2], [b1, b2]] = list(map(lambda s: s.split("-"), assignment_str))
    assignment_range_a = set(range(int(a1), int(a2) + 1))
    assignment_range_b = set(range(int(b1), int(b2) + 1))
    if assignment_range_a & assignment_range_b:
        contained += 1

print(contained)


