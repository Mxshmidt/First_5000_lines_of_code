import math
n = int(input())
summa = 0

for num in range(1, n + 1):
    summa += math.factorial(num)
print(summa)
