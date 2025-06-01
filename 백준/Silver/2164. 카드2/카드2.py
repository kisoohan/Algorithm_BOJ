from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
num = deque(range(1,N+1))

while len(num) != 1:
    num.popleft()
    num.append(num.popleft())

print(''.join(map(str,num)))
        