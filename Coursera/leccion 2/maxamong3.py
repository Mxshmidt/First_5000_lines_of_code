A = int(input())
B = int(input())
C = int(input())

if A > B:
    if A > C:
        print(A)
    else:
        print(C)
elif B > C:
    print(B)
else:
    print(C)
