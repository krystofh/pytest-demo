# Functions that shall be tested using pytest
# Date: 02.12.2024
# Author: krystofh


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
