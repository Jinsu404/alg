from collections import deque
import sys

d=deque()
n = int(input())

for _ in range(n):
    c = sys.stdin.readline().split()
    if c[0] == 'push_front':
        d.appendleft(c[1])
    elif c[0] == 'push_back':
        d.append(c[1])
    elif c[0] == 'pop_front':
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif c[0] == 'pop_back':
        if d:
            print(d.pop())
        else:
            print(-1)
    elif c[0] == 'size':
        print(len(d))
    elif c[0] == 'empty':
        if d:
            print(0)
        else:
            print(1)
    elif c[0] == 'front':
        if d:
            print(d[0])
        else:
            print(-1)
    elif c[0] == 'back':
        if d:
            print(d[-1])
        else:
            print(-1)