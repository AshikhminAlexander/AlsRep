DimAddr = input()
res = 0
with open(DimAddr, 'r') as Dm:
    Dm = [int(i.strip()) for i in Dm.readlines()]
avg = round(sum(Dm) / len(Dm))    
for i in Dm:
    res += abs(i - avg)
print(res)