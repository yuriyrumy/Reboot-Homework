# Створіть клас Library, який зберігає книги (у вигляді списку екземплярів класу Book). Реалізуйте __len__
# для повернення кількості книг у бібліотеці та __getitem__ для доступу до книги за заданим індексом.

class Library:
    def __init__(self, books):
        self.books = books

    def __len__(self):
        return len(self.books)

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.books[index]
        elif isinstance(index, str):
            return self.books.index(index)
        else:
            raise TypeError('Invalid Argument Type')


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f'{self.title} {self.author}'


b1 = Book("Title1", "Author1")
b2 = Book("Title2", "Author2")
b3 = Book("Title3", "Author3")

library = Library([b1, b2, b3])

print(len(library))
print(library[2])
