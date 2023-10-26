class Employee:
    def __init__(self, name, salary, age):
        self.__name = name 
        self.__salary = salary 
        self.__age = age  

    def display_employee_data(self):
        return f"Имя: {self.__name}, Зарплата($): {self.__salary}, Возраст: {self.__age}"

employee = Employee('Bob', 36000, 30)

print(employee.display_employee_data())