class User:
    def __init__(self):
        self._name = None

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name


class Employee(User):
    def setName(self, name):
        if len(name) > 0:
            self._name = name