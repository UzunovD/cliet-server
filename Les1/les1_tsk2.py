# 2.	Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
# последовательность кодов (не используя методы encode и decode) и определить тип, содержимое и длину
# соответствующих переменных.

# записать в байтовом типе:
words_byte = [b'class', b'function', b'method']

for word in words_byte:
    print(f'тип: {type(word)}, содержимое: {word}, текст: {str(word)[2:-1]}, динна: {len(word)}')
