import sys
from collections import deque

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
m = int(input())
c = list(map(int, sys.stdin.readline().split()))

dq = deque()
res = []
for i in range(n):
    if a[i] == 0:
        dq.append(b[i])

for j in c:
    dq.appendleft(j)
    res.append(dq.pop())

print(*res)