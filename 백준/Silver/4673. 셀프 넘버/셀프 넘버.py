num = []
total = 0

def process(N):
    total = N
    for i in str(N):
        total += int(i)
    num.append(total)

for i in range(1, 10001):
     process(i)

for i in range(1, 10001):
    if i not in num:
        print(i)