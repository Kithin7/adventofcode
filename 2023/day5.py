# day 5
# part 1
# mapping
    # [dest range start, source range start, range length]
    # numbers not in the ranges provide map to themselves
    # then chain together the maps
    # find lowest loc # from all seeds

# plan
    # index number targets the same seed through all lists
    # build treemap then find the lowest loc
import pprint


def link(source_, key_list: list):
    """input one source and its related key_list; returns the destination"""
    dest_ = int(source_)  # set equal by default
    # parse again
    for key_split in key_list:
        key_ = key_split.strip("\n").split(" ")
        dest_start = int(key_[0])
        source_start = int(key_[1])
        range_length = int(key_[2])
        if source_ in range(source_start, source_start + range_length):
            source_dest_factor = dest_start - source_start
            dest_ = source_ + source_dest_factor  # update dest_ if in map range
            break

    return int(dest_)


with open('day5_test.txt', 'r') as file:
    lines = file.readlines()  # idk just read the whole thing this time

    # parse into a more usable struct, like a list
    seeds_list = lines[0][lines[0].index(":") + 2:].strip("\n").split(' ')
    # [dest range start, source range start, range length]
    soil_block = lines[3:lines.index("\n", 3)]
    fertilizer_block = lines[22:lines.index("\n", 22)]
    water_block = lines[55:lines.index("\n", 55)]
    light_block = lines[96:lines.index("\n", 96)]
    temperature_block = lines[115:lines.index("\n", 115)]
    humidity_block = lines[136:lines.index("\n", 136)]
    location_block = lines[168:]

    print(seeds_list)
    #print(soil_block)

    seed_LL = []
    for seed in range(len(seeds_list)):
        seed_LL.append([int(seeds_list[seed])])  # append with a list and first entry is seed#
        seed_LL[seed].append(link(seed_LL[seed][0], soil_block))
        seed_LL[seed].append(link(seed_LL[seed][1], fertilizer_block))
        seed_LL[seed].append(link(seed_LL[seed][2], water_block))
        seed_LL[seed].append(link(seed_LL[seed][3], light_block))
        seed_LL[seed].append(link(seed_LL[seed][4], temperature_block))
        seed_LL[seed].append(link(seed_LL[seed][5], humidity_block))
        seed_LL[seed].append(link(seed_LL[seed][6], location_block))

    pprint.pprint(seed_LL)

    loc_list = [seed[-1] for seed in seed_LL]
    print('Part 1')
    print('lowest loc #:', min(loc_list))

    # part 2
        # seeds are actually in pairs (start, length)!
    seed_LL2 = []
    for seed in range(len(seeds_list)):
        if seed % 2 == 0:
            pass
        else:
            seed_LL2.append([range(int(seeds_list[seed-1]), int(seeds_list[seed]))])# append with a list for the next seed range
            seed_LL2[seed].append(link(seed_LL2[seed][0], soil_block))
            seed_LL2[seed].append(link(seed_LL2[seed][1], fertilizer_block))
            seed_LL2[seed].append(link(seed_LL2[seed][2], water_block))
            seed_LL2[seed].append(link(seed_LL2[seed][3], light_block))
            seed_LL2[seed].append(link(seed_LL2[seed][4], temperature_block))
            seed_LL2[seed].append(link(seed_LL2[seed][5], humidity_block))
            seed_LL2[seed].append(link(seed_LL2[seed][6], location_block))

    pprint.pprint(seed_LL2)

    loc_list2 = [seed[-1] for seed in seed_LL2]
    print('Part 2')
    print('lowest loc #:', min(loc_list2))
