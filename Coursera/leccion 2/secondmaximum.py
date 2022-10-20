a = 0
b = int(input())
c = 0
while b != 0:
    if a <= b:
        c = a
        a = b
    elif c <= b:
        c = b
    b = int(input())
print(c)
