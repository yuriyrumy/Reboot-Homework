# Створіть функцію, яка приймає рядок від користувача та записує його у файл.

file_name = 'example_file.txt'


def write_file(string: str, file):
    open_file = open(file, 'w', encoding='utf-8')
    open_file.write(string)
    open_file.close()
    print('Your line is written to a file.')


user_sting = input('Enter a string: ')
write_file(user_sting, file_name)
