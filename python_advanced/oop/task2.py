# Створіть клас Rectangle для представлення прямокутника.
# Додайте методи для обчислення площі та периметра прямокутника. Створіть об'єкт Rectangle і викличте ці методи.

class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return f'Square = {self.x * self.y}'

    def perimeter(self):
        return f'Perimeter = {2 * self.x + 2 * self.y}'


rect = Rectangle(2, 4)
square = rect.square()
perimeter = rect.perimeter()

print(square)
print(perimeter)
