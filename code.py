#!/usr/bin/python3
"""This is a sample Python script that adheres to PEP 8 style guide"""


class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


def calculate_square(n):
    """
    Calculate the square of a number.

    Args:
        n (int): The number to be squared.

    Returns:
        int: The square of the input number.
    """
    return n ** 2


def main():
    """Create an instance of MyClass"""
    obj = MyClass(name="Jane", age=10)

    """Display information using the display_info method"""
    obj.display_info()

    """Calculate and print the square of 5"""
    result = calculate_square(5)
    print(f"The square of 5 is: {result}")


if __name__ == "__main__":
    main()
