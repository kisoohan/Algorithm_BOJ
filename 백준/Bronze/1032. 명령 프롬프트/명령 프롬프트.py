N = int(input())

name_list = []

for i in range(N):
    name_list.append(input())

file_len = len(name_list)
pattern = list(name_list[0])

for i in range(len(pattern)):
    for j in range(1, N):
        if name_list[j][i] != pattern[i]:
            pattern[i] = '?'

print(''.join(pattern))