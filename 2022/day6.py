# day 6
# 4 characters in a set, review in order of 'datastream'
# first 'marker' (aka set) after how many characters?
N = 4
#N = int(input('N = '))
M = 14
spot1 = 0
spot2 = 0
Datastream = []
Data2 = []
No_match = [False] * N
Message = [False] * M

eof1 = False
eof2 = False
with open('day6_input.txt', 'r') as Read_input:
    while True:
        if eof1 and eof2:
            break
        if not eof1:
            spot1 += 1
        if not eof2:
            spot2 += 1
        Bit = Read_input.readline(1)
        Datastream.append(Bit)  # read 1 at a time
        Data2.append(Bit)

        if len(Datastream) > N:  # keep trimmed to N
            Datastream.pop(0)
            for i in range(N):
                if Datastream.count(Datastream[i]) >= 2:  # match found, so go next
                    No_match[i] = False
                    break
                else:
                    No_match[i] = True
            if No_match.count(True) == N and spot1 >= N:
                Output = spot1
                eof1 = True

        # part 2 - message check, needs 14 unique characters
        if len(Data2) > M:  # keep trimmed to M
            Data2.pop(0)
            for i in range(M):
                if Data2.count(Data2[i]) >= 2:  # match found, so go next
                    Message[i] = False
                    break
                else:
                    Message[i] = True
            if Message.count(True) == M and spot2 >= M:
                Output2 = spot2
                eof2 = True


print(Datastream)
print(Output)
print(Data2)
print(Output2)

