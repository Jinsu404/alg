import sys
sys.setrecursionlimit(10 ** 8)
from collections import deque

input = sys.stdin.readline

n, m, r = map(int,input().split())

q = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    s, e = map(int,input().split())
    q[s].append(e)
    q[e].append(s)

for j in range(n+1):
    q[j].sort()

cnt = 1

def dfs(v):
    global cnt 
    visited[v]=cnt
    cnt += 1
    for w in q[v]:
        if visited[w] == 0:
            dfs(w)

dfs(r)

for k in range(1, n+1):
    print(visited[k])