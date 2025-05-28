dic = {
    'A+' : 4.3,
    'A0' : 4.0,
    'A-' : 3.7,
    'B+' : 3.3,
    'B0' : 3.0,
    'B-' : 2.7,
    'C+' : 2.3,
    'C0' : 2.0,
    'C-' : 1.7,
    'D+' : 1.3,
    'D0' : 1.0,
    'D-' : 0.7,
    'F'  : 0.0}

N = int(input())
score = 0 
credit_num = 0 

for i in range(N):
    sub_name, credit, grade = input().split()
    credit = int(credit)
    grade = dic[grade]
    credit_num += credit
    score += credit * grade

avg = (score / credit_num)
avg = round(avg + 1e-8, 2)
print(f"{avg:.2f}")