# Напишіть генератор Фібоначчі, який видає числа у послідовності Фібоначчі.

def fibonacci(number: int):
    a, b = 0, 1
    for _ in range(number):
        yield a
        a, b = b, a + b


for i in fibonacci(10):
    print(i, end=' ')
