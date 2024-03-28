# Напишіть рекурсивну функцію, яка обчислює факторіал заданого числа.

def recursive_factorial(number: int) -> int:
    if number == 1:
        return 1

    return number * (recursive_factorial(number - 1))


result = recursive_factorial(5)
print(result)
