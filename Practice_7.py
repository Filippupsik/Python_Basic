# Задание 7
a = int(input("сколько километров пробежал спортсмен в первый день: "))  # Переменная км в 1-й день
b = int(input("Сколько километров спортсмен должен пробежать за день: "))  # Переменная конечного результата
result = a  # Переменная для наращивания 10% в день
counter = 1  # Переменная-счётчик дней
# Цикл для определения нужного дня
while result < b:
    result *= 1.1  # Увеличение результата на 10% при след. итерации
    counter += 1  # Увеличение кол-ва дней на след. итерации
print(f"на {counter} день спортсмен достиг результата — не менее {b} км")  # Вывод полученного результата
