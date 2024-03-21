# Напишіть ітератор CyclicIterator, який бере довільний ітерабельний об'єкт і циклічно перебирає його до нескінченності.
# Наприклад: ['a', 'b', 'c'] → a, b, c, a, b, c, a, b...

class CyclicIterator:
    def __init__(self, some_objects) -> None:
        self.some_objects = some_objects
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.some_objects) - 1:
            self.index = 0
        element = self.some_objects[self.index]
        self.index += 1
        return element


for i in CyclicIterator([1, 2, 3]):
    print(i, end=' ')
