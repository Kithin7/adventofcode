# day 3
# engine diagram
import copy
import pprint
# part 1
# grid matrix, search adjacent & diagonal to special chars (. is placeholder)

# assumptions:
    # looks like double-counting shouldn't be an issue? -> no nums adj to more than 1 special
    # edges are clear of specials, but not nums
    # one special doesn't touch two exact same nums
    # nums are 1-3 digits
# plan:
    # scan each row                                                 >>> for loop [row]
    # find special                                                  >>> for loop [col]
    # search 8 directions for a number                              >>> type(schematic[row][col] == int
        # check if num, then index until next . or special (NAN)    >>> str.isnumeric
        # append num to parts_list                                  >>> .append(schematic[][]) based on row/col of search direction
    # repeat

schematic = []
list_adj_nums = []
dif_list = []
copy_list = []
parts_list = []
special_chars = ('=', '+', '&', '@', '-', '#', '*', '/', '%', '$')
directions = {'ul': (-1, -1),  # (row=y , col=x)
              'u': (-1, 0),
              'ur': (-1, 1),
              'bl': (1, -1),
              'b': (1, 0),
              'br': (1, 1),
              'l': (0, -1),
              'r': (0, 1)}

with open('day3_input.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break

        line = line.rstrip('\n')
        schematic.append(line)  # schematic[row][col]
special_check = set(char_ for line_ in schematic for char_ in line_)
#print('characters present: ', special_check)
for char_ in ('.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
    special_check.remove(char_)
#print('specials present: ', special_check)

# scanning row(y) and col(x)
for row in range(0, len(schematic)-0):
    for col in range(0, len(schematic[row])-0):
        if schematic[row][col] in special_chars:  # detect special
            # now search in 8 directions
            adj_nums = set()  # set of nums adj to search origin, return at end of loop
            for search_dir in directions:

                # for keeping sanity:
                search_row = row + directions[search_dir][0]
                search_col = col + directions[search_dir][1]
                # conditional to check neighbors:
                if schematic[search_row][search_col].isnumeric():  # adj is a num
                    # loop to find left most index
                    left_index = search_col
                    while True:
                        left_index -= 1  # nudge left
                        # test
                        if left_index < 0:  # index error
                            left_index += 1  # nudge back right
                            break
                        elif not schematic[search_row][left_index].isnumeric():  # not num
                            left_index += 1  # nudge back right
                            break
                    # loop to find right most index
                    right_index = search_col
                    while True:
                        right_index += 1  # nudge right
                        # test
                        if right_index > len(schematic[search_row])-1:  # index error
                            right_index -= 1  # nudge back left
                            break
                        elif not schematic[search_row][right_index].isnumeric():  # not num
                            right_index -= 1  # nudge back left
                            break
                    #print(schematic[row][col], row, schematic[search_row][left_index:right_index])

                    # add num to set (for specific special)
                    adj_nums.add(int(schematic[search_row][left_index:right_index+1]))
                    print(row, schematic[row][col], adj_nums)

            list_adj_nums.append(adj_nums)  # list of sets
            #debug_row_adj_nums

    #print(list_adj_nums)
    dif_list = []
    for item in list_adj_nums:
        if item not in copy_list:
            dif_list.append(item)
    #print(dif_list)
    copy_list = copy.deepcopy(list_adj_nums)

    #pprint.pprint(debug_alladjnums)
#print(list_adj_nums)
parts_list = [nums for set_nums in list_adj_nums for nums in set_nums]
print(parts_list)

print('Part 1')
print('Sum of engine part number: ', sum(parts_list))

# part 2
