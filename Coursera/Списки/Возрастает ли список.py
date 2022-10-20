def IsAscending(A):
    i = 1
    while i != len(A) and A[i] > A[i - 1]:
        i += 1
    return i == len(A)


mylist = list(map(int, input().split()))

print('YES' * IsAscending(mylist), 'NO' * (not(IsAscending(mylist))))
