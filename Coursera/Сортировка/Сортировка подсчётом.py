A = map(int, input().split())
B = [0] * len(A)
min = 0
for num in A:

    if A[num] < min:
        B[num] = A[num]