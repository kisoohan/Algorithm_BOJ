Dice = list(map(int, input().split()))

if Dice[0] == Dice[1] == Dice[2]:
    print(10000+(Dice[0]*1000))
elif Dice[0] == Dice[1] or Dice[0] == Dice[2]:
    print(1000 + (Dice[0]*100))
elif Dice[1] == Dice[2]:
    print(1000 + (Dice[1]*100))
else:
    print(max(Dice)*100)