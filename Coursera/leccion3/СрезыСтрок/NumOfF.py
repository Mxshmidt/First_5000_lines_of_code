s = input()
pos = s.find('f')
if pos != -1:
    pos1 = s.find('f')
    pos2 = s[::-1].find('f')
    if pos1 + pos2 + 1 == len(s):
        print(pos1)
    else:
        print(pos1, len(s) - pos2 - 1)
