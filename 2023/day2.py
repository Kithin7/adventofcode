# day 2
# the cubes!

# determine which games are possible if the bag had:
# 12 red 13 green 14 blue
# then sum those game ID numbers

# part 1
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
        # game ID number---this will go to possibles list if possible
        game_id = int(line[line.index("e")+1:line.index(":")])
        # after game_id, split by ;
        # & color(s) are not always present
        # & colors are not always presented in the same order
        game_pulls = line[line.index(':') + 1::].rstrip('\n')
        hands = game_pulls.split(';')

        flag_game = False  # reset flag every game (line)
        for pull in hands:
            # if one pull/hand in the game is bad,
            # break and go to the next game
            if flag_game:
                break

            hand_colors = {'red': 0,
                           'green': 0,
                           'blue': 0}
            # read each member of hand into r,g,b
            for color in key_list:
                if color in pull:  # color is in pull string
                    # broke this out into steps for readability
                    num_index = pull.find(color)
                    color_num = pull[num_index-3:num_index]  # max is 2 digit # and there is always a space
                    color_num = color_num.lstrip(' ')  # clean up spaces
                    color_num = color_num.rstrip(' ')
                    hand_colors[color] = int(color_num)

                    # compare hand_colors to max_colors
                    if hand_colors[color] > max_colors[color]:  # not possible, throw flag and break
                        flag_game = True
                        break
                else:  # color not in pull string
                    pass

        # all hands from game are checked so now add game_id
        if not flag_game:
            possible_games.append(game_id)

    print('Part 1')
    print('Sum of possible games: ', sum(possible_games))

# part 2
# find min number of cubes possible (finding max of each color per game)
# return sum of (R*G*B) over all games
with open('day2_input.txt', 'r') as file:

    key_list = ('red', 'green', 'blue')

    power_games = []  # list of int, (R*G*B), sum at end

    while True:
        line = file.readline()
        if not line:
            break

        # parse line data
        # game ID number---this will go to possibles list if possible
        game_id = int(line[line.index("e")+1:line.index(":")])
        # after game_id, split by ;
        # & color(s) are not always present
        # & colors are not always presented in the same order
        game_pulls = line[line.index(':') + 1::].rstrip('\n')
        hands = game_pulls.split(';')  # list of "pulls"

        # reset for each game
        min_colors = {'red': 0,
                      'green': 0,
                      'blue': 0}  # per game basis
        flag_game = False

        for pull in hands:
            # if one pull/hand in the game is bad,
            # break and go to the next game
            if flag_game:
                break

            pull_colors = {'red': 0,
                           'green': 0,
                           'blue': 0}
            # read each member of hand into r,g,b
            for color in key_list:
                if color in pull:  # color is in pull string
                    # broke this out into steps for readability
                    num_index = pull.find(color)
                    color_num = pull[num_index-3:num_index]  # max is 2 digit # and there is always a space
                    color_num = color_num.lstrip(' ')  # clean up spaces
                    color_num = color_num.rstrip(' ')
                    pull_colors[color] = int(color_num)

                    # compare hand_colors to min_colors
                    if pull_colors[color] > min_colors[color]:
                        min_colors[color] = pull_colors[color]  # update bc more were needed than previously known

                else:  # color not in pull string
                    pass

        power_rgb = min_colors['red'] * min_colors['blue'] * min_colors['green']
        power_games.append(power_rgb)

    print('Part 2')
    print('Sum of power: ', sum(power_games))
    