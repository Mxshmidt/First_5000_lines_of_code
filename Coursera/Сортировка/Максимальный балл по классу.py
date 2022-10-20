fh = open('input.txt', 'r', encoding='utf-8')
List = [0] * 3
for line in fh:
    c = line.split()
    if c[2] == '9':
        if List[0] < int(c[3]):
            List[0] = int(c[3])
    if c[2] == '10':
        if List[1] < int(c[3]):
            List[1] = int(c[3])
    if c[2] == '11':
        if List[2] < int(c[3]):
            List[2] = int(c[3])
print(*List)
