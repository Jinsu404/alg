import sys
from collections import deque
input = sys.stdin.readline

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(a, b):
    q = deque()
    q.append((a, b))
    arr[a][b] = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < m and arr[nx][ny] == 1:
                q.append((nx,ny))
                arr[nx][ny] = 0

t = int(input())

for _ in range(t):
    cnt = 0

    m,n,k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]
    for _ in range(k):
        x,y = map(int, input().split())
        arr[y][x] = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                cnt+=1
                bfs(i,j)
    print(cnt)



