a = int(input())
b = 0
c = 0
d = 0
while a != 0:
    if b < a:
        b = a
        c = b
        d = 0
    if a == b:
        d += 1
    a = int(input())
print(d)
