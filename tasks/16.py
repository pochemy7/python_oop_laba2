class Employee:
    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def get_age(self):
        return self.__age

employee = Employee('Joe', 25000, 40)
print("Имя:", employee.get_name())
print("Зарплата:", employee.get_salary())
print("Возраст:", employee.get_age())