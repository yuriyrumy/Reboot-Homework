# Реалізуйте функцію, яка ділить два числа, але обробляє помилку ZeroDivisionError, якщо друге число дорівнює нулю.

def division(num1: str, num2: str):
    try:
        div = int(num1) / int(num2)
        return f'{num1} / {num2} = {div}'
    except ZeroDivisionError:
        return 'Division by zero!'
    except ValueError:
        return 'Error. Enter numbers!'


user_num1 = input('Enter first number: ')
user_num2 = input('Enter second number: ')
result = division(user_num1, user_num2)
print(result)
