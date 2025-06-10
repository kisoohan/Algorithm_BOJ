import sys
input = sys.stdin.readline

N = int(input())

time = []
for i in range(N):
    start, end = map(int,input().split())
    time.append([start, end])

time.sort(key = lambda x : (x[1],x[0]))

count = 0
last_time = 0

for start, end in time:
    if start >= last_time:
        count += 1
        last_time = end
        
print(count)