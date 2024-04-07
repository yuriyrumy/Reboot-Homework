# Створіть функціонал для управління бібліотекою. Використовуйте всі набуті знання у ООП для кращого проектування,
# використовуйте атрибути класу та атрибути інстансу, classmethod та staticmethod, приватні та захищені атрибути
# і так далі. Бібліотека повинна мати такі класи: User, Book, Library, Customer, Employee.
#
# Клас Book повинен мати такі атрибути як: title, author, isbn, copies (У одній бібліотеці),
# total_copies (По всім бібліотекам). Клас повинен мати метод check_availability який буде перевіряти чи є книга
# у бібліотеці. Метод update_total_copies який буде оновлювати загальну кількість копій книжок коли вони будуть
# змінюватись. Метод який буде оновлювати кількість книжок у конкретній бібліот. (змінювати параметр copies у інстанса).
# Також клас повинен мати метод validate_isbn який буде валідувати правильність isbn коду (ISBN 0-061-96436-0).
#
# Клас User повинен мати такі атрибути як name, user_id. ДАлі буде інфа про функціонал для Customer та Employee,
# де ви самі повинні розібратись які атрибути де мають бути та як це буде виглядати. Атрибути borrowed_books, salary,
# library. Методи для додавання книжки у бібліотеку та видаленню. Методи для взяття книжки з бібліотеки, та повернення.
#
# Клас Library буде мати поля books, users. Методи які дозволять зареєструвати юзера у бібліотеці,
# знайти книжку за isbn, та показати всі доступні книжки у бібліотеці.
#
# Важливо! Використовуйте все, атрибути класу, атрибути інстансу, клас методи та статик методи, проперті,
# приватні та протектед атрибути.

import re


class Book:
    title: str
    author: str
    isbn: str
    _copies: int

    def __init__(self, title: str, author: str, isbn: str, copies: int) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self._copies = copies
        self.__total_copies = copies

    def check_availability(self) -> bool:
        return self._copies > 0

    def update_copies(self, value) -> None:
        if value > 0:
            self._copies = value
        else:
            raise ValueError('Value Error.')

    @property
    def update_total_copies(self):
        return self.__total_copies

    @update_total_copies.setter
    def update_total_copies(self, value):
        if value > 0:
            self.__total_copies = value
        else:
            raise ValueError('Value Error.')

    @staticmethod
    def validate_isbn(isbn: str) -> str:
        pattern_isbn: str = r'ISBN \d-\d{3}-\d{5}-\d'
        result = re.fullmatch(pattern_isbn, isbn.upper())

        if len(isbn) == 18 and result is not None:
            return f'{isbn} - this ISBN is valid.'

        return f'{isbn} - this ISBN is invalid.'


class Library:
    name: str
    _books: list
    _employees: list
    _customers: list
    __library_count: int = 0

    def __init__(self, name: str) -> None:
        self._books = list()
        self._employees = list()
        self._customers = list()

        Library.__library_count += 1
        self.id = Library.__library_count
        self.name = f'{name} #{self.id}'

    def add_book_to_lib(self, book) -> None:
        self._books.append(book)

    def remove_book_from_lib(self, book) -> None:
        if book in self._books:
            self._books.remove(book)

    def register_employees(self, employee) -> None:
        self._employees.append(employee)

    def register_customers(self, customer) -> None:
        self._customers.append(customer)

    def find_book_by_isbn(self, isbn: str):
        for book in self._books:
            if book.isbn == isbn:
                return book

    def show_books(self):
        availability_books = [book for book in self._books if book.check_availability()]
        return availability_books


class User:
    _name: str
    __user_count: int = 0

    def __init__(self, name: str) -> None:
        self._name = name
        self._library = None

        User.__user_count += 1
        self._user_id = User.__user_count


class Employee(User):
    __salary: int

    def __init__(self, name, salary: int) -> None:
        super().__init__(name)
        self.__salary = salary

    @staticmethod
    def add_book(library, book):
        library.add_book_to_lib(book)

    @staticmethod
    def remove_book(library, book):
        library.remove_book_from_lib(book)


class Customer(User):
    _borrowed_books: list

    def __init__(self, name) -> None:
        super().__init__(name)
        self._borrowed_books = list()

    def borrow_book(self, book) -> None:
        self._borrowed_books.append(book)

    def return_book(self, book) -> None:
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)
