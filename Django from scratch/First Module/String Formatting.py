name = 'Максим'
surname = 'Шмидт'
age = '23'
word = 'лет'

if 0 < int(age) % 10 < 5:
    if int(age) % 10 != 1:
        word = 'года'
    else:
        word = 'год'

print(f'Привет, меня зовут {name} {surname} и мне {age} {word}.')
