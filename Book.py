import uuid


class Book:
    def __init__(self, name, writer, category):
        self.name = name
        self.writer = writer
        self.category = category
        self.id = None

    def setId(self, id):
        self.id = id

    def getName(self):
        return self.name

    def getWriter(self):
        return self.writer

    def getCategory(self):
        return self.category

    def getId(self):
        return self.id