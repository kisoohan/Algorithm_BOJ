N = int(input())
num = map(int, input().split())
result = sorted(set(num))

print(' '.join(map(str, result)))
