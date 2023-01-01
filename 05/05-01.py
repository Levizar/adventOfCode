
with open("./05-input") as file:
    lines = file.read().splitlines()

instruction_seperator_index = lines.index("")

pile_lines = lines[:instruction_seperator_index - 1]
index_str = lines[instruction_seperator_index - 1:instruction_seperator_index][0]
instructions = lines[instruction_seperator_index + 1:]

stack_accessor = {c:[] for c in index_str.split()}
for i, c in enumerate(index_str):
    if not c.isdigit():
        continue
    for pile_line in pile_lines[::-1]:
        if pile_line[i] != " ":
            stack_accessor[c].append(pile_line[i])

for instruction_str in instructions:
    # instruction_str is like "move 1 from 2 to 1"
    # create {"move": "1", "from": "2", "to": "1"}
    word_iterator = iter(instruction_str.split())
    actions = dict(zip(word_iterator, word_iterator))
    for _ in range(int(actions["move"])):
        to_move = stack_accessor[actions["from"]].pop()
        stack_accessor[actions["to"]].append(to_move)

res = "".join([stack[-1] for stack in stack_accessor.values()])
print(res)

