A = list(map(int, input().split()))
B = [0] * (max(A) + 1)
for i in A:
    B[i] = B[i] + 1
for j in range(max(A) + 1):
    print((str(j) + ' ') * B[j], end='')
