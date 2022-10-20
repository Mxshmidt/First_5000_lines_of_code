def summa():
    n = int(input())
    if n != 0:
        n += summa()
    return n


print(summa())
