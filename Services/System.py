from Services.UserRepository import UserRepository
from Services.BookRepository import BookRepository


class System:
    def __init__(self):
        self.userRepository = UserRepository()
        self.bookRepository = BookRepository()





