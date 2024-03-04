# Створіть клас Circle зі змінною класу pi, рівною 3.14. Додайте змінну екземпляру radius,
# ініціалізовану через конструктор. Додайте метод area, який обчислює і повертає площу круга.

class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        result = self.pi * self.radius ** 2
        return result


circle = Circle(10)
area = circle.area()

print(area)
