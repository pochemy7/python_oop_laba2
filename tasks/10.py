class Employee:

  def __init__(self):
    name = None
    age = None

    def name(self):
        name = None

    def age(self):
        age = None

    def display_info (self):
        print(f"имя: {self.name}")
        print(f"возраст: {self.age}")

user = Employee()

user.name = "Лера"
user.age = 30

user.display_info()