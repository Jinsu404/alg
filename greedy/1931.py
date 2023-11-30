import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
end = 0
time = []

for _ in range(n):
    time.append(list(map(int, input().split())))

time.sort(key=lambda x:(x[1], x[0]))

for i in time:
    if i[0] >= end:
        end = i[1]
        cnt += 1
print(cnt)