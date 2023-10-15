n = int(input())

for i in range(n):
    print(' '*i,'*'*((n-i)*2-1),sep='')
for i in range(n-2, -1 , -1):
    for j in range(i):
        print(' ',end='')
    for k in range((n-i)*2-1):
        print('*',end='')
    print('')