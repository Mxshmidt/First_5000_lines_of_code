n = int(input())
print(*tuple(range(10**n-1, 10**(n-1)-1, -2)))
