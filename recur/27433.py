import sys

n = int(input())

res = 1

def fac(n) :
    global res
    if n > 1:
        res = res * n
        n -= 1
        fac(n)

fac(n)
print(res)