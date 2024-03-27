# Створи абстрактний клас Shape та додай метод area, успадкуйся від цього класу та створи два класи Rectangle та Circle
# реалізувавши метод area. Створи інстанси класів Circle та Rectangle та виклич метод area.

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> None:
        pass


class Rectangle(Shape):
    width: int | float
    height: int | float

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def area(self) -> int | float:
        return self.width * self.height


class Circle(Shape):
    radius: int | float

    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self) -> int | float:
        return 3.14 * self.radius ** 2


r = Rectangle(4, 5)
c = Circle(9)
print(r.area())
print(c.area())
