# Задание 3

# Вариант 1
a = int(input('Введите число: '))  # переменная принимающая значения числа
c = int(f"{a}{a}")
d = int(f"{a}{a}{a}")
print(a + c + d)
# Можно в одну строку
print(a + int(f"{a}{a}") + int(f"{a}{a}{a}"))

# Вариант 2
a = input('Введите число: ')
b = int(a)
c = int(a + a)
d = int(a + a + a)
print(b + c + d)
# Можно в одну строку
print(int(a) + int(a + a) + int(a + a + a))
