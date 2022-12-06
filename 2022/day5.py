# day 5
# part 1 - figure out which crates are on top of each stack after move order
#       redo visual display of stack for ease of interaction
#       parse move orders - # to move, from loc1 to loc2

import copy

eof = False
Storage = []
Storage_T = []
lockout_setup = 0
Model = input('Crane model #?\n9000 or 9001\n    > ')

with open('day5_input.txt', 'r') as Read_input:
    while True:
        if eof:
            break

        Orders = Read_input.readline()

        # parse move orders & do the do
        if 'move' in Orders:
            # parsing orders
            Number = int(Orders[5:Orders.index(' f')])
            From_stack = int(Orders[Orders.index('m ')+1:Orders.index(' t')])-1
            To_stack = int(Orders[Orders.index('o ')+1:])-1
            # do the do
            if Model == '9000':  # part 1
                for N in range(Number):  # FILO
                    Crane = Storage_working[From_stack][0]
                    Storage_working[From_stack].pop(0)
                    Storage_working[To_stack].insert(0, Crane)
            else:  # part 2
                Crane = copy.deepcopy(Storage_working[From_stack][0:Number])
                for N in range(Number):
                    # print(Number, N, Crane, Storage_working[From_stack], Storage_working[To_stack])
                    Storage_working[From_stack].pop(0)
                    Storage_working[To_stack].insert(N, Crane[N])
                # print(Storage_working[To_stack])

        # store visual/initial condition of stack
        elif lockout_setup == 0:
            Storage.append(Orders)
            if Orders == '\n':  # end of initial stack
                Storage.pop(-1)  # clean up last blank line
                lockout_setup += 1  # ends setup so stuff isn't weird

                # reorganize/transpose
                for i in range(len(Storage)):  # for each in the list
                    for n in range(int((len(Storage[0])+1)/4)):  # for each 'crate stack'
                        # First in, Last out -aka- FILO
                        if len(Storage_T) < int((len(Storage[0])+1)/4):
                            Storage_T.append([])
                        Storage_T[n].append(Storage[i][4*n+1])

                # copy transcription and remove spaces so first is top
                Storage_working = copy.deepcopy(Storage_T)
                for j in range(len(Storage_working)):
                    for k in range(len(Storage_working[j])):
                        if Storage_working[j][0] == ' ':
                            Storage_working[j].pop(0)
                    Storage_working[j].pop(-1)
                Storage_T = copy.deepcopy(Storage_working)
                print("Setup complete!")
        else:
            print("Done")
            eof = True

# fun print statements for before/after/top crates
print('\n')
for P in range(len(Storage_working)):
    Storage_T[P].reverse()
    print(Storage_T[P])

print('\n')
for PP in range(len(Storage_working)):
    Storage_working[PP].reverse()
    print(Storage_working[PP])

print('\nTop crates are: ')
for p in range(len(Storage_working)):
    print(p+1, ': ', Storage_working[p][-1:])
