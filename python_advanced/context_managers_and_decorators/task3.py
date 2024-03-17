# Напишіть простий декоратор, який буде прінтити повідомлення “Function is been called” до та після виклику функції.
# Будьте уважні, деворатор повинен працювати з усіма функціями, які приймають різні параметри, та не забувайте повертати
# результат роботи функції.

def called_function(func):
    def inner(*args, **kwargs):
        print('Function is been called.')
        print(func(*args, **kwargs))
        print(f'Function is been called.')
    return inner


@called_function
def some_func(*args):
    return sum(args)


some_func(1, 2, 3, 4)
