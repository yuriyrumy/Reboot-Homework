# Напишіть ітератор, який буде працювати так само як функція range, приймати початковий елемент, останній та крок.

class RangeIterator:
    def __init__(self, start: int, end: int, step=1):
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            value = self.current
            self.current += self.step
            return value


for i in RangeIterator(1, 10, 2):
    print(i, end=' ')
