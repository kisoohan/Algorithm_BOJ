num = list(map(int,input().split()))
result = 0

for i in range (0, len(num)):  
    result += num[i] ** 2      

result = result % 10 
print(result)