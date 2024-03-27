# Створіть клас Account та приватний атрибут balance. Додайте метод який буде повертати значення приватного атрибуту.
# Створіть протектед атрибут account_holder.

class Account:
    _account_holder: str
    __balance: int

    def __init__(self, account_holder: str, balance: int) -> None:
        self._account_holder = account_holder
        self.__balance = balance

    def balance(self) -> int:
        return self.__balance


account = Account('Jack', 2500)
print(account.balance())
