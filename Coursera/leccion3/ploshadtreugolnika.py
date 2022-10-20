a = float(input())
b = float(input())
c = float(input())
d = 0.5
p = d * (a + b + c)
S = (p * (p - a) * (p - b) * (p - c)) ** d

if S % 2 == 0:
    print(int(S))
else:
    print('{0:.6f}'.format(S))
