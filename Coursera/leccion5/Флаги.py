n = int(input())
a = '+___ '
b = '|1 / '
c = r'|__\ '
d = '|    '

print(a * n)
for num in range(1, n + 1):
    print('|{0} / '.format(str(num)), end='')
print('')
print(c * n)
print(d * n)
