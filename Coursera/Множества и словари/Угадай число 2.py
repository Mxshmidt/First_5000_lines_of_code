maxNum = int(input())
Nums = set(range(1, maxNum + 1))
Possiblenums = Nums
while True:
    listNum = input()
    if listNum == 'HELP':
        break
    else:
        listNum = set(map(int, listNum.split()))
        # может называть числа, которые раньше уже называла
        # и получала NO, видимо забывая их вычёркивать из числа
        # возможных. Сравниваем пересечения
        if 2 * len(listNum & Possiblenums) <= len(Possiblenums):
            print('NO')
            Possiblenums -= listNum
        else:
            print('YES')
            Possiblenums = listNum & Possiblenums
print(*sorted(Possiblenums))
