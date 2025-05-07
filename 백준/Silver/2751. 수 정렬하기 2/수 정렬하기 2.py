import sys

N = int(sys.stdin.readline())
num = []

for i in range(N):
    a = int(sys.stdin.readline())
    num.append(a)

num.sort()

for number in num:
    print(number)
