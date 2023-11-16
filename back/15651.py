import sys
input = sys.stdin.readline

n, m = map(int, input().split())
res = []

def rec(num):
    if len(res) == m:
        print(' '.join(map(str, res)))
        return
    for i in range(1, n+1):
            res.append(i)
            rec(num)
            res.pop()

rec(0)