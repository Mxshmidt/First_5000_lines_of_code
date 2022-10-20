def reversiv():
    n = int(input())
    if n != 0:
        reversiv()
        print(n)
    else:
        print(n)


reversiv()
