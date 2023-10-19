import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

arr = [0 for _ in range(100001)]
q = deque()

q.append(n)

while q:
    x = q.popleft()
    if x == m : break
    for i in (x-1, x+1, x*2):
        if 0 <= i <= 100000 and arr[i] == 0:
            arr[i] = arr[x] + 1
            q.append(i)

print(arr[m])