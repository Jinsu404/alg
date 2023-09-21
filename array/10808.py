x = input()
i = [0]*26

for n in range(len(x)):
    i[ord(x[n])-97]+=1

print(*i)