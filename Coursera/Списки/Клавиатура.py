n = int(input())
C = list(map(int, input().split()))
k = int(input())
pj = list(map(int, input().split()))

for i in pj:
    C[i - 1] -= 1
for j in C:
    if j < 0:
        print('YES')
    else:
        print('NO')
