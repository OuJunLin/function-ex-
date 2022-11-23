def fun1(n):
    if n//10 == 0:
        return 1
    else:
        return 1 + fun1(n//10)

n = int(input())
print(fun1(n))