def height(name, d):
    return 0 if name not in d else height(d[name], d) + 1


a = {}
for i in range(1, int(input())):
    nCh, nPr = input().split()
    a[nCh] = nPr
for i in sorted(set(a.keys()) | set(a.values())):
    print(i, height(i, a))
