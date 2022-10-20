a = int(input())
b = 0
c = 0
while a != 0:
    if c < a:
        b += 1
    c = a
    a = int(input())
if b > 0:
    print(b - 1)
else:
    print(0)
