def distancia(a, b, c, d):
    di = ((c - a) ** 2 + (d - b) ** 2) ** 0.5
    return di


a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
P = (distancia(a, b, c, d)) + distancia(c, d, e, f) + distancia(e, f, a, b)

print(P)
