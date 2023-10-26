class User:
    def setAge(self, age):
        if age >= 0:
            self.age = age
        else:
            print('Need age more than or equal to 0')


class Employee(User):
    def setAge(self, age):
        if age <= 120:
            super().setAge(age)
        else:
            print('Need age less than or equal to 120')


employee = Employee()
employee.setAge(38)