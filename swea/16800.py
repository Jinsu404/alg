import sys
input = sys.stdin.readline
t = int(input())


for q in range(t):
    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]
    temp = 0

    res = []

    for i in range(n-m+1):
        for l in range(n-m+1):
            for j in range(m):
                for k in range(m):
                    temp+= arr[i+j][l+k]

            res.append(temp)
            temp=0

    print(f'#{q+1} {max(res)}')