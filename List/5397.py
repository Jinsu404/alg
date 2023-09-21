n = int(input())

for _ in range(n):
    s = input()
    pw1 = []
    pw2 = []
    for i in s:
        if i == '<':
            if len(pw1) > 0:
                pw2.append(pw1.pop())
        elif i == '>' : 
            if len(pw2) > 0:
                pw1.append(pw2.pop())
        elif i == '-' : 
            if len(pw1) > 0:
                pw1.pop()
        else:
            pw1.append(i)
    pw1.extend(reversed(pw2))
    
    print(''.join(pw1))