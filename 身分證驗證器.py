def englishToNumber(char):
    english = {"A":10, "B:":11, "C":12, "D":13, "E":14, "F":15, "G":16,\
        "H":17, "J":18, "K":19, "L":20, "M":21, "N":22, "P":23, "Q":24,\
        "R":25, "S":26, "T":27, "U":28, "V":29, "X":30, "Y":31, "W":32,\
        "Z":33, "I":34, "O":35}
    return english[char]//10, english[char]%10



def checkIdentity(n_list):
    x1, x2 = englishToNumber(n_list[0])
    p = x1 + (9*x2) + (8*n_list[1]) + (7*n_list[2]) + (6*n_list[3]) + (5*n_list[4]) + (4*n_list[5]) + (3*n_list[6]) + (2*n_list[7]) + n_list[8] + n_list[9]
    if p%10 == 0:
        return True
    else:
        return False



n = list(input())
for i in range(len(n)):
    if i != 0:
        n[i] = int(n[i])

if checkIdentity(n):
    print("CORRECT!!!")
else:
    print("WRONG!!!")