# Розробіть клас BankAccount для представлення банківського рахунку. Додайте методи для зняття та поповнення
# коштів на рахунку. Використовуйте магічний метод __str__ для виведення інформації про рахунок.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if self.balance < amount:
            print('There are not enough funds in the account for withdrawal!')
        else:
            self.balance -= amount

    def top_up(self, amount):
        self.balance += amount

    def __str__(self):
        return f'You account balance is: {self.balance}'


account = BankAccount(100)
account.withdraw(50)
account.top_up(200)
print(account)
