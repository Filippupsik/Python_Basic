#  Подключаем модуль functools и импортируем функцию reduce
from functools import reduce
# Задаём с помощью генератора список четных значений от 100 до 1000
my_list = [el for el in range(100, 1001) if el % 2 == 0]

def my_func(prev_el, el):
    '''Функция для вычисления произведения всех элементов списка'''

    return prev_el * el


#  Выводим результат работы функции reduce, аргументы - функция произведения и последовательность элементов списка
print(reduce(my_func, my_list))
