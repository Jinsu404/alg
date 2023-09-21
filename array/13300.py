n, k = map(int, input().split())

arr = [[0 for _ in range(6)] for _ in range(2)]

for i in range(n):
    s,g=map(int,input().split())
    arr[s][g-1] +=1

cnt=0
for i in arr:
    for j in i:
        if j>0:
            cnt+= j//k
            if j%k: cnt+=1

print(cnt)
            