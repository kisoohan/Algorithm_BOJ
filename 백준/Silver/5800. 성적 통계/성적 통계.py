K = int(input())

score = []
for i in range(K):
    score.append(list(map(int, input().split())))
    score[i] = sorted(score[i][1:],reverse= True)

for i in range(K):
    gap = []
    print(f"Class {i+1}")
    for j in range(len(score[i])-1):
        gap.append(score[i][j] - score[i][j+1])
    print(f"Max {max(score[i])}, Min {min(score[i])}, Largest gap {max(gap)}")
        


    







    
    
            
    

