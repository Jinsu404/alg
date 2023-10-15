from collections import deque
import sys

n , l = list(map(int, sys.stdin.readline().split()))
d = list(map(int,sys.stdin.readline().split()))

dq = deque()

for i in range(n):
    
    while dq and dq[-1] > d[i]:
        dq.pop()
    dq.append(d[i])

    if i >= l and d[i-l] == dq[0]:
        dq.popleft()

    print(dq[0],end=' ')