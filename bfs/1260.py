import sys
sys.setrecursionlimit(10 ** 8)
from collections import deque

input = sys.stdin.readline

n, m, r = map(int,input().split())

d = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    s, e = map(int,input().split())
    d[s].append(e)
    d[e].append(s)

for j in range(n+1):
    d[j].sort()


def dfs(v):
    print(v, end=' ')
    visited[v]=1
    for w in d[v]:
        if visited[w] == 0:
            dfs(w)

dfs(r)

print('')

visited2 = [0] * (n+1)

def bfs(v):
    q = deque([r])
    visited2[v] = 1
    while q:
        v = q.popleft()
        print(v, end=' ')
        for g in d[v]:
            if visited2[g] == 0:
                visited2[g] = 1
                q.append(g)

bfs(r)

