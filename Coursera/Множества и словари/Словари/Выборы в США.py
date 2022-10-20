Politics = {}
text = open('input.txt')
for line in text:
    a = line.split(' ')
    Politics[a[0]] = Politics.get(a[0], 0) + int(a[1])
for x, y in sorted(Politics.items()):
    print(x, y)
