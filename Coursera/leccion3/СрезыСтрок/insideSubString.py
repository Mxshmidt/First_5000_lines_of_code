words = input()
pos = words.find('h') + 1
pos2 = len(words) - words[::-1].find('h') - 1
rpp = (words[pos:pos2]).replace('h', 'H')
print(words[:pos], rpp, words[pos2:], sep='')
