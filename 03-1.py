
with open("./03-input") as file:
    rucksacks = file.read().splitlines()

alpha = "abcdefghyjklmnopqrstuvwxyz"
alpha += alpha.upper()
priority_item_map = {l: i for i, l in enumerate(alpha, start=1)}

priority_per_ruck_sack = []
for rucksack in rucksacks:
    middle_index = len(rucksack) // 2
    first, second = rucksack[:middle_index], rucksack[middle_index:]
    intersection = set(first) & set(second)
    dup = intersection.pop()
    priority_per_ruck_sack.append(priority_item_map[dup])

print(sum(priority_per_ruck_sack))
