# Створіть програму, яка отримує від користувача два інпути, конвертує цей інпут до числа і відловлює помилку,
# якщо конвертувати не вийшло.

def is_numbers(num1: str, num2: str):
    try:
        return f'Numbers: {int(num1)} and {int(num2)}'
    except ValueError:
        return 'Error. Enter numbers.'


user_num1 = input('Enter first number: ')
user_num2 = input('Enter second number: ')
result = is_numbers(user_num1, user_num2)
print(result)
