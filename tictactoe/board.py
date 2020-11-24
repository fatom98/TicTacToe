import pygame
from .constants import *
from itertools import cycle
from threading import Thread
from copy import deepcopy
from minimax.ai import Ai
from .game import Game


class Board:

    def __init__(self, win):
        self.win = win
        self.font = pygame.font.SysFont(None, 150, True)
        self.res()

    def res(self):
        self.board = []
        self.PARTICIPANTS = cycle("XO")
        self.turn = next(self.PARTICIPANTS)
        self.ai = Ai()
        self.game = Game()
        self.create_board()

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append("")

        self.draw()

    def draw(self):
        self.win.fill(WHITE)

        for row in range(2):
            pygame.draw.line(self.win, BLACK, (25, 225 + row * SQUARE_SIZE), (625, 225 + row * SQUARE_SIZE), 3)

            for col in range(2):
                pygame.draw.line(self.win, BLACK, (225 + col * SQUARE_SIZE, 25), (225 + col * SQUARE_SIZE, 625), 3)

    def place_x(self, pos):
        r, c = pos

        if self.board[r][c] == "":
            x1 = 25 + r * SQUARE_SIZE + 25
            x2 = x1 + 150
            y1 = 25 + c * SQUARE_SIZE + 25
            y2 = y1 + 150
            pygame.draw.line(self.win, BLACK, (x1, y1), (x2, y2), 4)
            pygame.draw.line(self.win, BLACK, (x2, y1), (x1, y2), 4)
            self.move(pos, "X")

    def place_o(self, pos):
        r, c = pos

        if self.board[r][c] == "":
            x = 25 + r * SQUARE_SIZE + SQUARE_SIZE//2
            y = 25 + c * SQUARE_SIZE + SQUARE_SIZE//2
            pygame.draw.circle(self.win, BLACK, (x, y), 75)
            pygame.draw.circle(self.win, WHITE, (x, y), 71)
            self.move(pos, "O")

    def move(self, pos, piece):
        r, c = pos
        self.board[r][c] = piece
        result = self.game.winner(self.board, self.turn)

        if not result:
            self.turn = next(self.PARTICIPANTS)

            if self.turn == "O":
                pos = self.ai.move(deepcopy(self.board))
                self.place_o(pos)

        else:
            self.done(result)

    def wait(self):
        pygame.time.wait(3 * SECOND)
        self.res()

    def done(self, result):

        if result == "tie":
            message = "Its a tie"

        else:
            message = f"{self.turn} Won!!!"

        text = self.font.render(message, True, BLUE)
        x = (WIDTH - text.get_width())//2
        y = (HEIGHT - text.get_height())//2
        self.win.blit(text, (x, y))
        self.turn = None
        thread = Thread(target=self.wait)
        thread.start()
