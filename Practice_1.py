#  Подключаем модуль argv для того, чтобы сделать скрипт с параметрами
from sys import argv
#  Задаём переменные для параметров скрипта
script_name, hours, rate_per_hour, prize = argv

def salary(hours, rate_per_hour, prize):
    '''Функция для расчета з\п'''

    return ((int(hours) * int(rate_per_hour)) + int(prize))


# Присваиваем значение переменной salary
salary = salary(hours, rate_per_hour, prize)
# Через ф-строки выводим расчет зп в консоль
print(f"Ваша зарплата составит: {salary}")
