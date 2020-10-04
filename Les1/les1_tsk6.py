# 6.	Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование»,
# «сокет», «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате
# Unicode и вывести его содержимое.

words = ['сетевое программирование', 'сокет', 'декоратор']
# создаем файл с кодировкой по умолчанию:
with open('test_file.txt', 'w') as f:
    f.writelines(words)
    print(f'Файл {f.name} по умолчанию имеет кодировку {f.encoding}')

# при попытке прочитать содержимое файла с ошибочной кодировкой получаем ошибку UnicodeDecodeError:
# 'utf-8' codec can't decode byte 0xf1 in position 0: invalid continuation byte:
with open('test_file.txt', 'r', encoding='utf-8') as f:
    try:
        (print(f.read()))
    except UnicodeDecodeError as err:
        print(f'Ошибка UnicodeDecodeError: {err}')
