import sys

n = int(input())

def rec(st, a, b):
    global cnt
    cnt += 1
    if a >= b : return 1
    elif st[a] != st[b] : return 0
    else : return rec(st, a+1, b-1)


def isPal(st):
    return rec(st, 0, len(st)-1)


for _ in range(n):
    s = sys.stdin.readline().rstrip()
    cnt = 0
    print(isPal(s) , cnt)