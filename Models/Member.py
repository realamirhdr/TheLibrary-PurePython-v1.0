from User import User


class Member(User):

    def __init__(self, username, password):
        super().__init__(username, password)
        self.id = None

    borrowed = []
    borrowedCounter = 0

    def borrow(self, book):
        self.borrowed.append(book)
        self.borrowedCounter += 1
        print('borrowed successfully.')

    def returnBorrowed(self, id):
        self.borrowed.pop(id - 1)
        self.borrowedCounter -= 1
        print('returned successfully.')

    def showAllBorrowed(self):
        if self.borrowedCounter != 0:
            for i in range(0, self.borrowedCounter):
                book = self.borrowed[i]
                info = str(i + 1) + ' ' + book.getName() + ' by ' + book.getWriter() + ', ' + str(book.getId())
                print(info)
        else:
            print('no books')

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def getBorrowedCounter(self):
        return self.borrowedCounter

