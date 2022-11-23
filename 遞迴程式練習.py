def refun(n):
    if n == 1:
        return n+1
    else:
        return refun(n-1)+refun(n//2)
    


n = int(input())
print(refun(n))