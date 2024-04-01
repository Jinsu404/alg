n = int(input())

arr = list(map(int, input().split()))
x = int(input())
cnt = 0
arr.sort()

s, e = 0, n-1
while s<e:
    if (arr[s]+arr[e]) < x:
        s +=1
    elif (arr[s]+arr[e] > x):
        e -= 1
    else:
        s += 1
        cnt +=1
print(cnt)