import sys
input = sys.stdin.readline

n, m = map(int, input().split())

res = []
checked = [False]* (n+1)

def rec(num):
    if len(res) == m:
        print(' '.join(map(str, res)))
        return
    for i in range(num, n+1):
        if checked[i] == False:
            checked[i] = True
            res.append(i)
            rec(i+1)
            checked[i]=False
            res.pop()

rec(1)

