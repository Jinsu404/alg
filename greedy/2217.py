n = int(input())

r = []
w = []
cnt = 1

for _ in range(n):
    r.append(int(input()))

r.sort(reverse=True)

for i in r:
    w.append(i*cnt)
    cnt +=1
    
print(max(w))