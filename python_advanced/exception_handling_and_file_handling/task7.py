# Обробіть виняток IndexError, коли програма намагається отримати доступ до неправильного індексу в списку.

some_list = ['apple', 'oranges', 10, 22, 33, 'Coffee']
user_index = input('Enter element index: ')

try:
    print(some_list[int(user_index)])
except IndexError:
    print('Error. List index out of range.')
except ValueError:
    print('Index must be a number.')
