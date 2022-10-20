A = int(input())
B = int(input())
A1 = int(input())
B1 = int(input())

if 0 <= A - A1 <= 1 or 0 <= A1 - A <= 1:
    if 0 <= (B - B1) <= 1 or 0 <= B1 - B <= 1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
