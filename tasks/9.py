class User:
    name = 'john'

    def show(self):
        return self.name

class Student:
    name = 'Alice'
    surname = 'Smith'

    def show(self):
        return f"{self.name} {self.surname}"

# Создаем объекты классов
user = User()
student = Student()

# Выводим значения свойств
print(user.name) 
print(student.name)  
print(student.surname)  