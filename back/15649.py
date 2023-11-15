import sys
input = sys.stdin.readline

n, m = map(int, input().split())
res = []
chk = [False] * (n + 1)

def rec(num):
    if num == m:
        print(' '.join(map(str, res)))
        return
    for i in range(1, n+1):
        if chk[i] == False:
            chk[i] = True
            res.append(i)
            rec(num+1)
            chk[i] = False
            res.pop()

rec(0)