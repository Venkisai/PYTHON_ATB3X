class Shape:
    def area(self):
        return "area of the Shape"

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


Shape1 = Rectangle(7,8)
print(Shape1.area())

Shape2 = Circle(15)
print(Shape2.area())

Shape3 = Shape()
print(Shape3.area())