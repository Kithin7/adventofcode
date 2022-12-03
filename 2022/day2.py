# day 2
win = ['A Y', 'B Z', 'C X']
draw = ['A X', 'B Y', 'C Z']
lose = ['A Z', 'B X', 'C Y']
SUM = 0
part2 = 0


def xyz_to_point(choice):
    if choice == 'X':
        return int(1)
    elif choice == 'Y':
        return int(2)
    elif choice == 'Z':
        return int(3)
    else:
        return ''


def lose_draw_win(xyz):
    if xyz == 'X':
        return int(0)
    elif xyz == 'Y':
        return int(3)
    elif xyz == 'Z':
        return int(6)
    else:
        return ''


def Chose_point(abc, xyz):
    # X = lose
    if xyz == 'X':
        if abc == 'A':
            return int(3)  # scissors
        elif abc == 'B':
            return int(1)  # rock
        else:
            return int(2)  # paper
    # Y = draw
    elif xyz == 'Y':
        if abc == 'A':
            return int(1)  # rock
        elif abc == 'B':
            return int(2)  # paper
        else:
            return int(3)  # scissors
    # Z = win
    elif xyz == 'Z':
        if abc == 'A':
            return int(2)  # paper
        elif abc == 'B':
            return int(3)  # scissors
        else:
            return int(1)  # rock
    else:
        return ''


with open('day2_input.txt', 'r') as Guide:
    while True:
        Round = Guide.readline()
        Round = Round.rstrip("\n")
        if not Round:
            break
        # points = outcome of round + choice
        points = 0
        if Round in win:
            points = 6 + xyz_to_point(Round[2])
        elif Round in draw:
            points = 3 + xyz_to_point(Round[2])
        elif Round in lose:
            points = xyz_to_point(Round[2])
        else:
            print('ERROR')
            print(Round)
            break
        # calc points and sum to running total
        SUM = SUM + points

        # part 2
        # X = lose, Y = draw, Z = win
        # calc points but based on new XYZ meaning
        part2 = part2 + Chose_point(Round[0], Round[2]) + lose_draw_win(Round[2])
    print('Part 1: ', SUM)
    print('Part 2: ', part2)
