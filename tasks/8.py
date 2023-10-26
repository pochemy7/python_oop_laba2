class User:
  name = 'oop python'

  def show(self):
    return self.cape(self.name)

  def cape(self,stri):
    return stri.upper()
class Student(User):# задание 1
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_initials(self):# задание 3
        first_initial = self.capitalize_first_letter(self.name)
        last_initial = self.capitalize_first_letter(self.surname)
        return f"{first_initial}{last_initial}"

    def capitalize_first_letter(self, string):# задание 2
        return string[0].upper() if string else ''

# создаем объект класса Student
student = Student('John', 'Doe')

# выводим инициалы студента
print(student.get_initials())