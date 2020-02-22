import numpy as np
from soupsieve.util import string

ROW_CNT = 9
COLUMN_CNT = 8


def createBoard():
    board = np.zeros((8, 9), dtype=int)
    return board


board = createBoard()
print(board)
gameEnd = False
turn = 0


def dropPiece(Board, Row, Col, playerPiece):  # drop the piece in the spot the player has chosen
    Board[Row][Col] = playerPiece


def validLoc(Board, Col):  # checks if the position we chose is valid for input
    if Board[7][Col] == 0:
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


def printBoard(Board):
    print(np.flip(Board, 0))


while not gameEnd:
    # name = input("Lets get started! What's your name? ")

    # player one
    if turn == 0:
        player = string(1)
    # player two
    else:
        player = string(2)

    turn = changeTurn(turn)
    col = int(input("Player " + player + ": Select which position you want to fill: 0-8:  "))
    if validLoc(board, col):
        row = nextOpenRow(board, col)
        dropPiece(board, row, col, player)
    printBoard(board)
