# Використовуючи всі набуті знання у успадкуванні та інкапсуляції спроектуй просту банківську систему.
# Створи клас Customer та BankAccount. Ти можеш створювати базові класи, абстрактні класи, на твій розсуд.
# Customer повинен мати такі атрибути як name, email, customer_id. BankAccount повинен мати
# balance, owner, account_number. У кастомера повинні бути методи для отримання інфи про атрибути.
# У BankAccount повинні бути методи поповнення та виведення коштів з усіма валідаціями,
# а також метод для отримання account_number


class Customer:
    name: str
    email: str
    customer_id: int

    def __init__(self, name: str, email: str, customer_id: int) -> None:
        self.name = name
        self.email = email
        self.customer_id = customer_id

    def get_info(self) -> str:
        return f'Name: {self.name}\nEmail: {self.email}\nCustomer ID: {self.customer_id}'


class BankAccount:
    _account_number: int
    _balance: int

    def __init__(self, owner, account_number: int, balance: int = 0) -> None:
        self._owner = owner
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount: int) -> None:
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount should be greater than 0.')

    def withdraw(self, amount: int) -> None:
        if amount > 0:
            if self._balance >= amount:
                self._balance -= amount
            else:
                raise ValueError('There is not enough money.')
        else:
            raise ValueError('Amount should be greater than 0.')

    def get_balance(self) -> int:
        return self._balance

    def get_account_number(self) -> int:
        return self._account_number


client1 = Customer('Jack', 'jackjack@gmail.com', 1)
account1 = BankAccount(client1, 1)

print(client1.get_info())
account1.deposit(400)
print(account1.get_balance())
account1.withdraw(300)
print(account1.get_balance())
