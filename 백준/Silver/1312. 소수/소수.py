A, B, N = map(int, input().split())

remainder = A%B

result = []
for i in range(N):
    result.append((remainder * 10) // B)
    remainder = (remainder * 10) % B

print(result[N-1])