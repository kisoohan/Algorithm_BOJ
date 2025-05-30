N = int(input())
A = set(input().split())

M = int(input())
B = input().split()

for i in B:
    if i in A:
        print(1)
    else:
        print(0)