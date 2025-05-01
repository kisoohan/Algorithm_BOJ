num = list(map(int, input().strip()))  # 입력을 문자 단위로 나눠서 정수로 변환하여 리스트에 저장
count = 0

if len(num) == 1:
    if num[0] % 3 == 0:
        print(0)
        print("YES")
    else:
        print(0)
        print("NO")
else:
    while len(num) > 1:
        sum_num = sum(num)
        num = list(map(int, str(sum_num)))
        count += 1

    if sum_num % 3 == 0:
        print(count)
        print("YES")
    else:
        print(count)
        print("NO")
