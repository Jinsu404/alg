n = int(input())

for _ in range(n):
    res = True
    k = [0]*26
    a, b = map(str,input().split())
    a1=list(a)
    b1=list(b)
    for i in a1:
        k[ord(i)-ord('a')] += 1
    for j in b1:
        k[ord(j)-ord('a')] -= 1
    for l in k:
        if l != 0 : res=False
    if res == True: 
        print('Possible')
    else: 
        print('Impossible')