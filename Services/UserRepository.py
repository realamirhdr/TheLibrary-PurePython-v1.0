


class UserRepository:

    def __init__(self):
        self.admin = Manager("admin", "admin")

    members = []
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

    def findMember(self, username, password):
        for member in self.members:
            if username.__eq__(member.getUsername()) and password.__eq__(member.getPassword()):
                return member

    def showAllMembers(self):
        if self.memberCounter == 0:
            print('no members')
        else:
            for member in self.members:
                info = member.getUsername() + ', ' + member.getPassword() + ', ' + str(member.getId())
                print(info)
