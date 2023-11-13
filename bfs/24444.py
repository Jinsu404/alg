import sys
sys.setrecursionlimit(10 ** 8)
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())

d = [[] for _ in range(n+1)]
visited = [0]*(n+1)
cnt=1

for i in range(m):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

for j in range(n+1):
    d[j].sort()

def bfs(v):
    global cnt

    q = deque([r])
    visited[r] = 1
    while q:
        v = q.popleft()
        for g in d[v]:
            if visited[g] == 0:
                cnt += 1
                visited[g] = cnt
                q.append(g)

bfs(r)

for k in range(1, n+1):
    print(visited[k])