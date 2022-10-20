List = list(map(int, input().split()))
List[List.index(max(List))], List[List.index(min(List))] = List[List.index(min(List))], List[List.index(max(List))]
print(*List)

