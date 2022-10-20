from math import sqrt


def MinDivisor(n):
    i = 2
    while n % i != 0:
        if sqrt(n) >= i:
            i += 1
        else:
            return n
    return i


n = int(input())
print(MinDivisor(n))
