
with open("./03-input") as file:
    rucksacks = file.read().splitlines()

alpha = "abcdefghyjklmnopqrstuvwxyz"
alpha += alpha.upper()
priority_item_map = {l: i for i, l in enumerate(alpha, start=1)}

priority_per_ruck_sack = []
stack = []
for i, rucksack in enumerate(rucksacks, start=1):
    stack.append(rucksack)
    if i % 3 == 0:
        a, b, c = set(stack.pop()), set(stack.pop()), set(stack.pop())
        common = (a & b & c).pop()
        priority_per_ruck_sack.append(priority_item_map[common])
print(sum(priority_per_ruck_sack))
