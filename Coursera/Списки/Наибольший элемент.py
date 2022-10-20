b = list(map(int, input().split()))
maxi = max(b)
for i in b:
    if b[i] == maxi:
        print(maxi, i, end=' ')
        break
