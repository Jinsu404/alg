import sys
input = sys.stdin.readline

n, m = map(int, input().split())
res = []

def rec(num):
    if len(res) == m:
        print(' '.join(map(str, res)))
        return
    for i in range(num, n+1):
            res.append(i)
            rec(i)
            res.pop()

rec(1)