import re
filename = input()
fhand = open(filename)
listofnums = list()
SSS = 0
for line in fhand:
    line.rstrip()
    if re.search('[0-9]+', line):
        listofnums.append(re.findall('[0-9]+', line))
for num in listofnums:
    i = 0
    for a in num:
        i += int(a)
    SSS += i
print(SSS)
