from tictactoe.game import Game


class Ai:

    def __init__(self):
        self.game = Game()
        self.score = {
            "X": +1,
            "O": -1,
            "tie": 0
        }

    def move(self, board):

        best_score = float("-inf")
        move = None

        for i in range(3):
            for j in range(3):

                if board[i][j] == "":

                    board[i][j] = "O"
                    score = self.minimax(board, 0, False, "X")
                    board[i][j] = ""

                    if score > best_score:
                        best_score = score

                        move = (i, j)

        return move

    def minimax(self, board, depth: int, maxPlayer: bool, turn):

        won = self.game.winner(board, turn)

        if won != False:
            return self.score[won]

        if maxPlayer:

            best_score = float("-inf")

            for i in range(3):
                for j in range(3):

                    if board[i][j] == "":

                        board[i][j] = "O"
                        score = self.minimax(board, depth + 1, False, "X")
                        board[i][j] = ""

                        best_score = max(score, best_score)

            return best_score

        else:

            best_score = float("inf")

            for i in range(3):
                for j in range(3):

                    if board[i][j] == "":

                        board[i][j] = "X"
                        score = self.minimax(board, depth + 1, True, "O")
                        board[i][j] = ""

                        best_score = min(score, best_score)

            return best_score
