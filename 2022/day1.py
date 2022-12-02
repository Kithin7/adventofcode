# day1
import math
import pandas as pd
inventory = pd.read_csv(open('day1_input.csv','r'),header=None, skip_blank_lines=False)
inventory.insert(1,'sum',0)
for i in range(len(inventory)):
    if math.isnan(inventory.iat[i,0]):
        continue
    else:
        try:
            inventory.iat[i, 1] = inventory.iat[i, 0] + inventory.iat[i-1, 1]
        except:
            inventory.iat[i, 1] = inventory.iat[i, 0]
        else:
            inventory.iat[i, 1] = inventory.iat[i, 0] + inventory.iat[i-1, 1]
#print(inventory)
print('Max calories is: ',max(inventory.iloc[:,1]))
#part 2
top3 = inventory.nlargest(3,'sum')
#print(top3)
print('Sum of top 3 is: ',sum(top3.iloc[:,1]))
