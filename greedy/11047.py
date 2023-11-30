import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coin = []
cnt = 0
for _ in range(n):
    coin.append(int(input()))

for i in range(n):
    if  k >= coin[n-i-1]:
        cnt += k//coin[n-i-1]
        k = k % coin[n-i-1]

print(cnt)