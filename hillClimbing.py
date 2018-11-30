from queen import Queen, Board


# Class to implement Hill climbing algorithm with random restart
class HillClimbing:

    def __init__(self, n):
        self.n = n
        self.heuristic = 0
        self.stepsClimbed = 0  # number of steps climbed to find solution
        self.stepsClimbedRestart = 0  # number of steps climbed after last random restart
        self.restarts = 0  # number of random restarts
        self.board = Board(n)  # a Board of size n upon which the solution is framed

    # function to perform hill climbing based on the heuristic
    def _climb_step(self):
        nextBoard = Board(self.n)
        tempBoard = Board(self.n)
        nextBoard.copy_queens(self.board)
        tempBoard.copy_queens(self.board)
        curHeuristic = self.board.get_heuristic()  # heuristic value of current board
        bestHeuristic = curHeuristic

        # Loop along each queen
        for i in range(self.n):
            tempBoard.queens[i] = Queen(0, tempBoard.queens[i].get_column())
            if i > 0:
                tempBoard.queens[i-1] = Queen(self.board.queens[i-1].get_row(), self.board.queens[i-1].get_column())

            # Loop to make the queen move along the coloumn
            for j in range(self.n):
                tempHeuristic = tempBoard.get_heuristic()

                # if tempHeuristic is less than the bestHeuristic,
                # then replace it as best and copy the tempBoard to nextBoard
                if tempHeuristic < bestHeuristic:
                    bestHeuristic = tempHeuristic
                    nextBoard.copy_queens(tempBoard)

                # move a step down the row
                if tempBoard.queens[i].get_row() < self.n-1:
                    tempBoard.queens[i].step()

        self.stepsClimbed += 1
        self.stepsClimbedRestart += 1

        if bestHeuristic == curHeuristic:  # no change in heuristic from last heuristic
            nextBoard.gen_random_board()  # generate a random configuration
            self.restarts += 1
            self.stepsClimbedRestart = 0
            bestHeuristic = nextBoard.get_heuristic()

        self.board.copy_queens(nextBoard)  # copy nextBoard to current board
        return bestHeuristic

    # function to generate solution for n queens problem
    def gen_solution(self):
        self.board.gen_random_board()
        self.heuristic = self.board.get_heuristic()

        # loops until heuristic is 0
        while self.heuristic > 0:
            self.heuristic = self._climb_step()

        print('Solution found')

    # calls the print function of the Board to print the queen configuration on Board
    def print_solution(self):
        self.board.print_board()














