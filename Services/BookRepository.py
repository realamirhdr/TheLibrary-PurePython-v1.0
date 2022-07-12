from Models.Book import Book

class BookRepository:
    books = []
    bookCounter = 0

    def addBook(self, name, writer, category):
        newBook = Book(name, writer, category)
        newBook.setId(self.bookCounter + 1)
        self.books.append(newBook)
        self.bookCounter += 1

    def findBook(self, id):
        for book in self.books:
            if id == book.getId():
                return book

    def removeBook(self, id):
        self.books.pop(id - 1)

    def showAllBooks(self):
        if self.bookCounter == 0:
            print('no books')
        else:
            for book in self.books:
                info = book.getName() + ' by ' + book.getWriter() + ', ' + book.getCategory() + ', ' + str(
                    book.getId())
                print(info)
