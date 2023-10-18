import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

cnt = 0
res = 0

q = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            cnt += 1
            q.append((i, j))
        if arr[i][j] == -1:
            cnt += 1

if cnt == n * m : print('0')
else : 
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0:
                    arr[nx][ny] += arr[x][y] + 1
                    q.append((nx,ny))
    Zcnt = 0
    for k in arr:
        if k.count(0): Zcnt += 1
    if Zcnt > 0: print(-1)
    else : print(max(map(max, arr))-1)



