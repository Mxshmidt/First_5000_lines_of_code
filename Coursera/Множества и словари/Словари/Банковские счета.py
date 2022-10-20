#  BC - Bank Customers
BC = {}
fh = open('input.txt')
for line in fh:
    func = line.strip().split()
    if func[0] == 'DEPOSIT':
        name = func[1]
        summa = int(func[2])
        BC[name] = BC.get(name, 0) + summa
    if func[0] == 'WITHDRAW':
        name = func[1]
        summa = int(func[2])
        BC[name] = BC.get(name, 0) - summa
    if func[0] == 'BALANCE':
        name = func[1]
        if name in BC:
            print(BC[name])
        else:
            print('ERROR')
    if func[0] == 'TRANSFER':
        name1 = func[1]
        name2 = func[2]
        summa = int(func[3])
        BC[name1] = BC.get(name1, 0) - summa
        BC[name2] = BC.get(name2, 0) + summa
    if func[0] == 'INCOME':
        p = int(func[1])
        for cust in BC:
            if BC[cust] > 0:
                BC[cust] += int((BC[cust] / 100) * p)
fh.close()
