S = input()
k = -2
pos = S.find('f')
if pos != -1:
    k = -1
    if S[pos + 1:].find('f') != -1:
        k = (S[pos + 1:].find('f')) + pos + 1
print(k)
