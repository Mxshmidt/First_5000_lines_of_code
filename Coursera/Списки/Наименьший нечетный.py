b = list(map(int, input().split()))
mini = max(b)
for i in b:
    if i <= mini and i % 2 > 0:
        mini = i
print(mini)
