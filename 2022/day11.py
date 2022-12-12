# day 11 - Monkey in the Middle
import math


class Monkey:
    """Monkey class"""
    def __init__(self, number_, items_, operation_, test_, test_true_, test_false_):
        self.number = int(number_)
        self.items = items_  # list
        self.operation = operation_
        self.test = int(test_)
        self.true = int(test_true_)
        self.false = int(test_false_)
        self.activity = 0


def new_monkey(number_, items_, operation_, test_, test_true_, test_false_):
    banana = Monkey(number_, items_, operation_, test_, test_true_, test_false_)
    return banana


def big_test(number_, divider_):
    return number_ % divider_


# read input and generate monkeys
zoo = []  # list of monkeys
end_of_file = [False, False]
with open("day11_input.txt", 'r') as read_input:
    while True:
        if end_of_file[0] and end_of_file[1]:
            break

        setup_monkey = read_input.readline().rstrip('\n')
        # collect info, then make monkey
        if "Monkey " in setup_monkey:
            number = setup_monkey[setup_monkey.index(" ")+1:-1]
            end_of_file[0] = False
        elif "Starting " in setup_monkey:
            item_string = setup_monkey[setup_monkey.index(": ")+2:]
            # need to parse the string again
            items = []
            ii = 0
            for i in range(item_string.count(",")+1):  # for each comma+1 = number of items in the string
                items.append(int(item_string[ii:ii+2]))
                ii += 4
        elif "Operation: " in setup_monkey:
            operation = setup_monkey[setup_monkey.index('= ')+2:]
        elif "Test: " in setup_monkey:
            test = int(setup_monkey[setup_monkey.index('by ')+3:])
        elif "true" in setup_monkey:
            test_true = int(setup_monkey[setup_monkey.index("y ")+2:])
        elif "false" in setup_monkey:
            test_false = int(setup_monkey[setup_monkey.index("y ")+2:])
        else:
            # blank line, so make monkey
            if end_of_file[0]:
                end_of_file[1] = True
            elif not setup_monkey:
                end_of_file[0] = True
                zoo.append(new_monkey(number, items, operation, test, test_true, test_false))

mod = 1
for mm in range(len(zoo)):
    mod *= zoo[mm].test
# play out each round
for r in range(10000):  # Part 1 = 20; part 2 = 10000
    for j in range(len(zoo)):  # iterate through monkeys
        if len(zoo[j].items) == 0:
            continue  # skip monkey if no items
        else:
            inspected_item = 0
            for k in range(len(zoo[j].items)):  # iterate through each item
                # monkey inspects = operation and activity += 1
                zoo[j].activity += 1
                # decode and do operation
                old = zoo[j].items[0]
                inspected_item = eval(zoo[j].operation)  # eval is dangerous but w/e
                # inspected_item = math.floor(inspected_item / 3)  # worry /3 rounding down -- only for part 1
                # test - true/false - pass item (to end of list) & remove
                inspected_item %= mod
                if inspected_item % zoo[j].test == 0:  # test true
                    zoo[zoo[j].true].items.append(inspected_item)
                else:  # test false
                    zoo[zoo[j].false].items.append(inspected_item)
                zoo[j].items.pop(0)  # remove original item

    if r+1 in [1, 20]:
        print('\n-----After round', r+1, '-----')
        for m in range(len(zoo)):
            # print('Monkey', m, ': ', list(zoo[m].items))
            print('Monkey', m, 'activity:', zoo[m].activity)


# two most active monkeys determine "monkey business"
def monkey_business(list_of_monkeys):
    maxes = []
    for jj in range(len(list_of_monkeys)):
        # find 2 most active monkeys
        maxes.append(list_of_monkeys[jj].activity)
        if len(maxes) > 2:
            maxes.pop(maxes.index(min(maxes)))
    serious_business = maxes[0] * maxes[1]
    return serious_business


output_1 = monkey_business(zoo)
print('\n-----Activity-----')
for m in range(len(zoo)):
    print('Monkey', m, ': ', zoo[m].activity)
print('Monkey business after', r+1, 'rounds:', output_1)
