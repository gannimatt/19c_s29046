from square_generator.square_generator import SquareGenerator, RangeError
import math

class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise RangeError("End of range cannot be less than start for square generation.")
        squares = [x ** 2 for x in range(start, end + 1)]
        return squares

# Example usage:
cubic_gen = CubicGenerator()
try:
    squares_1_to_5 = cubic_gen.generate_squares(5, 1)  # Attempting to generate squares with end < start
    print("Generated squares:", squares_1_to_5)
except RangeError as e:
    print("Error:", e)

# Example usage:
square_gen = CubicGenerator()
try:
    squares_1_to_10 = square_gen.generate_squares(1, 10)  # Attempting to generate squares with end < start
    print("Generated squares:", squares_1_to_10)
    square_roots = square_gen.calculate_square_roots(squares_1_to_10)
    print("Square roots:", square_roots)
except RangeError as e:
    print("Error:", e)
