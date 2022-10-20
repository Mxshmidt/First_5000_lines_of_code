P = int(input())
X = int(input())
Y = int(input())
k = (X * 100) + Y
S = (k + k * P / 100)
print(int(S // 100), int(S % 100))
