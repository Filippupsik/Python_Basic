def division(num_1, num_2):
    '''Функция для вычисления частного'''

    try:
        div = num_1 / num_2
        print(round(div, 2))
    # обработчик ошибки, сделанный через исключение
    except ZeroDivisionError as err:
        print(err)


# получение параметров от пользователя и
division(int(input()), int(input()))

