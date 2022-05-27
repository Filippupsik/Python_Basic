# Импортируем функции count и cycle из модуля itertools
from itertools import count
from itertools import cycle

# Цикл для итерации и получения целых чисел от 3 до 10
for el in count(3):
    if el > 10:
        break
    else:
        print(el)

# Цикл для итерации повторения элементов какого-либо списка
c = 0
for el in cycle([1, 2, 3]):
    if c > 10:
        break
    print(el)
    c += 1
