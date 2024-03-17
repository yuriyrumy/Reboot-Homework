# Напишіть декоратор, який буде приймати необмежену кількість типів даних (str, int і так далі) та перевіряти
# аргументи які передали в декоровану функцію на те чи вони є типами, які передали в декоратор, та повертати
# помилку якщо ні. Наприклад ми передали @my_decorator(int, str) а декоровану функцію викликали з аргументами
# func(2, “hello”, True) повинна повернутись помилка бо ми не очікуємо bool тип.

def type_checker(*types, **kwtypes):
    def decorator(func):
        def inner(*args, **kwargs):
            type_list = list()
            for i_type in range(len(types)):
                if types[i_type] not in type_list:
                    type_list.append(types[i_type])
            for k in kwtypes:
                if kwtypes[k] not in type_list:
                    type_list.append(kwtypes[k])
            for i_arg in range(len(args)):
                if type(args[i_arg]) not in type_list:
                    raise TypeError('Invalid type in function.')
            for i_kwarg in kwargs:
                if type(kwargs[i_kwarg]) not in type_list:
                    raise TypeError('Invalid type in function.')
            return func(*args, **kwargs)
        return inner
    return decorator


@type_checker(bool, str, int)
def some_func(a, b, c):
    return a, b, c


print(some_func(2, 'hello', True))
