x = int(input())
y = int(input())
print('YES'if y % (y + 1 - x) == 0 else 'NO')
