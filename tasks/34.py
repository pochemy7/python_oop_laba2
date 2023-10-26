class User:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.__capeFirst(self.name)

    def __capeFirst(self, stri):
        return stri


class Employee(User):
    def setEmployeeInfo(self, employee_id):
        self.employee_id = employee_id


employee = Employee()
employee.setName("Jay")
employee.setEmployeeInfo(33)
print(employee.getName())
print(employee.employee_id)