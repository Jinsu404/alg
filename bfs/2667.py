import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

arr = []
cnt = 0
sizeArr = []

for _ in range(n):
  # arr.append(list(map(int, input().rstrip())))
  arr.append(list(map(int, list(input().rstrip()))))

dy = [0,1,0,-1]
dx = [1,0,-1,0]


def bfs(a, b):
    q = deque()
    q.append((a, b))
    arr[a][b] = 0
    size = 1
   
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and n > ny >=0 and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                size += 1
                q.append((nx,ny))
    return(size)

for i in range(n):
  for j in range(n):
    if arr[i][j] == 1:
        sizeArr.append(bfs(i,j))
        cnt+=1

sizeArr.sort()
print(cnt)
for i in sizeArr:
   print(i)