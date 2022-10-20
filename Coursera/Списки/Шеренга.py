sheet = list(map(int, input().split()))
petya = int(input())
i = 0
while i <= len(sheet) - 1 and petya <= sheet[i]:
    i += 1
print(i+1)
