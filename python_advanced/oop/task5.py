# Розробіть клас Vehicle для представлення транспортного засобу. Додайте атрибути, такі як назва, швидкість і вартість.
# Реалізуйте метод __gt__, який порівнює два транспортних засоби за швидкістю.
# Створіть список транспортних засобів і відсортуйте його за швидкістю за допомогою функції sorted()

class Vehicle:
    def __init__(self, name, speed, cost):
        self.name = name
        self.speed = speed
        self.cost = cost

    def __repr__(self):
        return f'{self.name}. Speed: {self.speed}. Cost: {self.cost}'

    def __gt__(self, other):
        if self.speed > other.speed:
            return f'{self.name} faster than {other.name}.'
        elif self.speed < other.speed:
            return f'{other.name} faster than {self.name}.'
        else:
            return f'This cars {self.name} and {other.name} have the same speed.'


v1 = Vehicle('Audi', 260, 10000)
v2 = Vehicle('BMW', 250, 9000)
v3 = Vehicle('Lexus', 210, 12000)
v4 = Vehicle('Honda', 290, 14000)
v5 = Vehicle('Toyota', 300, 18000)

result = sorted([v1, v2, v3, v4, v5], key=lambda car: repr(car.speed))

print(v1 > v2)

for i in result:
    print(i)
