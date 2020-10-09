# 1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных
#  данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый 'отчетный' файл в формате CSV.
import os
import re
import csv


def get_data():
    os_name_list = []
    os_code_list = []
    os_prod_list = []
    os_type_list = []
    main_data = [[], ]

    structure = [
        ('Изготовитель системы', os_prod_list),
        ('Название ОС', os_name_list),
        ('Код продукта', os_code_list),
        ('Тип системы', os_type_list),
    ]

    for tag in structure:
        main_data[0].append(tag[0])

    directory = os.getcwd()
    files = list(filter(lambda x: x.startswith('info') and x.endswith('.txt'), os.listdir(directory)))
    i = 1
    for file in files:
        main_data.append([])
        with open(file, 'r') as f:
            data = f.read()
            for tag, lst in structure:
                regex_pattern = re.compile(f'{tag}.+')
                similar = regex_pattern.search(data)
                info = similar.group()[len(tag) + 1:].strip()
                lst.append(info)
                main_data[i].append(info)
            i += 1

    return main_data


def write_to_csv():
    with open('info.csv', 'w', encoding='utf-8') as f:
        data = get_data()
        f_writer = csv.writer(f)
        for row in data:
            f_writer.writerow(row)

    with open('info.csv', encoding='utf-8') as f:
        print(f.read())


if __name__ == '__main__':
    write_to_csv()
