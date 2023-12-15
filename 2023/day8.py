# day 8
    # part 1

# linked list/ node run?

# initialize stuff here
print('Part 1')
with open('day8_input.txt', 'r') as file:
    flag_nodes = False
    nodes = {}
    while True:
        line = file.readline()
        if not line:
            break

        line = line.rstrip("\n")
        # parse input file
        if line == "":
            flag_nodes = True

        elif flag_nodes:
            node_name = line[0:3]
            left = line[7:10]
            right = line[12:15]
            nodes[node_name] = (left, right)
        else:
            run_path = line
print(run_path)
print(nodes)


def node_run(dictionary_: dict, node_: str, lr_: str):
    if lr_ == "L":
        lr_ = 0
    else:
        lr_ = 1
    next_node = dictionary_[node_][lr_]
    return next_node


node = 'AAA'
steps = 0
while node != 'ZZZ':
    node = node_run(nodes, node, run_path[steps % len(run_path)])
    steps += 1

print('# of steps from AAA to ZZZ:', steps)

# part 2 - superpositional ghost aka multi node tracking
## this code will take like 23 days to run...
print('Part 2')
ghost_nodes = [keys for keys in nodes if keys[-1] == "A"]
ghost_ends = [keys for keys in nodes if keys[-1] == "Z"]
print(ghost_nodes)
print(ghost_ends)
steps2 = 0
while False:
    for item in ghost_nodes:
        node = node_run(nodes, item, run_path[steps2 % len(run_path)])
        ghost_nodes[ghost_nodes.index(item)] = node
    steps2 += 1
    # check if all end in Z
    ghost_check = 0
    for item in ghost_nodes:
        if item[-1] != 'Z':
            break
        else:
            ghost_check += 1
    if ghost_check >= len(ghost_nodes):
        break
    print(steps2, ghost_nodes)

# part 2 - superpositional ghost aka multi node tracking
## but I had to look up help
## LCM for starting points
cycle_count = []
for node in ghost_nodes:
    steps2 = 0
    while node[-1] != 'Z':
        node = node_run(nodes, node, run_path[steps2 % len(run_path)])
        steps2 += 1
    cycle_count.append(steps2)
    print(node, steps2)


def prime_factorization(number: int):
    primes = []
    divisor = number
    while True:
        divisor -= 1
        if divisor == 1:
            break
        elif number % divisor == 0:
            primes.append(divisor)
    return primes


def product(list_to_multiply):
    prod = 1
    for item_ in list_to_multiply:
        prod *= float(item_)
    return prod


def flatten(nest_, flat_list_):
    if nest_ == flat_list_:
        raise KeyError
    for i in range(len(nest_)):
        if type(nest_[i]) == list:
            flatten(nest_[i], flat_list_)
        else:
            flat_list_.append(nest_[i])


primes = []
for number in cycle_count:
    primes.append(prime_factorization(number))
flat_primes = []
flatten(primes, flat_primes)
print(flat_primes)
prime_set = set(flat_primes)
print(prime_set)
print('# of steps for a ghost xxA to xxZ:', int(product(prime_set)))
