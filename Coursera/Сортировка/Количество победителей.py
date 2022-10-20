fh = open('input.txt', 'r', encoding='utf-8')
List = [0] * 6
# 3, 4, 5 индексы - количество победителей на 9, 10 и 11 класс соответственно
for line in fh:
    c = line.split()
    if c[2] == '9':
        if List[0] == int(c[3]):
            List[3] += 1
        if List[0] < int(c[3]):
            List[0] = int(c[3])
            List[3] = 1
    if c[2] == '10':
        if List[1] == int(c[3]):
            List[4] += 1
        if List[1] < int(c[3]):
            List[1] = int(c[3])
            List[4] = 1
    if c[2] == '11':
        if List[2] == int(c[3]):
            List[5] += 1
        if List[2] < int(c[3]):
            List[2] = int(c[3])
            List[5] = 1
for num in range(3, 6, 1):
    print(List[num], end=" ")
