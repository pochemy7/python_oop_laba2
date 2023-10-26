class Employee:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def set_name(self, name):
        self.__name = name

    def set_surname(self, surname):
        self.__surname = surname

user = Employee('Stan', 'Smith')
user.set_name('Gwen')
user.set_surname('Johnson')
print(user.get_name())
print(user.get_surname())