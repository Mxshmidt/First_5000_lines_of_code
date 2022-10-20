a = int(input())
b = int(input())

if a < b:
    for num in range(a, b + 1):
        print(num, end=' ')
else:
    for num in range(a, b - 1, -1):
        print(num, end=' ')
def rangereverse(n):
    for num in range(10, 1)