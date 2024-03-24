# Створіть клас Vehicle який матиме атрибути mark та model та метод get_info() який буде повертати інформацію
# про марку та модель авто. Створіть ще два класи Car та Moto які будуть додавати додаткові атрибути wheels
# і успадковуватись від Vehicle. Створіть сутності класів Car та Moto та викличте там метод get_info().

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


car1 = Car('Toyota', 'Supra MK IV', 4)
moto1 = Moto('Yamaha', 'R6', 2)

print(car1.get_info())
print(moto1.get_info())
