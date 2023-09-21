sum=1
for i in range(3):
    sum*=int(input())
s=list(str(sum))
for j in range(10):
    print(s.count(str(j)))