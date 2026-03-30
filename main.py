import pygame
from board import Board
from ai import AI

WIDTH = 640
HEIGHT = 640
SQUARE_SIZE = WIDTH // 8

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess AI - Minimax")

board = Board()
ai = AI()

selected = None
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            x, y = pygame.mouse.get_pos()
            row = y // SQUARE_SIZE
            col = x // SQUARE_SIZE

            if selected:
                board.move(selected, (row, col))
                selected = None

                ai_move = ai.get_best_move(board)
                pygame.event.pump()
                if ai_move:
                    board.move(ai_move[0], ai_move[1])

            else:
                selected = (row, col)

    board.draw(screen)

    pygame.display.update()

pygame.quit()