text = open('input.txt').read().split()
p = {}
for word in text:
    p[word] = p.get(word, 0) + 1
Listy = list()
for word in p:
    if len(Listy) == 0:
        Listy.append([word, p[word]])
    elif p[word] == Listy[0][1]:
        Listy.append([word, p[word]])
    elif int(p[word]) > int(Listy[0][1]):
        Listy.clear()
        Listy.append([word, p[word]])
Listy.sort()
print(Listy[0][0])
