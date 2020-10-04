# 4.	Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового
# представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).

words = ['разработка', 'администрирование', 'protocol', 'standart']

words_byte = list(map(lambda x: x.encode('utf-8'), words))
words_str = list(map(lambda x: x.decode('utf-8'), words_byte))
print(words_byte)
print(words_str)

# через функцию


def convert(source: iter, mode, encoding='utf-8'):
    '''
    Converts the original sequence to the specified one, according to the mode

    :param source: the source iterable sequence
    :param mode: conversion mode
    :param encoding: encoding for conversion
    :return: returns a list of converted expressions
    '''

    result = []
    for elem in source:
        if mode == 'encode':
            result.append(elem.encode(encoding))
        elif mode == 'decode':
            result.append(elem.decode(encoding))
    return result


words_byte = convert(words, 'encode')
words_str = convert(words_byte, 'decode')
print(words_byte)
print(words_str)
