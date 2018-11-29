from queen import Queen, Board


class HillClimbing:

    def __init__(self, n):
        self.n = n
        self.heuristic = 0
        self.stepsClimbed = 0
        self.stepsClimbedRestart = 0
        self.restarts = 0
        self.board = Board(n)

    def _climb_step(self):
        nextBoard = Board(self.n)
        tempBoard = Board(self.n)
        nextBoard.copy_queens(self.board)
        tempBoard.copy_queens(self.board)
        curHeuristic = self.board.get_heuristic()
        bestHeuristic = curHeuristic

        for i in range(self.n):
            tempBoard.queens[i] = Queen(0, tempBoard.queens[i].get_column())
            if i > 0:
                tempBoard.queens[i-1] = Queen(self.board.queens[i-1].get_row(), self.board.queens[i-1].get_column())

            for j in range(self.n):
                tempHeuristic = tempBoard.get_heuristic()

                if tempHeuristic < bestHeuristic:
                    bestHeuristic = tempHeuristic
                    nextBoard.copy_queens(tempBoard)

                if tempBoard.queens[i].get_row() < self.n-1:
                    tempBoard.queens[i].step()

        self.stepsClimbed+=1
        self.stepsClimbedRestart+=1

        if bestHeuristic == curHeuristic:
            # print('random start')
            nextBoard.gen_random_board()
            self.restarts += 1
            self.stepsClimbedRestart = 0
            bestHeuristic = nextBoard.get_heuristic()

        self.board.copy_queens(nextBoard)
        return bestHeuristic

    def gen_solution(self):
        # newBoard = Board(self.n)
        # newBoard.gen_random_board()
        # self.board.gen_random_board()
        self.heuristic = self.board.get_heuristic()

        while self.heuristic > 0:
            self.heuristic = self._climb_step()
            # print(self.heuristic)

        if self.heuristic == 0:
            print('Solution found')
            # self.heuristic = newHeuristic

    def print_board(self):
        tboard = [[0 for x in range(self.n)] for x in range(self.n)]
        # print(tboard)
        for q in self.board.queens:
            tboard[q.get_row()][q.get_column()] = 1

        for i in range(self.n):
            for j in range(self.n):
                print(tboard[i][j], end=" ")

            print("\n")














