"""
n - 벽길이
m - 롤러 길이
section - 칠해야 하는곳 위치
"""
def solution(n, m, section):
    arr = [0 for _ in range(n)]
    cnt = 0
    
    for i in section:
        arr[i-1] = 1
    for j in range(len(arr)):
        if arr[j] == 1:
            cnt += 1
            for k in range(j,j+m):
                if k == n : break
                arr[k] = 0
            
    
    return cnt