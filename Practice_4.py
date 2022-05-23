def my_func(x: float, y: int):
    '''Функция возведения x^y'''

    return x**y


print(my_func(3, -7))


def my_func2(x: float, y: int):
    '''Функция возведения x^y, вариант через цикл'''

    a = 1
    for i in range(0, y, -1):
        a = a / x
    return a


print(my_func(3, -5))
