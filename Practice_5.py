def my_sum():
    '''Функция перебора введенных значений на ошибки'''

    el_sum = 0
    # Цикл дя обработки данных, работающий по переменной-флагу
    while True:
        err = False  # Переменная-флаг для выполнения цикла
        my_list = input("Введите несколько чисел, нажмите 'q', что бы выйти: ").split()  # Запрашиваем данные
        # Цикл для перебора введенных данных, проверка на ошибки и на спец. символ
        for el in my_list:
            # Проверка на спец. символ
            if el.lower() == 'q':
                return el_sum
            # Проверка на ошибки через исключение, смена значения переменной-флага
            else:
                try:
                    el_sum += int(el)
                except ValueError:
                    err = True
        # Ветвление для вывода значений (текста ошибки в случае ошибки, суммы элементов если без ошибки)
        if err:
                print(f"{ValueError}")
        else:
            print(f'{el_sum}')


# Вызов функции
print(my_sum())
