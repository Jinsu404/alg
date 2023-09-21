l = []
for i in range(9):
    l.append(int(input()))

a=0
b=0
for j in range(8):
    for k in range(j+1,9):
        if(sum(l)-(l[j]+l[k]) == 100):
            a=l[j]
            b=l[k]
            break

l.remove(a)
l.remove(b)
l.sort()
for n in l:
    print(n)
