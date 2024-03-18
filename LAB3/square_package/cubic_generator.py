from square_package.square_generator import SquareGenerator

class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            print("End of the range must be greater than or equal to the start!!!")
        squares = [x**2 for x in range(start, end + 1)]
        return squares

    def generate_cubes(self, start, end):
        cubes = [x**3 for x in range(start, end + 1)]
        return cubes

