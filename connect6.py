import numpy as np
from soupsieve.util import string
import pygame
import sys
import math

ROW_CNT = 8
COLUMN_CNT = 9
AQUA = (0, 128, 128)
YELLOW = (255, 215, 0)
RED = (128, 0, 0)
BLACK = (0, 0, 0)


def createBoard():
    board = np.zeros((ROW_CNT, COLUMN_CNT), dtype=int)
    return board


board = createBoard()
print(board)
gameEnd = False
turn = 0


def dropPiece(Board, Row, Col, playerPiece):  # drop the piece in the spot the player has chosen
    Board[Row][Col] = playerPiece


def validLoc(Board, Col):  # checks if the position we chose is valid for input
    if Board[ROW_CNT - 1][Col] == 0:
        return True
    return False


def nextOpenRow(Board, Col):  # gets the next open row on the column we're on
    for Row in range(ROW_CNT):
        if Board[Row][Col] == 0:
            return Row


def changeTurn(Turn):
    Turn += 1  # increments to 1 for player 2's turn
    Turn %= 2  # maintains turn to stay between 0 and 1
    return Turn


def checkWin(Board):
    # counter = 1
    # check for horizontal win
    for r in range(ROW_CNT - 1):
        for c in range(COLUMN_CNT - 5):  # range is exclusive, so it goes from 0 to (COLUMN_CNT-5)-1 == 3
            if Board[r][c] == Board[r][c + 1] == Board[r][c + 2] == Board[r][c + 3] == Board[r][c + 4] \
                    == Board[r][c + 5] != 0:
                return True

    # check for vertical win
    for c in range(COLUMN_CNT - 1):
        for r in range(ROW_CNT - 5):  # range is exclusive, so it goes from 0 to (R0W_CNT-5)-1 == 2
            if Board[r][c] == Board[r + 1][c] == Board[r + 2][c] == Board[r + 3][c] == Board[r + 4][c] \
                    == Board[r + 5][c] != 0:
                return True

    # check for + slope diagonal win
    for c in range(COLUMN_CNT - 5):  # range is exclusive, so it goes from 0 to (COLUMN_CNT-5)-1 == 3
        for r in range(ROW_CNT - 5):  # range is exclusive, so it goes from 0 to (R0W_CNT-5)-1 == 2
            if Board[r][c] == Board[r + 1][c + 1] == Board[r + 2][c + 2] == Board[r + 3][c + 3] == Board[r + 4][c + 4] \
                    == Board[r + 5][c + 5] != 0:
                return True

    # check for - slope diagonal win
    for c in range(COLUMN_CNT - 5):  # range is exclusive, so it goes from 0 to (COLUMN_CNT-5)-8=1 == 3
        for r in range(5, ROW_CNT):  # starts at 5 and goes until ROW_CNT - 1
            if Board[r][c] == Board[r - 1][c + 1] == Board[r - 2][c + 2] == Board[r - 3][c + 3] == Board[r - 4][c + 4] \
                    == Board[r - 5][c + 5] != 0:  # wont need to check != 0 because the element it starts at wont be 0
                return True

    return False


def printBoard(Board):  # the axis of the board is row 1 column one, so pieces fill downward, so I flipped it and
    # assigned it a new axis on row
    print(np.flip(Board, 0))


def drawBoard(Board):
    for c in range(COLUMN_CNT):
        for r in range(ROW_CNT):
            # size of width and height, as well as the position on the y(r) and x(c) axis = defines a rectangle
            # we add a square size to r to the empty row can be displayed at the top, since the axis of the board starts
            # at (0,0) which is top left, so we shifted  down to account for the offset we left
            pygame.draw.rect(screen, AQUA, (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            # c * SQUARE_SIZE + SQUARE_SIZE/2, r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE/2, SQUARE_SIZE,
            # SQUARE_SIZE)) is the position for the center of the circle, by adding the offset SQUARE_SIZE/2
            pygame.draw.circle(screen, BLACK,
                               (int(c * SQUARE_SIZE + SQUARE_SIZE / 2), int(r * SQUARE_SIZE + SQUARE_SIZE +
                                                                            SQUARE_SIZE / 2)), radius)

        for c2 in range(COLUMN_CNT):
            for r2 in range(ROW_CNT):
                if Board[r2][c2] == 1:
                    pygame.draw.circle(screen, YELLOW,
                                       (int(c2 * SQUARE_SIZE + SQUARE_SIZE / 2),
                                        height - int(r2 * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), radius)
                elif Board[r2][c2] == 2:
                    pygame.draw.circle(screen, RED,
                                       (int(c2 * SQUARE_SIZE + SQUARE_SIZE / 2),
                                        height - int(r2 * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), radius)

    pygame.display.update()


pygame.init()

SQUARE_SIZE = 100
width = COLUMN_CNT * SQUARE_SIZE
height = (ROW_CNT + 1) * SQUARE_SIZE
size = (width, height)
screen = pygame.display.set_mode(size)
radius = int(SQUARE_SIZE / 2 - 4)

drawBoard(board)
pygame.display.update()

while not gameEnd:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameEnd = True

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))
            posx = event.pos[0]
            if turn == 0:  # something is wrong up here
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARE_SIZE / 2)), radius)
            elif turn == 1:
                pygame.draw.circle(screen, RED, int(posx, int(SQUARE_SIZE / 2)), radius)

            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            # player one
            if turn == 0:
                player = string(1)  # casted to string bc I can't concatenate string and int inside of user input call
            # player two
            else:
                player = string(2)

            turn = changeTurn(turn)
            posx = event.pos[0]
            col = int(math.floor(posx / SQUARE_SIZE))

            if validLoc(board, col):
                row = nextOpenRow(board, col)
                dropPiece(board, row, col, player)

            if checkWin(board):
                print("Congrats Player " + player + "! YOU WON!")
                gameEnd = True

            printBoard(board)
            drawBoard(board)

pygame.QUIT()
sys.exit()
