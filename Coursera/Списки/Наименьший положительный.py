b = list(map(int, input().split()))
mini = max(b)
for i in b:
    if mini >= i > 0:
        mini = i
print(mini)
