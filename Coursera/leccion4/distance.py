def distancia(a, b, c, d):
    di = ((c - a) ** 2 + (d - b) ** 2) ** 0.5
    return di


a = float(input())
b = float(input())
c = float(input())
d = float(input())
print('{0:.5f}'.format(distancia(a, b, c, d)))
