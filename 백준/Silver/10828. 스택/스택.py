from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

stack = deque()
for i in range(N):
    command = input().split()

    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        print(-1 if not stack else stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(1 if not stack else 0)
    elif command[0] == 'top':
        print(-1 if not stack else stack[-1])