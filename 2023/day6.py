# day 6
    # toy boat race!
    # looks like an optimization problem
        # charge up time vs actually racing
# part 1
    # determine the number of ways you can beat the record in each race
    # return products of the number of ways to win as the answer

# plan
    # race time, rt
    # hold time, ht = x
    # speed, v = ht
    # distances, d = v(rt-ht)

    # parabola >>> d = ht(rt-ht) = ht*rt - ht^2
    # opens upsidedown bc a value is -
    # find midpoint between roots to get the max d
    # OR
    # calculus for derivative, d(d)/d(ht) = rt - 2ht = 0 solve
    # rt/2 = ht

    # BUT! we just need to beat the record, d > rec
    # I did some math

with open('day6_input.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break

        # parse input
        if "Time" in line:
            times = line.strip('\n').split(" ")
            times.remove(times[0])
        else:
            distances = line.strip('\n').split(" ")
            distances.remove(distances[0])
# clean up
for i in range(len(times)):
    try:
        times.remove('')
    except:
        break
for i in range(len(distances)):
    try:
        distances.remove('')
    except:
        break

print(times)
print(distances)

# math
ht_list = []  # part 1
ways = 0  # part 2

for race in range(len(times)):  # for each race
    rt = int(times[race])
    d_rec = int(distances[race])
    ht_rec = [0, rt]  # initialize at bounds
    # solve ht_rec twice
    ht_rec[0] = int((-1 * rt + (rt ** 2 - 4 * d_rec) ** 0.5) / -2)
    ht_rec[1] = int((-1 * rt - (rt ** 2 - 4 * d_rec) ** 0.5) / -2)
    ht_list.append(ht_rec[1]-ht_rec[0])  # number of ways to win (discrete times)
print(ht_list)

# part 2
times2 = int(''.join(times))
distances2 = int(''.join(distances))
rt = times2
d_rec = distances2
ht_rec2 = [0, rt]
ht_rec2[0] = int((-1 * rt + (rt ** 2 - 4 * d_rec) ** 0.5) / -2)
ht_rec2[1] = int((-1 * rt - (rt ** 2 - 4 * d_rec) ** 0.5) / -2)
ht_list2 = ht_rec2[1] - ht_rec2[0]

def product(list_to_multiply: list):
    prod = 1
    for item in list_to_multiply:
        prod *= float(item)
    return prod


print('Part 1')
print('Product of numbers: ', int(product(ht_list)))
print('Part 2')
print('Number of ways to win: ', (ht_list2))
# part 2
    # lol bad kerning
    #concat line and resolve
