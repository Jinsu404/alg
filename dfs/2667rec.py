import sys
input = sys.stdin.readline

n = int(input())
map = [list(map(int, input().strip())) for _ in range(n)]
chk = [[False]*n for _ in range(n)]
res = []
cnt = 0

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def dfs(x, y):
    global cnt
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if chk[nx][ny] == False and map[nx][ny] == 1: 
                chk[nx][ny] = True
                dfs(nx,ny)
        

for i in range(n):
    for j in range(n):
        if map[i][j] == 1 and chk[i][j] == False:
            chk[i][j] = True
            cnt = 0
            dfs(i, j)
            res.append(cnt)

res.sort()
print(len(res))
for i in res:
    print(i)
