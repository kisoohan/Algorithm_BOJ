N, x = map(int,input().split())
A = list(map(int, input().split()))
num = []

for i in range(N):
    if x > A[i]:
        num.append(A[i])
        
print(' '.join(map(str,num)))