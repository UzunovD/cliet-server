# 3.	Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в
# байтовом типе.
words = ['attribute', 'класс', 'функция', 'type']
invalid = []
for word in words:
    byte = word.encode()
    if '\\' in str(byte):
        invalid.append(word)
print(f'Невозможно записать в байтовом типе слова: {", ".join(invalid)}')

# Вариант II
# импорт пишется в начале файла, но сейчас он тут:
import string

words = ['attribute', 'класс', 'функция', 'type']
invalid = []
for word in words:
    if not set(word) <= set(string.printable):
        invalid.append(word)
print(f'Невозможно записать в байтовом типе слова: {", ".join(invalid)}')
