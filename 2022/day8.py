# day 8: treetop tree house
# given tree matrix, count how many are 'visible' from outside the grid?

# read input
escape_loop = False
forest = []
visible = []
with open("day8_input_test.txt", 'r') as read_input:
    while True:
        Row = read_input.readline().rstrip("\n")
        if escape_loop or not Row:
            break
        forest.append(Row)

# make copy but made of 0's for not visible
for i in range(len(forest)):
    visible.append([])
    for j in range(len(forest[0])):
        visible[i].append(0)

# determine visible (1) or not (0)
# if visible, then mark visible (regardless if only visible from 1 direction and not the other 3)
for row in range(len(forest)):
    for col in range(len(forest[0])):
        # all edges are visible
        if row == 0 or row == len(forest)-1 or col == 0 or col == len(forest[0])-1:
            visible[row][col] = 1

        else:  # not edges
            # compare value with all previous values in the direction
            # from left
            if forest[row][col] == max(forest[row][:col+1]) and forest[row][col] not in forest[row][:col]:
                visible[row][col] = 1
            # from right
            if forest[row][col] == max(forest[row][col:]) and forest[row][col] not in forest[row][col+1:]:
                visible[row][col] = 1
            # iterate through the rows
            for r in range():
                # from top
                if forest[row][col]:
            for r in range():
                # from bottom
                if :

# count all visible 1's
output_1 = 0
for k in range(len(visible)):
    output_1 += sum(visible[k])
    print(forest[k], visible[k])
print("Number of visible trees:", output_1)