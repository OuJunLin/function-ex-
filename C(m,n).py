def factorial(n):
    result1 = 1
    for i in range(1, n+1):
        result1 *= i
    
    return result1




def C(m, n):
    return factorial(m)/(factorial(n)*factorial(m-n))



m, n = map(int, input().split())
print("{:.0f}" .format(C(m, n)))