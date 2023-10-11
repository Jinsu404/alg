import sys
from collections import deque

t = int(input())

for _ in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    d = sys.stdin.readline().rstrip()[1:-1].split(",")
    dq = deque(d)
    flag = True
    r = 0

    if n == 0:
        dq=[]
    for c in p:
        if c == 'R':
            r += 1
        elif c == 'D':
            if len(dq)==0:
                print('error')
                flag=False
                break
            else:
                if r % 2 == 0:
                    dq.popleft()
                else:
                    dq.pop()
    if flag: 
        if r % 2 == 1:
            dq.reverse()
        print('[' + ','.join(dq) + ']')
        