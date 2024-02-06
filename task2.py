import time


def paste_sort(data: [int]) -> [int]:
    """Сортировка вставками.
    :return: Отсортированный массив
    :param data: Массив который надо отсортировать
    """
    for i in range(len(data)):
        x = data[i]
        j = i
        while j > 0 and x < data[j-1]:
            data[j] = data[j-1]
            j -= 1
        data[j] = x
    return data


def main():
    # Дописать решение задачи №2
    pass


if __name__ == '__main__':
    # main()
    example_data = [4, 7, 2, 8, 4, 2, 9, 0, 1]
    new_data = paste_sort(example_data)

    start_time = time.time()
    print(new_data)
    print(time.time() - start_time)

    start_time = time.time()
    print(sorted(example_data))
    print(time.time() - start_time)
