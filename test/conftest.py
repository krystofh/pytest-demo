#!/usr/bin/env python3
"""
File: conftest.py
Author: krystofh
Date: 2024-12-02
Description: Conftest file stores global fixtures, this is an example
"""

from typing import Literal
import pytest
import source.shapes as shapes


@pytest.fixture
def is_debug() -> Literal[True]:
    return True


@pytest.fixture
def rectangle_collection() -> list[shapes.Rectangle]:
    unit_rectangle = shapes.Rectangle(1, 1)
    small_rectangle = shapes.Rectangle(3, 4)
    big_rectangle = shapes.Rectangle(10, 20)
    return [unit_rectangle, small_rectangle, big_rectangle]
