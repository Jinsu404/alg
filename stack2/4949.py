import sys

while True:
    p = sys.stdin.readline().rstrip()

    if p == '.': break
    flag = True

    stk = []
    for i in p:
        if i == '(' or i =='[':
            stk.append(i)
        elif i == ')':
            if stk and stk[-1] == '(':
                stk.pop()
            else : 
                flag = False
                break
        elif i == ']':
            if stk and stk[-1] == '[':
                stk.pop()
            else : 
                flag = False
                break
    if flag and len(stk) == 0:
        print('yes')
    else : 
        print('no')