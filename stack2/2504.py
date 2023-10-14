import sys

p = sys.stdin.readline().rstrip()

stk = []
res = 0
temp = 1
temp2 = ''
flag = True
for i in p:
    if i == '(':
        stk.append(i)
        temp *= 2
    elif i == '[':
        stk.append(i)
        temp*=3
    elif i == ')':
        if not stk or stk[-1] != '(':
            flag = False
            break
        elif temp2 == '(':
            res += temp
        temp//=2
        stk.pop()
    elif i == ']':
        if not stk or stk[-1] != '[':
            flag = False
            break
        elif temp2 == '[':
            res+=temp
        temp//=3
        stk.pop()
    temp2 = i

if flag and not stk: print(res)
else : print(0)