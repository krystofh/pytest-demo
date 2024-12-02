#!/usr/bin/env python3
"""
File: shapes.py
Author: krystofh
Date: 2024-12-02
Description: Collection of shapes demonstrating inheritance. See tests/test_shapes.py on the testing of classes
"""

import math


class Shape:

    # Initializing
    def __init__(self):
        print("Shape created.")

    def area(self):
        pass

    def center(self):
        pass

    def perimeter(self):
        pass

    # Destructor
    def __del__(self):
        print("Shape deleted.")


class Rectangle(Shape):
    def __init__(self, a: float, b: float):
        super().__init__()
        self.width = a
        self.height = b

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height


class Square(Rectangle):
    def __init__(self, a):  # new constructor with single parameter
        # inherit the methods
        super().__init__(
            a, a
        )  # use square's side 'a' for both rectangle width and height


class Circle(Shape):

    def __init__(self, radius: float):
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius
