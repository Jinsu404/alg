for i in range(3):
    x = list(map(int, input().split()))
    if(x.count(0)==0): print('E')
    elif(x.count(0)==1): print('A')
    elif(x.count(0)==2): print('B')
    elif(x.count(0)==3): print('C')
    else: print('D')