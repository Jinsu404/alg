import sys
from collections import deque

n, m = list(map(int,sys.stdin.readline().split()))
l = list(map(int,sys.stdin.readline().split()))
d = deque()

cnt = 0

for i in range(1,n+1):
    d.append(i)

while l:
    if l[0] == d[0]:
        l.pop(0)
        d.popleft()
    else:
        if d.index(l[0]) > len(d)/2 :
            d.appendleft(d.pop())
            cnt += 1
        else:
            d.append(d.popleft())
            cnt += 1
print(cnt)