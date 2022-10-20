fh = open('input.txt')
Maindict = {}
for line in fh:
    for word in line.split():
        if word not in Maindict:
            Maindict[word] = 0
        else:
            Maindict[word] += 1
        print(Maindict[word], end=' ')
