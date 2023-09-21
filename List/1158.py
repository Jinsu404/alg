n, k = map(int, input().split())
a = [i for i in range(1,n+1)]
res=[]
c=k-1
while(a):
    if c >= len(a):
        c = c % len(a)
    else:
        res.append(str(a.pop(c)))
        c += k-1

print("<", ", ".join(res), ">", sep='')