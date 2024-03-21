import math
class SquareGenerator:
    def generate_squares(self, start, end):

        squares = [x ** 2 for x in range(start, end + 1)]
        return squares

    def calculate_square_roots(self, numbers):

        square_roots = [math.sqrt(num) for num in numbers]
        return square_roots

# Example usage:
square_gen = SquareGenerator()
squares_1_to_10 = square_gen.generate_squares(1, 10)
print("Generated squares:", squares_1_to_10)

square_roots = square_gen.calculate_square_roots(squares_1_to_10)
print("Square roots:", square_roots)
