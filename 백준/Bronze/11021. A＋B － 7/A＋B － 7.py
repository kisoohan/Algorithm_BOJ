T = int(input())
n = 0
for i in range(T):
    a, b = map(int, input().split())
    n += 1
    print(f"Case #{n}: {a+b}")
    