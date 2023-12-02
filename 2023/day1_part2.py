# part 2
with open('day1_input.txt', 'r') as file:
    cal_vals = []
    strip_list = []

    left_chars = 'qwryuipadghjkl;xcvbm,./\n'
    right_chars = 'qwyuipasdfghjkl;zcvbm,./\n'

    text2num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    while True:
        line = file.readline()
        if not line:
            break

        stripped = line.rstrip(right_chars)  # keep o e r x n t
        stripped = stripped.lstrip(left_chars)  # keep o t f s e n
        strip_list.append(stripped)

        first = 10 ** 100
        last = -1

        # new plan
        # look at nums and numtext, compare with smallest and large known indices, update as found
        # string.index(thing) is our friend, should have done it like this for the first part...
        for i in range(1, len(nums)):
            # check for textnum
            try:
                stripped.index(text2num[i])
            except ValueError:
                pass
            else:
                if stripped.index(text2num[i]) < first:
                    first = i
                if stripped.index(text2num[i]) > last:
                    last = i
            # check for num
            try:
                stripped.index(nums[i])
            except ValueError:
                pass
            else:
                if stripped.index(nums[i]) < first:
                    first = i
                if stripped.index(nums[i]) > last:
                    last = i

        cal_vals.append(int(str(first) + str(last)))

    print(strip_list)
    print(cal_vals)
    print('part 2 = ', sum(cal_vals))
