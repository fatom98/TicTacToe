class Game:

    def winner(self, board, turn):

        if (board[0][0] == board[0][1] == board[0][2] != "" or
            board[1][0] == board[1][1] == board[1][2] != "" or
            board[2][0] == board[2][1] == board[2][2] != "" or
            board[0][0] == board[1][0] == board[2][0] != "" or
            board[0][1] == board[1][1] == board[2][1] != "" or
            board[0][2] == board[1][2] == board[2][2] != "" or
            board[0][0] == board[1][1] == board[2][2] != "" or
                board[0][2] == board[1][1] == board[2][0] != ""):

            return turn

        elif "" not in board[0] and "" not in board[1] and "" not in board[2]:
            return "tie"

        else:
            return False
