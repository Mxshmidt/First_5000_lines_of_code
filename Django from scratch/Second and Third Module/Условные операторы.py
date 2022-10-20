num = int(input())

print('Четное число' if num % 2 == 0 else 'Нечетное число')
print(f'Это число {num}' if 0 < num < 7 else 'Введите корректное число от 1 до 6')

List = []
for _ in range(1, 19):
    List.append(_)
    print(List[_ - 1])
