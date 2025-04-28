T = int(input())
list = []

for i in range(T):
    a = input()
    list.append(a)

list = set(list)
result = sorted(list, key = lambda x: (len(x), x))

for i in result:
    print(i)
