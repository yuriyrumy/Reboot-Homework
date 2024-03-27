# Створіть діамантову проблему успадкування з класів A, B, C і D, де D успадковує від B і C, а B і C успадковують від A.
# Кожен клас повинен мати метод introduce() який буде повертати інфу про клас.
#
# Створіть інстанси цих класів та повикликайте метод introduce(). Приберіть у деяких класах цей метод
# і протестуйте те як python вирішує проблему діамантового успадкування у цьому випадку.

class A:
    def introduce(self) -> str:
        return 'This is class A.'


class B(A):
    def introduce(self) -> str:
        return 'This is class B.'


class C(A):
    def introduce(self) -> str:
        return 'This is class C.'


class D(B, C):
    def introduce(self) -> str:
        return 'This is class D.'


a = A()
b = B()
c = C()
d = D()
print(a.introduce())
print(b.introduce())
print(c.introduce())
print(d.introduce())
print(D.mro())
