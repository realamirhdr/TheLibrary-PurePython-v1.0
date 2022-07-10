from Member import Member
from Manager import Manager
from Book import Book


class System:
    def __init__(self):
        self.admin = Manager("admin", "admin")

    members = []
    books = []
    bookCounter = 0
    memberCounter = 0

    def adminAuth(self, username, password):
        if username.__eq__(self.admin.getUsername()) and password.__eq__(self.admin.getPassword()):
            return True

    def memberAuth(self, username, password):
        for member in self.members:
            if username.__eq__(member.getUsername()) and password.__eq__(member.getPassword()):
                return True

    def addMember(self, username, password):
        newMember = Member(username, password)
        newMember.setId(self.memberCounter + 1)
        self.members.append(newMember)
        self.memberCounter += 1

    def addBook(self, name, writer, category):
        newBook = Book(name, writer, category)
        newBook.setId(self.bookCounter + 1)
        self.books.append(newBook)
        self.bookCounter += 1

    def findBook(self, id):
        for book in self.books:
            if id == book.getId():
                return book

    def findMember(self, username, password):
        for member in self.members:
            if username.__eq__(member.getUsername()) and password.__eq__(member.getPassword()):
                return member

    def removeBook(self, id):
        self.books.pop(id - 1)

    def showAllMembers(self):
        if self.memberCounter == 0:
            print('no members')
        else:
            for member in self.members:
                info = member.getUsername() + ', ' + member.getPassword() + ', ' + str(member.getId())
                print(info)

    def showAllBooks(self):
        if self.bookCounter == 0:
            print('no books')
        else:
            for book in self.books:
                info = book.getName() + ' by ' + book.getWriter() + ', ' + book.getCategory() + ', ' + str(book.getId())
                print(info)
