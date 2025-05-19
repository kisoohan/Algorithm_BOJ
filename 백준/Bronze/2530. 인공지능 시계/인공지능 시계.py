hour, minute, second = map(int,input().split())
time = int(input())

minute += time//60
second += time % 60


if second >= 60:
    minute += second // 60
    second %= 60

if minute >= 60:
    hour += minute // 60
    minute %= 60

hour %= 24
    
print(hour, minute, second)
