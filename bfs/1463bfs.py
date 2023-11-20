from collections import deque

n = int(input())

arr=[0] * (n+1)
q = deque()
q.append(n)
while q:
    tmp = q.popleft()
    if tmp == 1:
        break
    if tmp % 3 == 0 and arr[tmp//3] == 0:
        q.append(tmp//3)
        arr[tmp//3] = arr[tmp]+ 1
    if tmp % 2 == 0 and arr[tmp//2] == 0:
        q.append(tmp//2)
        arr[tmp//2] = arr[tmp]+ 1
    if arr[tmp-1] == 0:
        q.append(tmp-1)
        arr[tmp-1] = arr[tmp] + 1

print(arr[1])