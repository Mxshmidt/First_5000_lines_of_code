List = list(map(int, input().split()))
k = len(List) // 2
i = 0
while k != i // 2:
    List[i], List[i + 1] = List[i + 1], List[i]
    i += 2
print(*List)
