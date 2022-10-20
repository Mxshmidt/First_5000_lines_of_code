def Evklid(a, b):
    if a % b == 0:
        return b
    c = b
    d = a % b
    return Evklid(c, d)


def ReduceFraction(n, m):
    return n // Evklid(n, m), m // Evklid(n, m)


first = int(input())
second = int(input())

print(*ReduceFraction(first, second))
