# До попереднього завдання додайте клас Electric та додайте туди приватний атрибут battery та метод charge()
# який буде встановлювати атрибут battery до 100. Створіть окремий клас ElectricCar та ElectricMoto та успадкуйтесь
# від Vehicle та Electric. Створіть інстанси всіх класів, та викличте метод mro для кожного інстансу,
# щоб подивитись порядок успадкування в кожному класі.

class Vehicle:
    def __init__(self, mark: str, model: str) -> None:
        self.mark = mark
        self.model = model

    def get_info(self) -> str:
        return f'Mark: {self.mark}, model: {self.model}'


class Car(Vehicle):
    def __init__(self, mark, model, wheels: int) -> None:
        super().__init__(mark, model)
        self.wheels = wheels


class Moto(Vehicle):
    def __init__(self, mark, model, wheels: int) -> None:
        super().__init__(mark, model)
        self.wheels = wheels


class Electric:
    def __init__(self) -> None:
        self.__battery = 0

    def __charge(self) -> None:
        self.__battery = 100


class ElectricCar(Vehicle, Electric):
    pass


class ElectricMoto(Vehicle, Electric):
    pass


electric_car1 = ElectricCar('Tesla', 'Model S')
electric_moto1 = ElectricMoto('AGM', '2000W')

print(isinstance(electric_car1, Vehicle))
print(isinstance(electric_car1, Electric))
print(isinstance(electric_car1, Car))
print()
print(isinstance(electric_moto1, Vehicle))
print(isinstance(electric_moto1, Electric))
print(isinstance(electric_moto1, Moto))
print()
print(ElectricCar.mro())
print(ElectricMoto.mro())
