# day 7
# disk is full, so we need to del some stuff to make room

# idea to use directories and lists and files w/ sizes
# tried making a tree data structure with class type obj, but it hurt my brain... so dictionary time!
# anytree lib might have been useful... but w/e

class Node:
    """node class, contains: """
    def __init__(self, name_, parent_, value_=0):
        self.name = name_
        self.parent = parent_
        self.value = value_
        self.child = {}


def new_node(name_, parent_, value_=0):
    new = Node(name_, parent_, value_)
    return new


root = new_node('root/', None, 0)
level = 0
end_the_loop = False
with open('day7_input.txt', 'r') as read_input:
    while True:
        bit = read_input.readline()
        bit.rstrip('\n')
        if end_the_loop or not bit:
            print('\ndone reading file...')
            break

        # what do when line read
        if '$ cd /' in bit:  # go to root dir
            current_dir = 'root/'
            level = 0
            # print(level)
        elif '$ cd ..' in bit:  # go up 1 level to parent dir X (this elif is before the other to filter correctly)
            current_dir = str(root.child[current_dir].parent)
            level -= 1
            # print(level)
        elif '$ cd ' in bit:  # go down 1 level to child dir X
            current_dir = bit[bit.index('d ') + 2:-1]
            level += 1
            # print(level)
        elif '$ ls' in bit:  # list all child of current_dir
            continue  # skip as it doesn't actually do anything super important?
        elif 'dir ' in bit:  # make a dir of name X
            space_parse = bit.index(' ')
            name = bit[space_parse + 1:].rstrip('\n')
            # update root
            root.child[name] = new_node(name, current_dir)
            # update parent_dir with new child
            if current_dir == 'root/':
                continue
            else:
                root.child[current_dir].child[name] = name
            # print('added dir ', name)
        else:  # make entry ""
            space_parse = bit.index(' ')
            size = int(bit[:space_parse])
            name = bit[space_parse + 1:].rstrip('\n')
            # make new_node in the correct spot
            root.child[name] = new_node(name, current_dir, size)
            # update parent_dir with new child
            if current_dir == 'root/':
                continue
            else:
                root.child[current_dir].child[name] = name
            # print('added file ', name)
print('number of line/files in system:', len(root.child.keys()))

# part 1
# Find all the directories with a total size of at most 100000 (some files might be double counted in this way)
# What is the sum of the total sizes of those directories?

# recursively sum all directories and their sub-dir
key_list = list(root.child.keys())
print('\nsumming directories...')
output_1 = 0


def sum_dir(dir_name):
    # func to sum a dir, but check for sub_dir and sum those first (recursively)
    total = 0
    # check for sub_dir
    sub_key = list(root.child[dir_name].child.keys())
    for ii in range(len(sub_key)):  # for each child in dir
        # try to sum everything
        child_name = root.child[dir_name].child[sub_key[ii]]  # check if the child has a value already
        if root.child[child_name].value != 0:  # add if value
            total += root.child[child_name].value
        else:  # else sub_dir value = 0, recursion
            root.child[child_name].value = sum_dir(child_name)  # find child's value and store
            total += root.child[child_name].value  # add child's value
    return total


# go through and call sum_dir on each dir in root (it will recursively call itself)
for i in range(len(key_list)):
    key_spot = key_list[i]
    if root.child[key_spot].value == 0:  # only update dir with value = 0 (don't overwrite leaf)
        root.child[key_spot].value = sum_dir(key_spot)
    # now find all dir <100k and sum together
    # sum dir if it has children & value <100k
    if (root.child[key_spot].value <= 100000) and (len(list(root.child[key_spot].child.keys())) > 0):
        output_1 += root.child[key_spot].value

for rj in range(len(key_list)):
    key_spot = key_list[rj]
    print(str(root.child[key_spot].name), '=', root.child[key_spot].value)

print('\nSum of all dir <100k =', output_1)
print('answer is higher than 281021')
