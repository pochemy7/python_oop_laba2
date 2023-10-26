class Student:
    pass


class Employee:
    pass


employee = Employee()
print(isinstance(employee, Employee))  # True
print(isinstance(employee, Student))  # False


class Student1:
    name = None

    def __init__(self, name):
        self.name = name


class Employee1:
    name = None

    def __init__(self, name):
        self.name = name


users = [
    Student1('user1'),
    Employee1('user2'),
    Student1('user3'),
    Employee1('user4'),
    Student1('user5'),
    Employee1('user6'),
    Student1('user7'),
]

for user in users:  # задание 1, вывести только имена работников, без студентов
    if isinstance(user, Employee1):
        print(user.name)