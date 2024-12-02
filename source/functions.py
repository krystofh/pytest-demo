#!/usr/bin/env python3
"""
File: functions.py
Author: krystofh
Date: 2024-12-02
Description: Arithmetic functions that shall be tested using pytest
"""


def add(a: int, b: int) -> int:
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


def subtract(a: int, b: int) -> int:
    result = a - b
    print(f"{a} - {b} = {result}")
    return result


def multiply(a: int, b: int) -> int:
    result = a * b
    print(f"{a} * {b} = {result}")
    return result


def divide(a: int, b: int) -> None | float:
    if b == 0:
        print("Division by zero is not allowed.")
        raise ZeroDivisionError  # raise exception that can be caught by pytest or program code
        return
    result = a / b
    print(f"{a} / {b} = {result}")
    return result
