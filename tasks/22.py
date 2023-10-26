class Validator:  # задание 1, создать класс validator
    email = None
    domain = None
    number = None
    def isEmail(self, email):
        if '@' in email:
            print("Correct:)")
        else:
            print("Wrong:_;")