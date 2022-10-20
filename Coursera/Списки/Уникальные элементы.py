List = list(map(int, input().split()))
List2 = []
for num in List:
    a = List.count(num)
    if a == 1:
        List2.append(num)
print(*List2)

