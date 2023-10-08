import sys
from collections import deque

n = int(input())
queue = deque([])

for _ in range(n):
    c = sys.stdin.readline().split()
    if c[0] == 'push' : queue.append(c[1])
    elif c[0] == 'pop' :
        if queue: print(queue.popleft())
        else : print(-1)
    elif c[0] == 'size': print(len(queue))
    elif c[0] == 'empty': 
        if len(queue) == 0 : print(1)
        else : print(0)
    elif c[0] == 'front' :
        if queue: print(queue[0])
        else : print(-1)
    elif c[0] == 'back' :
        if queue: print(queue[-1])
        else : print(-1)