# TASK 1
# squares = [x**2 for x in range(1, 11)]
# print("List of squares of numbers from 1 to 10:")
# print(squares)

# TASK 2
# def generate_squares(start, end):
#     squares = [x**2 for x in range(start, end + 1)]
#     return squares

# # Example usage of the function
# start_num = 1
# end_num = 15
# squares_list = generate_squares(start_num, end_num)

# print(f"List of squares of numbers from {start_num} to {end_num}:")
# print(squares_list)

# TASK 3
# class SquareGenerator:
#     def generate_squares(self, start, end):
#         squares = [x**2 for x in range(start, end + 1)]
#         return squares
    
# # Example usage of the class and its method
# square_gen = SquareGenerator()
# squares_list = square_gen.generate_squares(3, 8)
# print(squares_list)
    
# TASK 4
# import math
# class SquareGenerator:
#     def generate_squares(self, start, end):
#         squares = [x**2 for x in range(start, end + 1)]
#         return squares
    
#     def calculate_square_roots(self, numbers):
#         square_roots = [math.sqrt(num) for num in numbers]
#         return square_roots
    
# # Example usage of the class and its method
# square_gen = SquareGenerator()
# squares_list = square_gen.generate_squares(3, 8)
# square_roots_list = square_gen.calculate_square_roots(squares_list)
# print(squares_list)
# print(square_roots_list)

# TASK 5
# import math
# class SquareGenerator:
#     def generate_squares(self, start, end):
#         if end < start:
#             print("End of the range must be greater than or equal to the start.")
#         squares = [x**2 for x in range(start, end + 1)]
#         return squares
    
#     def calculate_square_roots(self, numbers):
#         square_roots = [math.sqrt(num) for num in numbers]
#         return square_roots
    
# # Example usage of the class and its method
# square_gen = SquareGenerator()
# squares_list = square_gen.generate_squares(8, 3)
# square_roots_list = square_gen.calculate_square_roots(squares_list)
# print(squares_list)
# print(square_roots_list)

# TASK 6
from square_generator import SquareGenerator

square_gen = SquareGenerator()
squares_list = square_gen.generate_squares(3, 7)
square_roots_list = square_gen.calculate_square_roots(squares_list)
print(squares_list)
print(square_roots_list)