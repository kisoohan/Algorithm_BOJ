N, M = map(int, input().split())

dic_poke = {}
dic_num = {}
for i in range(1,N+1):
    key = input()
    dic_poke[key] = i
    dic_num[str(i)] = key

for _ in range(M):
    a = input()
    if a.isdigit():
        print(dic_num[a])
    else:
        print(dic_poke[a])