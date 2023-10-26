class Position:
    def __init__(self, title):
        self.title = title


class Department:
    def __init__(self, name):
        self.name = name

class User:
    def __init__(self, name, position, department):
        self.name = name
        self.position = position
        self.department = department


position = Position("Программист")
department = Department("Чая")

employee = User("Максим", position, department)
print("Name:", employee.name)
print("Position:", employee.position.title)
print("Department:", employee.department.name)