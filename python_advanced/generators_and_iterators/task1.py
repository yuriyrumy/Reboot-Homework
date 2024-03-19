# Напишіть функцію-генератор з назвою count_down, яка отримує число і повертає зворотній відлік від цього числа до 0.


def count_down(number: int):
    for n in range(number, -1, -1):
        yield n


for i in count_down(10):
    print(i, end=' ')
