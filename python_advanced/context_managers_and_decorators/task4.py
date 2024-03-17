# Напишіть декоратор, який буде прінтити “{імʼя функції яку викликали} is been called with parameters:
# {список параметрів з якими функцію викликали}”, а після виклику функції “Function {function_name}
# return this value: {значення яке функція повернула}”.

def function_info(func):
    def inner(*args, **kwargs):
        print(f'{func.__name__} is been called with args: {args}, kwargs: {kwargs}')
        result = func(*args, **kwargs)
        print(f'Function {func.__name__} return this value: {result}')
        return result
    return inner


@function_info
def some_func(*args):
    return sum(args)


some_func(1, 2, 3, 4)
