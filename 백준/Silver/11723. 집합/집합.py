import sys
input = sys.stdin.readline

S = set()
M = int(input())

for _ in range(M):
    cal = input().split()
    if cal[0] == 'add':
        S.add(int(cal[1]))
    elif cal[0] == 'remove':
            S.discard(int(cal[1]))
    elif cal[0] == 'check':
        if int(cal[1]) in S:
            print(1)
        else:
            print(0)
    elif cal[0] == 'toggle':
        if int(cal[1]) in S:
            S.remove(int(cal[1]))
        else:
            S.add(int(cal[1]))
    elif cal[0] == 'all':
        S = set(range(1, 21))
    elif cal[0] == 'empty':
        S.clear()
            
    
