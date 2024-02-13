from random import randint


def create_login(user: str) -> str:
    """Лоиг из ФИО.
    :param user: ФИО пользователя
    :return: Сгенерированный логин
    """
    data_user = user.split(' ')
    return f'{data_user[0]}_{data_user[1][0]}{data_user[2][0]}'


def create_password() -> str:
    """
    Генерация пароля.
    Обязательно должен содержать:
    - Заглваные английские буквы
    - Прописные английские буквы
    - Цифры
    :return: Сгенерированный пароль
    """
    n_num = randint(1, 3)
    n_abc = randint(1, 3)
    n_ABC = 8 - n_num - n_abc
    num = [chr(randint(48, 57)) for _ in range(n_num)]
    abc = [chr(randint(97, 122)) for _ in range(n_abc)]
    ABC = [chr(randint(65, 90)) for _ in range(n_ABC)]
    s = num + abc + ABC
    for _ in range(20):
        x1, x2 = randint(0, 7), randint(0, 7)
        s[x1], s[x2] = s[x2], s[x1]
    return ''.join(s)


def create_new_table(in_file_name: str, out_file_name: str):
    """Создание новой таблицы с логинами и паролями
    :param in_file_name: Название файла для обработки
    :param out_file_name: Название файла для сохранения
    """
    in_file = open(in_file_name)
    head = in_file.readline()
    new_data = head[:-1] + ',Login,Password\n'
    for line in in_file.readlines():
        line_data = line.split(',')
        login = create_login(line_data[1])
        password = create_password()
        new_data += f'{line[:-1]},{login},{password}\n'
    in_file.close()
    new_file = open(out_file_name, 'w')
    new_file.write(new_data)
    new_file.close()


if __name__ == '__main__':
    create_new_table('students.csv', 'students_password.csv')
