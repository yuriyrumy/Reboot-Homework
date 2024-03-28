# Напишіть рекурсивну функцію, яка повертає лічільник з числа яке ми до неї передамо до 1-го.
# За допомогою модулю time зробіть затримку в 1 секунду між кожним повертанням лічільника.

from time import sleep


def recursive_count_down(number: int) -> int:
    if number == 1:
        return 1

    print(number)
    sleep(1)
    return recursive_count_down(number - 1)


result = recursive_count_down(10)
print(result)
