def addNumber(n):
    sum1 = 0
    for i in range(len(n)):
        sum1 += int(n[i])
    
    return sum1



count1 = (input())
n = [int(i) for i in input().split()]
n.sort()
n = [str(i) for i in n]
n.sort(key=addNumber)

for i in n:
    print(i, end=" ")