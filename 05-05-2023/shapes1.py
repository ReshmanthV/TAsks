"""This is basic python code calculating areas and perimeters of different shapes"""
import math


class Triangle():
    """This is triangle class"""

    def find_area(self, sides_of_triangle):
        """This function finds area of Triangle"""
        side1, side2, side3 = sides_of_triangle
        semi_peri = (side1 + side2 + side3) / 2
        return (semi_peri * (semi_peri - side1) * (semi_peri - side2) * (semi_peri - side3)) ** 0.5

    def find_perimeter(self, sides_of_triangle):
        """This function finds perimeter of Triangle"""
        return sum(sides_of_triangle)


class Rectangle():
    """This is rectangle class"""

    def find_area(self, sides_of_rect):
        """This function finds area of Rectangle"""
        length, width = sides_of_rect
        return length * width

    def find_perimeter(self, sides_of_rect):
        """This function finds perimeter of Rectangle"""
        return 2 * sum(sides_of_rect)


class Circle:
    """This is Circle class """

    def find_area(self, sides_of_circ):
        """This function finds area of Circle"""
        return math.pi * sides_of_circ[0] ** 2

    def find_perimeter(self, sides_of_circ):
        """This function finds perimeter of Circle"""
        return 2 * math.pi * sides_of_circ[0]


sides = list(map(float, input("Enter sides separated with spaces : ").split()))

if len(sides) == 1:
    circle = Circle()
    print("Perimeter of Circle : ", circle.find_perimeter(sides))
    print("Area of Circle : ", circle.find_area(sides))
elif len(sides) == 3:
    trinagle = Triangle()
    print("Perimeter of Triangle : ", trinagle.find_area(sides))
    print("Area of Triangle : ", trinagle.find_perimeter(sides))
elif len(sides) == 2:
    rectangle = Rectangle()
    print("Perimeter of Rectangle/Square : ", rectangle.find_area(sides))
    print("Area of Rectangle/Square : ", rectangle.find_perimeter(sides))
