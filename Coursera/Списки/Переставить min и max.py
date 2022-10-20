List = list(map(int, input().split()))
Ma = List.index(max(List))
Mi = List.index(min(List))
List[Ma], List[Mi] = List[Mi], List[Ma]
print(*List)
