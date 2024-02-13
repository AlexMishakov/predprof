def main():
    """Основная функция."""

    # Подготовка данных
    file = open('students.csv')
    file.readline()
    data_file = []
    for line in file.readlines():
        line = line.replace('\n', '')
        data = line.split(',')
        if data[4] == 'None':
            data[4] = 0
        else:
            data[4] = int(data[4])
        data_file.append(tuple(data))

    # Сортировка вставкой
    for i in range(len(data_file)):
        x = data_file[i]
        j = i
        while j > 0 and x[4] > data_file[j-1][4]:
            data_file[j] = data_file[j-1]
            j -= 1
        data_file[j] = x


    # Вывод первых трех из 10-x классов
    count = 0
    for l in data_file:
        if '10' in l[3]:
            print(f'{count+1} место: {l[1]}')
            count += 1
        if count == 3:
            break


if __name__ == '__main__':
    main()
