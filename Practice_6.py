# Задание 6
revenue = int(input("Укажите выручку компании: "))  # Переменная выручки компании
cost = int(input("Укажите издержки компании: "))  # Переменная издержек компании
profit = revenue - cost
if profit > 0:
    # Расчет рентабельности фирмы:
    print(f"Фирма отработала с прибылью, рентабельность фирмы состовляет {profit / revenue:.2f}")
    people = int(input("Введите количество сотрудников: "))  # Переменная кол-ва сотрудников
    # Расчет прибыли фирмы на одного сотрудника:
    print(f"Прибыль фирмы на одного сотрудника составляет {profit / people:.2f}")
else:
    print("Фирма отработала без прибыли")  # Случай, если отработали без прибыли
