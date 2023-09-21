x=list(str(input()))
n=[0]*10
for i in range(len(x)):
    if(x[i]=='6'):
        if(n[6]<=n[9]):n[6]+=1
        else:n[9]+=1
    elif(x[i]=='9'):
        if(n[6]>=n[9]):n[9]+=1
        else:n[6]+=1
    else: n[int(x[i])]+=1

print(max(n))