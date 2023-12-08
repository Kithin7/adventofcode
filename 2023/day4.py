# day 4
# scratch offs
# right to match left, pts = 2^(n-1), where n is # matches
# return sum pts from all cards

# part 1
left = []
right = []
points = []
points2 = []
cards = []

with open('day4_input.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        # input/parse
        # index 11:40 = Left; 43:end = right

        left = line[line.index(":")+2:line.index("|")].split(" ")
        right = line[line.index("|")+2::].strip(" \n").split(" ")
        while True:
            if "" in right:
                right.remove("")
            elif "" in left:
                left.remove("")
            else:
                break

        ## compare L & R for matches
        #matched = 0
        #for num in right:
        #    if num in left:
        #        matched += 1
        ## calc pts
        #if matched > 0:
        #    points.append(2 ** (matched - 1))

        matched2 = 0
        combined_set = set(left + right)
        matched2 = len(right)+len(left)-len(combined_set)
        points2.append(int(2 ** (matched2 - 1)))

        #print(left, right)
        #print(combined_set)
        #print(matched2)

        # part 2
            # actually the rules change :)
            # you actually win copies of the N next cards, where N is the # of matches
            # how many total scratchcards do you have now?
        cards.append(matched2)
print('matches:', cards)


def propagate(prop_list: list):
    counting_list = [1] * len(prop_list)  # list of 1s, used to count copies of each (index +1 = card#)
    for i in range(len(prop_list)):  # iter over list
        reach = prop_list[i]
        for j in range(reach):  # iter to add +1 over the reach
            for k in range(counting_list[i]):  # repeat for each copy
                counting_list[i+j+1] += 1  # index of card + reach + 1 bc index starts at 0

    return counting_list


import timeit
print(timeit.timeit('int(sum(propagate(cards)))', setup="from __main__ import propagate", globals=globals(), number=1))
copies = propagate(cards)

print('total:  ', copies)

#print(points2)
print('\nPart 1')
print('Cards total worth:', int(sum(points2)), 'pts')

print('Part 2')
print('Total number of cards:', int(sum(copies)), 'cards')


