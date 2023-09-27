import sys
n= int(input())
stk = list(map(int,sys.stdin.readline().split()))
res=[-1]*n
b=[]
for i in range(n):
    while b and stk[b[-1]] < stk[i]:
        res[b.pop()]=stk[i]
    b.append(i)

print(*res)