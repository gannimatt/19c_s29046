import math


class RangeError(Exception):
    """Custom exception for handling invalid range."""


class SquareGenerator:
    def generate_squares(self, start, end):

        if end < start:
            raise RangeError("End of range cannot be less than start.")

        squares = [x ** 2 for x in range(start, end + 1)]
        return squares

    def calculate_square_roots(self, numbers):

        square_roots = [math.sqrt(num) for num in numbers]
        return square_roots
