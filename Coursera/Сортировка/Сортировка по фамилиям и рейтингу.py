fh = open('input.txt', 'r', encoding='utf8')
NuevaList = []
for line in fh:
    a = line.split()
    NuevaList.append((a[0], a[1], a[3]))
fh.close()

NuevaList.sort(key=lambda x: x[0])

outFile = open('output.txt', 'w', encoding='utf-8')
for line in NuevaList:
    line = [line[0], line[1], line[-1]]
    print(' '.join(map(str, line)), end='\n', file=outFile)
outFile.close()
