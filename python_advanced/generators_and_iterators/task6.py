# Додайте до попереднього ітератора CycleIterator метод peek, який буде підглядувати та повертати наступне значення,
# але не переходити на наступну ітерацію. Наприклад ітератор вже повернув a, b наступний елемент - c,
# якщо я викличу peek він його поверне, а якщо я викличу next() або в циклі наступну ітерацію викличу
# він повинен все одно повернути c.

class CyclicIterator:
    def __init__(self, some_objects) -> None:
        self.some_objects = some_objects
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.some_objects):
            self.index = 0
        element = self.some_objects[self.index]
        self.index += 1
        return element

    def peak(self):
        if self.index == len(self.some_objects):
            return self.some_objects[0]
        else:
            return self.some_objects[self.index]


cycle_iter = CyclicIterator([1, 2, 3])
print(next(cycle_iter))  # 1
print('Peak:', cycle_iter.peak())  # 2
print(next(cycle_iter))  # 2
print(next(cycle_iter))  # 3
print('Peak:', cycle_iter.peak())  # 1
print('Peak:', cycle_iter.peak())  # 1
print(next(cycle_iter))  # 1
print('Peak:', cycle_iter.peak())  # 2
