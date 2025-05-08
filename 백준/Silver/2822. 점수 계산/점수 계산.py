score = []
line = []
sum = 0

for i in range(8):
    n = int(input())
    score.append((n, i+1))

score.sort(reverse = True)

for i in range(5):
    sum += score[i][0]
print(sum)

for i in range(5):
    line.append(score[i][1])

line.sort()
print(' '.join(map(str, line)))