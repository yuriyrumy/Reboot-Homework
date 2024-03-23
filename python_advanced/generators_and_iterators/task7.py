# Створіть ітератор, який буде фільтрувати значення. Ітератор приймає ітеровану послідовність та функцію.
# Якщо функція на елементі поверне True то ми повертаємо цей елемент. Важливо, працювати з цим ітератором
# за допомогою циклу while проходячись по ньому за допомогою методів ітератора.

class FilterIterator:
    def __init__(self, some_objects, func):
        self.some_objects = some_objects
        self.func = func
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        for _ in range(len(self.some_objects)):
            if self.index == len(self.some_objects):
                raise StopIteration
            element = self.some_objects[self.index]
            self.index += 1
            if self.func(element):
                return element


f_iter = FilterIterator([1, 2, 3, 4, 6], lambda x: x % 2 == 0)
while True:
    try:
        print(next(f_iter))
    except StopIteration:
        break
