count = int(input("Введите количество элементов списка: "))  # Запрос у пользователя количества элементов списка
my_list = []
counter = 0

#  Цикл добавления элементов в список
while counter != count:
    el = input("Введите элемент списка: ")
    my_list.append(el)
    counter += 1

#  Ветвление для сохранения посленего элемента на своём месте, в случае, если их количество не четное
if count % 2 == 1:
    count = count - 1

#  Цикл для обмена значений по индексам, и вывод значений
i = 0
while i != count:
    a = my_list[i]
    b = my_list[i + 1]
    my_list[i] = b
    my_list[i + 1] = a
    i += 2
print(my_list)
