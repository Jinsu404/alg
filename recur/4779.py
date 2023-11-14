def cantor(n, l) :
    mid = n//3
    if n == 0 : return "-"
    
    for i in range(mid, mid*2):
        l[i]=" "
    l[:mid]= cantor(mid, l[:mid])
    l[mid*2:] = cantor(mid, l[mid*2:])
    return l




while True:
    try:
        n = int(input())
        arr = cantor(3**n, list("-"*(3**n)))
        for i in arr:
            print(i, end='')
        print()
    except: break