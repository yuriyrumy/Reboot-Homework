# Розробіть клас Book, атрибутами якого є title та author.
# Реалізуйте __eq__ для перевірки рівності на основі назви та автора та __ne__ для перевірки нерівності.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        raise TypeError('Unsupported operand type for ==.')

    def __ne__(self, other):
        if isinstance(other, Book):
            return self.title != other.title or self.author != other.author
        raise TypeError('Unsupported operand type for !=.')


book1 = Book('Book of Banana', 'Mike')
book2 = Book('The Monkey', 'Sofia')
book3 = Book('Book of Banana', 'Mike')

print(book1 != book2)
print(book2 == book3)
