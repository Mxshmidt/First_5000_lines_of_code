List = list(map(int, input().split()))
List2 = List.copy()

Amax = max(List)
List.remove(Amax)
Bmax = max(List)
List.remove(Bmax)
Cmax = max(List)

Amin = min(List2)
List2.remove(Amin)
Bmin = min(List2)
List2.remove(Bmin)
Cmin = min(List2)

if Amin * Bmin * Amax > Amax * Bmax * Cmax:
    print(Amax, Amin, Bmin, end=' ')
else:
    print(Amax, Bmax, Cmax, sep=' ')
