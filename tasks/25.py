class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class EmployeesCollection:
    def __init__(self):
        self.employees = []


class EmployeesCollection:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, salary):
        new_employee = Employee(name, salary)
        self.employees.append(new_employee)

    def list_employees(self):
        for employee in self.employees:
            print(f"Имя: {employee.name}, Зарплата: {employee.salary}")

class EmployeesCollection:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, salary):
        new_employee = Employee(name, salary)
        self.employees.append(new_employee)

    def list_employees(self):
        for employee in self.employees:
            print(f"Имя: {employee.name}, Зарплата: {employee.salary}")

    def total_salary(self):
        total = sum(employee.salary for employee in self.employees)
        return total

class EmployeesCollection:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, salary):
        new_employee = Employee(name, salary)
        self.employees.append(new_employee)

    def list_employees(self):
        for employee in self.employees:
            print(f"Имя: {employee.name}, Зарплата: {employee.salary}")

    def total_salary(self):
        total = sum(employee.salary for employee in self.employees)
        return total

class EmployeesCollection:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, salary):
        new_employee = Employee(name, salary)
        self.employees.append(new_employee)

    def list_employees(self):
        for employee in self.employees:
            print(f"Имя: {employee.name}, Зарплата: {employee.salary}")

    def total_salary(self):
        total = sum(employee.salary for employee in self.employees)
        return total

    def average_salary(self):
        total = self.total_salary()
        count = len(self.employees)
        if count == 0:
            return 0
        average = total / count
        return average


# Создаем коллекцию работников
employee_collection = EmployeesCollection()

# Добавляем работников
employee_collection.add_employee("Валера", 44444)
employee_collection.add_employee("Ян", 63243)
employee_collection.add_employee("Диман", 5500)

# Выводим список работников
employee_collection.list_employees()

# Рассчитываем суммарную зарплату
total_salary = employee_collection.total_salary()
print(f"Суммарная зарплата: {total_salary}")

# Рассчитываем среднюю зарплату
average_salary = employee_collection.average_salary()
print(f"Средняя зарплата: {average_salary}")