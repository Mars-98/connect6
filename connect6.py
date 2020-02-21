import numpy as np

ROW_CNT = 9
COLUMN_CNT = 8
TURN = 0
FIRST_TURN = 0


def createBoard():
    board = np.zeros((8, 9), dtype=int)
    return board


board = createBoard()
print(board)
gameEnd = False


def choosePiece():
    pass


def validPosition():
    pass


def nextOpenRow():
    pass


# def changeTurn(turn=TURN):
#     if firstT == 0:
#         return 0
#     turn += 1  # increments to 1 for player 2's turn
#     turn %= 2  # maintains turn to stay between 0 and 1
#     firstT += 1
#     return turn


def printBoard(board):
    pass


while not gameEnd:
    # player one
    if TURN == 0:  # changeTurn(FIRST_TURN, TURN) == 0:
        col = int(input("Player 1: Select which circle you want to: 0-8:  "))

    # player two
    else:
        col = int(input("Player 2: Select which circle you want to: 0-8:  "))

# changeTurn(FIRST_TURN, TURN);
