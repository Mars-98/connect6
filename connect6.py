import numpy as np

ROW_CNT = 9
COLUMN_CNT = 8


def createBoard():
    board = np.zeros((8, 9), dtype=int)
    return board


def choosePiece():
    pass


def validPosition():
    pass


def nextOpenRow():
    pass


def printBoard(board):
    pass


board = createBoard()
print(board)
gameEnd = False
turn = 0

while not gameEnd:
    # player one
    if turn == 0:
        col = int(input("Player 1: Select which circle you want to: 0-8:  "))

    # player two
    else:
        col = int(input("Player 2: Select which circle you want to: 0-8:  "))

    turn += 1  # increments to 1 for player 2's turn
    turn %= 2  # maintains turn to stay between 0 and 1
