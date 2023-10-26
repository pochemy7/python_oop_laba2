class Employee:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_surname(self):
        return self.surname

    def set_surname(self, surname):
        self.surname = surname


employee = Employee("Олег", "Артёмов", 43000)
print(employee.get_name())
print(employee.get_surname())
print(employee.get_salary())

employee.set_name("Сергей")
employee.set_surname("Петров")
employee.set_salary(51200)

print(employee.get_name())
print(employee.get_surname())
print(employee.get_salary())