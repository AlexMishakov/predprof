def main(in_file_name: str, out_file_name: str, serach_name: str):
    """
    Основная функция.
    Ищет пользователя по имени и фамилии, создает новую таблицу со средней оценкой по классу
    :param in_file_name: Название файла для обработки
    :param out_file_name: Название файла для сохранения
    :param serach_name: Кого искать
    """
    f = open(in_file_name)
    f.readline()
    all_klass = {}
    for line in f.readlines():
        data = line.split(',')
        score = 0
        if data[4] != 'None\n':
            score = int(data[4])
        user_klass = data[3]
        if user_klass in all_klass.keys():
            klass = all_klass[user_klass]
            all_klass[user_klass] = (klass[0]+score, klass[1]+1)
        else:
            all_klass[user_klass] = (score, 1)

        if serach_name in data[1]:
            print(f'Ты получил: {score}, за проект - {data[2]}')

    f.close()

    data_new_file = 'klass,avg\n'
    for klass, data_klass in all_klass.items():
        sm_klass, count_klass = data_klass
        avg_klass = sm_klass / count_klass
        data_new_file += f'{klass},{avg_klass:.4}\n'

    new_f = open(out_file_name, 'w')
    new_f.write(data_new_file)
    new_f.close()


if __name__ == '__main__':
    main('students.csv', 'student_new.csv', 'Хадаров Владимир')
