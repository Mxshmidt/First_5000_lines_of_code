def interSection(A, B):
    r = []
    ai = 0
    bi = 0
    while ai < len(A) and bi < len(B):
        if A[ai] == B[bi]:
            r.append(A[ai])
            ai += 1
            bi += 1
        elif A[ai] > B[bi]:
            bi += 1
        elif A[ai] < B[bi]:
            ai += 1
    return r


List = list(map(int, input().split()))
List2 = list(map(int, input().split()))
print(*interSection(List, List2))
