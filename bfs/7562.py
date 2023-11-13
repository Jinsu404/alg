import sys
from collections import deque
input = sys.stdin.readline

n=int(input())


dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(a, b):
    q = deque()
    q.append((a, b))
    
    while q:
        x,y = q.popleft()
        if x == gx and y == gy:
            print(arr[x][y]-1)
            return
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx,ny))

for _ in range(n):  
    l = int(input())
    arr = [[0]*l for _ in range(l)]
    kx, ky = map(int, input().split())
    gx, gy = map(int, input().split())
    arr[kx][ky]= 1

    if kx == gx and ky == gy:
        print(0)
        continue
    bfs(kx, ky)


