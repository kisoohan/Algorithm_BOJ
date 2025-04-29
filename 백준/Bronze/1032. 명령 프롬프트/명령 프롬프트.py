N = int(input()) #파일 갯수

name_list = []
for i in range(N):
    name_list.append(input())

file_length = len(name_list[0]) #파일 이름 갯수
pattern = list(name_list[0]) #pattern에 첫번째 파일 이름 저장

for i in range(file_length):# 파일 이름 갯수만큼 반복
    for j in range(1, N): #두 번째 파일부터 마지막 파일까지 반복 
        if name_list[j][i] != pattern[i]:
            pattern[i] = '?'
            break
    
print(''.join(pattern))
