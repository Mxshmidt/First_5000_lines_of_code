n = int(input())
L = list(map(int, input().split()))
m = int(input()) + 1
K = list(map(int, input().split()))
Villages = []
Shelters = []
Final = []
#делаем списки с кортежами
for i in range(n):
    Villages.append((L[i], i + 1))
for i in range(m - 1):
    Shelters.append((K[i], i + 1))
#сортируем по возрастанию
Villages.sort()
Shelters.sort()
#Два цикла по городам и вложенный по бомбоубежищам
count = 0
countsh = 0
while count != n:
    while countsh != m - 1:
        if abs(Villages[count][0] - Shelters[countsh][0]) > abs((Villages[count][0]) - Shelters[countsh][0]):
            countsh += 1
        else:
            Final.append((Villages[count][1], Shelters[countsh][1]))
            break
    count += 1
Final.sort()
for num in Final:
    print(num[1], end=' ')
