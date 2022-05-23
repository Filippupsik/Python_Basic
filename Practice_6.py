def int_func(word):
    for el in word:
        els = 0
        if 97 <= ord(el) <= 122:
            els += 1
            if els > word.index(el):
                print(word.title())
        else:
            print("Введите слово на латинице!!!")
        break


int_func(str(input("Введите слово на латинице: ")).lower())
