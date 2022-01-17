N,K = map(int,input().split())
coin = []

count = 0
for i in range(N):
    x = int(input())
    if x > K:
        continue
    else:
        coin.append(x)


for c in coin[::-1]:
    a = K // c
    K -= c*a
    count += a
    if K == 0:
        break
print(count)
