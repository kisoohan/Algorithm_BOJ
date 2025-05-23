word = input()
count = 0 
for i in 'aeiou':
    count += word.count(i)
print(count) 