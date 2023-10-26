class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        square = self.width * self.height
        return square

    def get_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter

    def get_ratio(self):
        square = self.get_square()
        perimeter = self.get_perimeter()
        ratio = square // perimeter
        return ratio


rectangle = Rectangle(5, 12)
square = rectangle.get_square()
perimeter = rectangle.get_perimeter()
ratio = rectangle.get_ratio()

print(f"Площадь прямоугольника: {square}")
print(f"Периметр прямоугольника: {perimeter}")
print(f"Отношение площади к периметру: {ratio}")