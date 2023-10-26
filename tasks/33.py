class User:
    def __init__(self, name, surname, age, salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary

    def getName(self):
        return self.name

    def getSurn(self):
        return self.surname

    def getAge(self):
        return self.age

    def getSalary(self):
        return self.salary


class Student(User):
    def __init__(self, name, surname, age, salary, year):
        super().__init__(name, surname, age, salary)
        self.year = year

    def getYear(self):
        return self.year