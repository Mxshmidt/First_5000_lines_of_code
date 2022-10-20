List = list(map(int, input().split()))
last = List.pop()
List.insert(0, last)
print(*List)
