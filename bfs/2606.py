import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

d = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

def search(v):
    global cnt
    visited[v] = 1
    for i in d[v]:
        if visited[i] == 0:
            cnt+=1
            search(i)

search(1)

print(cnt)