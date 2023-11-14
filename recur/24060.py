import sys
n, m = map(int,input().split())

def mergesort( ar ):
    if len(ar) == 1: return ar

    mid = (len(ar)+1) // 2

    L = mergesort(ar[:mid])
    R = mergesort(ar[mid:])

    i, j = 0, 0
    newArr = []
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            newArr.append(L[i])
            res.append(L[i])
            i += 1
        else:
            newArr.append(R[j])
            res.append(R[j])
            j += 1
    while i < len(L):
        newArr.append(L[i])
        res.append(L[i])
        i += 1
    while j < len(R):
        newArr.append(R[j])
        res.append(R[j])
        j += 1

    return newArr


arr = list(map(int, sys.stdin.readline().split()))

res = []

mergesort(arr)

if len(res) >= m:
    print(res[m-1])
else:
    print(-1)