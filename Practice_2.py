# Задание 2
a = int(input("Введите общее время в секундах: "))
hour = a // 3600
minute = (a % 3600) // 60
second = a % 60
print(f"{hour:02}:{minute:02}:{second:02}")