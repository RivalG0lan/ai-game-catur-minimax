import pygame
from piece import Piece

WIDTH = 640
SQUARE_SIZE = WIDTH // 8

class Board:

    def __init__(self):

        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.create_board()

    def create_board(self):

        for i in range(8):
            self.board[1][i] = Piece("pawn", "black")
            self.board[6][i] = Piece("pawn", "white")

        # rook
        self.board[0][0] = Piece("rook","black")
        self.board[0][7] = Piece("rook","black")
        self.board[7][0] = Piece("rook","white")
        self.board[7][7] = Piece("rook","white")

        # knight
        self.board[0][1] = Piece("knight","black")
        self.board[0][6] = Piece("knight","black")
        self.board[7][1] = Piece("knight","white")
        self.board[7][6] = Piece("knight","white")

        # bishop
        self.board[0][2] = Piece("bishop","black")
        self.board[0][5] = Piece("bishop","black")
        self.board[7][2] = Piece("bishop","white")
        self.board[7][5] = Piece("bishop","white")

        # queen
        self.board[0][3] = Piece("queen","black")
        self.board[7][3] = Piece("queen","white")

        # king
        self.board[0][4] = Piece("king","black")
        self.board[7][4] = Piece("king","white")

    def draw(self, screen):

        colors = [(240,217,181),(181,136,99)]

        for row in range(8):
            for col in range(8):

                color = colors[(row+col)%2]

                pygame.draw.rect(
                    screen,
                    color,
                    (col*SQUARE_SIZE,row*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE)
                )

                piece = self.board[row][col]

                if piece:
                    piece.draw(screen,row,col)

    def move(self,start,end):

        r1,c1 = start
        r2,c2 = end

        piece = self.board[r1][c1]

        if piece:
            self.board[r2][c2] = piece
            self.board[r1][c1] = None

    def get_all_moves(self,color):

        moves = []

        for r in range(8):
            for c in range(8):

                piece = self.board[r][c]

                if piece and piece.type == "pawn" and piece.color == color:

                    if color == "white":
                        nr = r - 1
                    else:
                        nr = r + 1

                    if 0 <= nr < 8 and self.board[nr][c] is None:
                        moves.append(((r,c),(nr,c)))

        return moves

    def clone(self):

        new_board = Board()

        for r in range(8):
            for c in range(8):

                piece = self.board[r][c]

                if piece:
                    new_board.board[r][c] = Piece(piece.type, piece.color)
                else:
                    new_board.board[r][c] = None

        return new_board