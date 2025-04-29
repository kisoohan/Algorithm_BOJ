N = int(input())
F = int(input())

N = (N//100)*100

for i in range(100):
    if((N + i) % F == 0):
        result = N+i
        break

two = result % 100
print(f"{two:02d}")