# 1 task
square_num = [x ** 2 for x in range(1, 11)]
print(square_num)

# 2 Task
def e_squares(start, end):
    return [x ** 2 for x in range(start, end)]


print(e_squares(3, 15))

# 3 Task
class SquareGenerator:
    @staticmethod
    def e_squares(start, end):
        return [x ** 2 for x in range(start, end)]

# 4 Task
import math

l1 = SquareGenerator.e_squares(1, 11)
l2 = [math.pow(x, 2) for x in l1]

print(l2)


# 6 Task

from task_07.square_generator import SquareGenerator

print(SquareGenerator.e_squares(6, 9))


