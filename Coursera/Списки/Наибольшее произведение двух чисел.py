List = list(map(int, input().split()))
List2 = List.copy()
# ищем максимум суммы положительных
FMax = max(List)
List.remove(FMax)
SMax = max(List)
PMax = FMax + SMax
# максимум суммы отрицательных, если они есть. Если их нет, то сумма все равно будет мала.
FNMax = min(List2)
List2.remove(FNMax)
SNMax = min(List2)
NMax = abs(FNMax) + abs(SNMax)

if PMax > NMax:
    print(SMax, FMax, end=' ')
else:
    print(FNMax, SNMax, end=' ')
