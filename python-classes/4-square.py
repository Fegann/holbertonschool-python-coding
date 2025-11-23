#!/usr/bin/python3
"""
This module defines a Square class with private size,
getter and setter for size, area method, and print method.
"""


class Square:
    """Represents a square with private size, area, and print method."""

    def __init__(self, size=0):
        self.size = size  # use setter for validation

    @property
    def size(self):
        """Getter to retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter to validate and set the size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with '#' characters."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
