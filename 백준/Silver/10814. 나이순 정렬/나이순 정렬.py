N = int(input())
mem = []

for _ in range(N):
    age, name = input().split()
    mem.append((int(age), name))

mem = sorted(mem, key = lambda x:x[0])

for age, name in mem:
    print(age, name)