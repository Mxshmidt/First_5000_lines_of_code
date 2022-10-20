inFile = open('input.txt', 'r', encoding='utf-8')
Lines = set(inFile.read().split())
print(len(Lines))
