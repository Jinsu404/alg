import sys

word = list(sys.stdin.readline().rstrip())
n = int(input())
copy=[]

for _ in range(n):
    c = sys.stdin.readline().split()
    if c[0] == 'L' and len(word) > 0:
        copy.append(word.pop())
    elif c[0] == 'D' and len(copy) > 0:
        word.append(copy.pop())
    elif c[0] == 'B' and len(word) > 0 :
        word.pop()
    elif c[0] == 'P':
        word.append(c[1])

for i in word:
    print(i, end="")
for j in reversed(copy):
    print(j, end="")