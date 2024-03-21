from square_generator.square_generator import SquareGenerator, RangeError


class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):

        if end < start:
            raise RangeError("End of range cannot be less than start.")

        cubes = [x ** 3 for x in range(start, end + 1)]
        return cubes


# Example usage:
cubic_gen = CubicGenerator()
cubes_1_to_5 = cubic_gen.generate_squares(1, 5)
print("Generated cubes:", cubes_1_to_5)

# Example usage:
square_gen = SquareGenerator()
try:
    squares_1_to_10 = square_gen.generate_squares(1, 10)  # Attempting to generate squares with end < start
    print("Generated squares:", squares_1_to_10)
    square_roots = square_gen.calculate_square_roots(squares_1_to_10)
    print("Square roots:", square_roots)
except RangeError as e:
    print("Error:", e)
