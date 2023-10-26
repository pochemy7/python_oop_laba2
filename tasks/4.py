class Employee:
    name = None
    salary = None

    def name(self):
        name = None

    def salary(self):
        salary = None

    def display_info(self):
        print('The first worker is', name1, "\nand his salary is", salary1)
        print('The second worker is', name2, "\nand his salary is", salary2)


name1 = "Don"
salary1 = "3500$"

name2 = "Smith"
salary2 = "4000$"

workers = Employee()

workers.display_info()
