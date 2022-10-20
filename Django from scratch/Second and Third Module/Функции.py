def s(a, b):
    ploschad = a * b
    print(ploschad)


s(5, 5)


def calc(a, b, type=None):
    ploschad = a * b
    p = (a + b) ** 2
    if type == 's':
        print(f'Площадь прямоугольника равна {ploschad}')
    elif type == 'p':
        print(f'Периметр прямоугольника равен {p}')
    else:
        print(f'Площадь прямоугольника равна {ploschad}, периметр равен {p}')


def maxinlist(list):
    print(f'Максимальное число в списке{list.sort()[-1]}')


new_list = [9, 1, 7, 3, 5, 6, 4]
maxinlist(new_list)

n_list = [2, 7, 1]


def listsum(list):
    summa = 0
    for i in range(list):
        summa += list[i]
    print(
        summa
    )

listsum(n_list)