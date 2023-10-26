class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_name(self):
        return self.name

    def display_salary(self):
        return self.salary

    def increase_salary(self):
        self.salary *= 1.10  # Увеличение зарплаты на 10%

employee = Employee('Johny', 5000)

print(f"Имя работника: {employee.display_name()}")
print(f"Зарплата работника: {employee.display_salary()}")

employee.increase_salary()
print(f"Увеличенная зарплата: {employee.display_salary()}")