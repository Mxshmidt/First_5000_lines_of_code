haha = input()
pos = haha.find('h')
if pos != -1:
    pos1 = haha.find('h')
    pos2 = len(haha) - haha[::-1].find('h')
    print(haha[:pos1], end='')
    print(haha[pos1:pos2 - 1], end='')
    print(haha[pos1 + 1:pos2], end='')
    print(haha[pos2:])
