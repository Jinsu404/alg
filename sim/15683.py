import sys, copy
input = sys.stdin.readline

n , m = map(int, input().split())
arr = []
cctv = []
cctv_cnt = 0
minN = n*m+1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
mode = [
    [],
    [[0],[1],[2],[3]],
    [[0, 2],[1, 3]],
    [[0,1],[1,2],[2,3],[3,0]],
    [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    [[0,1,2,3]]
]

def watch(x, y, dir, temp):
    for i in dir:
        nx, ny = x, y
        while True:
            nx = nx + dx[i]
            ny = ny + dy[i]
            if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] != 6:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = -1
            else:
                    break


def solve(room, C):
    global minN
    temp = copy.deepcopy(room)

    if C == cctv_cnt:
        tc = 0
        for i in temp:
            tc += i.count(0)
        minN = min(tc, minN)
        return
    modeN, x, y = cctv[C]
    for i in mode[modeN]:
        watch(x, y, i, temp)
        solve(temp, C+1)
        temp = copy.deepcopy(room)


for i in range(n):
    l = list(map(int, input().split()))
    arr.append(l)
    for j in range(m):
        if l[j] in [1, 2, 3, 4, 5]:
            cctv.append([l[j], i, j]) # cctv 리스트에 mode, 좌표값 넣기
            cctv_cnt += 1

solve(arr, 0)
print(minN)
