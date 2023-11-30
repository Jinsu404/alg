num = int(input())

arr = [999 for _ in range(num+1)]
arr[1] = 0

for i in range(2, num+1):
    arr[i]=arr[i-1]+1
    if (i%3)==0:
        arr[i]=min(arr[i], arr[i//3]+1)
    if (i%2)==0:
        arr[i]=min(arr[i], arr[i//2]+1)

print(arr[num])