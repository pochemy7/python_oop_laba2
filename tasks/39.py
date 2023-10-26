class User:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Employee(User):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def get_employee_id(self):
        return self.employee_id


class Programmer(Employee):
    def __init__(self, name, employee_id, programming_languages):
        super().__init__(name, employee_id)
        self.programming_languages = programming_languages

    def get_programming_languages(self):
        return self.programming_languages

    def code(self):
        return f"{self.name} is coding."


class Programmer(Employee):
    def __init__(self, name, employee_id, programming_languages):
        super().__init__(name, employee_id)
        self.programming_languages = programming_languages

    def get_programming_languages(self):
        return self.programming_languages

    def code(self):
        return f"{self.name} is coding."


class Designer(Employee):
    def __init__(self, name, employee_id, design_tools):
        super().__init__(name, employee_id)
        self.design_tools = design_tools

    def get_design_tools(self):
        return self.design_tools

    def design(self):
        return f"{self.name} is designing."


programmer = Programmer("Abygale", 32112, ["C#", "C++"])
print(programmer.get_name())
print(programmer.get_programming_languages())
print(programmer.code())

designer = Designer("Robert", 70000, ["Photoshop", "Illustrator"])
print(designer.get_name())
print(designer.get_design_tools())
print(designer.design())