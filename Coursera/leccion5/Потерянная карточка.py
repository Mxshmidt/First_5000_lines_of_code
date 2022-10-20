n = int(input())
suminput = 0
sumtotal = 0

for i in range(n - 1):
    k = int(input())
    suminput += k
for j in range(n + 1):
    sumtotal += j
num = sumtotal - suminput
print(num)
