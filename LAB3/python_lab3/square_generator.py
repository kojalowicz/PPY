# 5 Task
class SquareGenerator:
    @staticmethod
    def e_squares(start, end):
        if start > end:
            raise ValueError("")
        return [a** 2 for a in range(start, end)]
