from Services.System import System


class Main:

    def removeTabs(string):
        return string.replace("    ", "")

    library = System()

    while True:
        menu = '''
        1.login as a member
        2.login as a manager
        3.exit'''
        menu = removeTabs(menu)
        menuOperationNumber = int(input(menu + '\n'))
        if menuOperationNumber == 1:
            username = input('username: ')
            password = input('password: ')
            if library.userRepository.memberAuth(username, password):
                member = library.userRepository.findMember(username, password)
                while True:
                    memberMenu = '''
                    1.show all books
                    2.borrow a book 
                    3.return a book
                    4.show all borrowed books
                    5.log out
                    '''
                    memberMenu = removeTabs(memberMenu)
                    memberMenuNumber = int(input(memberMenu + '\n'))
                    if memberMenuNumber == 1:
                        library.bookRepository.showAllBooks()

                    elif memberMenuNumber == 2:
                        library.bookRepository.showAllBooks()
                        if library.bookRepository.bookCounter > 0:
                            intendedBookId = int(input('enter the id of the book you want to borrow: '))
                            book = library.bookRepository.findBook(intendedBookId)
                            member.borrow(book)
                            book = None

                    elif memberMenuNumber == 3:
                        member.showAllBorrowed()
                        if member.getBorrowedCounter() > 0:
                            intendedBookId = int(input('enter the number of the book you want to return: '))
                            member.returnBorrowed(intendedBookId)

                    elif memberMenuNumber == 4:
                        member.showAllBorrowed()

                    elif memberMenuNumber == 5:
                        username = ""
                        password = ""
                        break

        elif menuOperationNumber == 2:
            username = input('username: ')
            password = input('password: ')
            if library.userRepository.adminAuth(username, password) == True:
                while True:
                    managerMenu = '''
                    1.add member
                    2.add book
                    3.show all members
                    4.show all books 
                    5.remove a book 
                    6.log out
                    '''
                    managerMenu = removeTabs(managerMenu)
                    managerMenuNumber = int(input(managerMenu + '\n'))
                    if managerMenuNumber == 1:
                        username = input('enter the new member\'s username: ')
                        password = input('enter the new member\'s password: ')
                        library.userRepository.addMember(username, password)

                    elif managerMenuNumber == 2:
                        bookName = input('enter the new book\'s name: ')
                        writerName = input('who is the new book\'s writer: ')
                        category = input('enter the new books\'s category: ')
                        library.bookRepository.addBook(bookName, writerName, category)

                    elif managerMenuNumber == 3:
                        library.userRepository.showAllMembers()

                    elif managerMenuNumber == 4:
                        library.bookRepository.showAllBooks()

                    elif managerMenuNumber == 5:
                        library.bookRepository.showAllBooks()
                        intendedBookId = int(input('enter the id of the book: '))
                        library.bookRepository.removeBook(intendedBookId)

                    elif managerMenuNumber == 6:
                        username = ""
                        password = ""
                        break
            else:
                print('incorrect username or password')
        elif menuOperationNumber == 3:
            quit()

