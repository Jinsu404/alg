import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
  arr.append(list(map(int, input())))


dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(a, b):
    q = deque()
    q.append((a,b))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = arr[x][y] + 1
                    q.append((nx,ny))
    return arr[n-1][m-1]

print(bfs(0,0))

