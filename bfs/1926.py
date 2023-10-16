import sys
from collections import deque

cnt = 0 
MaxSize = 0

n, m = map(int,sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(i , j):
    size = 1
    q = deque()
    q.append((i,j))

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<= nx < n and 0<= ny < m:
                if arr[nx][ny] == 1 and not visited[nx][ny]:
                    size += 1
                    visited[nx][ny] = True
                    q.append((nx,ny))
    return size

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            cnt +=1
            r = bfs(i,j)
            if MaxSize < r:
                MaxSize = r

print(cnt)
print(MaxSize)

