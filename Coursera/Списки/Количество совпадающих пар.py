List = list(map(int, input().split()))
count = 0
i = 0
n = 0
while i != len(List):
    n = List[i]
    for num in range(i + 1, len(List)):
        if List[num] == n:
            count += 1
    i += 1
print(count)
