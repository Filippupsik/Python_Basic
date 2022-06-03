# Задаём некий список
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

def generator():
    '''Функция для определения оригинальных элементов'''

    for i in range(1, len(my_list)):
        if my_list[i] > my_list[i-1]:
            yield my_list[i]


#  Записываем значения в новый список c помощью генератора и выводим их
new_list = [el for el in generator()]
print(new_list)
