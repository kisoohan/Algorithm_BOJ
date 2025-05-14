while True:
    sen = input().split()
    sen = ''.join(sen)
    
    if sen == "#":
        break
    else:
        count = 0
        for i in 'aeiouAEIOU':
            count += sen.count(i)
        print(count)