# day 1
# part 1
with open('day1_input.txt', 'r') as file:
    cal_vals = []
    chars = 'qwertyuiopasdfghjkl;zxcvbnm,./\n'
    while True:
        line = file.readline()
        if not line:
            break

        stripped = line.rstrip(chars)
        stripped = stripped.lstrip(chars)
        cal_vals.append(int(str(stripped[0] + stripped[-1])))
        # print(cal_vals)

    print('part 1 = ', sum(cal_vals))

# part 2
with open('day1_input.txt', 'r') as file:
    cal_vals = []
    strip_list = []

    left_chars = 'qwryuipadghjkl;zxcvbm,./\n'
    right_chars = 'qwyuipasdfghjkl;zcvbm,./\n'

    text2num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    while True:
        line = file.readline()
        if not line:
            break

        stripped = line.rstrip(right_chars)
        stripped = stripped.lstrip(left_chars)
        strip_list.append(stripped)

        # detect number spelled out
        # first num
        if stripped[0] in nums:
            cal_vals.append(str(stripped[0]))
        else:
            for tnum in text2num:
                try:
                    stripped.index(tnum)
                except ValueError:
                    pass
                else:
                    if stripped.index(tnum) == 0:
                        cal_vals.append(str(text2num.index(tnum)))
                    else:
                        pass
        # second num
        if stripped[-1] in nums:
            cal_vals[-1] = int(str(cal_vals[-1]) + str(stripped[-1]))
        else:
            for tnum in text2num:
                try:
                    stripped.index(tnum)
                except ValueError:
                    pass
                else:
                    if stripped.index(tnum) + len(tnum) == len(stripped):
                        cal_vals[-1] = int(str(cal_vals[-1]) + str(text2num.index(tnum)))
                    else:
                        pass
    print(len(strip_list), strip_list)
    print(len(cal_vals), cal_vals)
    print('part 2 = ', sum(cal_vals))
    check = []
    for i in range(0, len(strip_list)):
        check.append([strip_list[i], cal_vals[i]])
    import pprint
    pprint.pprint(check)

