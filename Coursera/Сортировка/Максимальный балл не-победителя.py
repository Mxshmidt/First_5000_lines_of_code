from heapq import nlargest
fh = open('input.txt', 'r', encoding='utf-8')
Rates9 = []  # создаем общий список с баллами 9, 10, 11 класс
Rates10 = []
Rates11 = []
for line in fh:
    r = line.split(" ")
    if int(r[2]) == 9:
        if int(r[3]) not in Rates9:
            Rates9.append(int(r[3]))
    elif int(r[2]) == 10:
        if int(r[3]) not in Rates10:
            Rates10.append(int(r[3]))
    else:
        if int(r[3]) not in Rates11:
            Rates11.append(int(r[3]))
print(nlargest(2, Rates9)[1], end=" ")
print(nlargest(2, Rates10)[1], nlargest(2, Rates11)[1], sep=" ")
