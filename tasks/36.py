class User:
    def __init__(self):
        self.__name = ''

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name


class Employee(User):
    def setName(self, name):
        if len(name) > 0:
            super().setName(name)
        else:
            print("Name cannot be empty")


employee = Employee()
employee.setName("Josh")
print("Employee Name:", employee.getName())
employee.setName("")