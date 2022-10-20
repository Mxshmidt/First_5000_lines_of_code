a = float(input())
n = int(input())


def dasistfastpow(a, n):
    if n % 2 > 0:
        return a * a ** (n - 1)
    return a * dasistfastpow(a, n - 1)


print(dasistfastpow(a, n))
