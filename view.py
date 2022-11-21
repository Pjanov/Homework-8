def request_data() -> tuple:
    '''
    Запросить данные пользователя
    :return: кортеж из строк
    '''
    surname = input('Введите Фамилию: ')
    name = input('Введите Имя: ')
    group = input('Введите Класс: ')
    return surname, name, group


def num_id() -> int:
    '''
    Запросить номер ID
    '''
    number_id = int(input('Введите номер ID: '))
    return number_id


def menu() -> None:
    '''
    Вывод меню приложения
    '''
    print('МЕНЮ ПРИЛОЖЕНИЯ: ')
    print('1 => Вывести БД в консоль')
    print('2 => Добавить запись в БД')
    print('3 => Извлечь запись по ID')
    print('4 => Импорт данных в БД с ID')
    print('5 => Импорт данных без ID')
    print('6 => Экспорт данных из БД')
    print('7 => Обновить запись по ID')
    print('8 => Удалить запись по ID')
    print()


def get_menu_number() -> int:
    '''
    Запрос у пользователя номера меню
    '''
    num = int(input('ВЫБЕРЕТЕ ПУНКТ ИЗ МЕНЮ: '))
    print()
    return num


def error_message():
    '''
    Сообщение о ошибке
    '''
    print('Такого пункта нет')


if __name__ == '__main__':
    # print(request_data())
    # num_id()
    # menu()
    # print(get_menu_number())
    pass
