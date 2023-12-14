# day 7
    # camel cards - poker but while riding a camel!
# part 1
hands_list = []  # from the input
bids_list = []  # from the input

with open('day7_input.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break

        # parse input
        deal = line.strip('\n').split(' ')
        hands_list.append(deal[0])
        bids_list.append(int(deal[1]))
print(hands_list)
print(bids_list)
type_list = []  # type, strength for each item
rank_list = []  # num for rank 1-len


def hand_type(hand_: str):
    # find hand type
    # types   =  5, 4, full=(3+pair), 3, 2pair, pair, high
    # match_t =  7, 6, 5,             4, 3,     2,    1
    value_ = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']  # index/pos = value, (0 & 1 not used)
    decode = {}  # str'value': int(count)
    for card in hand_:
        count = 0
        value = str(value_.index(card))
        for i in range(len(hand_)):  # count number of times card occurs in hand
            if card == hand_[i]:
                count += 1
        decode[value] = count
    key_list = list(decode.keys())

    # assign hand type & rel strength
    if len(decode) == 1:  # 5 of a kind
        match_type = 7
        strength = int(key_list[0])
    elif len(decode) == 2:  # 4 of a kind --OR -- full house
        if decode.get(key_list[0]) == 4 or decode[key_list[1]] == 4:  # 4 of a kinda
            match_type = 6
            if decode.get(key_list[0]) == 4:
                strength = int(key_list[0])
            else:
                strength = int(key_list[1])
        else:  # full house
            match_type = 5
            if decode.get(key_list[0]) == 3:
                strength = (int(key_list[0]), int(key_list[1]))
            else:
                strength = (int(key_list[1]), int(key_list[0]))
    elif len(decode) == 3:  # 3 of a kind -- OR -- 2 pairs
        if decode[key_list[0]] == 3 or decode[key_list[1]] == 3 or decode[key_list[2]] == 3:  # 3 of a kind
            match_type = 4
            if decode[key_list[0]] == 3:
                strength = int(key_list[0])
            elif decode[key_list[1]] == 3:
                strength = int(key_list[1])
            else:
                strength = int(key_list[2])
        else:  # 2 pairs
            match_type = 3
            strength_pairs = [int(key) for key in key_list if decode[key] == 2]
            strength = (max(strength_pairs), min(strength_pairs))
    elif len(decode) == 4:  # 1 pair
        match_type = 2
        for keys in key_list:
            if decode[keys] == 2:
                strength = int(keys)
    else:  # no match, high card
        match_type = 1
        strength_high = [int(key) for key in key_list]
        strength = max(strength_high)

    return int(match_type), strength


for hand in hands_list:
    type_list.append((hand_type(hand)))  # find the type and store
print(type_list)
# rank
    # compare type, on ties, compare strength
from operator import itemgetter
five_kind = sorted([card for card in type_list if card[0] == 7], key=itemgetter(1), reverse=True)
four_kind = sorted([card for card in type_list if card[0] == 6]
full_house = sorted([card for card in type_list if card[0] == 5]
three_kind = sorted([card for card in type_list if card[0] == 4]
two_pair = sorted([card for card in type_list if card[0] == 3]
pair_ = sorted([card for card in type_list if card[0] == 2]
high_card = sorted([card for card in type_list if card[0] == 1]
print(five_kind)
print(four_kind)
print(full_house)
print(three_kind)
print(two_pair)
print(pair_)
print(high_card)

# score winnings = sum(rank * bid)
winnings = 0
for item in range(len(bids_list)):
    winnings += bids_list[item] * rank_list[item]

print('Part 1')
print('Sum of things: ', winnings)

# part 2
