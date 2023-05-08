"""This is basic python code calculating areas and perimeters of different shapes"""
import math


class Shape:
    """This is shape in which child class inherit value of sides from this class """

    def __init__(self, num_of_sides):
        self.no_of_sides = num_of_sides
        self.sides = [0 for i in range(num_of_sides)]

    def input_sides(self):
        """This function takes sides as input"""
        self.sides = [float(input("Enter Side : ")) for i in range(self.no_of_sides)]


class Triangle(Shape):
    """This is triangle class"""

    def __init__(self):
        Shape.__init__(self, 3)

    def find_area(self):
        """This function finds area of Triangle"""
        side1, side2, side3 = self.sides
        semi_peri = (side1 + side2 + side3) / 2
        return (semi_peri * (semi_peri - side1) * (semi_peri - side2) * (semi_peri - side3)) ** 0.5

    def find_perimeter(self):
        """This function finds perimeter of Triangle"""
        return sum(self.sides)


class Rectangle(Shape):
    """This is rectangle class"""

    def __init__(self):
        Shape.__init__(self, 2)

    def find_area(self):
        """This function finds area of Rectangle"""
        length, width = self.sides
        return length * width

    def find_perimeter(self):
        """This function finds perimeter of Rectangle"""
        return 2 * sum(self.sides)


class Square(Shape):
    """This is Square class """

    def __init__(self):
        Shape.__init__(self, 1)

    def find_area(self):
        """This function finds area of Square"""
        side = self.sides[0]
        return side * side

    def find_perimeter(self):
        """This function finds perimeter of Square"""
        return 4 * self.sides[0]


class Circle:
    """This is Circle class """

    def __init__(self):
        self.radius = float(input("Enter radius of Circle : "))

    def find_area(self):
        """This function finds area of Circle"""
        return math.pi * self.radius * self.radius

    def find_perimeter(self):
        """This function finds perimeter of Circle"""
        return 2 * math.pi * self.radius


print()
print("For Circle -- 'c'")
print("For Triangle -- 't'")
print("For Rectangle -- 'r'")
print("For Square -- 's'")
print()
try:
    shape = input("Select Shape : ")
except ValueError:
    exit(0)
if shape == 'c':
    circle = Circle()
    print("Perimeter of Circle : ", circle.find_perimeter())
    print("Area of Circle : ", circle.find_area())
elif shape == 't':
    triangle = Triangle()
    triangle.input_sides()
    print("Perimeter of Triangle : ", triangle.find_area())
    print("Area of Triangle : ", triangle.find_perimeter())
elif shape == 'r':
    rectangle = Rectangle()
    rectangle.input_sides()
    print("Perimeter of Rectangle : ", rectangle.find_area())
    print("Area of Rectangle : ", rectangle.find_perimeter())
elif shape == 's':
    square = Square()
    square.input_sides()
    print("Perimeter of Square : ", square.find_perimeter())
    print("Area of Square : ", square.find_area())
