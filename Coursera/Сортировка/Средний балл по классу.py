fhand = open('input.txt', 'r', encoding='utf-8')
List9 = []
List10 = []
List11 = []
for line in fhand:
    a = line.split()
    if a[2] == '9':
        List9.append(int(a[3]))
    elif a[2] == '10':
        List10.append(int(a[3]))
    elif a[2] == '11':
        List11.append(int(a[3]))

fhand.close()

print(sum(List9) / len(List9), end=' ')
print(sum(List10) / len(List10), end=' ')
print(sum(List11) / len(List11), end=' ')
