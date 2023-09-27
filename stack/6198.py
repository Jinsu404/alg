import sys
n = int(input())
res=0
stk=[]
b=[]

for i in stk:
    while b and b[-1] <= i:
        b.pop()
    res+=len(b)
    b.append(i)
print(res)
