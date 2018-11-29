import random
import numpy as np


class Queen:

    def __init__(self, row, column):
        self.row = row
        self.column = column

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column

    def step(self):
        self.row += 1


class Board:

    def __init__(self, n):
        self.n = n
        self.queens = np.empty([self.n], dtype=Queen)
        self.gen_random_board()

    def gen_random_board(self):
        for i in range(self.n):
            self.queens[i] = Queen(random.randint(0, self.n-1), random.randint(0, self.n-1))

        # return self.queens

    def get_heuristic(self):
        tempHeuristic = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self._is_conflict(self.queens[i], self.queens[j]):
                    tempHeuristic += 1

        return tempHeuristic

    @staticmethod
    def _is_conflict(q1, q2):
        if q1.get_row() == q2.get_row() or q1.get_column() == q2.get_column():
            return True

        elif abs(q1.get_column() - q2.get_column()) == abs(q1.get_row() - q2.get_row()):
            return True

        else:
            return False

    def copy_queens(self, b):
        for i in range(self.n):
            self.queens[i] = Queen(b.queens[i].get_row(), b.queens[i].get_column())