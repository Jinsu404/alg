import math

n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))

    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    if distance == 0:
        if r1 == r2: print(-1)
        else: print(0)
    else:
        if (r1+r2) == distance or abs(r2-r1) == distance:
            print(1)
        elif (r1+r2) > distance and abs(r2-r1) < distance:
            print(2)
        else:
            print(0) 
        