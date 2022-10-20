n = int(input())
a = list(map(int, input().split()))
a.sort()
s = 0
for i in a:
    if i >= n:
        s += 1
        n = i + 3
print(s)
