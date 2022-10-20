with open('input.txt', 'r', encoding='utf8') as inFile:
    list_Dep, dict_Dep = list(), dict()
    for devide in inFile:
        dict_Dep[' '.join(devide.split()[:-1])] = int(devide.split()[-1])
        #  чтобы просуммировать, лямбда функция поменяет
        #  местами со значением и сумма идет как бы на ключ
    all_people = sum(map(lambda x: dict_Dep[x], dict_Dep))
    list_Dep = list(map(lambda x: [x, int(450 * dict_Dep[x] / all_people),
                                   450 * dict_Dep[x] / all_people -
                                   int(450 * dict_Dep[x] / all_people)],
                        dict_Dep))
    sum_party = sum(map(lambda x: x[1], list_Dep))
    for ordnung in sorted(list_Dep, key=lambda x: (x[2], x[1]), reverse=True):
        if sum_party == 450:
            break
        ordnung[1], sum_party = ordnung[1] + 1, sum_party + 1
    print(*map(lambda x: f'{x[0]} {x[1]}', list_Dep), sep='\n')
