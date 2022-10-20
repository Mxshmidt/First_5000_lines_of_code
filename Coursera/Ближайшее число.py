count = int(input())
a = list(map(int, input().split()))
b = int(input())
c = 0

for num in a:
    if abs(b) + abs(num) > c:
        c = num
print(c)
