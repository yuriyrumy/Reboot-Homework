# Розробіть клас Counter, який буде мати атрибут класу count. Створіть метод get_count який буде повертати атрибут
# класу count. Кожного разу, коли ми створюємо екземпляр класу Counter ми повинні збільшувати атрибут класу counter на 1,
# тим самим зберігаючи там кількість екземплярів створених для цього класу. А під час виклику метода get_count ми повинні
# фіксувати кількість викликів даного методу для кожного екземпляру.

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1
        self.value = 0

    @staticmethod
    def get_count():
        return Counter.count

    def method_called(self):
        self.value += 1
        return self.value


c1 = Counter()
c2 = Counter()

result = c1.get_count()
print(result)  # 2
print(c1.method_called())  # 1
