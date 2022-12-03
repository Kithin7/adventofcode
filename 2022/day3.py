# day 3
# 1 line = 1 bag, each bag has two equal halves
# find common item in each halve and sum the priorities of all bags
# a-z = 1-26, A-Z = 27-52

Matches = []
Sum = 0
Sum2 = 0
count = 0
N = int(input('group size, N, = '))
BagSet = []

with open('day3_input.txt', 'r') as Manifest:
    while True:
        Bag = Manifest.readline()
        Bag = Bag.rstrip('\n')
        if not Bag:
            break
        count = count + 1

        # part 2
        # store groups of n bags for checking common item
        BagSet.append(Bag)
        nMatch = False
        Letter = ''
        if len(BagSet) == N:  # once BagSet has N # in it, do this:
            for L in range(len(BagSet[0])):  # check each letter in bag 0
                for LL in range(N):  # check each bag (for 'current letter' in bag 0)
                    if BagSet[0][L] in BagSet[LL]:  # if match
                        nMatch = True
                        Letter = BagSet[0][L]
                    else:
                        nMatch = False
                        Letter = ''
                        break
                if nMatch:
                    break
            # Letter to num & Sum2
            Sum2 = Sum2 + ord(Letter)
            if Letter.islower():
                Sum2 = Sum2 - 96
            elif Letter.isupper():
                Sum2 = Sum2 - 38

            # BagSet clean up N times
            for LLL in range(N):
                BagSet.pop(0)
        # end part 2

        # part 1
        Size = int(len(Bag)/2)
        Flag = False
        # find matches
        for i in range(Size):
            if Flag:
                break
            for j in range(Size):
                if Bag[i] == Bag[Size+j]:
                    Matches.append(Bag[i])
                    Flag = True
                    break
    # sum priorities of matches
    for k in range(len(Matches)):
        Sum = Sum + ord(Matches[k])
        if Matches[k].islower():
            Sum = Sum - 96
        elif Matches[k].isupper():
            Sum = Sum - 38
        else:
            print('ERROR AT ', k, Matches[k])
            break


print('\n# of lines read:   ', count)
print('# of matches:      ', len(Matches))
print('Sum of matches:    ', Sum)
print('-----------------------')
print('N =', N)
print('Sum of N bags:     ', Sum2)
