L = list(map(int, input().split()))
T = list(map(int, input().split()))
Sum = 0
L.sort()
T.sort(reverse=True)
for n in range(len(L)):
    Sum += L[n] * T[n]
print(Sum)
