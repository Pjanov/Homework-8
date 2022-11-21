import csv


count_id = 'counter_ID.csv'
file_import = 'data_import.csv'
file_import_without_id = 'import_without_ID.csv'
file_export = 'exporting_data.csv'
db = 'database.csv'


def global_mapping():
    '''
    Шаблон словаря
    '''
    return {'ID': 'Идентификатор', 'Last_name': 'Фамилия', 'First_name': 'Имя', 'Group': 'Класс'}


def read_data(csvfile_name: str) -> list[dict]:
    '''
    Считать данные из csv файла
    :param file_name: путь к файлу
    :param delim: разделитель полей
    :return: данные в виде списока словарей
    '''
    with open(csvfile_name, 'r', encoding='utf-8') as data:
        reader = csv.DictReader(data)
        res = [row for row in reader]
        return res


def write_data(csvfile_name: str, data_lst: list[dict], m='a', delim=',') -> None:
    '''
    Дозаписывает данные в csv файл
    :param csvfile_name: путь к файлу
    :param data_lst: принемает список словарей
    :param m: операция с файлом, по умолчанию добавляет запись
    :param delim: разделитель полей
    :return: None
    '''
    with open(csvfile_name, mode=m, newline='', encoding='utf-8') as data:
        header = ['ID', 'Last_name', 'First_name',
                  'Group']  # названия заголовков
        writer = csv.DictWriter(data, delimiter=delim, fieldnames=header)
        if m == 'w':
            writer.writeheader()  # запись заголовка
        writer.writerows(data_lst)


def convert_to_list(data: tuple) -> list:
    '''
    Преобразование данных в список
    :param data: принемает кортеж
    :return: список
    '''
    res = [el for el in data]
    return res


def get_id(file_name=count_id) -> str:
    '''
    Получить ID
    :param file_name: путь к счетчику ID
    :return: значение ID + 1
    '''
    with open(file_name, 'r', encoding='utf-8') as id_reading:
        reader = id_reading.readline()
        reader = str(int(reader) + 1)
        with open(file_name, 'w', encoding='utf-8') as write_id:
            write_id.write(reader)
    return reader


def extracting_record(user_id: str, file_mame=db, delim=','):
    '''
    Извлечь запись по ID. Запись извлекается и выводится в консоль
    :param file_mame: путь к файлу
    :param user_id: номер ID
    :param delim: разделитель полей
    '''
    res = []
    with open(file_mame, 'r', newline='', encoding='utf-8') as data:
        reader = csv.DictReader(data, delimiter=delim)
        for row in reader:
            if str(user_id) == row['ID']:
                res.append(
                    f"{row['ID']} => {row['Last_name']},{row['First_name']},{row['Group']}")
                break
    print(''.join(res))


def read_db(file_name=db):
    '''
    Выводит БД в консоль
    :param file_name: путь к файлу
    :return: None
    '''
    with open(file_name, 'r', newline='', encoding='utf-8') as data:
        reader = csv.DictReader(data)
        for row in reader:
            print(
                f"{row['ID']},{row['Last_name']},{row['First_name']},{row['Group']}")


def delete_record(num_id: int, file_name=db) -> list[dict]:
    '''
    Удалить запись по ID
    :param num_id: номер ID
    :param num_id: путь к файлу БД
    '''
    list_dict = []
    with open(file_name, 'r', newline='', encoding='utf-8') as data:
        reader = csv.DictReader(data, delimiter=',')
        for row in reader:
            if str(num_id) in row['ID']:
                row.clear()
            else:
                list_dict.append(row)
    return list_dict


def update_record(num_id: int, file_name=db):
    '''
    Обновить запись по ID
    :param num_id: номет ID
    :param file_name: путь к файлу БД
    :return: обновленный словарь
    '''
    list_dict = []
    with open(file_name, 'r', newline='', encoding='utf-8') as data:
        reader = csv.DictReader(data, delimiter=',')
        for row in reader:
            if str(num_id) in row['ID']:
                new_dict = {
                    'ID': num_id,
                    'Last_name': input(f"Было: {row['Last_name']}, стало: "),
                    'First_name': input(f"Было: {row['First_name']}, стало: "),
                    'Group': input(f"Было: {row['Group']}, стало: ")}
                list_dict.append(new_dict)
                break
    return list_dict


def reader_without_ID(file_name=db) -> list:
    '''
    Чтение данных из файла csv без ID
    :param file_name: путь к файлу
    :return: список
    '''
    lst = []
    with open(file_name, 'r', encoding='utf-8') as data:
        reader = csv.reader(data, delimiter=',')
        for line in reader:
            lst.append(f"{line[1]},{line[2]},{line[3]}\n")
        return lst


def writer_without_ID(lst: list, file_name=file_import_without_id):
    '''
    Записывает полученные данные в файл csv
    :param lst: список с данными
    :return: None
    '''
    with open(file_name, 'w', encoding='utf-8') as data:
        data.writelines(lst)


if __name__ == '__main__':
    # global_mapping()
    # print(read_data(db))
    # print(write_data(file_import, q))
    # print(convert_to_list(('000', '111', '222')))
    # print(get_id(count_id))
    # print(extracting_record(1))
    # read_db()
    # delete_record(2)
    # print(update_record(2))
    # print(writer_without_ID(reader_without_ID()))
    pass
