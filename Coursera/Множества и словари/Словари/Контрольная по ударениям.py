Maindict = set()
fh = open('input.txt')
N = int(fh.readline().strip())
for i in range(N):
    Maindict.add(fh.readline().strip())
SecondDict = set()
for slovo in Maindict:
    SecondDict.add(slovo.lower())
mistakes = 0
hw = fh.readline().strip().split()
for word in hw:
    if word in Maindict:
        continue
    if word.islower() or sum(i.isupper() for i in word) > 1:
        mistakes += 1
    elif word.lower() in SecondDict:
        mistakes += 1

fh.close()
print(mistakes)
