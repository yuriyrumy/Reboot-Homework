# Напишіть програму, яка пропонує користувачу ввести список чисел, відокремлених комами. Перетворіть введений рядок
# у список цілих чисел і обробляйте помилки ValueError (у випадку невірного введення цілих чисел)
# та IndexError (у випадку доступу до індексів, що виходять за межі діапазону).

user_numbers = input('Enter numbers separated by commas: ')
numbers = list()
try:
    numbers = [int(n) for n in user_numbers.split(',')]
except ValueError:
    print('Error. You must enter numbers separated by commas.')
else:
    print(numbers)

user_index = input('Enter element index: ')
try:
    print(numbers[int(user_index)])
except IndexError:
    print('Error. List index out of range.')
except ValueError:
    print('Index must be a number.')
