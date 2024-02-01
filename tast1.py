def show_result(name_user: str, file_name: str) -> str:
    """
    Вывод результата студента.
    :param name_user: Имя студента
    :param file_name: Файл где искать
    :return: Строка результата
    """
    f = open(file_name)
    f.readline()

    for line in f.readlines():
        data = line.split(',')
        score = 0
        if data[4] != 'None\n':
            score = int(data[4])
        if name_user in data[1]:
            return f'Ты получил: {score}, за проект - {data[2]}'

    f.close()


def create_table(name_file: str, name_new_file: str):
    """
    Создание таблицы со средней оценкой по классу.
    :param name_file: Где искать
    :param name_new_file: Имя нового файла
    """
    f = open(name_file)
    f.readline()

    all_klass = {}

    '''
    all_klass = {
        '11М': (34, 9)
    }
    '''

    for line in f.readlines():
        data = line.split(',')

        user_klass = data[3]
        score = 0
        if data[4] != 'None\n':
            score = int(data[4])

        if user_klass in all_klass.keys():
            klass = all_klass[user_klass]
            all_klass[user_klass] = (klass[0]+score, klass[1]+1)
        else:
            all_klass[user_klass] = (score, 1)

    f.close()

    data_new_file = 'klass,avg\n'
    for klass, data_klass in all_klass.items():
        sm_klass, count_klass = data_klass
        avg_klass = sm_klass / count_klass
        data_new_file += f'{klass},{avg_klass:.4}\n'

    new_f = open(name_new_file, 'w')
    new_f.write(data_new_file)
    new_f.close()


if __name__ == '__main__':
    print(show_result('Хадаров Владимир', 'students.csv'))
    create_table('students.csv', 'student_new.csv')
