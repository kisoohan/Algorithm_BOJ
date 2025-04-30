first_color = input()
second_color = input()
third_color = input()

dic = {
    'black':[0, 1],
    'brown':[1, 10],
    'red':[2, 100],
    'orange':[3, 1000],
    'yellow':[4, 10000],
    'green':[5, 100000],
    'blue':[6,1000000],
    'violet':[7,10000000],
    'grey':[8,100000000],
    'white':[9,1000000000]}

value1, mul1 = dic[first_color]
value2, mul2 = dic[second_color]
value3, mul3 = dic[third_color]

result = ((value1 *10) + value2) * mul3
print(result)