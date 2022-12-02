##Kithin's (dot)py code for AdventOfCode.com/2017/day/1
# 1122 sums to 3 (1+2)
# 1111 sums to 4 all 1s match the next
# 1234 sums 0
# 91212129 sums 9 
# -circular_list -loop -checking -variable_length -input -output
Checking = True
Upcount = 0
Sum = 0
print("T O T A L L Y   A   R O B O T")
Captcha = input("Please enter the number: ")
Num_length = len(str(Captcha))
while Checking == True:
    if Num_length > Upcount+1:
        if Captcha[Upcount] == Captcha[Upcount + 1]:
            Sum = Sum + int(Captcha[Upcount])
            Upcount = Upcount + 1
        else:
            Upcount = Upcount + 1
            
    elif Num_length == Upcount+1:
        if Captcha[0] == Captcha[Num_length-1]:
            Sum = Sum + int(Captcha[0])
            Upcount = Upcount + 1
            Checking = False
        else:
            Upcount = Upcount + 1
            Checking = False
            
    elif Num_length == Upcount - 1:
        Checking = False
        
    else:
        Checking = False
        print("oops, something went wrong...")
print(Sum)
