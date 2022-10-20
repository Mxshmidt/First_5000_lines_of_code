a = float(input())
n = int(input())
c = 0


def stepen(a, n):
    c = a
    if n > 0:
        while n != 1:
            n -= 1
            c *= a
        if n == 1:
            return c
    if n < 0:
        while n != -1:
            n += 1
            c *= a
        if n == -1:
            return 1 / c
    if n == 0:
        return 1


print(stepen(a, n))
