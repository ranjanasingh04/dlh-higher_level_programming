#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Retrieve position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position with validation."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )

        self.__position = value

    def area(self):
        """Return square area."""
        return self.__size ** 2

    def my_print(self):
        """Print square using #."""
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return string representation of square."""
        if self.__size == 0:
            return ""

        lines = []

        # vertical spacing
        for i in range(self.__position[1]):
            lines.append("")

        # square rows
        for i in range(self.__size):
            lines.append(
                " " * self.__position[0] + "#" * self.__size
            )

        return "\n".join(lines)
