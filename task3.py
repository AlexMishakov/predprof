
def search(_id_project: int):
    print(f'test {_id_project}')


def main():
    while True:
        id_project = input('Введите id проекта: ')
        if id_project == 'СТОП':
            break

        search(int(id_project))


if __name__ == '__main__':
    main()
