class user:
    name =  None

user.name = 'stan'
user.surname = 'smit'
print(user.name)
print(user.surname)


print("=============================")


class Employee:
    name = None
    age = None
    salary = None

    def name(self):
        name = None

    def age(self):
        age = None

    def salary(self):
        salary = None

    def display_info(self):
        print(f"имя: {self.name}")
        print(f"возраст: {self.age}")
        print(f"зарплата: {self.salary}")

users = Employee()
users.name = "Вика"
users.age = 23
users.salary = 30000

users.display_info()