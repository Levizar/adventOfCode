from tools import import_input_file


inputs = import_input_file()
bags = []
items_current_bag = []
for item in inputs:
    if item != "":
        items_current_bag.append(int(item))
        continue
    bags.append(items_current_bag)
    items_current_bag = []
bags.append(items_current_bag)

    

total_calorie_per_bag = [sum(bag) for bag in bags]
sorted_bags = sorted(total_calorie_per_bag)
print(sum(sorted_bags[-3:]))

