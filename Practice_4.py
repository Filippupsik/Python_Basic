#  Задаём список
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

def generator():
    '''Функция для определения оригинальных элементов'''

    for i in range(0, len(my_list)):
        if my_list.count(my_list[i]) == 1:
            yield my_list[i]


#  Записываем в переменную новый лист и выводим её
new_list = [el for el in generator()]
print(new_list)
