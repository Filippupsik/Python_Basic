def my_func(a, b, c):
    '''Функция определяющая два наибольших числа и их сумму'''

    if a > c and b > c:
        print(a + b)
    elif a > b and c > b:
        print(a + c)
    elif b > a and c > a:
        print(b + c)
    else:
        print("Введите три разных числа")


my_func(int(input("Введите 1 число: ")),
        int(input("Введите 2 число: ")),
        int(input("Введите 3 число: ")))
