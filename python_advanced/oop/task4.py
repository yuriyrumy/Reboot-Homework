# До класу Circle створеного у попередньому завданні додайте два метода, класметод from_diameter,
# який буде приймати діаметр та повертати екземпляр класу з радіусом розрахованим з переданого у метод діаметру.
# Додайте статикметод check_radius, який буде отримувати радіус, та перевіряти його на валідність
# (радіус повинен бути більший за 0)

class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        result = self.pi * self.radius ** 2
        return result

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter)

    @staticmethod
    def check_radius(radius):
        return radius > 0


circle = Circle.from_diameter(10)
area = circle.area()
valid = Circle.check_radius(17)

print(area)
print(valid)
