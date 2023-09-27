n = int(input())

cnt = 1
stk =[]
res=[]
c = True
for _ in range(n):
    a = int(input())
    while cnt <= a :
        stk.append(cnt)
        res.append('+')
        cnt+=1
        
    if stk[-1] == a:
        stk.pop()
        res.append('-')
    else:
        c = False
        break

if c :
    for i in res:
        print(i)
else:
    print('NO')