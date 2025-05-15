while True:
    A = input().split()
    name = A[0]
    age = int(A[1])
    weight = int(A[2])
    
    if name == '#' and age == 0 and weight == 0:
        break
    elif age > 17 or weight >= 80:
        print(name, "Senior")
    else:
        print(name, "Junior")