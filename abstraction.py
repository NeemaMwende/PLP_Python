# from abc import abstractmethod, ABC

# class Animal(ABC):
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         return "Bark"

# dog = Dog()
# print(dog.make_sound())

from abc import ABC, abstractmethod
import math

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Method to compute the area of the shape"""
        pass

# Concrete class for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * (self.__radius ** 2)

# Concrete class for Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

# Function to print the area of any shape
def print_area(shape):
    if isinstance(shape, Shape):
        print(f"The area is: {shape.area()}")
    else:
        print("Invalid shape")

# Instantiate shapes
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Print areas
print_area(circle)      # Output: The area is: 78.53981633974483
print_area(rectangle)  # Output: The area is: 24
