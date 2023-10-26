class Employee:
    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.set_age(age)

    def get_name(self):
        return self.__name

    def get_salary(self):
        return f"${self.__salary}"

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if 0 <= age <= 120:
            self.__age = age
        else:
            raise ValueError("Age must be between 0 and 120.")

employee = Employee('Jihn', 4444, 24)
print("Name:", employee.get_name())
print("Salary:", employee.get_salary())
