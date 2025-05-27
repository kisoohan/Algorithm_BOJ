N, M = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int,input().split())))

M, K = map(int, input().split())
B = []
for i in range(M):
    B.append(list(map(int,input().split())))

result_matrix = [] 
for i in range(N):
    j_result = []
    for j in range(K):
        add = 0
        for k in range(M):
            add += (A[i][k] * B[k][j])
        j_result.append(add)
    result_matrix.append(j_result)

for row in result_matrix:
    print(' '.join(map(str, row)))