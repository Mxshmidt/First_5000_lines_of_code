def rightnum(num):
    temp = [int(i) for i in num if i.isdigit()]
    temp = temp[1:] if len(temp) == 11 else [495] + temp
    return ''.join(map(str, temp))


inputed = [input() for _ in range(4)]
stroka = inputed[0]
for line in range(1, len(inputed)):
    print('YES' if rightnum(inputed[line]) == rightnum(stroka) else 'NO')
