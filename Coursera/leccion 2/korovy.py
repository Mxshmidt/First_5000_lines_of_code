n = int(input())
if n == 1 or (n % 10) == 1 and 11 != n:
    print(n, 'korova')
elif 2 <= n <= 4 or n > 20 and 2 <= (n % 10) <= 4:
    print(n, 'korovy')
else:
    print(n, 'korov')
