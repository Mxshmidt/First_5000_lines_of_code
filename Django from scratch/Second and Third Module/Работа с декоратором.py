import datetime

def recTime(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        func(*args, **kwargs)
        done = datetime.datetime.now() - start
        print(f'Функция завершилась за {done} сек')
    return wrapper


@recTime
def spisok(n, type=None):
    a = list(range(0, n + 1))
    if type == 't':
        b = tuple(a)
        for num in b:
            print(num)
    else:
        for num in a:
            print(num)


spisok(6)
spisok(6, type='t')
