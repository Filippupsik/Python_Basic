#  Задаём значения для списков с помощью генератора
print([el for el in range(20, 241) if el % 20 == 0 and el for el in range(20, 241) if el % 21 == 0])
