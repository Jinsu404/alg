from collections import deque
import sys

n , l = list(map(int, sys.stdin.readline().split()))
d = list(map(int,sys.stdin.readline().split()))

dq = deque()

for i in range(n):
    temp = d[i]
    
    while dq and dq[-1] > temp:
        dq.pop()
    dq.append(temp)
        
    if i >= l and dq[0] == d[i-l]: dq.popleft()
    
    print(dq[0], end=' ')