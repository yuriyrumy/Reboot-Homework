# Напишіть рекурсивну функцію, яка знаходить n-не число послідовності фібоначчі.

def recursive_fibonacci(number: int) -> int:
    if number <= 1:
        return number
    else:
        return recursive_fibonacci(number - 1) + recursive_fibonacci(number - 2)


result = recursive_fibonacci(7)
print(result)
