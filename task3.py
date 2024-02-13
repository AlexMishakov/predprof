def search(_id_project: int, file_name: str) -> str:
    """Фукнция поиска проекта по id.
    :param _id_project: id проекта для поиска
    :param file_name: Где искать
    :return: Результат поиска
    """
    f = open(file_name)
    f.readline()

    for line in f.readlines():
        data = line.split(',')
        if _id_project == int(data[2]):
            f.close()
            return f'Проект № {_id_project} делал: {data[1]} он(а) получил(а) оценку - {data[4]}'

    f.close()
    return 'Ничего не найдено'


def menu():
    """Меню программы."""
    while True:
        id_project = input('Введите id проекта: ')
        if id_project == 'СТОП':
            break

        print(search(int(id_project), 'students.csv'))


if __name__ == '__main__':
    menu()
