from square_generator.square_generator import SquareGenerator, RangeError

# Example usage:
square_gen = SquareGenerator()
try:
    squares_1_to_10 = square_gen.generate_squares(1, 10)  # Attempting to generate squares with end < start
    print("Generated squares:", squares_1_to_10)
    square_roots = square_gen.calculate_square_roots(squares_1_to_10)
    print("Square roots:", square_roots)
except RangeError as e:
    print("Error:", e)
