import pygame
from tictactoe.constants import *
from tictactoe.board import Board

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe")
clock = pygame.time.Clock()


def convert(pos):
    x, y = pos
    row, col = x//SQUARE_SIZE, y//SQUARE_SIZE
    return row, col


def main():

    run = True
    board = Board(WIN)

    while run:

        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                row, col = convert(event.pos)
                turn = board.turn

                if turn == "X":
                    board.place_x((row, col))

        pygame.display.update()


if __name__ == "__main__":
    main()
