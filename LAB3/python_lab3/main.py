# 1 task
from abc import abstractmethod

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


# 8 Task
class CubicGenerator(SquareGenerator):
    @staticmethod
    def e_cubes(start, end):
        if start > end:
            raise ValueError("")
        return [a ** 3 for a in range(start, end)]

# 9 Task
class CubicGenerator(SquareGenerator):
    @staticmethod
    def e_squares(start, end):
        if start > end:
            raise ValueError("")
        return [a ** 2 for a in range(start, end)]


    # Task 10

    from abc import ABC, abstractmethod

    class SquareGenerator(ABC):

        @abstractmethod
        def gen_squares(self, start, end):
            pass

    class CubicGenerator(SquareGenerator):

        def gen_squares(self, start, end):
            if start > end:
                raise ValueError("")
            return [x ** 3 for x in range(start, end)]