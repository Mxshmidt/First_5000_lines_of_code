fh = open('input.txt')
cust = {}
for line in fh:
    a = line.rstrip().split()
    customer = a[0]
    product = a[1]
    count = int(a[2])
    if customer in cust:
        cust[customer][product] = cust[customer].get(product, 0) + count
    else:
        cust[customer] = {}
        cust[customer][product] = count
for pokupschik in sorted(cust):
    print(pokupschik, ':', sep='')
    for tovar in sorted(cust[pokupschik]):
        print(tovar, cust[pokupschik][tovar])
