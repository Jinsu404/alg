import sys
n = int(input())

paper = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n):
    a, b = map(int,sys.stdin.readline().split())
    for i in range(10):
        for j in range(10):
            paper[a+i-1][b+j-1] = 1

cnt = 0
for i in paper:
    cnt += i.count(1)
print(cnt)

 