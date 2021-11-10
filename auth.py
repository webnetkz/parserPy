# Словарь пользователей
dictionary = {
    'id1': {
        'login': 'admin',
        'pass': '123'
    },
    'id2': {
        'login': 'dbqqbq',
        'pass': '123'
    },
    'id3': {
        'login': 'mylogin',
        'pass': '123'
    }
}

# Функция принимает один аргумент в ввиде словаря
def authorization(dictionary):
    # Запрашиваем ввести логин
    answ = input('Enter login: ')
    # Переменная для записи произошедших ошибок
    errs = ''
    # Если пользователь ввел верные данные
    succ = ''

    # Перебераем циклом словарь
    for id in dictionary:
        # Рассматриваем ошибочное поведение пользователя
        if answ == '':
            errs = 'You have not enter login!'
        elif answ != dictionary[id]['login']:
            errs = 'Invalid login!'
        # Если логин пользователя существует в словаре
        if answ == dictionary[id]['login']:
            # Запрашиваем ввести пароль
            answ_2 = input('Enter password: ')
            # Проверяем пароль на соответствие логину
            if answ_2 == '':
                errs = 'You have not enter password!'
            elif answ_2 != dictionary[id]['pass']:
                errs = 'Invalid password!'
            else:
                succ = 'Success!!!'
    # Проверка на вывод сообщения            
    if succ != '':
        print(succ)
    else:
        print(errs)
    

# А это собственно запуск функции
authorization(dictionary)