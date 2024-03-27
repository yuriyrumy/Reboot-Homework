# До класу Account додайте за допомогою декоратора @property гетер та сетер для приватного атрибуту balance.
# При встановлені цього параметру зробіть перевірку у сетері, щоб це значення було більшим за 0.

class Account:
    _account_holder: str
    __balance: int

    def __init__(self, account_holder: str, balance: int) -> None:
        self._account_holder = account_holder
        self.__balance = balance

    @property
    def balance(self) -> int:
        return self.__balance

    @balance.setter
    def balance(self, value: int) -> None:
        if value < 0:
            raise ValueError('Error. The balance cannot be less than 0.')
        self.__balance = value


account = Account('Jack', 100)
print(account.balance)
account.balance = -200
print(account.balance)
