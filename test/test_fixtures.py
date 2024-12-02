#!/usr/bin/env python3
"""
File: test_fixtures.py
Author: krystofh
Date: 2024-12-02
Description: Demonstration of how to use fixtures in testing
"""

import pytest
import source.functions as functions
import source.shapes as shapes
import math


"""
“Yield” fixtures yield instead of return. With these fixtures, we can run some code and 
pass an object back to the requesting fixture/test, just like with the other fixtures. 
The only differences are:
    - return is swapped out for yield.
    - Any teardown code for that fixture is placed after the yield.

Once pytest figures out a linear order for the fixtures, it will run each one up until it
returns or yields, and then move on to the next fixture in the list to do the same thing.
Once the test is finished, pytest will go back down the list of fixtures, but in the reverse order, 
taking each one that yielded, and running the code inside it that was after the yield statement.
"""


# Define a list of reusable circle objects
@pytest.fixture(
    scope="module"
)  # scope changes when the fixture is destroyed, module: the fixture is destroyed during teardown of the last test in the module.
def circle_collection() -> list[shapes.Circle]:
    unit_circle = shapes.Circle(1)
    small_circle = shapes.Circle(5)
    big_circle = shapes.Circle(20)
    yield [
        unit_circle,
        small_circle,
        big_circle,
    ]  # alternative to return, but enables cleaning up afterwards
    del unit_circle, small_circle, big_circle  # clean-up steps (teardown code)


@pytest.fixture
def rectangle_collection() -> list[shapes.Rectangle]:
    unit_rectangle = shapes.Rectangle(1, 1)
    small_rectangle = shapes.Rectangle(3, 4)
    big_rectangle = shapes.Rectangle(10, 20)
    return [unit_rectangle, small_rectangle, big_rectangle]


# Test function using the fixture
def test_circles(circle_collection) -> None:
    for circle in circle_collection:
        # By passing the fixture as argument, one has access to all the objects that were initialised
        assert circle.area() == math.pi * circle.radius**2
