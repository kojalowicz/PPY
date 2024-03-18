# TASK 1
# squares = [x**2 for x in range(1, 11)]
# print("List of squares of numbers from 1 to 10:")
# print(squares)

# TASK 2
def generate_squares(start, end):
    squares = [x**2 for x in range(start, end + 1)]
    return squares

# Example usage of the function
start_num = 1
end_num = 15
squares_list = generate_squares(start_num, end_num)

print(f"List of squares of numbers from {start_num} to {end_num}:")
print(squares_list)

