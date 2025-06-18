A, B = input().split()

maxA = A.replace('5','6')
maxB = B.replace('5','6')
maxAB = int(maxA) + int(maxB)

minA = A.replace('6','5')
minB = B.replace('6','5')
minAB = int(minA) + int(minB)

print(minAB, maxAB)