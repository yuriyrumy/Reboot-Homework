# Створіть простий метаклас, який буде прінтити будь яке повідомлення, коли новий клас створюється за його допомогою.

class SimpleMeta(type):
    def __new__(cls, name, bases, attrs):
        print('Creating class object')
        return super().__new__(cls, name, bases, attrs)


class MyClass(metaclass=SimpleMeta):
    pass


my_class = MyClass()
print(my_class)
