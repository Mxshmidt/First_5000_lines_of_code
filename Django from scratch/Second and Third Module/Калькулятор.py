def calc(a, b, type):
    if type == '+':
        return a + b
    if type == '-':
        return a - b
    if type == '*':
        return a * b
    if type == '/':
        try:
            return a / b
        except:
            print('На ноль делить нельзя')
    else:
        print('Введите параметр type')


while True:
    a = int(input())
    b = int(input())
    c = input()
    print(calc(a, b, c))
