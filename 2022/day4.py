# day 4
# in how many assignment pairs does 1 range fully contain the other?
count = 0
count2 = 0
# open file, read line by line
with open('day4_input.txt','r') as Pairing_list:
    while True:
        Pair = Pairing_list.readline()
        Pair = Pair.rstrip('\n')
        if not Pair:
            break

        # parse input
        #   - between start/stop and , between sets
        Set_1 = Pair[0:Pair.index(',')]
        Set_2 = Pair[Pair.index(',')+1:len(Pair)]
        Set_1a = int(Set_1[0:Set_1.index('-')])
        Set_1b = int(Set_1[Set_1.index('-')+1:len(Set_1)])
        Set_2a = int(Set_2[0:Set_2.index('-')])
        Set_2b = int(Set_2[Set_2.index('-')+1:len(Set_2)])

        # determine fully contained, count if fully contained
        # 2 cases: first in second or second in first
        # (1a >= 2a and 1b <= 2b) or (2a >= 1a and 2b <= 1b) else not fully contained
        if (Set_2a <= Set_1a) and (Set_1b <= Set_2b):
            count = count + 1
        elif (Set_1a <= Set_2a) and (Set_2b <= Set_1b):
            count = count + 1


        # part 2 - any overlap at all
        # overlap possible at left right and middle (1 on 2 or 2 on 1)
        # 1a <= 2a <= 1b or 1a <= 2b <= 1b // 2a <= 1a <= 2b or 2a <= 1b <= 2b
        if Set_1a <= Set_2a and Set_2a <= Set_1b:
            count2 = count2 + 1
        elif Set_1a <= Set_2b and Set_2b <= Set_1b:
            count2 = count2 + 1
        elif Set_2a <= Set_1a and Set_1a <= Set_2b:
            count2 = count2 + 1
        elif Set_2a <= Set_1b and Set_1b <= Set_2b:
            count2 = count2 + 1


print('\nNumber of fully contained: ', count)
print('Number of any overlaps:    ', count2)
