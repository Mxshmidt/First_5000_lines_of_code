n = int(input())
C = list(map(int, input().split()))
k = int(input())
pj = list(map(int, input().split()))

for i in pj:
    C[i - 1]  -=  1

for i in C:
    if i < 0:
        print('YES')
    else:
        print('NO')