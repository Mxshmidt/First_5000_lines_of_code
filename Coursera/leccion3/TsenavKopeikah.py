import math
n = float(input())
k = (n - (math.floor(n))) * 100
print(int(n), end=' ')
print(round(k))
