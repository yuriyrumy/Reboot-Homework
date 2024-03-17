# Напишіть декоратор, який приймає як параметр число,
# та робить time.sleep перед викликом декорованої функції на це число.

import time


def sleeper(n):
    def decorator(func):
        def inner(*args, **kwargs):
            time.sleep(n)
            result = func(*args, **kwargs)
            return result
        return inner
    return decorator


@sleeper(5)
def some_func(num):
    return [i ** 2 for i in range(num)]


print(some_func(20))
