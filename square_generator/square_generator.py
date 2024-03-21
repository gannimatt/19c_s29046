from abc import ABC, abstractmethod
import math

class RangeError(Exception):
    """Custom exception for handling invalid range."""

class SquareGenerator(ABC):
    @abstractmethod
    def generate_squares(self, start, end):
        pass

    def calculate_square_roots(self, numbers):
        square_roots = [math.sqrt(num) for num in numbers]
        return square_roots
