class Employee:
    def show(self, name, salary):
        return name + '' + salary + ''

worker = Employee()

print(worker.show('john', ' 3650$'))