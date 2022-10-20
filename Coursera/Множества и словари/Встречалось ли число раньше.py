a = list(map(int, input().split()))
b = set()
for i in a:
    if i not in b:
        print('NO')
    else:
        print('YES')
    b.add(i)
