class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print(name + ' ' + salary)

user = Employee('John', '3000$')