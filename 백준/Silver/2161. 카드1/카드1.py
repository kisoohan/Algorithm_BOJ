num = int(input())

card_list = []
trash_list= []

for i in range(1, num+1):
    card_list.append(i)

if len(card_list) == 1:
    print(card_list[0])
else:
    while len(card_list) > 1:
        num1 = card_list.pop(0)
        trash_list.append(num1)
        
        num2 = card_list.pop(0)
        card_list.append(num2)

    trash_list.append(card_list[0])
    
    result = list(map(str,trash_list))    
    print(' '.join(result)) 