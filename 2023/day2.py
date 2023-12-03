# day 2
# the cubes!

# determine which games are possible if the bag had:
# 12 red 13 green 14 blue
# then sum those game ID numbers

with open('day2_input.txt', 'r') as file:

    key_list = ('red', 'green', 'blue')
    max_colors = {'red': 12,
                  'green': 13,
                  'blue': 14}
    possible_games = []  # list of int

    while True:
        line = file.readline()
        if not line:
            break

        # parse line data
        game_id = line[6:line.index(":")]  # game ID number---this will go to possibles list if possible
        print("id:", game_id)
        # after game_id, split by ;
        # & color(s) are not always present
        # & colors are not always presented in the same order
        game_pulls = line[line.index(':') + 1::].rstrip('\n')
        hands = game_pulls.split(';')

        flag_game = False  # reset flag every game (line)
        for pull in hands:
            if flag_game:
                # if one pull/hand in the game is bad,
                # break and go to the next game
                break

            hand_colors = {'red': 0,
                           'green': 0,
                           'blue': 0}
            # read each member of hand into r,g,b
            # max is 2 digit # and there is always a space
            for color in key_list:
                # broke this out into steps for readability
                num_index = pull.find(color)
                color_num = pull[num_index-3:num_index]
                color_num = color_num.lstrip(' ')  # clean up spaces
                color_num = color_num.rstrip(' ')
                hand_colors[color] = int(color_num)

                # compare hand_colors to max_colors
                if hand_colors[color] > max_colors[color]:  # not possible
                    flag_game = True
                    break

                else:  # possible
                    possible_games.append(game_id)

    print('Sum of possible games: ', sum(possible_games))
