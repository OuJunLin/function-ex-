def power1(a, n):
    if n == 1:
        return a
    else:
        return a*power1(a, n-1)

def power2(a, n):
    if n == 1:
        return a
    elif n%2 == 0:
        return power2(a, n/2)*power2(a, n/2)
    else:
        return a*power2(a, n-1)

a, n = map(int, input().split())
print(power1(a, n))
print(power2(a, n))