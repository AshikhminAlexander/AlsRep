import sys

with open(sys.argv[1], 'r') as dm:
    dm = [int(i.strip()) for i in dm.readlines()]
res = 0
avg = round(sum(dm) / len(dm)) 
   
for i in dm:
    res += abs(i - avg)
    
print(res)