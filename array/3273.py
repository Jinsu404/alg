import sys
n = int(input())
l=list(map(int,sys.stdin.readline().split()))
x=int(input())

cnt=0
l.sort()
s=0
e=n-1
while s<e:
    sum = l[s]+l[e]
    if sum == x : 
        s+=1
        cnt+=1
    elif sum < x : s+=1
    elif sum > x : e-=1

print(cnt)