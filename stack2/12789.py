import sys

n = int(input())
p = list(map(int, sys.stdin.readline().split()))

stk = []
cnt = 1

for i in p:
    if cnt == i:
        cnt+=1
    else:
        stk.append(i)
    while stk:
        if stk[-1] == cnt:
            cnt +=1
            stk.pop()
        else:
            break

if not stk:
    print('Nice')
else:
    print('Sad')