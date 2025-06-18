N, K = map(int,input().split())

stack = []
for i in range(N):
    stack.append(i+1)

result = []
index = 0

while len(stack) != 0:
    index = (index + K - 1) % len(stack)
    a = stack.pop(index)
    result.append(a)
    
print('<' + ', '.join(map(str, result)) + '>')