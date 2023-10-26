class User:
    name = None
    surname = None


class Employee:
    pass


class Employee(User):
    pass


worker = Employee()
worker.name = "William"
worker.surname = "Afton"
print("Имя:", worker.name, "\nФaмилия:", worker.surname)