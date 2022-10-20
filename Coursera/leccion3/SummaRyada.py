n = int(input())
z = 1
S = 0

while z <= n:
    S += (1 / z ** 2)
    z += 1
if S % 2 == 0:
    print(int(S))
else:
    print('{0:.6f}'.format(S))
