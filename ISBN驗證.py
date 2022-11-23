n = input().split()
for i in range(len(n)):
    if n[i] == "X":
        n[i] = 10
    else:
        n[i] = int(n[i])



def addNumber(n_list):
    n_out = []
    for i in range(len(n_list)):
        sum1 = 0
        for j in range(i+1):
            sum1 += n_list[j]
        n_out.append(sum1)
        
    return n_out



def checkISBN(n_list):
    n_list = addNumber(n_list)
    n_list = addNumber(n_list)
    if n_list[9]%11 == 0:
        return True
    else:
        return False

if checkISBN(n):
    print("YES")
else:
    print("NO")