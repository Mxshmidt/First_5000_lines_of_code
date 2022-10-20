a = int(input())
b = int(input())


def summy(first, second):
    if second == 0:
        return first
    else:
        second -= 1
        first += 1
    return summy(first, second)


print(summy(a, b))
