List = list(map(int, input().split()))
count = 1
n = 0
for n in range(0, len(List) - 1):
    if List[n] != List[n + 1]:
        count += 1
    n += 1
print(count)
