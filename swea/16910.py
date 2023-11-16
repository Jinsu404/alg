n = int(input())


for i in range(n):
    m = int(input())
    cnt = 0
    for j in range(1, m+1):
        for k in range(1, m+1):
            if m*m >= (j*j + k*k):
                cnt +=1
    
    print(f'#{i+1} {(cnt+m)*4+1}')