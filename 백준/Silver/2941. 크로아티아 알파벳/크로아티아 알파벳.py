word = input()
alpha = ['c=','dz=','lj','nj','c-','d-','s=','z=']

for i in alpha:
    word = word.replace(i, '*')

print(len(word))
    