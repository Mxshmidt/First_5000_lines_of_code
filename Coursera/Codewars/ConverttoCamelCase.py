def to_camel_case(text):
    newword = ''
    if '-' in text:
        i = text.index('-')
        newword += text[:i]
        newword += text[i+1:]
        to_camel_case(newword)
    if '_' in text:
        i = text.index('_')
        newword.join(text[:i])
        newword.join(text[i:])
        to_camel_case(newword)
    return newword
    return text


print(to_camel_case(input()))
