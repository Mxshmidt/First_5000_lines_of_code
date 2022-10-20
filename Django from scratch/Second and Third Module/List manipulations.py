List1 = []

List2 = [1,'abc',[26, 0.75], (1,2,3),{'apple':50}]
List1.append(List2[1])
List1.append(List2[3])
print(*List1)
