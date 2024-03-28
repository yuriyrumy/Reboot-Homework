# Напишіть рекурсивну функцію, яка обчислює суму цифр заданого числа.

def recursive_sum(number: int) -> int:
    if number < 10:
        return number

    return number % 10 + recursive_sum(number // 10)


result = recursive_sum(1234)
print(result)
