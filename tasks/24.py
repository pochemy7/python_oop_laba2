class Employee:
    __name = None
    __salary = None

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def getName(self):
        return self.__name

    def getSalary(self):
        return f"{self.__salary}$"


employees = [
    Employee('stan', 0),
    Employee('eric', 14239),
    Employee('kyle', 22398),
    Employee('kenny', 10002),
]
for employee in employees:
    print(f"Name: {employee.getName()}, Salary: {employee.getSalary()}")