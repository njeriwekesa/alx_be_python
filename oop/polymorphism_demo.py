# polymorphism_demo.py
import math

class Shape:
    """Base class for shapes."""
    def area(self):
        """Method to calculate area. Must be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement this method.")


class Rectangle(Shape):
    """Rectangle shape, overrides area calculation."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    """Circle shape, overrides area calculation."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
