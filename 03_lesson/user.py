class User:
    def __init__(self, first_name, last_name):
        self.name = first_name
        self.surname = last_name

    def printName(self):
        print(self.name)

    def printSurname(self):
        print(self.surname)

    def printUser(self):
        print(self.name, self.surname)
