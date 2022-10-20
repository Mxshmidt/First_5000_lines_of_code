def Neighbors(A):
    i = 1
    while i != len(A):
        if A[i] > 0 and A[i - 1] > 0:
            return A[i - 1], A[i]
        elif A[i] < 0 and A[i - 1] < 0:
            return A[i - 1], A[i]
        i += 1
    return ' '


B = list(map(int, input().split()))
print(' '.join(map(str, Neighbors(B))))
