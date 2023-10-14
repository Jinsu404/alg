import sys

n = int(input())
cnt = 0

for _ in range(n):
    p = sys.stdin.readline().rstrip()
    stk = []
    for i in p:
        if stk:
            if stk[-1] == i:
                stk.pop()
            else:
                stk.append(i)
        else:
            stk.append(i)
        
    if len(stk) == 0:
        cnt += 1
    
print(cnt)
