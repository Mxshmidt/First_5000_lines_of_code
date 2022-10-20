a = int(input())
i = 0
C = [input().split() for now in range(a)]
C.sort(key=lambda x: -int(x[1]))
for i in C:
    print(i[0])
