class User:
    __name = None

    def __init__(self, name):
        self.__name = name

user1 = User('1')
user2 = User('2')

print(user1 == user1) 
print(user1 == user2)

#emp1 = Employee('john')
#emp2 = Employee('eric')

#print(emp1 == emp2)
#Результат сравнения emp1 == emp2 будет False, так как у них разные имена, и объекты различаются.

#emp1 = Employee('john')
#emp2 = Employee('eric')

#print(emp1 == emp1)
#Результат сравнения emp1 == emp1 будет True, так как emp1 сравнивается с самим собой, и они представляют один и тот же объект.

#emp1 = Employee('john')
#emp2 = Employee('john')

#print(emp1 == emp2)
#Результат сравнения emp1 == emp2 будет False, даже если имена одинаковы, потому что emp1 и emp2 представляют разные объекты.


#emp1 = Employee('john')
#emp2 = Employee('eric')

#print(emp1 != emp1)
#Результат сравнения emp1 != emp1 будет False, так как emp1 сравнивается с самим собой, и они представляют один и тот же объект. != проверяет, что объекты не равны.

#emp1 = Employee('john')
#emp2 = emp1

#print(emp1 == emp2)
#Результат сравнения emp1 == emp2 будет True, так как emp1 и emp2 указывают на один и тот же объект.

#emp1 = Employee('john')
#emp2 = Employee('eric')

#print(emp1 !== emp2)
#Оператор !== не существует в Python. Вместо этого используется != для проверки неравенства.

#emp1 = Employee('john')
#emp2 = emp1
#emp2.name = 'eric'

#print(emp1 == emp2)
#Результат сравнения emp1 == emp2 будет True, так как emp1 и emp2 указывают на один и тот же объект, и изменение имени в одном объекте также изменяет его в другом. 