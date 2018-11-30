import random
import numpy as np


# Class for a queen on the board, holds the row and column position of the queen
class Queen:

    def __init__(self, row, column):
        self.row = row
        self.column = column

    # returns the row position of the queen
    def get_row(self):
        return self.row

    # returns the column position of the queen
    def get_column(self):
        return self.column

    # function to move the queen one step down the row
    def step(self):
        self.row += 1


# Board class to hold n queens
class Board:

    def __init__(self, n):
        self.n = n
        self.queens = np.empty([self.n], dtype=Queen)  # array to hold n queen objects

    # generates a random configuration of n queens
    def gen_random_board(self):
        for i in range(self.n):
            self.queens[i] = Queen(random.randint(0, self.n-1), random.randint(0, self.n-1))

    # returns the heuristic of the current board
    def get_heuristic(self):
        tempHeuristic = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self._is_conflict(self.queens[i], self.queens[j]):
                    tempHeuristic += 1

        return tempHeuristic

    # checks whether two queens are in conflict or not
    @staticmethod
    def _is_conflict(q1, q2):
        # check for row and column
        if q1.get_row() == q2.get_row() or q1.get_column() == q2.get_column():
            return True

        # check along the diagonal
        elif abs(q1.get_column() - q2.get_column()) == abs(q1.get_row() - q2.get_row()):
            return True

        # no conflict
        else:
            return False

    # Utility functions
    # function to copy the queens from another board to current board
    def copy_queens(self, b):
        for i in range(self.n):
            self.queens[i] = Queen(b.queens[i].get_row(), b.queens[i].get_column())

    # function to print the board with 1s at positions of queens
    def print_board(self):
        tboard = [[0 for x in range(self.n)] for x in range(self.n)]

        for q in self.queens:
            tboard[q.get_row()][q.get_column()] = 1

        for i in range(self.n):
            for j in range(self.n):
                print(tboard[i][j], end=" ")

            print("\n")