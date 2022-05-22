# Задаём начальный список и запрашиваем элемент у пользователя
my_list = [8, 6, 4, 4, 3, 1]
reit = int(input("Введите число: "))

# Цикл для обработки нового значения
for el in my_list:
    # Ветвление для случая когда в списке есть эелементы идентичные указанному
    if el == reit:
        a = my_list.index(el)
        b = my_list.count(el)
        c = a+b
        my_list.insert(c, reit)
        break
    # Ветвление для случая когда указанный элемент больше всех элементов списка
    elif reit > el:
        a = my_list.index(el)
        my_list.insert(a, reit)
        break
    # Ветвление для случая когда указанный элемент меньше всех (работает только с невозврастающем списком)
    elif reit < my_list[-1]:
        my_list.append(reit)
        break
print(my_list)
