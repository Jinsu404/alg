a1 = list(input())
b1 = list(input())
w = [0]*26
for i in a1:
    w[ord(i)-ord('a')] += 1
for j in b1:
    w[ord(j)-ord('a')] -= 1
        

print(sum(map(abs,w)))