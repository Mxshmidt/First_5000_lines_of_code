def count(string):
    # The function code should be here
    word = string.strip()
    countDic = {}
    for letter in word:
        countDic[letter] = countDic.get(letter, 0) + 1
    return countDic
print(count('aba'))