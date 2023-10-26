class Car:
    color = None  # none временно пустое значение
    fuel = None
    weight = None  # задание 1
    stamp = None

    def go(self):
        time = None

    def turn(self):
        where = None

    def stop(self):
        when = None

    def display_info(self):  # задание 2
        print(f"цвет: {self.color}")
        print(f"объем бака: {self.fuel}")
        print(f"вес: {self.weight}")
        print(f"марка авто: {self.stamp}")


myCar = Car()

myCar.color = "purple"
myCar.fuel = 50
myCar.weight = "weight"
myCar.stamp = "bmv"

myCar2 = Car()  # задание 3

myCar2.color = "blue"
myCar2.fuel = 35
myCar2.weight = "weight"
myCar2.stamp = "audi"

myCar.go()
myCar.turn()
myCar.stop()

myCar.display_info()
print("==========")
myCar2.display_info()
