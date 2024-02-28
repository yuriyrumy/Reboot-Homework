# Напишіть програму, яка відкриває файл для читання та обробляє помилку FileNotFoundError, якщо файл не знайдено.

file_name = 'example_file.txt'
try:
    file = open(file_name, 'r', encoding='utf-8')
    read_file = ''.join(file.readlines())
    print(f'The contents of the file: \n{read_file}')
    file.close()
except FileNotFoundError:
    print('File not found.')
