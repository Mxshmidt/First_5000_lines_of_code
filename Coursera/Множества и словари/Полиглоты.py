#  код не прошел, смотри тот, что в 9 строк
amount = int(input())
AllLanguages = set()
Studentspack = []
Widespread = []  # говорят все
for i in range(amount):
    count = int(input())
    StudentLanguages = set()
    for j in range(count):
        language = input()
        StudentLanguages.add(language)
        AllLanguages.add(language)
    Studentspack.append(StudentLanguages)
# проверяем каждый язык на присутствие в каждом множестве
for idioma in AllLanguages:
    coount = 0  # считаем для проверки
    for student in Studentspack:
        if idioma in student:
            coount += 1
    if coount == amount:
        Widespread.append(idioma)
print(len(Widespread))
print(*Widespread)
print(len(AllLanguages))
print(*AllLanguages, sep="\n")
