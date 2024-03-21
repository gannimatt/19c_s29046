# Using list comprehension to generate a list of squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]
print(squares)


def generate_squares(start, end):
    squares = [x**2 for x in range(start, end + 1)]
    return squares

squares_1_to_10 = generate_squares(1, 10)
print(squares_1_to_10)

class SquareGenerator:
    def generate_squares(self, start, end):
        squares = [x**2 for x in range(start, end + 1)]
        return squares

# Example usage:
square_gen = SquareGenerator()
squares_1_to_10 = square_gen.generate_squares(1, 10)
print(squares_1_to_10)
