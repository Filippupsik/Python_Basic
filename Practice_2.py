def user_data(user_name, user_birthday, user_city, user_email):
    '''Функция выводит данные о пользователе в одну строку'''

    print(f'Имя: {user_name}, Город проживания: {user_city}, Email: {user_email}, Год рождения: {user_birthday}')


# Задаём четко присвоенные аргументы
user_data(user_name=str(input()),
          user_birthday=int(input()),
          user_email=str(input()), 
          user_city=str(input()))
