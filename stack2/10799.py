import sys

p = sys.stdin.readline().rstrip()

cnt = 0
stk = []

temp=''
for i in p:
    if i == '(':
        stk.append(i)
        temp = i
    else:
        if stk[-1] == '(' and temp == '(':
           stk.pop()
           temp = i
           cnt+=len(stk)
        else :
            stk.pop()
            cnt+=1
            temp = i

print(cnt)
