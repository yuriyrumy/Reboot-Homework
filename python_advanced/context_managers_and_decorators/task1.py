# Створіть простий контекстний менеджер FileOpener, який буде відкривати файл,
# повертати його та закривати при виході з контексту.

class FileOpener:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()


with FileOpener('example.txt', 'r') as f:
    print(f.read())
