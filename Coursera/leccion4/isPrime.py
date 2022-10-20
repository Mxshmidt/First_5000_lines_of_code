import math

a = int(input())
d = 2


def IsPrime(n):
    global d
    if d > math.sqrt(n):
        return True
    else:
        while d <= math.sqrt(n):
            if n % d == 0:
                return False
            elif math.ceil(math.sqrt(n)) == d:
                return True
            else:
                d += 1
        return True


if IsPrime(a):
    print('YES')
else:
    print('NO')
