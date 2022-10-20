listy = list(map(int, input().split()))
x = len(listy)
y = 1
for y in listy:
    if listy[y] > listy[y - 1]:
        print(listy[y], end=' ')
