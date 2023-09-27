import sys
n = int(input())
top = list(map(int, sys.stdin.readline().split()))
stk = []
res = [0] * n
for i in range(0,n):
    while stk:
        if stk[-1][0] >= top[i]:
            res[i] = stk[-1][1]+1
            break
        else:
            stk.pop()
            
    stk.append((top[i],i))

print(*res)