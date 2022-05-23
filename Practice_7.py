def int_func(my_list):
    for el in my_list:
        els = 0
        if 97 <= ord(el) <= 122:
            els += 1
            if els > my_list.index(el):
                print(my_list.title())
        else:
            print("Введите слова на латинице!!!")
        break


int_func(str(input("Введите несколько слов на латинице через пробел: ")).lower())
