from tools import import_input_file_raw
from functools import reduce
import operator
import pprint


monkeys_setup = [lines.splitlines() for lines in import_input_file_raw().split("\n\n")]

class Monkey():
    def __init__(self, name, starting_items, operation_func, test, true_throw, false_throw, monkeys):
        self.name = name
        # each items are worry levels
        self.items = starting_items
        self.operation_str = operation_func
        self.testing_condition = test
        self.monkey_true_throw = true_throw
        self.monkey_false_throw = false_throw
        self.monkeys = monkeys

        self.nbr_inspection = 0
        self.highest_common_denominator = 0

    
    def __str__(self):
        return (
            f"""{self.name}
{self.items=}
{self.operation_str=}
{self.testing_condition=}
{self.monkey_true_throw=}
{self.monkey_false_throw=}"""
        )

    
    def play_turn(self):
        while self.items:
            item = self.items.pop(0)
            item = self.inspect(item)
            monkey = self.chose_monkey(item)
            self.throw_at(monkey, item)


    def inspect(self, item):
        # increase worry level as the monkey inspect the item
        old = item
        new = eval(self.operation_str)

        # keep of the number of inspection this monkey did
        self.nbr_inspection += 1

        return new % self.highest_common_denominator


    def chose_monkey(self, item):
        test_result = item % self.testing_condition == 0

        choosen_monkey_index = self.monkey_true_throw if test_result else self.monkey_false_throw
        choosen_monkey = self.monkeys[choosen_monkey_index]
        return choosen_monkey


    def throw_at(self, monkey, item):
        monkey.receive(item)


    def receive(self, item):
        self.items.append(item)
    

def main():
    # part 1:
    # find the monkey_business = first_most_active_monkey_exchange * second_most_active_monkey_exchange
    
    monkeys = []
    # parse setup of initial situation and formula

    for setup in monkeys_setup:
        name, start, operation, test_condition, if_true, if_false = setup
        
        # start = "Starting items: 54, 65, 75, 74"
        items = list(map(int, start.split(": ")[1].split(", ")))
        # operation = "Operation: new = old + 6"
        func_str = operation.split("new = ")[1] # eval(func_str)
        # test_condition = "Test: divisible by 23"
        testing_condition = int(test_condition.split("divisible by ")[1])
        # if_true = "If true: throw to monkey 2"
        true_throw = int(if_true.split("monkey ")[1])
        # if_false = "If false: throw to monkey 3"
        false_throw = int(if_false.split("monkey ")[1])
        monkey = Monkey(name, items, func_str, testing_condition, true_throw, false_throw, monkeys)
        monkeys.append(monkey)

    highest_common_denominator = reduce(operator.mul, (m.testing_condition for m in monkeys))
    for monkey in monkeys:
        monkey.highest_common_denominator = highest_common_denominator

    # process the rounds
    for _ in range(10000):
        for monkey in monkeys:
            monkey.play_turn()

    monkeys_sorted = list(sorted(monkeys, key=lambda m: m.nbr_inspection, reverse=True))
    monkey_business = monkeys_sorted[0].nbr_inspection * monkeys_sorted[1].nbr_inspection
    print(monkey_business)


main()
