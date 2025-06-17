import sys
input = sys.stdin.readline

N = int(input())

info = []
for i in range(N):
    name, score1, score2, score3 = input().split()
    info.append([name, int(score1), int(score2), int(score3)])

info.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for name in info:
    print(name[0])
