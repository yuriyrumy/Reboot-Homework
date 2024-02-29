# Напишіть програму, яка читає вміст текстового файлу та виводить кількість слів у ньому.

file_name = 'example_file.txt'

try:
    file = open(file_name, 'r', encoding='utf-8')
    words = len(file.read().split())
    file.close()
except FileNotFoundError:
    print('File not found.')
else:
    print(words)
