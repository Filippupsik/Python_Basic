def factorial(n):
    '''Функция для вычесления факториала'''

    digit = 1
    for i in range(1, n + 1):
        digit *= i
        yield digit


# Вызываем функцию-генератор для вычисления факториала и выводим результат
for el in factorial(10):
    print(el)
