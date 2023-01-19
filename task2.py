SecAddr, DotsAddr = input(), input()
with open(SecAddr, 'r') as sec:
    ox, oy = [float(i) for i in sec.readline().strip().split()]
    r=float(sec.readline())

with open(DotsAddr, 'r') as dots:
    dots = dots.readlines()
    
for i in dots:
    x, y = [float(j) for j in i.strip().split()]
    
    if (x - ox)**2 + (y - oy)**2 == r**2:
        print(0)
    elif (x - ox)**2 + (y - oy)**2 < r**2:
        print(1)
    else:
        print(2)