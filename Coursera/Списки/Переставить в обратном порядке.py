b = list(map(int, input().split()))
copya = b[:]
n = 0
k = -1
for num in b:
    b[n] = copya[k]
    n += 1
    k -= 1
print(*b)
