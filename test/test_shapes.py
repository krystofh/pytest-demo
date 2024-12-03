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
from test.test_fixtures import circle_collection  # Import the fixture
import time


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

    @pytest.mark.xfail(
        reason="Using fake perimeter calculation to demonstrate expected fail mark"
    )
    def test_perimeter2(self):
        assert self.square.perimeter() == 2 * self.rectangle.perimeter()


class TestCase1:
    @pytest.mark.skip(reason="Showcase of skip mark, delete if needed")
    # Test function using the fixture imported from test_fixures.py
    def test_circles(self, circle_collection) -> None:
        for circle in circle_collection:
            # By passing the fixture as argument, one has access to all the objects that were initialised
            assert circle.area() == math.pi * circle.radius**2

    @pytest.mark.smoke  # add custom mark
    # Use fixture from conftest file without need of import statement
    def test_rectangles(self, rectangle_collection):
        for rectangle in rectangle_collection:
            assert rectangle.area() == rectangle.width * rectangle.height

    @pytest.mark.slow  # slow test
    def test_slow(self):
        time.sleep(5)
        assert 1 == 1  # dummy assert
