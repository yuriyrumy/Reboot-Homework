# Напишіть реалізацію патерну Singleton за допомогою створення метакласу.
# Сінглтон - це патерн при якому ми можемо створити лише 1 інстанс для нашого класу.

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass


s1 = Singleton()
s2 = Singleton()

print(s1 == s2)
