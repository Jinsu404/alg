n = int(input())

for q in range(n):
    m = int(input())
    l = list(input().rstrip())
    flag = True
    if (m%2) == 1:
        flag = False
    else:
        for i in range(m//2):
            if l[i] != l[m//2+i]:
                flag = False
    
    if flag:
        print(f'#{q+1} Yes')
    else:
        print(f'#{q+1} No')
