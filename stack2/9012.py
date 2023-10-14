import sys

n = int(input())

for _ in range(n):
    p = sys.stdin.readline().rstrip()
    stk=[]
    for i in p:
        if i == '(':
            stk.append(i)
        else:
            if stk:
                stk.pop()
            else:
                stk.append(i)
                break
    if stk:
        print('NO')
    else:
        print('YES')