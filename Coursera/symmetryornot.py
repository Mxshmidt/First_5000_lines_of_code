num = int(input())
A = num // 1000
B = (num // 100) % 10
C = (num // 10) % 10
D = num % 10
print((num // 100) - ((num % 10 * 10) + (num % 100 // 10)) + 1)
