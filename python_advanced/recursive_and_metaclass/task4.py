# Напишіть рекурсивну функцію, яка приймає рядок та повертає його у зворотньому порядку.

def recursive_reverse(string: str) -> str:
    if len(string) == 0:
        return ''

    return string[len(string) - 1:] + recursive_reverse(string[:-1])


result = recursive_reverse('hello')
print(result)
