import view
import model as mod
from colorama import init
from colorama import Fore


init()
print(Fore.GREEN)


def create_record():
    '''
    Добавляет новую запись в БД
    '''
    list_dict = []
    rec_id = mod.get_id().split()
    data = mod.convert_to_list(view.request_data())
    lst = rec_id + data
    res = dict(el for el in zip(mod.global_mapping().keys(), lst))
    list_dict.append(res)
    mod.write_data(mod.db, list_dict)


def extracting_record_id():
    '''
    Функция запрашивает ID и выводит запись в консоль
    '''
    number_id = view.num_id()
    mod.extracting_record(number_id)


def import_db():
    '''
    Считывает данные из файла и дозаписывает в БД
    '''
    list_dict = mod.read_data(mod.file_import)
    mod.write_data(mod.db, list_dict)


def export_db():
    '''
    Считывает данные из файла БД записывает в csv файл
    '''
    list_dict = mod.read_data(mod.db)
    mod.write_data(mod.file_export, list_dict, 'w')


def update_record_db():
    '''
    Функция обновляет запись по ID в БД
    '''
    number_id = view.num_id()
    data = mod.delete_record(number_id)
    new_dict = mod.update_record(number_id)
    mod.write_data(mod.db, data, 'w')
    mod.write_data(mod.db, new_dict)


def del_record_db():
    '''
    Запршивает номер ID для удаления записи из БД
    '''
    number_id = view.num_id()
    data = mod.delete_record(number_id)
    mod.write_data(mod.db, data, 'w')


def import_db_without_id():
    '''
    Импорт данных без ID в файл csv
    '''
    lst_data = mod.reader_without_ID()
    mod.writer_without_ID(lst_data)


def application_menu():
    '''
    Меню приложеия
    '''
    view.menu()
    num = view.get_menu_number()
    if num == 1:
        mod.read_db()
    elif num == 2:
        create_record()
    elif num == 3:
        extracting_record_id()
    elif num == 4:
        import_db()
    elif num == 5:
        import_db_without_id()
    elif num == 6:
        export_db()
    elif num == 7:
        update_record_db()
    elif num == 8:
        del_record_db()
    else:
        view.error_message()


if __name__ == '__main__':
    # print(create_record())
    application_menu()
    pass
