N = int(input())

def num(n):
    s = str(n)
    for c in s:
        if c != '4' and c != '7':
            return False
    return True

while True:
    if num(N):
        print(N)
        break
    else :
        N -= 1