inFile = open('input.txt', 'r', encoding='utf8')
n = int(inFile.readline())
mans = (inFile.readlines())
minPP = 40
passMans = []

# перевод баллов в целые числа
for i in range(len(mans)):
    mans[i] = mans[i].split()   # разбиваем строку на "слова"
    mans[i][-1] = int(mans[i][-1])
    mans[i][-2] = int(mans[i][-2])
    mans[i][-3] = int(mans[i][-3])

# формирование списка студентов набравших достаточно баллов
for man in mans:
    if man[-1] >= minPP and man[-2] >= minPP and man[-3] >= minPP:
        passMans.append(man[-3] + man[-2] + man[-1])
passMans.sort(reverse=1)


# выполнение условий задания
# проверяем, сколько сдтудентов набрали минимальный балл
if passMans and len(passMans) > n:
    # до тех пор пока прошедших больше чем мест и у них разные баллы
    # отсеиваем студентов с наименьшими баллами
    while len(passMans) > n and passMans[0] != passMans[-1]:
        passMans = passMans[:passMans.index(min(passMans))]
    # если баллы равны но людей больше мест
    # пишем единицу
    if len(passMans) > n and passMans[0] == passMans[-1]:
        print(1)
    else:
        print(min(passMans))    # проходной балл
# в случае если набравших минимальный балл меньше, чем мест
# пишем нолик
else:
    print(0)

inFile.close()