N, K = map(int,input().split())

coin = []
for i in range(N):
    coin.append(int(input()))

coin.sort(reverse = True)

count = 0
for coins in coin:
    if K == 0:
        break
    count += K // coins
    K %= coins
    
print(count)