fh = open('input.txt')
p = {}
for line in fh:
    a = line.split()
    for word in a:
        p[word] = p.get(word, 1) + 1
Gotov = []
for someword in p:
    Gotov.append((p[someword], someword))
#  так оставим прямую сортировку для букв,
#  и обратную для цифр
Gotov.sort(key=lambda x: (-x[0], x[1]))
for item in Gotov:
    print(item[1])
