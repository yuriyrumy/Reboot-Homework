# Створіть простий контекстний менеджер file_opener за допомогою декоратора з contextlib, який буде відкривати файл,
# повертати його та закривати при виході з контексту.

from contextlib import contextmanager


@contextmanager
def file_opener(filename, mode):
    file = open(filename, mode)
    yield file
    file.close()


with file_opener('example.txt', 'r') as f:
    print(f.read())
