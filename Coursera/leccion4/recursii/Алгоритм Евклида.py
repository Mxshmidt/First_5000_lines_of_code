first = int(input())
second = int(input())


def Evklid(a, b):
    if a % b == 0:
        return b
    c = b
    d = a % b
    return Evklid(c, d)


print(Evklid(first, second))
