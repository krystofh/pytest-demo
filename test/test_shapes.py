#!/usr/bin/env python3
"""
File: test_shapes.py
Author: krystofh
Date: 2024-12-02
Description: Test classes for objects from shapes.py demonstrating how to test class methods
"""

import pytest
import source.shapes as shapes
import math


# Define a test class for testing Circle class
class TestCircle:
    # Method used to initialize class objects and prepare the testing
    def setup_method(self, method):
        self.circle = shapes.Circle(3.5)  # example object

    # Method used to clean up after tests
    def teardown_method(self, method):
        del self.circle  # delete object after use

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius**2

    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius


# Define test class for testing Rectangle class
class TestRectangle:
    # Method used to initialize class objects and prepare the testing
    def setup_method(self, method):
        self.rectangle = shapes.Rectangle(3, 4)  # example object

    # Method used to clean up after tests
    def teardown_method(self, method):
        del self.rectangle  # delete object after use

    def test_area(self):
        assert self.rectangle.area() == self.rectangle.width * self.rectangle.height

    def test_perimeter(self):
        assert (
            self.rectangle.perimeter()
            == self.rectangle.width * 2 + self.rectangle.height * 2
        )


# Define test class for testing Square class
class TestSquare:
    # Method used to initialize class objects and prepare the testing
    def setup_method(self, method):
        self.rectangle = shapes.Rectangle(
            4, 4
        )  # for comparison with the special rectangle case 'square'
        self.square = shapes.Square(4)  # example object

    # Method used to clean up after tests
    def teardown_method(self, method):
        del self.square  # delete object after use
        del self.rectangle

    def test_area(self):
        assert self.square.area() == self.rectangle.area()

    def test_perimeter(self):
        assert self.square.perimeter() == self.rectangle.perimeter()
