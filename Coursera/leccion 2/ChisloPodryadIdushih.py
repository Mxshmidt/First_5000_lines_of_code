a = int(input())
proveryalshik = 0
count = 0
countmax = 1

while a != 0:
    if proveryalshik == 0:
        proveryalshik = a
    if proveryalshik == a:
        count += 1
        if countmax <= count:
            countmax = count
    if proveryalshik != a:
        proveryalshik = a
        if countmax <= count:
            countmax = count
        count = 1
    a = int(input())
print(countmax)
