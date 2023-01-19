n, m = [int(i) for i in input().split()]
way = [1]                                      
while 1:
    way.append((way[-1] + m - 1) % n)
    if way[-1] == 0:
        way[-1] = n
    if way[-1] == 1:
        way.pop()
        break
print(*way, sep='')   