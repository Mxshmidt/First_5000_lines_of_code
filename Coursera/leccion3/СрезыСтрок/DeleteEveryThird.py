s = str(input())
n = 1
while n != len(s):
    if n % 3 != 0:
        print(s[n], end='')
    n += 1

